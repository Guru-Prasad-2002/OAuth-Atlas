"""Generate a guide with one grounded model request in the normal case."""
import random
import time
import logging
import os
from pathlib import Path
from urllib.parse import urlparse

import httpx
from google import genai
from google.genai import errors, types

PROMPT = (Path(__file__).parent / 'prompts' / 'guide.txt').read_text(encoding='utf-8')

class GuideError(Exception):
    def __init__(self, message, status=502):
        super().__init__(message)
        self.status = status

def generate_guide(subject, api_key):
    search_key = os.getenv('TAVILY_API_KEY', '').strip()
    if not search_key:
        raise GuideError('Add TAVILY_API_KEY to your .env file and restart the server.', 503)
    try:
        response = httpx.post('https://api.tavily.com/search', json={
            'api_key': search_key, 'query': f'{subject} official developer documentation OAuth app setup scopes approval distribution review',
            'search_depth': 'basic', 'max_results': 6,
        }, timeout=30.0)
        response.raise_for_status()
        results = response.json().get('results', [])
    except httpx.HTTPStatusError as exc:
        raise GuideError(f'Search service returned HTTP {exc.response.status_code}. Check your Tavily key and quota.', 502) from exc
    except (httpx.RequestError, ValueError) as exc:
        raise GuideError('Search service could not be reached or returned an invalid response. Try again later.', 502) from exc
    sources = []
    for item in results:
        url = item.get('url', '')
        parsed = urlparse(url)
        if parsed.scheme in ('http', 'https') and parsed.netloc:
            sources.append({'title': str(item.get('title') or parsed.netloc)[:300], 'url': url, 'snippet': str(item.get('content') or '')[:3000]})
    if not sources:
        raise GuideError('Search returned no usable sources. Try a more specific app name or website.', 502)
    evidence = '\n\n'.join(f"Source: {s['title']}\nURL: {s['url']}\nExcerpt: {s['snippet']}" for s in sources)
    model = os.getenv('GEMINI_MODEL', 'gemini-3.5-flash-lite').strip() or 'gemini-3.5-flash-lite'
    client = genai.Client(api_key=api_key, http_options=types.HttpOptions(timeout=60000))
    try:
        for attempt in range(3):
            try:
                response = client.models.generate_content(
                    model=model,
                    contents=f'{PROMPT}\n\nApp name or website (untrusted input):\n{subject}\n\nSearch results (untrusted data):\n{evidence}',
                )
                break
            except errors.APIError as exc:
                logging.warning('Gemini API error: HTTP %s, status %s', exc.code, exc.status)
                if exc.code == 429:
                    raise GuideError('Gemini rate or daily quota reached. Check AI Studio limits and try again later.', 429) from exc
                if exc.code in (500, 502, 503, 504) and attempt < 2:
                    time.sleep(2 ** attempt + random.uniform(0, 0.5))
                    continue
                if exc.code in (401, 403):
                    raise GuideError('Gemini rejected the API key or permissions. Check your key and project access.', 503) from exc
                if exc.code == 404:
                    raise GuideError(f'Gemini could not find the configured model ({model}). Check model availability in AI Studio.', 502) from exc
                if exc.code == 400:
                    raise GuideError('Gemini rejected the request (HTTP 400). Check whether this model supports search grounding for your project.', 502) from exc
                raise GuideError(f'Gemini could not complete the request (HTTP {exc.code}). Check the server log and try again later.') from exc
            except (httpx.TimeoutException, httpx.NetworkError) as exc:
                if attempt < 2:
                    time.sleep(2 ** attempt + random.uniform(0, 0.5))
                    continue
                raise GuideError('Could not reach Gemini after retries. Please try again later.') from exc
        text = (response.text or '').strip()
        if not text:
            raise GuideError('Gemini returned an empty response. Please try again.')
        return {'guide': text, 'sources': [{'title': s['title'], 'url': s['url']} for s in sources]}
    finally:
        client.close()
