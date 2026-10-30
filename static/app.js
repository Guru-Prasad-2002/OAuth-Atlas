const form = document.querySelector('#guide-form');
const button = document.querySelector('#submit');
const status = document.querySelector('#status');
const result = document.querySelector('#result');
let currentGuide = null;

document.querySelector('#download').addEventListener('click', () => {
  if (!currentGuide) return;
  const { app, guide, sources } = currentGuide;
  const cleanTitle = app.replace(/[\r\n]+/g, ' ');
  const filename = app.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '').slice(0, 60) || 'oauth';
  const sourceLines = sources.map((source) => `- [${source.title.replace(/[\[\]\r\n]/g, ' ')}](${source.url})`);
  const markdown = `# OAuth guide: ${cleanTitle}\n\nGenerated from public sources; verify requirements before acting. No provider setup was performed.\n\n${guide}\n\n## Search results\n\nThese are search results, not all necessarily sources used in the guide.\n\n${sourceLines.length ? sourceLines.join('\n') : 'No search sources were returned; treat this guide as unverified.'}\n`;
  const url = URL.createObjectURL(new Blob([markdown], { type: 'text/markdown;charset=utf-8' }));
  const link = document.createElement('a');
  link.href = url; link.download = `${filename}-oauth-guide.md`; link.click();
  setTimeout(() => URL.revokeObjectURL(url), 1000);
});

// Render a small safe subset of Markdown without inserting model-generated HTML.
function inlineText(parent, text) {
  const pattern = /\[([^\]]+)\]\((https?:\/\/[^\s)]+)\)|\*\*([^*]+)\*\*|`([^`]+)`/g;
  let last = 0, match;
  while ((match = pattern.exec(text)) !== null) {
    parent.append(document.createTextNode(text.slice(last, match.index)));
    if (match[1]) {
      const link = document.createElement('a');
      link.href = match[2]; link.textContent = match[1]; link.target = '_blank'; link.rel = 'noopener noreferrer';
      parent.append(link);
    } else {
      const el = document.createElement(match[3] ? 'strong' : 'code');
      el.textContent = match[3] || match[4]; parent.append(el);
    }
    last = pattern.lastIndex;
  }
  parent.append(document.createTextNode(text.slice(last)));
}

function renderGuide(text) {
  const container = document.querySelector('#guide');
  container.replaceChildren();
  let list = null;
  for (const line of text.split(/\r?\n/)) {
    const heading = line.match(/^\s{0,3}#{1,3}\s+(.+)/);
    const item = line.match(/^\s*(?:([-*])\s+|(\d+)[.)]\s+)(.+)/);
    if (heading) {
      list = null; const h = document.createElement('h3'); inlineText(h, heading[1]); container.append(h);
    } else if (item) {
      const kind = item[2] ? 'OL' : 'UL';
      if (!list || list.tagName !== kind) { list = document.createElement(kind.toLowerCase()); container.append(list); }
      const li = document.createElement('li'); inlineText(li, item[3]); list.append(li);
    } else if (line.trim()) {
      list = null; const p = document.createElement('p'); inlineText(p, line); container.append(p);
    } else { list = null; }
  }
}

form.addEventListener('submit', async (event) => {
  event.preventDefault();
  const app = document.querySelector('#app-name').value.trim();
  if (!app) { status.textContent = 'Enter an app name or website.'; return; }
  button.disabled = true;
  result.hidden = true;
  status.textContent = 'Researching the app and generating your guide. This may take a minute...';
  try {
    const response = await fetch('/api/generate', {
      method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ app })
    });
    const data = await response.json();
    if (!response.ok) throw new Error(data.error || 'Could not generate the guide.');
    currentGuide = { app, guide: data.guide, sources: data.sources };
    renderGuide(data.guide);
    const list = document.querySelector('#sources');
    list.replaceChildren();
    for (const source of data.sources) {
      const item = document.createElement('li');
      const link = document.createElement('a');
      link.href = source.url;
      link.textContent = source.title;
      link.target = '_blank';
      link.rel = 'noopener noreferrer';
      item.append(link);
      list.append(item);
    }
    document.querySelector('#no-sources').hidden = data.sources.length > 0;
    result.hidden = false;
    status.textContent = '';
  } catch (error) {
    status.textContent = error.message || 'Something went wrong. Please try again.';
  } finally { button.disabled = false; }
});
