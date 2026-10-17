# Projects

Sushant Nemade's categorized AI project portfolio.

Discovery source: [https://github.com/KalyanM45/AI-Project-Gallery](https://github.com/KalyanM45/AI-Project-Gallery). Eligibility snapshot: 2026-10-06.

One project is implemented at a time. Source-gallery end-to-end checkmarks are eligibility signals, not production certification.
Planned entries are links only: their code, data, model licenses and runtime still require audit.

## Published Reference Implementations

### [AI Blog Publisher (BlogBoard)](https://github.com/Sushant-Nemade/ai-blog-publisher)

Primary category: **Generative and Agentic AI**. Portfolio placement: **Responsible automation**.
Source: [https://github.com/KalyanM45/Multi-Agentic-Blog-Generation](https://github.com/KalyanM45/Multi-Agentic-Blog-Generation); license: MIT; upstream revision: `8b743e21ac0e940dc8bd159f5d94a8f5eb17c630`.
Verification: Offline workflow, Linux/Windows CI and hosted browser checks passed; live AI/search/R2 integrations unverified.
[Synthetic reference demo](https://sushant-nemade.github.io/ai-blog-publisher/)

### [GitPulse: Audience Workspace](https://github.com/Sushant-Nemade/gitpulse)

Primary category: **Data and Developer Tools**. Portfolio placement: **Trustworthy data and developer tools**.
Concept reference: [https://github.com/KalyanM45/GitPulse](https://github.com/KalyanM45/GitPulse); source license: unverified MIT claim. No upstream code imported; original implementation license: MIT; specification revision: `8af259174045fce5c081b36e36b407df82834823`.
Verification: Original code; strict typing, security audits, desktop/mobile tests, Linux/Windows CI, hosted fictional demo and one public GitHub REST sync verified. Hosted private API remains unverified.
[Synthetic reference demo](https://sushant-nemade.github.io/gitpulse/)

### [Doclify](https://github.com/Sushant-Nemade/Doclify)

Primary category: **Data and Developer Tools**. Portfolio placement: **Trustworthy data and developer tools**.
Source: [https://github.com/KalyanM45/Doclify](https://github.com/KalyanM45/Doclify); license: AGPL-3.0-only; upstream revision: `93dfd6632929e0b1dc4b10b1ff0f2115aa890d01`.
Verification: Attributed AGPLv3 derivative; offline CLI, safe caching, reviewed publication, installed wheel/source checks, Linux 3.10/3.13 and Windows 3.13 CI and dependency audits passed. SDK tests use mocked responses; live Groq inference unverified.
[Download the reference CLI and source](https://github.com/Sushant-Nemade/Doclify/releases/tag/v0.3.0-reference)

### [Market Insight Research Workbench](https://github.com/Sushant-Nemade/MarketInsight)

Primary category: **Generative and Agentic AI**. Portfolio placement: **Trustworthy data and developer tools**.
Source: [https://github.com/KalyanM45/MarketInsight](https://github.com/KalyanM45/MarketInsight); license: GPL-3.0-only; upstream revision: `7fae6d81d09810273fa30f7f50003f42dc51646a`.
Verification: Attributed GPLv3 workbench; 37 Python tests, 20 desktop/mobile browser cases, installed source/wheel checks, Linux/Windows CI, non-root container and dependency audits passed. Real Yahoo Finance quote/history verified with TLS enabled. Paid AI inference remains unverified; public preview is fictional data.
[Synthetic reference demo](https://sushant-nemade.github.io/MarketInsight/)
[Download the reference CLI and source](https://github.com/Sushant-Nemade/MarketInsight/releases/tag/v0.2.0-reference)

## Categorized Backlog

### Generative and Agentic AI

- [AI Blog Publisher (BlogBoard)](https://github.com/Sushant-Nemade/ai-blog-publisher) - reference
- [Market Insight Research Workbench](https://github.com/Sushant-Nemade/MarketInsight) - reference
- [Travel Planning Agent (TravelBrain)](https://github.com/KalyanM45/TravelBrain-Multi-Agent-AI-Travel-Planner) - planned

### Data and Developer Tools

- [GitPulse: Audience Workspace](https://github.com/Sushant-Nemade/gitpulse) - reference
- [Doclify](https://github.com/Sushant-Nemade/Doclify) - reference

### Predictive Machine Learning

- [Airbnb Price Prediction](https://github.com/KalyanMurapaka45/End-to-End-Airbnb-Price-Prediction) - planned
- [Boston House Price Prediction](https://github.com/KalyanMurapaka45/House-Price-Prediction) - planned
- [Diamond Price Prediction](https://github.com/KalyanM45/Diamond-Price-Prediction) - planned
- [Flight Fare Prediction](https://github.com/KalyanMurapaka45/Flight-Fare-Prediction) - planned
- [Heart Disease Prediction](https://github.com/KalyanMurapaka45/Heart-Disease-Prediction) - planned
- [Spam E-Mail Detection](https://github.com/KalyanMurapaka45/Spam-Email-Detection) - planned
- [Student Performance Prediction](https://github.com/KalyanMurapaka45/Student-Perfomance-Prediction) - planned

### Computer Vision

- [Respire: Chest Disease Detection](https://github.com/KalyanM45/End-to-End-Chest-Disease-Classification) - planned

### Recommendation Systems

- [Movie Recommendation System](https://github.com/KalyanMurapaka45/End-to-End-Movie-Recommendation-System) - planned

## Delivery Policy

Active implementation: none. Next pending candidate: Travel Planning Agent (TravelBrain), subject to fresh license and runnable-path audits.
No automatic daily imports or unattended publishing. Return in a later session to request the next project.
Healthcare and financial examples remain educational until separately validated for any proposed real use.

[Project status and pending work](docs/PROJECT_STATUS_AND_PENDING_WORK.md) | [Release checklist](docs/RELEASE_CHECKLIST.md) | [Portfolio](https://sushant-nemade.github.io/)

## Maintain the Catalog

```text
python -m tools.catalog
python -m tools.catalog --check
python -m unittest discover -s tests -v
```

Edit projects.json, then regenerate this README. Preserve source attribution and distinguish local tests from live integration evidence.
