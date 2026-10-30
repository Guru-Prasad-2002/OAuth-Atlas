# OAuth guide: GitHub

> **Review note:** This generated snapshot is incomplete: it does not provide registration steps or a verified effort estimate. Start with [GitHub's OAuth app registration instructions](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/creating-an-oauth-app) and verify the remaining claims before acting.

Generated from public sources; verify requirements before acting. No provider setup was performed.

## Provider and scope
* Provider: GitHub
* Scope: OAuth apps allow developers to link user accounts and request specific permissions via scopes, such as `user:follow`, `project`, `read:project`, `delete_repo`, `write:packages`, `admin:org`, `write:org`, `read:org`, `admin:public_key`, `write:public_key`, `read:public_key`, `admin:org_hook`, and `gist` [Scopes for OAuth apps - GitHub Docs](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/scopes-for-oauth-apps).
* Public versus internal use: Scopes and public versus internal distribution requirements can change over time.

## Difficulty and estimated effort
* Difficulty and estimated effort are unknown based on the provided search results.

## Before you start
* Ensure you understand how OAuth scopes work on GitHub, as applications can request named groups of permissions to access public and non-public data [Authorizing OAuth apps - GitHub Docs](https://docs.github.com/en/apps/oauth-apps/using-oauth-apps/authorizing-oauth-apps).
* Note that the available search excerpts do not establish the initial registration form requirements or UI click paths.

## Steps to register and configure the OAuth app
* The provided search excerpts do not contain the specific step-by-step UI instructions to register an OAuth app on GitHub.
* During the authorization flow, your app redirects users to request their identity, GitHub redirects them back, and your app accesses the API using the user's access token [Authorizing OAuth apps - GitHub Docs](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/authorizing-oauth-apps).
* Your app can specify a space-delimited list of requested scopes (such as `user:email`) during the authorization or redirection request [Authorizing OAuth apps - GitHub Docs](https://docs.github.com/en/apps/oauth-apps/using-oauth-apps/authorizing-oauth-apps), [Authorizing OAuth apps - GitHub Docs](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/authorizing-oauth-apps), [Read-Only OAuth Scope · community · Discussion #7891 · GitHub](https://github.com/orgs/community/discussions/7891).

## Approval requirements and possible waiting time
* Approval requirements and waiting times are unknown or not mentioned in the provided search results.

## Common blockers and what to do next
* If an application creates more than ten tokens for the same user and scope combination, GitHub automatically revokes one of the existing tokens [Authorizing OAuth apps - GitHub Docs](https://docs.github.com/en/apps/oauth-apps/using-oauth-apps/authorizing-oauth-apps).
* Other common blockers are unaddressed due to incomplete search coverage.

## What an agent can do and where a person must take over
* Evidence is unavailable in the search results to define specific boundaries between what an automated agent can do versus what a person must manually handle during GitHub OAuth app registration.

## Evidence and uncertainty
* Claims regarding specific permission scopes (e.g., `user:follow`, `gist`, `admin:org`) and the web application redirection flow are supported directly by official GitHub documentation [Scopes for OAuth apps - GitHub Docs](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/scopes-for-oauth-apps), [Authorizing OAuth apps - GitHub Docs](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/authorizing-oauth-apps).
* A third-party blog post from Northflank was used to add helpful context regarding how OAuth app linking differs from GitHub App installations [Integrating with GitHub - GitHub Apps and OAuth | Blog — Northflank](https://northflank.com/blog/integrating-with-github-github-apps-and-oauth).
* Registration UI steps, developer account prerequisites, approval times, and setup difficulty are completely unknown due to a lack of matching documentation in the search results.

## Search results

These are search results, not all necessarily sources used in the guide.

- [Scopes for OAuth apps - GitHub Docs](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/scopes-for-oauth-apps)
- [Authorizing OAuth apps - GitHub Docs](https://docs.github.com/en/apps/oauth-apps/using-oauth-apps/authorizing-oauth-apps)
- [Authorizing OAuth apps - GitHub Docs](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/authorizing-oauth-apps)
- [Integrating with GitHub - GitHub Apps and OAuth | Blog — Northflank](https://northflank.com/blog/integrating-with-github-github-apps-and-oauth)
- [Read-Only OAuth Scope · community · Discussion #7891 · GitHub](https://github.com/orgs/community/discussions/7891)
- [GitHub oAuth apps: What's the most granular scope to get access to Pull Requests?](https://stackoverflow.com/questions/74314624/github-oauth-apps-whats-the-most-granular-scope-to-get-access-to-pull-requests)
