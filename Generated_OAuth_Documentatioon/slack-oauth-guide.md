# OAuth guide: Slack

> **Review note:** This is an unedited generated snapshot, not a verified guide. Slack supports unlisted distribution to other workspaces; Marketplace listing is a separate review, and workspace admins may require approval. A single-workspace app may still need OAuth to act for other users. The 4–8 week security review claim below is from a third-party source and has not been verified. See [Slack distribution](https://docs.slack.dev/app-management/distribution/) and [Marketplace review](https://docs.slack.dev/slack-marketplace/slack-marketplace-review-guide/).

Generated from public sources; verify requirements before acting. No provider setup was performed.

## Provider and scope
* Provider: Slack [https://docs.slack.dev/authentication/installing-with-oauth](https://docs.slack.dev/authentication/installing-with-oauth)
* Scopes define what APIs an app can call, grouping permissions by user and bot-level access using a `resource:permission` format [https://hoop.dev/blog/oauth-2-0-workflow-approvals-in-slack-f, https://help.magentrix.com/wikis/help/slack-permission-scopes].
* Scopes and public versus internal use can change requirements [https://www.resumelens.org/blog/slack/slack-oauth-and-app-distribution].

## Difficulty and estimated effort
* Internal apps can be created and deployed in minutes with no Slack review [https://www.resumelens.org/blog/slack/slack-oauth-and-app-distribution].
* Apps requesting sensitive scopes require a Security Review that can take four to eight weeks on first submission [https://www.resumelens.org/blog/slack/slack-oauth-and-app-distribution].

## Before you start
* Identify whether your app is internal (restricted to a single workspace) or distributed for public use [https://www.resumelens.org/blog/slack/slack-oauth-and-app-distribution].
* Review your app's requested scopes and identify which ones are required versus optional [https://slack.dev/introducing-optional-scopes-for-slack-apps].
* Prepare your app's callback behavior and match it with your registered Redirect URIs [https://hoop.dev/blog/oauth-2-0-workflow-approvals-in-slack-f].

## Steps to register and configure the OAuth app
* Configure your app's scopes and settings via the App Management page or an App Manifest [https://slack.dev/introducing-optional-scopes-for-slack-apps].
* For internal apps, retrieve the bot token directly from the app's Install App page in the Slack UI without using an OAuth flow [https://www.resumelens.org/blog/slack/slack-oauth-and-app-distribution].
* For distributed apps, direct users or workspace admins to an authorization URL where they review requested scopes and grant user consent [https://hoop.dev/blog/oauth-2-0-workflow-approvals-in-slack-f].
* Handle the authorization callback by exchanging the temporary authorization code for an access token via `oauth.v2.access` [https://docs.slack.dev/authentication/installing-with-oauth, https://slack.dev/introducing-optional-scopes-for-slack-apps].

## Approval requirements and possible waiting time
* Internal apps require no Slack review [https://www.resumelens.org/blog/slack/slack-oauth-and-app-distribution].
* Apps requesting standard scopes go through a standard App Directory review to test installation, verify core functionality, check scope usage, and evaluate listing completeness [https://www.resumelens.org/blog/slack/slack-oauth-and-app-distribution].
* Apps requesting sensitive scopes (`admin.*`, `calls:write`, `dnd:write`, or access to all messages across a workspace) undergo a Security Review requiring a demo video, detailed documentation of scope usage, and a listing form, which can take four to eight weeks on first submission [https://www.resumelens.org/blog/slack/slack-oauth-and-app-distribution].

## Common blockers and what to do next
* Broken OAuth redirect or misconfigured callback URLs are frequent causes of failure [https://www.resumelens.org/blog/slack/slack-oauth-and-app-distribution, https://hoop.dev/blog/oauth-2-0-workflow-approvals-in-slack-f].
* Being overly broad with scopes can trigger review rejections [https://hoop.dev/blog/oauth-2-0-workflow-approvals-in-slack-f]. Requesting unused scopes (such as `files:read` without touching files) leads to rejection [https://www.resumelens.org/blog/slack/slack-oauth-and-app-distribution].
* Encountering `scope_not_allowed_on_enterprise` happens when installing apps in an Enterprise org with incompatible scopes [https://docs.slack.dev/authentication/installing-with-oauth].
* Encountering `unapproved_scope` happens if requested scopes are still in review or were not submitted by the developer [https://docs.slack.dev/authentication/installing-with-oauth].

## What an agent can do and where a person must take over
* An agent can draft configuration manifests, structure code to handle `oauth.v2.access` responses, and implement feature gating [https://slack.dev/introducing-optional-scopes-for-slack-apps].
* A person must take over to record demo videos, submit listings for App Directory or Security Reviews, authorize workspace permissions, and handle administrative console tasks [https://www.resumelens.org/blog/slack/slack-oauth-and-app-distribution, https://hoop.dev/blog/oauth-2-0-workflow-approvals-in-slack-f].

## Evidence and uncertainty
* Claims regarding internal app setup, standard reviews, sensitive scope review timelines (4–8 weeks), and common rejection reasons are supported by the ResumeLens Slack Blog [https://www.resumelens.org/blog/slack/slack-oauth-and-app-distribution].
* Claims regarding authorization consent screens and callback misdirection are supported by Hoop.dev [https://hoop.dev/blog/oauth-2-0-workflow-approvals-in-slack-f].
* Claims regarding `scope_not_allowed_on_enterprise`, `unapproved_scope`, and the three-step token exchange are supported by Slack Developer Docs [https://docs.slack.dev/authentication/installing-with-oauth].
* Claims regarding scope naming conventions are supported by Magentrix Help Center (third-party source used because it details scope formatting rules) [https://help.magentrix.com/wikis/help/slack-permission-scopes].
* Claims regarding optional scopes and manifests are supported by the Slack Developers Blog [https://slack.dev/introducing-optional-scopes-for-slack-apps].
* The exact timeline for standard App Directory reviews is incomplete in the provided excerpts. Third-party blog sources are estimates rather than official SLAs where exact timelines are not specified by primary docs.

## Search results

These are search results, not all necessarily sources used in the guide.

- [Slack OAuth Scopes + App Distribution — Internal Apps, Marketplace, and the Approval Story — ResumeLens Slack Blog](https://www.resumelens.org/blog/slack/slack-oauth-and-app-distribution)
- [OAuth 2.0 Workflow Approvals in Slack: A Comprehensive Guide](https://hoop.dev/blog/oauth-2-0-workflow-approvals-in-slack-a-comprehensive-guide)
- [Installing via OAuth authorization code flow | Slack Developer Docs](https://docs.slack.dev/authentication/installing-with-oauth)
- [Slack Permission Scopes Reference | Help Center](https://help.magentrix.com/wikis/help/slack-permission-scopes)
- [Give users the power to choose: introducing optional scopes for Slack apps | Blog | Slack Developers](https://slack.dev/introducing-optional-scopes-for-slack-apps)
- [Adding additional user_scope param to Slack integration - Auth0 Community](https://community.auth0.com/t/adding-additional-user-scope-param-to-slack-integration/94577)
