# Project Status and Pending Work Register

**Portfolio owner:** Sushant Nemade  
**Last updated:** 2026-10-28

**Scope:** AI Blog Publisher, GitPulse, Doclify, Market Insight, TravelBrain, Airbnb Price Workbench, Boston Housing Research Workbench, and portfolio maintenance

**Purpose:** Record remaining implementation, verification, deployment and owner decisions without overstating readiness.

## Executive Summary

Seven projects are published as tested reference implementations. Market Insight's
implementation/release gates are complete; paid model inference and managed
private hosting remain separate boundaries. Public synthetic browser references
are available for Blog Publisher, GitPulse and Market Insight; Doclify is
distributed as an installable CLI with public source and wheel downloads.
TravelBrain adds a complete browser/private planning workflow for three catalog
cities, illustrative budgets and optional weather/AI. It is not a worldwide
booking or live-fare service.
Airbnb Price Workbench adds an original MIT implementation with separately
licensed NYC2019 data, host-disjoint evaluation and real browser ONNX predictions.
Its historical benchmark is not a current-market price or revenue guarantee.
Boston Housing adds a GPLv3 historical research adaptation with real browser
ONNX inference. It estimates old tract medians, not individual/current houses;
its nonstandard OpenML rights metadata and historic bias are explicitly retained
as limitations rather than presented as commercial/fairness clearance.

The first three projects retain their 2026-10-14 evidence snapshot. Market Insight
was updated with its 2026-10-17 implementation and release evidence; TravelBrain
records its 2026-10-18 release review below; Airbnb records its 2026-10-20 release.
This update does not claim a new
live-provider evaluation of the other projects.

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
| [Market Insight](https://github.com/Sushant-Nemade/MarketInsight) | Published GPLv3 workbench and [synthetic reference](https://sushant-nemade.github.io/MarketInsight/) | 37 Python tests, 20 browser cases, installed-package checks, Linux/Windows CI and non-root container checks. Real Yahoo quote/history verified. | Paid AI inference, individual live financial endpoint availability and managed private hosting remain operator/provider boundaries. |
| [TravelBrain](https://github.com/Sushant-Nemade/TravelBrain) | GPLv3 planning workbench and [illustrative reference](https://sushant-nemade.github.io/TravelBrain/) | 27 Python tests, 27 browser/server parity combinations, 14 browser cases, installed wheel/source checks, clear dependency audits and a real Open-Meteo forecast. | Groq inference, commercial weather arrangements and managed private hosting remain conditional. No live flight/hotel availability or booking is implemented. |
| [Airbnb Price Workbench](https://github.com/Sushant-Nemade/airbnb-price-workbench) | Original MIT project and [actual browser model](https://sushant-nemade.github.io/airbnb-price-workbench/) | 18 Python tests, 16 browser cases, 30 authored sklearn/browser parity scenarios, real-data training reproduction, installed packages, Linux/Windows/container gates and audits pass. | NYC2019 filtered scope only; no temporal/current-market, revenue or individual-coverage guarantee. |
| [Boston Housing Research Workbench](https://github.com/Sushant-Nemade/boston-housing-workbench) | GPLv3 adaptation and [actual browser model](https://sushant-nemade.github.io/boston-housing-workbench/) | 30 Python tests, 8 browser cases, 20 authored parity probes, independently reproduced training, clean installed wheel/source, Linux/Windows/container gates, audits and public desktop/mobile smoke pass. | Historical tract medians only; random split, capped targets, residual bias and nonstandard Public data-license label. Not for current housing decisions. |

### Public Access Update

The four earlier web references also have historical snapshots on Cloudflare Pages,
independently of local computers or tunnels. Those manually pinned mirrors were
not refreshed during this security update. The catalog/profile/site primary URLs
now point to the current verified GitHub Pages builds above; the actual hosted
Blog Publisher sanitizer is patched DOMPurify3.4.17. Cloudflare is not advertised
as a current security-patched fallback. Doclify remains a downloadable CLI.
Airbnb Price Workbench is separately hosted on GitHub Pages. Its public model
works without a local computer or Python server; the existing Cloudflare
collection was not changed because account sign-in was unavailable this session.
Ten desktop/mobile hosted checks passed, including nonblank charts, article
navigation and TravelBrain plan/save/export. Private API, database and environment
paths were rejected. No local API or paid provider endpoint was exposed.

See [public hosting and update/rollback runbook](PUBLIC_DEMOS.md) for selected
source builds, artifact expiration, safety checks and manual production updates.
This changes public-reference hosting, not any live-provider/private-hosting
boundary recorded below. That hosting update did not enable paid services or
unattended application publication. The separately activated reviewed-maintenance
system is described below; it does not operate the optional live providers.

Recorded audits found no known dependency vulnerabilities in the tested released
dependency sets. Market Insight's formerly affected renderer chain was removed;
its frontend and Python audits pass. Recheck before subsequent releases; this is
not a guarantee of future security.

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

The completed [destination implementation](https://github.com/Sushant-Nemade/MarketInsight)
preserves the upstream history and GPLv3 license. It replaces the inherited SDK
and unrestricted agent flow with a typed financial research workspace, bounded
provider access, private SQLite reports and optional grounded synthesis.

The complete sample workflow and private API integration are verified, not only
startup. A real Yahoo Finance quote and 251 history rows were also verified with
TLS enabled. The [public reference](https://sushant-nemade.github.io/MarketInsight/)
contains authored fictional companies, never the real smoke-test dataset.

### Gate Resolution and Remaining Boundaries

| ID | Work item | Current blocker/dependency | Completion evidence |
| --- | --- | --- | --- |
| MI-01 | Resolve renderer/SDK dependencies | Completed: C1/KaTeX/Prism renderer chain removed; maintained React/Chart.js/Lucide/Zod stack | Frontend audit, lint, runtime contracts and browser tests pass. |
| MI-02 | Complete UI/API/authentication integration | Completed as a structured JSON workflow, not the obsolete SDK stream | Actual browser tests verify research, owner connection, saved report reopening/deletion, export and errors on desktop/mobile. |
| MI-03 | Audit financial-data tools | Completed bounded adapter with dates, explicit missing tables, reporting currency and origin/request limits | Provider fixtures and real quote/history smoke passed. Individual vendor endpoints may still be restricted or unavailable; this is not fabricated or hidden. |
| MI-04 | Validate complete backend environment | Completed frozen backend/frontend locks; unused tracing/agent dependencies removed | Linux/Windows tests/audits and installed-wheel/source checks pass. |
| MI-05 | Verify chosen model/data providers | Data quote/history verified; paid AI inference remains unverified and conditional | SDK MockTransport tests verify grounding, fixed origins, token bounds and redaction. Owner must approve/configure paid live synthesis before claiming real model-backed evaluation. |
| MI-06 | Define research ownership | Completed single-owner report model; shared conversation checkpoints retired | Authenticated SQLite records retain questions/provenance and bounded history. Multi-user identity/conversation persistence remains optional separate scope. |
| MI-07 | Complete release/performance gates | Completed reference gates; main JS roughly 485 KB rather than ~2.9 MB | 37 Python tests, 20 browser cases, package checks, Linux/Windows CI and non-root container verification pass. |
| MI-08 | Operate a hosted application | Public fictional reference provided; managed private backend hosting remains optional/unconfigured | Operator chooses HTTPS hosting, access/secrets policy, durable storage, backup and monitoring before exposing private live research. |

### Remaining Operator Work

1. Configure an approved model/account/budget and record paid inference evidence
  only if real AI synthesis is selected. Sample/evidence workflows do not need it.
2. Recheck financial endpoint availability and provider/data rights for intended use.
3. Complete managed private hosting only if that service scope is selected.
4. Maintain dependency audits and human interpretation of financial/model output.

Implementation evidence: [Market Insight release status](https://github.com/Sushant-Nemade/MarketInsight/blob/main/docs/RELEASE_STATUS.md).

The [reference prerelease](https://github.com/Sushant-Nemade/MarketInsight/releases/tag/v0.2.0-reference)
includes the verified wheel/source archives and SHA-256 checksums at commit
`07e51ed048e19610c572b6acfe12a54769ebe0b9`.
[Final CI](https://github.com/Sushant-Nemade/MarketInsight/actions/runs/39065844114)
and [Pages deployment](https://github.com/Sushant-Nemade/MarketInsight/actions/runs/39066236450)
passed. The public site was checked at its real repository path on desktop/mobile,
including nonblank chart pixels and all nine dependency license notices.

No trading execution, personalized investment advice, forecasting accuracy or
investment-performance guarantee is included in the current stage.

## 5. TravelBrain

### Completed Baseline

- Attributed GPLv3 fork preserving upstream history and source
  `59db5bb0f1aeebd593a5114c67f8e619afceb25a`.
- Paris/Lisbon/Kyoto catalog; 1-10 days, 1-8 travelers, interests, pace and activity exclusions.
- Source-linked, non-repeating itinerary slots; explicit unallocated time when
  catalog coverage is insufficient, not invented places or opening hours.
- Exact minor-unit budgets with illustrative allowances/FX, exclusions and over-budget warnings.
- Browser-local saved trips plus authenticated private SQLite create/update/reopen/delete;
  stale revisions fail visibly. JSON/Markdown export and printing work.
- Optional fixed-origin Open-Meteo and Groq adapters with bounded responses,
  timeouts, concurrency, requests and output; no browser provider-key/database intake.
- Twenty-seven Python tests, including 27 cross-runtime planning combinations;
  fourteen desktop/mobile browser cases and an installed wheel outside checkout pass.
- A real two-day Paris forecast was observed through the actual adapter at
  2026-10-17T23:59:13+00:00 with TLS verification enabled. No raw forecast was published.

### Remaining Boundaries

| ID | Work item | Classification | Acceptance evidence |
| --- | --- | --- | --- |
| TB-01 | Verify live Groq commentary and quality | Conditional on approved account/model/budget and trip-data upload consent | A real bounded response is checked against itinerary evidence; unsupported advice is corrected. Mocks are not live-inference proof. |
| TB-02 | Confirm itinerary details before travel | User/provider boundary, not a completed live-data claim | Opening hours, reservations, prices, transfers and accessibility are independently checked with current authoritative sources. |
| TB-03 | Operate a private hosted service | Optional/unconfigured | HTTPS, restricted access, durable storage, permissions, exercised restore, retention and maintenance ownership are established. |
| TB-04 | Broaden cities, live fares or bookings | Optional expansion, not implemented | Review data/provider rights, reliability and domain-specific evaluation before adding each capability. Do not promise worldwide support or transactions. |
| TB-05 | Commercial weather use | Conditional on intended use | Review Open-Meteo hosted API terms, quota and any required commercial arrangement; current free adapter uses non-commercial terms and visible attribution. |

Public trips contain authored planning data, illustrative prices and no private
records. Source links identify places, not verified availability or prices.
Step-free filtering is a preference, not an accessibility certification. Free-text
notes are retained but not interpreted by the deterministic constraint engine.

Evidence: [release status](https://github.com/Sushant-Nemade/TravelBrain/blob/main/docs/RELEASE_STATUS.md),
[reference downloads](https://github.com/Sushant-Nemade/TravelBrain/releases/tag/v0.2.1-reference)
and [verification workflow](https://github.com/Sushant-Nemade/TravelBrain/actions/runs/39083316338).

Source commit `67b224b130917ac22b1f0e7b3cfcb43f6a9a6e57` passed Linux 3.11/3.13,
Windows 3.13 and the non-root container HTTP gates. The
[public deployment](https://github.com/Sushant-Nemade/TravelBrain/actions/runs/39083633992)
passed; the real repository-path site was checked on mobile, including local
photo/notices and successful Kyoto itinerary generation. The prerelease contains
the successful CI's wheel/source assets and SHA-256 checksums.
Version 0.2.1 corrects the earlier Lisbon image with a verified Wikimedia photo,
visible creator/CC BY 4.0 credit and five bundled notice records. Package checks
select the current version and reject stale/missing UI assets. Version 0.2.0 is
marked superseded; its original tag and archives were not silently replaced.

## 6. Airbnb Price Workbench

### Completed Reference

- Original MIT code/model; no code, data, saved model or assets imported from the
  unlicensed gallery reference at `2b6dc21406cfe0a24d303d1db12505403abed52e`.
- Separately reviewed Kaggle NYC2019 version3, publisher CC0/Inside Airbnb credit,
  checksum-pinned fetch, 48,895 source/47,924 eligible rows. Raw rows and identifiers
  are not redistributed; published parity scenarios are authored examples.
- Host-disjoint train/selection/calibration/test partitions. Test7,092 listings:
  MAE48.80 USD versus52.66 borough/room median and69.51 global median; RMSE90.71,
  R-squared0.357. Historical interval coverage90.81%, mean width201.81 USD.
- Actual ONNX model in Python and browser; integrity bounds/checksum, single-input
  and local CSV prediction, saved browser scenarios, evidence and JSON/CSV exports.
- Eighteen Python and sixteen browser cases pass; all30 authored sklearn parity
  scenarios agree within3 cents on desktop/mobile. Audits, installed artifacts,
  Linux3.11/3.13, Windows3.13, non-root Docker and actual-data retraining gates pass.
- Source `b6cf6931dc4d47f8617656e11352757ec989c2df`,
  [CI39344597914](https://github.com/Sushant-Nemade/airbnb-price-workbench/actions/runs/39344597914),
  [Pages39344969201](https://github.com/Sushant-Nemade/airbnb-price-workbench/actions/runs/39344969201)
  and the [verified source/wheel release](https://github.com/Sushant-Nemade/airbnb-price-workbench/releases/tag/v0.1.0-reference)
  are published. The real repository-path browser app passed parity/export/image/
  chart/layout/notice/private-path checks on desktop/mobile.

### Remaining Boundaries

| ID | Work item | Classification | Acceptance evidence |
| --- | --- | --- | --- |
| AP-01 | Newer data/current-market evaluation | Optional new scope; required before current-price claims | Review rights/source, retrain and evaluate defensible temporal and geographic holdouts; retain drift/uncertainty evidence. |
| AP-02 | Stronger interval/group validation | Required before stronger coverage claims | Evaluate dependence, segment coverage and distribution shift. Current empirical marginal coverage is not an individual guarantee. |
| AP-03 | Managed remote Python API | Optional; public browser inference already works | Define HTTPS/access/global quotas/logging/monitoring before exposing server-side inference. No paid endpoint or database is needed for the current app. |
| AP-04 | Cloudflare mirror | Optional; existing collection requires account sign-in | Build/upload only a reviewed static model/runtime bundle with matching notices, verify it publicly, then advertise its actual URL. Current GitHub Pages URL is already public. |

No booking, live Airbnb integration, current legal/zoning eligibility, causal
pricing strategy, income guarantee or housing/lending decision use is claimed.
See [model card](https://github.com/Sushant-Nemade/airbnb-price-workbench/blob/main/docs/MODEL_CARD.md)
and [operations](https://github.com/Sushant-Nemade/airbnb-price-workbench/blob/main/docs/OPERATIONS.md).

## 7. Boston Housing Research Workbench

### Completed Reference

- Actual GPLv3 fork preserving history and upstream commit
  `61515c0c4e70fca380728d8752048d38e48eeefa`; legacy pickle models are never loaded.
- Pinned OpenML 531 version1 bytes, SHA-256 verified before parsing. No raw ARFF
  or training rows are bundled; published parity scenarios are authored inputs.
- Eleven strict named finite inputs, excluding B and LSTAT. Train323/calibration81/
  test102; five-fold selection only within training. Historical test MAE $2,000.09
  versus $5,882.35 training-median baseline, R-squared0.8518. Nominal90% historical
  band coverage96.08%; this is not an individual/current-price guarantee.
- Actual Python/browser ONNX inference with verified hashes, local saved scenarios,
  bounded CSV batches, evidence/provenance views and safe exports.
- Thirty Python tests and eight desktop/mobile browser cases, independent training,
  audits, non-root container and clean installed wheel/source checks pass. TDD
  regressions include unknown/excluded input rejection, unsafe model-entry removal
  and the installed static-file ASGI disconnect lifecycle.
- [Verified source/wheel release](https://github.com/Sushant-Nemade/boston-housing-workbench/releases/tag/v0.1.1-reference)
  at source `b5a9c0e04f7ad449f207964a4cf77c7a218b217b`,
  [CI40602904407](https://github.com/Sushant-Nemade/boston-housing-workbench/actions/runs/40602904407),
  [Pages40603092891](https://github.com/Sushant-Nemade/boston-housing-workbench/actions/runs/40603092891)
  and actual public desktop/mobile model smoke all pass.
- Real local load report: 1,000 total synthetic journeys, 3,000 checked requests,
  measured peak16 active, zero failed journeys; not 1,000 simultaneous humans or
  browsers. P95~1.41s/P99~1.62s with tracing. Native ONNX memory is not measured by
  Python traced-allocation figures. Hardware-specific evidence, not a capacity SLA.

### Remaining Boundaries

| ID | Boundary | Acceptance before stronger use |
| --- | --- | --- |
| BH-01 | Dataset rights | OpenML reports Public, a nonstandard label. No CC/OSI/commercial clearance is inferred. Obtain appropriate data-rights review before noneducational use. |
| BH-02 | Historic bias and geographic dependence | Excluding B/LSTAT does not establish fairness. New representative data, geographic/temporal evaluation and domain/legal review are required before considering any real housing use. Current app explicitly forbids valuation/lending/allocation decisions. |
| BH-03 | Target censoring and uncertainty | MEDV is top-coded at $50,000; estimates/bands are clipped to 5-50 thousand historic USD. Historical empirical coverage is not individual or shifted-distribution coverage. |
| BH-04 | Optional hosted Python service | Browser inference is already public. A remote API needs HTTPS, edge rate limits, resource budgets and an operator; none is advertised as currently hosted. |

## 8. Daily Reviewed Maintenance

**Activated:** the seven released gallery projects have active
`Daily Reviewed Maintenance` workflows at **12:00 noon Europe/Berlin**, pinned to
controller `e205849fa00bfcafb83b1bc645ae26e9ca378b47`, including immutable executed-RED
repair evidence, a separately pinned larger reviewer and explicit proof-gated
deployment recovery. All callers use the same seven-project registry and guarded
delivery policy. A shared Berlin-date round robin
selects one project per day; 2026-10-28 starts with Blog Publisher, followed by
GitPulse, Doclify, Market Insight, TravelBrain, Airbnb and Boston. Starts are
best-effort GitHub schedules, not exact-time or availability guarantees.

Actual [TravelBrain pilot40596897772](https://github.com/Sushant-Nemade/TravelBrain/actions/runs/40596897772)
passed 27/27 tests, 4/4 integration cases and 1,000/1,000 serial offline itinerary
journeys, with zero observed failures/errors/skips. Real isolated model planning
and author inference returned **no-safe-change**: no code improvement, PR, security
remediation or deployment was invented. The [durable actual report](https://github.com/Sushant-Nemade/TravelBrain/blob/maintenance-reports/latest.json)
records counts, source SHA, workload limits and model-response provenance.

The security-fixed toolchain was also exercised by
[pilot40602640097](https://github.com/Sushant-Nemade/TravelBrain/actions/runs/40602640097):
27 tests, four integration cases, 1,000 serial journeys and real inference again
completed with no-safe-change. No PR/improvement was manufactured.

The later [real repair pilot40621360289](https://github.com/Sushant-Nemade/TravelBrain/actions/runs/40621360289)
demonstrated an actual negative-budget regression, GREEN 2/2, final 29/29 tests,
4/4 integration cases and 1,000 serial journeys both before and after the change
with zero failures. A separately pinned 7B reviewer approved it.
[Bot PR5](https://github.com/Sushant-Nemade/TravelBrain/pull/5) passed complete
independent CI and was merged by
[trusted reconciliation40623354813](https://github.com/Sushant-Nemade/TravelBrain/actions/runs/40623354813),
not a routine human merge, producing `c79ed99baa98235fa0717b803a1c32feb93228cc`.
[Full post-merge CI40623391622](https://github.com/Sushant-Nemade/TravelBrain/actions/runs/40623391622)
passed. The suppressed Pages callback was then fixed with explicit verified-run
promotion; the [versioned delivery report](https://github.com/Sushant-Nemade/TravelBrain/blob/maintenance-reports/runs/maintenance-2026-10-28-pilot-40621360289.json)
preserves the original merge and separately verified current deployment revision.
Controller [CI40660929643](https://github.com/Sushant-Nemade/autonomous-quality-redteam-harness/actions/runs/40660929643)
passed 69 tests on all three Python/OS jobs plus the existing security/package gates.
The final protected workflow-only main `a5c793ca3e912dbeb8405edfdfaef78017ead0ee`
retains the agent merge and passed
[main CI40662028220](https://github.com/Sushant-Nemade/TravelBrain/actions/runs/40662028220)
and [proof-gated Pages40662530170](https://github.com/Sushant-Nemade/TravelBrain/actions/runs/40662530170).
[Trusted housekeeping40662759511](https://github.com/Sushant-Nemade/TravelBrain/actions/runs/40662759511)
then recorded **deployed**, checking the successful deployment job rather than
assuming a green CI run meant publication.

The system performs genuine baseline tests/integration, bounded local workloads,
small approved-function proposals, behavioral RED-before-change, GREEN, separate
review contexts and at most two repairs, then final regression/workload gates.
A separate trusted publisher can open a reviewed PR and explicitly dispatch normal
CI, while generated code runs without credentials or network. Global/per-project
stop controls, date deduplication, pending-PR avoidance, durable sanitized reports
and a 15:00 Berlin missing/blocked-evidence monitor are implemented.

**The owner authorized guarded unattended delivery on 2026-10-28.** Every project
requires its exact existing CI jobs on protected main, strict base freshness,
administrator enforcement, PR-only/linear history and no force pushes/deletions.
A separate trusted exact-SHA guard can merge only the approved bounded bot candidate
after matching real RED/GREEN/review evidence and complete independent CI. Routine
manual approval/start is not required. The merged main SHA receives another full CI
run; only successful current-main push/dispatch verification can deploy. Delivery
events and a six-hour bounded reconciliation handle missed events and limited retries.
Six Pages workflows accept an explicit successful-main CI run ID. A separate
read-only guard validates owner, workflow, event, exact current SHA and the complete
successful job set before checkout. Main is checked again just before deployment.
Missing Pages callbacks receive at most two dispatch attempts; failed deployment
receives one retry. A skipped deployment is never reported as delivered.
No self-review or bypass of checks is permitted. Safety/platform failures stop
promotion rather than being silently accepted.

Cloudflare snapshots remain manual, and Doclify release/PyPI publication is not
automatically performed. Automated open-weight model review is not an independent
human pentest or expert-security substitute. No paid AI credential
or inference endpoint is used; GitHub compute/storage policies still apply.

Six workload profiles are serial repeated existing regression journeys with
documented mocks/fixtures, not 1,000 concurrent users; Boston uses 1,000 total
journeys with a maximum16-worker profile. Only TravelBrain's complete unattended
path and Boston's separate real load run were exercised before activation; the
other per-project adapters are configured for their selected days, not falsely
reported as already live-tested. Existing project CI remains mandatory.

The previous harness's fixed counts, claimed remediation dialogue and load numbers
are explicitly labeled legacy fixtures, not operational evidence. Its old
three-trigger 09:00 replay workflow is now manual-only.

Operations, budgets, source/model pins, stop/recovery and actual activation evidence:
[maintenance runbook](https://github.com/Sushant-Nemade/autonomous-quality-redteam-harness/blob/main/docs/MAINTENANCE_OPERATIONS.md).
The [public evidence console](https://sushant-nemade.github.io/autonomous-quality-redteam-harness/)
displays actual per-project reports; missing or blocked evidence is not a pass.

### Security Maintenance At Activation

Existing ordinary CI exposed newer advisory data after the earlier reference
snapshots. Only affected certifi/filelock/opentelemetry-api locks were refreshed;
DOMPurify3.4.17 and Zod4.6.7 replaced the affected frontend versions. CI/container
tools now use fixed uv0.13.4. No audit suppression or release-gate bypass was added.
Doclify retains Python3.10: a verified compatible pre-affected filelock3.20.3 is
constrained only there; newer Python uses the patched current release. Its actual
Python3.10 audit and 39 tests passed, with one Windows symlink-permission skip.
Other affected projects' existing local suites and known-vulnerability audits passed.

Airbnb retraining also exposed CPU-kernel drift: Linux MAE49.51 versus reference48.80.
Pinning its reproduction job to the verified reference Haswell BLAS kernel restored
the unchanged tolerance without changing saved weights, dataset, splits or metrics.
Controlled local reproduction exactly matched the recorded MAE, and
[Linux/Windows/container/reproduction CI40603723402](https://github.com/Sushant-Nemade/airbnb-price-workbench/actions/runs/40603723402)
passed. The published historical model was not replaced.

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
- Work on one new gallery candidate at a time. Seven other candidates remain planned,
  not implemented. Do not start another candidate without a later explicit request.

## Related Documents

- [Project catalog](../README.md)
- [Release and deployment checklist](RELEASE_CHECKLIST.md)
- [Public portfolio](https://sushant-nemade.github.io/)

Update this register when implementation, configuration, verification or
deployment status changes. Optional expansions remain uncommitted scope until
explicitly selected. Reviewed maintenance is activated as described above; exact
future start times, daily code improvements, release dates and production SLAs
are not promised.