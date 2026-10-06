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
Verification: Original code; strict typing, security audits, desktop/mobile tests, Linux/Windows CI and one public GitHub REST sync verified. Hosted private API remains unverified.

## Categorized Backlog

### Generative and Agentic AI

- [AI Blog Publisher (BlogBoard)](https://github.com/Sushant-Nemade/ai-blog-publisher) - reference
- [Market Insight](https://github.com/KalyanM45/MarketInsight) - planned
- [Travel Planning Agent (TravelBrain)](https://github.com/KalyanM45/TravelBrain-Multi-Agent-AI-Travel-Planner) - planned

### Data and Developer Tools

- [GitPulse: Audience Workspace](https://github.com/Sushant-Nemade/gitpulse) - reference
- [Doclify](https://github.com/KalyanM45/Doclify) - planned

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

Active implementation: none. Next pending candidate: Doclify, subject to fresh license and runnable-path audits.
No automatic daily imports or unattended publishing. Return in a later session to request the next project.
Healthcare and financial examples remain educational until separately validated for any proposed real use.

[Release checklist](docs/RELEASE_CHECKLIST.md) | [Portfolio](https://sushant-nemade.github.io/)

## Maintain the Catalog

```text
python -m tools.catalog
python -m tools.catalog --check
python -m unittest discover -s tests -v
```

Edit projects.json, then regenerate this README. Preserve source attribution and distinguish local tests from live integration evidence.
