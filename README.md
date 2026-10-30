# OAuth Atlas

OAuth Atlas is a proof of concept for researching the steps and approval requirements for provider OAuth apps. A developer registers an OAuth app with a provider; their users can then authorize the integration to access selected data. The requirements depend on the provider, requested scopes, and distribution path.

**Live demo:** https://oauth-atlas-svvu.onrender.com/  
**Examples:** Download the saved GitHub, Slack, and Gmail snapshots from the home page, or find them in `Generated_OAuth_Documentatioon/`. These examples are unedited generated outputs with review notes added; they are not fully verified guides.

## How it works

1. Enter an app name or website. Flask validates the input.
2. Tavily searches for OAuth setup, distribution, and approval information. The application passes up to six returned excerpts to Gemini as untrusted evidence.
3. One Gemini model request normally produces a guide. The prompt asks for official sources, uncertainty, blockers, and human versus agent responsibilities. The browser displays the guide and search results, and can download Markdown.

This is a single search-and-synthesis workflow, not an autonomous browser agent. It does not register provider apps, access accounts, test setup flows, or verify generated claims. No database is required; downloaded guides are not retained on the server. Sample snapshots are files in the repository. The UI does not provide permanent links to newly generated guides.

## Evidence check and findings

We checked a sample of the saved output against official documentation on October 30, 2026; the generated snapshots are retained for transparency, with review notes at the top. This is a sample check, not a full audit.

- **Slack:** A generated claim implies broad review requirements and an unverified 4–8 week security review. [Slack's distribution guide](https://docs.slack.dev/app-management/distribution/) distinguishes single-workspace and unlisted distribution from Marketplace review and workspace-admin approval. The [Marketplace review guide](https://docs.slack.dev/slack-marketplace/slack-marketplace-review-guide/) describes separate prerequisites and timelines. The third-party timing claim is not verified.
- **Gmail:** A sample implies review always applies for sensitive/restricted scopes. [Google's restricted-scope guidance](https://developers.google.com/identity/protocols/oauth2/production-readiness/restricted-scope-verification) describes exceptions and cases where a security assessment is required. A forum anecdote is not a reliable approval-time estimate.
- **GitHub:** The sample couldn't find registration steps. [GitHub's registration documentation](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/creating-an-oauth-app) provides them. The sample remains incomplete and links to the official instructions.

Provider setup was not attempted. Other generated claims, third-party sources, and estimated effort have not been fully checked. Search snippets may omit important conditions, and the model can make unsupported claims or cite irrelevant sources. Verify requirements with the provider before acting.

## Run locally

Requires Python 3.10 or later, a Gemini API key, and a Tavily API key. In Windows Command Prompt:

```cmd
py -m venv .venv
.venv\Scripts\activate.bat
python -m pip install -r requirements.txt
copy .env.example .env
```

Edit `.env` and add `GEMINI_API_KEY` and `TAVILY_API_KEY`. Optionally set `GEMINI_MODEL` to a model available to your Gemini project; the default is `gemini-3.5-flash-lite`. Never commit keys. Then run:

```cmd
python -m flask --app app run --debug
```

Open http://127.0.0.1:5000/. Stop with Ctrl+C. In PowerShell, activate the environment with `.\.venv\Scripts\Activate.ps1` and copy the example with `Copy-Item .env.example .env`.

## Deploy

On Render, create a Python web service from the GitHub repository, choose the Free instance, and set:

- Build: `pip install -r requirements.txt`
- Start: `gunicorn --timeout 240 app:app`
- Environment variables: `GEMINI_API_KEY`, `TAVILY_API_KEY`, and optionally `GEMINI_MODEL`.

The free service may take time to wake after inactivity. API quotas are shared by all visitors and may be exhausted; model availability and limits vary by project. Temporary model/network failures are retried up to twice, which can consume more quota; quota errors are not retried automatically. The app has no per-user authentication or rate limiting and is intended as a low-volume demonstration. Keep usage and billing limits in mind when sharing the URL.

## Project layout

- `app.py`: Flask routes, request validation, and sample downloads.
- `guide_service.py`: Tavily search, Gemini call, bounded retries, and error handling.
- `prompts/guide.txt`: research and guide instructions.
- `templates/` and `static/`: browser interface and Markdown download.
- `Generated_OAuth_Documentatioon/`: saved example snapshots with review notes.
- `.env.example`: configuration placeholders; real keys stay in `.env` locally or Render environment variables.
