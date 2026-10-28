# Public Demo Hosting

Reviewed: 2026-10-27. Current security-patched primary builds use GitHub Pages.
Cloudflare project `sushant-ai-demos` contains four older manually pinned mirrors.

**Do not treat the Cloudflare snapshots as current security builds.** They were
not republished with the latest dependency repairs because deployment authentication
was unavailable. Primary catalog/profile/portfolio links now select verified current
GitHub Pages builds instead. Historical directory: https://sushant-ai-demos.pages.dev/

| Project | Current primary public URL | Historical snapshot or downloads |
| --- | --- | --- |
| AI Blog Publisher | https://sushant-nemade.github.io/ai-blog-publisher/ | Older mirror: https://sushant-ai-demos.pages.dev/ai-blog-publisher/ |
| GitPulse | https://sushant-nemade.github.io/gitpulse/ | Older mirror: https://sushant-ai-demos.pages.dev/gitpulse/ |
| Market Insight | https://sushant-nemade.github.io/MarketInsight/ | Older mirror: https://sushant-ai-demos.pages.dev/MarketInsight/ |
| TravelBrain | https://sushant-nemade.github.io/TravelBrain/ | Older mirror: https://sushant-ai-demos.pages.dev/TravelBrain/ |
| Airbnb Price Workbench | https://sushant-nemade.github.io/airbnb-price-workbench/ | [Verified downloads](https://github.com/Sushant-Nemade/airbnb-price-workbench/releases/tag/v0.1.0-reference); no second hosted mirror |
| Boston Housing Research Workbench | https://sushant-nemade.github.io/boston-housing-workbench/ | [Verified downloads](https://github.com/Sushant-Nemade/boston-housing-workbench/releases/tag/v0.1.1-reference); historical research only |
| Doclify | [CLI and source downloads](https://github.com/Sushant-Nemade/Doclify/releases/tag/v0.3.0-reference) | [Repository](https://github.com/Sushant-Nemade/Doclify) |

## Hosting Choice

The current browser references run on GitHub Pages, with actual browser-local
ONNX inference for Airbnb and Boston. Four earlier snapshots remain on Cloudflare.
Neither delivery is a tunnel to a laptop. Local terminals can close and the computer can be switched off.
The production hostname remains stable between deployments while the account
and project remain active. No domain purchase, paid plan, cloud database, API
key or public local-server ingress was required. Free-service terms and limits
still apply; this is not an uptime SLA or a promise of permanent hosting.

A named tunnel can preserve a hostname, but does not keep its origin online.
It needs a continuously running origin/connector, suitable domain routing and
access controls. A quick trycloudflare URL is not an appropriate persistent
portfolio link. Neither kind was installed or exposed here.

## What Is Public

- Blog Publisher: a synthetic article reader, not anonymous AI generation.
- GitPulse: fictional audience/dashboard data, not the owner's real database.
- Market Insight: fictional research data, not a public paid market/AI endpoint.
- TravelBrain: a functional browser-local planner with illustrative budgets;
  private SQLite, live weather and Groq features still need the private server.
- Doclify: an installable CLI, not an invented hosted upload-and-generate service.
- Airbnb Price Workbench: an actual trained historical NYC2019 model, uncertainty,
  browser-local CSV/scenarios and exports, not current rental quotes or bookings.
- Boston Housing Research Workbench: an actual historical tract-median model,
  not individual/current housing valuation or lending/allocation decisions.

All four newly primary GitHub Pages URLs returned HTTP200 after current successful
CI/deployments. The actual hosted Blog Publisher sanitizer reports DOMPurify3.4.17.
Boston's public desktop/mobile model/photo/chart and layout checks passed. The
maintenance evidence console and portfolio were independently checked on desktop/mobile.

The Airbnb GitHub Pages deployment was independently verified on desktop/mobile,
including all30 authored sklearn parity scenarios, batch export, chart pixels,
legal notices and private-path404 responses. The Cloudflare account required
sign-in during this release; its existing four-project collection was not changed
and no unverified fifth Cloudflare URL is advertised. Its manual bundle remains
a reviewed snapshot, not automatic synchronization of every new project.

Browser storage belongs to each host/origin; saved trips do not automatically
migrate between Cloudflare, GitHub Pages and localhost. Export them when needed.
Private owner tokens, provider keys, reports, SQLite files, source-upload flows,
and local API ports are not published. HTTPS and basic response headers are set;
hosting alone does not establish factual accuracy or production certification.

## Reproduce the Bundle

This command reproduces the builder's **historical pinned selection**, not the
latest security-patched sources. Review and update every `DEMO_BUILDS` pin first
before using its output for any new deployment. Do not blindly redeploy old artifacts.

From this repository, using Python 3.13+ and an authenticated GitHub CLI account
with access to the public repositories' Actions artifacts:

```sh
python -m unittest discover -s tests -v
python -m tools.public_demos
```

The builder downloads **successful owner-repository Pages artifacts**, records
their commit/run/archive SHA-256 in `deployment.json`, preserves subpaths and
license/font/photo notices, and creates:

```text
build/cloudflare/public-demos.zip
build/cloudflare/site/
```

Only these generated output paths are owned by the builder. Do not use its output
directory for private or manually maintained files. The bundle rejects traversal,
links, duplicate paths, server handlers, environment/database files and oversized
archives. The exact development-only `js/config.js.example` template is omitted
and that choice is recorded; runtime `config.js` and all license notices remain.
No automated secret detector can guarantee arbitrary inputs are secret-free:
review the selected source/build evidence and resulting public assets too.

## Deploy and Update

1. Review the intended source commit and its successful CI/Pages runs. Update
   `DEMO_BUILDS` in `tools/public_demos.py` to those explicitly selected run IDs.
   Mirrors are pinned snapshots, not automatically synchronized to arbitrary main changes.
2. If GitHub's short-lived Pages artifact expired, rerun that Pages deployment
   only after checking it still represents the intended current main revision.
   Never redeploy an old run blindly: that could roll back the GitHub fallback.
   For newer code, select the newer successful run instead.
3. Run the builder and tests. Inspect the generated provenance and file set;
   keep private/local data out of the output. Preserve project licenses and notices.
4. In Cloudflare Workers & Pages, open `sushant-ai-demos`, create a production
   deployment and upload the ZIP. Review the complete uploaded-file summary,
   then deploy. The initial deployment used the authenticated browser, not a
   token copied into chat or committed source.
5. Verify the stable hostname, all four subpaths, articles/assets/charts, planning,
   saving/export, source/license links and desktop/mobile layouts. Check that
   environment/database/private API paths still fail. Promote portfolio links
   only after these checks pass.

Keep the last verified bundle and provenance for rollback. Use Cloudflare's
deployment rollback or redeploy that reviewed ZIP; retain the GitHub Pages links
as independent fallbacks. Deleting this Pages project or changing the hostname
requires updating all published links first. No scheduled publishing was enabled.

## Observed Verification

The initial deployment accepted 131 files. Ten actual hosted browser checks
covered the directory plus four demos at 1440px and 390px: all loaded with no
horizontal overflow, visible images and nonblank charts. TravelBrain generated
a Lisbon plan, saved it locally and exported JSON; the Blog Publisher article
opened correctly. Five environment/database/private-API paths returned404 on
each viewport. The source artifacts contain no Python backend or private state.

The public `deployment.json` is the source/build provenance record, not a secret.
The related portfolio/profile links are maintained separately from private
provider verification and any future authenticated managed backend deployment.