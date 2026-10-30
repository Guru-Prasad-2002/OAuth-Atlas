# OAuth guide: Gmail

> **Review note:** This is an unedited generated snapshot, not a verified guide. Statements below that sensitive or restricted scopes always require review overlook exceptions; a security assessment may be needed depending on the app and its data handling. The third-party waiting-time anecdote is not an official estimate. See [Google verification guidance](https://developers.google.com/identity/protocols/oauth2/production-readiness/sensitive-scope-verification) and [restricted scope verification](https://developers.google.com/identity/protocols/oauth2/production-readiness/restricted-scope-verification).

Generated from public sources; verify requirements before acting. No provider setup was performed.

## Provider and scope
* The provider is Google (referencing Gmail APIs via Google for Developers) [Google for Developers](https://developers.google.com/identity/protocols/oauth2/scopes).
* Gmail OAuth scopes include sensitive and restricted permissions (such as reading, composing, sending, and permanently deleting email) that control access to user data [Google for Developers](https://developers.google.com/identity/protocols/oauth2/scopes), [Google Cloud Platform Console Help](https://support.google.com/cloud/answer/13461325?hl=en).
* Scopes, public use versus internal use, and policy rules can change requirements [Google for Developers](https://developers.google.com/identity/protocols/oauth2/scopes).

## Difficulty and estimated effort
* Difficulty is moderate to high due to Google's app verification requirements for sensitive and restricted scopes [Google for Developers](https://developers.google.com/identity/protocols/oauth2/scopes).
* Estimated effort is unknown from the available search excerpts, but historical and user reports suggest waiting times can span weeks to months [Gmail API Oauth Approval been waiting almost 3 months](https://stackoverflow.com/questions/55784613/gmail-api-oauth-approval-been-waiting-almost-3-months).

## Before you start
* Identify whether your application requires sensitive or restricted scopes, as these trigger mandatory Google review [Google for Developers](https://developers.google.com/identity/protocols/oauth2/scopes).
* Ensure your project contact details are kept up-to-date in the Google Cloud Console, as all communication with the OAuth review team occurs via email [Google Cloud Platform Console Help](https://support.google.com/cloud/answer/13461325?hl=en).

## Steps to register and configure the OAuth app
* Configure your OAuth consent screen on the Google Cloud Console [Google for Developers](https://developers.google.com/identity/protocols/oauth2/scopes).
* Provide scope justifications explaining how your application will use any sensitive or restricted scopes [Google Cloud Platform Console Help](https://support.google.com/cloud/answer/13461325?hl=en).
* Record and provide a demo video demonstrating your app's functionality, the OAuth flow, and how the requested scopes are being used [Google Cloud Platform Console Help](https://support.google.com/cloud/answer/13461325?hl=en).

## Approval requirements and possible waiting time
* Sensitive and restricted scopes require review by Google [Google for Developers](https://developers.google.com/identity/protocols/oauth2/scopes).
* If requesting restricted scopes, the OAuth review team will reach out to start a security assessment [Google Cloud Platform Console Help](https://support.google.com/cloud/answer/13461325?hl=en).
* Exact waiting times are not officially specified in the provided excerpts, but community discussions highlight that reviews can face significant delays and take a long time [Gmail API Oauth Approval been waiting almost 3 months](https://stackoverflow.com/questions/55784613/gmail-api-oauth-approval-been-waiting-almost-3-months).

## Common blockers and what to do next
* If verification is delayed, community discussions note that you can follow up via email with Google's review contacts, though official response times vary [Gmail API Oauth Approval been waiting almost 3 months](https://stackoverflow.com/questions/55784613/gmail-api-oauth-approval-been-waiting-almost-3-months).
* Ensure your scope justifications and demo videos strictly match Google's requirements to prevent verification rejections [Google Cloud Platform Console Help](https://support.google.com/cloud/answer/13461325?hl=en).

## What an agent can do and where a person must take over
* Search results do not provide explicit Google-specific rules for AI agents interacting with Gmail OAuth, though general third-party security commentary notes that high-stakes actions and broad permissions require careful scoping and human oversight [OAuth Scopes for AI Agents: Step-Up, the Scope Union Trap, and RFC 9396](https://ssojet.com/blog/oauth-scopes-ai-agents-permission-design-agentic-applications), [Connect Your Agent to the Hosted Stripe MCP Server (mcp.stripe.com): OAuth, the 14 Tools, and a Safe Setup · Cesar Ayala](https://cesarayala.dev/blog/connect-agent-stripe-mcp-server-oauth). Note: Third-party blog sources (*ssojet.com* and *cesarayala.dev*) were used here because official Google documentation excerpts did not detail agent-specific boundaries.
* A human must manage project contact configurations, submit verification materials, and handle security assessments [Google Cloud Platform Console Help](https://support.google.com/cloud/answer/13461325?hl=en).

## Evidence and uncertainty
* Claims regarding scope sensitivity, justification rules, and demo video requirements are supported directly by Google documentation [Google for Developers](https://developers.google.com/identity/protocols/oauth2/scopes), [Google Cloud Platform Console Help](https://support.google.com/cloud/answer/13461325?hl=en).
* Claims regarding long approval wait times are based on user discussions and are estimates/historical anecdotes rather than formal guarantees [Gmail API Oauth Approval been waiting almost 3 months](https://stackoverflow.com/questions/55784613/gmail-api-oauth-approval-been-waiting-almost-3-months).
* Exact timelines, automated workspace installation steps, and specific security assessment criteria are unknown or incomplete based on the provided search excerpts.

## Search results

These are search results, not all necessarily sources used in the guide.

- [OAuth 2.0 Scopes for Google APIs  |  Google for Developers](https://developers.google.com/identity/protocols/oauth2/scopes)
- [Gmail API Oauth Approval been waiting almost 3 months](https://stackoverflow.com/questions/55784613/gmail-api-oauth-approval-been-waiting-almost-3-months)
- [Submitting your app for verification - Google Cloud Platform Console Help](https://support.google.com/cloud/answer/13461325?hl=en)
- [OAuth Scopes for AI Agents: Step-Up, the Scope Union Trap, and RFC 9396](https://ssojet.com/blog/oauth-scopes-ai-agents-permission-design-agentic-applications)
- [Access Data on Behalf of Other Users with OAuth 2 Guide | Mailchimp Developer](https://mailchimp.com/developer/marketing/guides/access-user-data-oauth-2)
- [Connect Your Agent to the Hosted Stripe MCP Server (mcp.stripe.com): OAuth, the 14 Tools, and a Safe Setup · Cesar Ayala](https://cesarayala.dev/blog/connect-agent-stripe-mcp-server-oauth)
