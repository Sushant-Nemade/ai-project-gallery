# Project Status and Pending Work Register

**Portfolio owner:** Sushant Nemade  
**Status reviewed:** 2026-10-14  
**Scope:** AI Blog Publisher, GitPulse, Doclify, and the in-progress Market Insight adaptation  
**Purpose:** Record remaining implementation, verification, deployment and owner decisions without overstating readiness.

## Executive Summary

Three projects are published as tested reference implementations. Market Insight
is a fourth project in local development, not a released application. The public
browser previews for Blog Publisher and GitPulse are available; Doclify is
distributed as an installable CLI with public source and wheel downloads.

Published source, passing tests and a working preview are different from a
verified live integration or an operated production service. The remaining work
below does not invalidate completed reference releases; it identifies what is
needed before stronger claims or additional deployment scope are appropriate.

This is a dated evidence snapshot, not a continuous monitoring report. Test counts,
dependency findings, provider availability and hosting status must be rechecked
when the relevant code, dependency lock, configuration or infrastructure changes.

## Status Definitions

| Term | Meaning |
| --- | --- |
| Tested reference | Documented source and selected reproducible workflows have been verified. Not production certification. |
| In progress | Implementation has begun, but release gates remain. |
| Implemented but unverified live | Code exists, but the real configured service or operating environment has not been tested. |
| Not implemented | The capability is absent from the current implementation. |
| Conditional | Needed only if the specified provider, hosting or product feature is selected. |
| Optional expansion | A separate future feature, not a prerequisite for the current reference release. |

## Portfolio Overview

| Project | Current delivery | Verified evidence | Remaining boundary |
| --- | --- | --- | --- |
| [AI Blog Publisher](https://github.com/Sushant-Nemade/ai-blog-publisher) | Published reference and [public reader](https://sushant-nemade.github.io/ai-blog-publisher/) | Offline draft/review/publication, mocked graph routing, browser tests and CI. Latest local review: 19 Python tests plus 15 subtests passed. | Real Groq generation, news research and optional R2 integration remain unverified. The displayed article is synthetic. |
| [GitPulse](https://github.com/Sushant-Nemade/gitpulse) | Published reference and [sample dashboard](https://sushant-nemade.github.io/gitpulse/) | Local API/snapshot tests, browser checks, CI and one real public GitHub REST baseline sync. Latest local review: 20 Python tests passed. | Hosted private API, operational persistence/restore and unattended collection remain unverified or unconfigured. |
| [Doclify](https://github.com/Sushant-Nemade/Doclify) | Published reference with [public source and wheel downloads](https://github.com/Sushant-Nemade/Doclify/releases/tag/v0.3.0-reference) | Offline CLI, reviewed publication, installed-wheel checks and Linux/Windows CI. Latest local review: 39 Python tests passed; one host-permission symlink test skipped. | Live Groq inference and generated-documentation quality remain unverified. No website is required for the CLI. |
| Market Insight | Local adaptation in progress; no completed destination release or public service | Six startup/security readiness tests passed; inherited frontend compiles. | Renderer dependencies, UI/API integration, financial tools, full dependency environment, live providers and release CI still need work. |

The latest review found no known dependency vulnerabilities in the three released
local Python environments or the two released frontend dependency trees. This is
not a guarantee of future security. Market Insight has a separate unresolved
frontend audit described below.

## 1. AI Blog Publisher

### Completed Baseline

- Private drafts, strict editorial checks and digest-bound human approval.
- Local article publication with input/index validation and failure handling.
- Sanitized static reader, navigation and desktop/mobile checks.
- Reproducible dependencies, CI, Pages delivery and retained upstream MIT attribution.

### Pending Work

| ID | Work item | Classification and dependency | Completion evidence |
| --- | --- | --- | --- |
| BP-01 | Verify real Groq tutorial generation | Implemented but unverified live; owner-configured key, approved topic and provider terms/quota review | One real draft is generated, manually reviewed and published through the documented approval path; model/configuration and outcome recorded without secrets. |
| BP-02 | Verify factual quality and source accuracy | Required before describing generated articles as reviewed real content | Reviewer checks factual claims, citations and technical examples; corrections and uncertainty are retained. |
| BP-03 | Verify live news research | Conditional on using Tavily or Guardian | Configured research returns usable provenance; empty results, timeouts and provider failures do not produce fabricated news. |
| BP-04 | Verify optional R2 history/storage behavior | Conditional on selecting R2; local operation does not require it | Credentials/permissions and failure behavior are tested. Do not claim transactional cloud publication: publication currently remains a reviewed local static-site workflow. |
| BP-05 | Publish and check a real reviewed article | Depends on BP-01 and BP-02 | Successful site checks and CI deployment; deployed article renders correctly on desktop/mobile and retains review evidence. |
| BP-06 | Establish operating requirements | Conditional on operating the website as a service | Agree monitoring, availability expectations, rollback, maintenance ownership and any load checks; do not claim an unsupported uptime SLA. |
| BP-07 | Public generation or multi-user editing | Optional expansion; not implemented | Design authenticated accounts, authorization, queueing, quotas, spending controls, server-side secrets and moderation before exposing generation. |

### Deployment Position

The article reader is already public. Readers do not need an AI key or Python
backend. Generate and review content privately, then deploy only approved public
articles through the existing Pages workflow. Adding a visitor-facing generation
service is a separate scope, not a requirement for a usable article website.

**Evidence:** [Release status](https://github.com/Sushant-Nemade/ai-blog-publisher/blob/main/docs/RELEASE_STATUS.md)
and [operations](https://github.com/Sushant-Nemade/ai-blog-publisher/blob/main/docs/OPERATIONS.md).

## 2. GitPulse

### Completed Baseline

- Original implementation with atomic SQLite snapshots, stable GitHub identities,
  append-only observations and protected local API routes.
- Typed browser dashboard, safe text rendering and CSV export.
- One real public GitHub REST baseline sync; public previews retain fictional data.
- Automated tests, CI and public static preview delivery.

### Pending Work

| ID | Work item | Classification and dependency | Completion evidence |
| --- | --- | --- | --- |
| GP-01 | Verify sustained account-specific operation | Partially verified: one baseline sync; live change history is not established | Multiple approved snapshots are observed over time; timestamps are labeled observation times, not actual follow dates. |
| GP-02 | Host the private API | Not deployed; owner chooses host, budget and access model | HTTPS backend with restricted origins, secure owner authentication and a durable database path; real dashboard/API connection verified. |
| GP-03 | Verify persistence and recovery | Required before relying on hosted audience history | Restart preserves state; backup and restoration are exercised; restore limits, retention and recovery steps documented. |
| GP-04 | Enable unattended collection | Conditional; currently disabled by default | Approved scheduler runs bounded syncs; quotas, failures, alerts and snapshot preservation are checked. |
| GP-05 | Exercise real follow/loss/refollow observations | Deterministic fixtures verified; live events unverified | Subsequent real observations are reviewed without manipulating other accounts or claiming recovery of historical events. |
| GP-06 | Establish production operations | Conditional on sustained hosted use | Validate health checks, redacted logs, access policy, load expectations and disaster-recovery procedures. Docker runtime remains unverified if selected. |
| GP-07 | Multi-user accounts/OAuth/data isolation | Optional expansion; not implemented | Per-user identity, permissions, isolated histories and revocation are tested. Never distribute the owner API token to anonymous visitors. |
| GP-08 | Cloud replication or additional analytics | Optional expansion; not implemented | Evaluate licensing/permissions and storage/data requirements, then add feature-specific tests. GraphQL contribution totals and exact upstream feature parity are not current claims. |

### Deployment Position

GitHub Pages already hosts the sample dashboard, but cannot run its Python API or
maintain a private SQLite database. Real hosted use needs a separate HTTPS service
with durable storage. Until then, the authenticated local application is the
appropriate account-specific delivery route. Never publish a real database or
private snapshot as sample data.

**Standing limitation:** History starts when collection begins. Actual follower
join dates and data preceding collection cannot be reconstructed by the current
implementation and are not promised completion items.

**Evidence:** [Release status](https://github.com/Sushant-Nemade/gitpulse/blob/main/docs/RELEASE_STATUS.md)
and [operations](https://github.com/Sushant-Nemade/gitpulse/blob/main/docs/OPERATIONS.md).

## 3. Doclify

### Completed Baseline

- Bounded local discovery, strict configuration, incremental summary caching and
  digest/source-checked reviewed publication with explicit README replacement.
- Credential-free offline structural documentation and mocked Groq SDK boundary tests.
- Source-complete wheel/archive builds, checksum-listed public downloads and CI.
- Original AGPLv3 license, upstream attribution and source-availability notices retained.

### Pending Work

| ID | Work item | Classification and dependency | Completion evidence |
| --- | --- | --- | --- |
| DC-01 | Verify live Groq summarization and synthesis | Implemented but unverified live; owner-configured key and explicit upload consent | Run on synthetic or approved source; inspect generated documentation and approve/publish it; record provider/model outcome without credentials. |
| DC-02 | Evaluate documentation accuracy | Required before making quality claims about AI-generated output | Compare output with actual source behavior, installation requirements and limits; correct hallucinated claims and retain review evidence. |
| DC-03 | Evaluate adversarial source/prompt handling | Not established by existing reference tests | Adversarial fixtures cannot induce prohibited actions or confidential-data disclosure; document residual limitations rather than claiming immunity. |
| DC-04 | Review deployment-machine permissions and retention | Operational requirement for private source use | Review Windows ACLs where applicable, define artifact/cache cleanup and backup retention, and test restoration/stale-lock handling. |
| DC-05 | Stronger isolation or resource controls | Optional expansion for untrusted repositories or service use | Define and test isolation against concurrent hostile filesystem changes and whole-run resource limits. Current local-directory assumptions must remain visible. |
| DC-06 | Hosted upload-and-generate website | Optional expansion; not implemented | Authenticate users, obtain upload consent, isolate non-executing workers, bound archives/paths, define deletion/retention and quotas, and prominently offer corresponding source under AGPL obligations. |
| DC-07 | Publish a separate package-registry distribution | Optional expansion; not configured | Choose an authorized distinct package name and account, validate artifacts/provenance and preserve license/source notices. Do not publish to the upstream author's PyPI package. |

### Deployment Position

A website is not required. Users can download and install the reference CLI today,
and its offline workflow is usable. The derivative distribution is
`doclify-portfolio`; the command is `doclify`. Upstream `pip install doclify` is
not a substitute for this modified version. Real AI runs send selected source to
Groq and require explicit consent and applicable privacy/organizational approval.

**Standing limitations:** Secret screening is incomplete; local filesystem access
assumes a trusted directory; individual file writes are atomic, not a multi-file
transaction. Context character bounds are not exact token or monetary estimates.

**Evidence:** [Release status](https://github.com/Sushant-Nemade/Doclify/blob/main/docs/RELEASE_STATUS.md),
[operations](https://github.com/Sushant-Nemade/Doclify/blob/main/docs/OPERATIONS.md)
and [reference downloads](https://github.com/Sushant-Nemade/Doclify/releases/tag/v0.3.0-reference).

## 4. Market Insight

### Current Stage

Only a local readiness stage has been verified. The adaptation is not yet a
published destination repository/release and is not publicly hosted. The catalog
entry links the [upstream source](https://github.com/KalyanM45/MarketInsight), not a
completed Sushant-owned implementation.

Six tests establish credential-free health checks, protected fail-closed chat,
input bounds and explicit provider-key/origin separation. The frontend compiles
with a configurable endpoint instead of the upstream author's hosted API.
These results do not prove a complete financial-research workflow.

### Release Blockers and Pending Work

| ID | Work item | Current blocker/dependency | Completion evidence |
| --- | --- | --- | --- |
| MI-01 | Resolve renderer/SDK dependencies | Last audit: ten findings, six low/four moderate, in inherited KaTeX/Prism/C1 SDK chains; compatible automatic fixes unavailable | Select maintained dependencies or verified patches, rebuild and rerun auditing and browser compatibility/security tests. Do not suppress findings or use forced upgrades as proof of safety. |
| MI-02 | Complete UI/API/authentication integration | Frontend compilation only; the protected API and inherited SDK stream format are not verified together | Real browser tests cover authentication, queries, streaming/rendering, error states, cancellation and conversation boundaries. |
| MI-03 | Audit financial-data tools | Tool provenance, input/resource limits and error behavior are not verified end-to-end | Bound lookups, retain sources and dates, distinguish missing/stale data, and test failures without fabricated prices or forecasts. |
| MI-04 | Validate the complete backend environment | Small readiness environment tested; full upstream dependency lock unverified | Trace actual consumers, regenerate frozen dependencies, audit them and reproduce the complete application in supported environments. |
| MI-05 | Verify chosen model/data providers | No approved live credentials/budget supplied for this stage | Select provider/model, configure the matching key privately, approve costs/terms, then record an actual provider-to-UI smoke test. OpenAI credentials must not be reused for Thesys. |
| MI-06 | Complete conversation ownership | Shared persistence deliberately absent | Define supported conversation behavior; add identity-scoped storage only with tested authorization, isolation and retention. |
| MI-07 | Complete release and performance gates | Browser, full-stack, packaging and CI gates pending; inherited main JavaScript chunk roughly 2.9 MB | Reduce or justify delivery costs; run required checks, document limitations and publish an attributed GPLv3 reference only after gates pass. |
| MI-08 | Operate a hosted application | Not deployed; separate from reference publication | Select frontend/backend hosting, authenticated access, server-side secrets, quotas, monitoring and rollback; verify deployment without exposing an anonymous paid endpoint. |

### Required Sequence

1. Resolve MI-01 and select the supported renderer/provider protocol.
2. Complete MI-02, MI-03, MI-04 and supported conversation behavior.
3. Configure approved live accounts and perform MI-05, or explicitly deliver a
   separately verified sample mode without claiming live AI/data operation.
4. Complete MI-07 and publish the tested reference with GPLv3 attribution.
5. Complete MI-08 only if a hosted-service scope and budget are approved.

No trading execution, personalized investment advice, forecasting accuracy or
investment-performance guarantee is included in the current stage.

## Cross-Project Owner Decisions

| Decision | Why it is needed | Responsible role |
| --- | --- | --- |
| Portfolio references, private owner tools or public multi-user products | Determines whether existing delivery is sufficient or new identity/hosting work is required | Portfolio owner |
| Provider account, model, terms and cost limits | Real verification cannot use unspecified credentials or unapproved paid services | Account owner, with maintainer implementing controls |
| Hosting account, region, budget and durable storage | Determines HTTPS, persistence, privacy and operating responsibilities | Hosting/account owner |
| Data/source-upload permission and retention | Private code, account data and research inputs must not be published or uploaded without approval | Data owner and maintainer |
| Maintenance and incident/rollback ownership | A public service needs operational responsibility beyond a successful build | Maintainer/hosting owner |

At the latest review, required live-provider credentials were not configured in
the reviewed local environments. Credentials must be entered locally or through
an appropriate secret manager, never in chat, committed source or this register.

## Completion and Evidence Policy

- Complete tasks only after the corresponding acceptance evidence is recorded.
- Track reference release, live integration and hosted operation independently.
- Record the relevant commit, dependency lock, commands, environment and review date.
- Keep synthetic previews clearly labeled; model mocks are not live-provider proof.
- Preserve upstream attribution and the applicable MIT/GPL/AGPL license notices.
- Recheck audits before release; passing checks do not establish an uptime SLA or
  permanent security, privacy, factual-accuracy or domain-suitability guarantee.
- Work on one new gallery candidate at a time. Do not count the ten other planned
  candidates as implemented projects or start another while Market Insight is active.

## Related Documents

- [Project catalog](../README.md)
- [Release and deployment checklist](RELEASE_CHECKLIST.md)
- [Public portfolio](https://sushant-nemade.github.io/)

Update this register when implementation, configuration, verification or
deployment status changes. Optional expansions remain uncommitted scope until
explicitly selected; no future release dates or automatic daily execution are promised.