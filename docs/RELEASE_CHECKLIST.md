# One-Project Release Checklist

1. Recheck the gallery's end-to-end eligibility and resolve the canonical source repository.
2. Audit code, data, model and asset licenses. Missing permission blocks copying; preserve upstream attribution.
3. Record the source revision and reproduce the controlling workflow before changing it.
4. Complete one bounded implementation with explicit inputs, failure handling and safe defaults.
5. Run focused tests immediately after each substantive change; retain reproducible dependency locks.
6. Verify deterministic workflows, dependency and secret checks, and desktop/mobile behavior where applicable.
7. Test configured live providers separately. Never present fixtures, mocks or unconfigured integrations as production evidence.
8. Publish only truthful release status. A reference implementation is not a production certification or uptime guarantee.
9. Add one primary technical category, portfolio placement and evidence links to projects.json; regenerate and check the catalog.
10. Update the existing profile and portfolio additively. Preserve prior projects and design.
11. Record remaining provider, deployment and domain-validation limitations before considering the next candidate.

Future projects start only on a later explicit request, not on a timer. No credentials belong in code, chat, fixtures or the catalog.

## Public Access Review: 2026-10-14

All three released reference implementations pass their current Python suites
and local dependency audits. Their latest published CI runs are successful.
This does not establish live-provider availability or production hosting.

| Project | Usable today | Remaining live-use boundary |
| --- | --- | --- |
| [AI Blog Publisher](https://sushant-nemade.github.io/ai-blog-publisher/) | Public article reader; one labeled synthetic reference article. Local draft/review/publication workflow. | Live Groq and optional news/search/R2 integrations need configured smoke tests. No public article-generation API or multi-user editor. |
| [GitPulse](https://sushant-nemade.github.io/gitpulse/) | Public sample dashboard; authenticated local API and CLI; a real public REST sync was previously verified. | Public dashboard is not a hosted private API. Private hosting needs HTTPS, persistent storage, access controls and verified backup/restore. |
| [Doclify](https://github.com/Sushant-Nemade/Doclify) | Installable local CLI; offline structural documentation and reviewed publication. | Live Groq inference needs a user-configured key and explicit source-upload consent. A website is optional, not required for a CLI. |

Reference verification remains separate from live integration and managed service
readiness. Offline/sample modes must never be presented as real model inference,
account-specific live data, or an operational SLA.

## AI Blog Publisher: Real Content Delivery

1. Clone the derivative and install its frozen Python and frontend dependencies.
2. Configure the required Groq key locally, never in browser code or Git. Add
	Tavily/Guardian only if news research is needed; local storage does not need R2.
3. Generate one article using the documented CLI with a non-sensitive topic.
4. Inspect the private draft, verify factual claims and sources, and approve its
	complete content digest. Publication must preserve any previous article index.
5. Run site-integrity checks and commit only the reviewed public article/index.
6. Let successful CI deploy the static Pages artifact; verify the deployed article
	on desktop and mobile and record the real-provider smoke evidence.

Readers need no AI key or backend. If visitors should generate articles, that is
a separate service: add authenticated accounts, queueing, per-user quotas, model
budget limits and server-side secrets before hosting. Do not expose the owner CLI
or a shared provider key as an anonymous public endpoint.

## GitPulse: Private Live Dashboard

1. Follow the repository's local setup and build its frontend before serving the API.
2. Set GITHUB_USERNAME, a strong local API_TOKEN, and a persistent DATABASE_PATH.
	Keep any optional GitHub token server-side. Start the documented loopback API.
3. Run one actual sync, check the resulting snapshot/history, and verify that
	unauthenticated API calls fail and the previous snapshot survives sync failures.
4. Select an explicitly approved host with HTTPS and a durable data volume. Free
	ephemeral hosting is unsuitable for retaining audience history without backups.
5. Restrict CORS to the intended dashboard origin and keep access private. A static
	Pages frontend can connect to the approved HTTPS API after explicit authentication.
6. Test backup/restore, restart persistence, rate limits, redacted logs and health
	checks before enabling any scheduled collection.

The current API_TOKEN authorizes one account workspace. Do not hand its owner token
to public visitors. A multi-user product needs user identity/OAuth, per-user data
isolation and permission checks first. Never publish the local database as sample data.

## Doclify: Developer Distribution

1. Download the derivative source or its doclify-portfolio wheel, not the upstream
	PyPI package. The public [reference release](https://github.com/Sushant-Nemade/Doclify/releases/tag/v0.3.0-reference)
	contains verified CI artifacts and checksums. Verify Python compatibility and
	the included AGPL notices.
2. Install the derivative in a dedicated environment and run doclify --help and
	doclify --license. Start with a synthetic or approved project directory.
3. Run init, inspect doclify.yaml, then run --dry-run and --offline. Inspect the
	private Markdown artifact before publish --approve FULL_DIGEST.
4. For real AI generation, configure GROQ_API_KEY locally and use --allow-upload
	only after reviewing selected files and the provider's terms/data handling.
5. Record a real generation/review/publication smoke test separately from offline
	reference tests. Never upload third-party/private company code without permission.

A hosted upload-and-generate website would need consent, isolated non-executing
workers, archive/path controls, authentication, quotas, deletion/retention policy,
and a prominent corresponding-source offer under the AGPL. Do not add such hosting
merely to make a CLI portfolio entry look live.

## Market Insight: Completed Reference (2026-10-17)

The [GPLv3 derivative](https://github.com/Sushant-Nemade/MarketInsight) now has a
complete source-dated research workspace, bounded data retrieval, private saved
reports and optional synthesis. The old renderer/agent/tracing path was replaced,
not silently presented as a working live product. Thirty-seven Python tests,
twenty browser cases, Linux/Windows builds, installed-package checks, audits and
the non-root container gate passed. A real Yahoo quote/history lookup was verified
with TLS enabled. The [public reference](https://sushant-nemade.github.io/MarketInsight/)
uses authored fictional data only.

1. Use the public synthetic reference without credentials, or follow the
	repository's frozen setup to run the complete UI/API locally.
2. Configure the private owner token and explicitly enable live data for actual
	research. Keep reports/database files out of the public site and Git.
3. If AI synthesis is selected, choose the provider/model and configure the
	matching key privately. OpenAI and Thesys origins use different keys. Paid
	inference remains unverified until an approved account/budget smoke is run.
4. Follow the current operations guide for TLS trust, provider/data rights,
	persistent storage, access/retention, backup and any remote HTTPS deployment.

No personalized financial advice, forecast accuracy, trading execution,
multi-user SaaS isolation or operational SLA is claimed.

## Next Candidate

TravelBrain is next in the catalog, subject to a new license/data/runnable-path
review and a later explicit request. Do not begin another candidate automatically.