# AGENTS.md — Maneesh Athi Personal AI Portfolio

## Mission
Build independent, public-safe portfolio repositories that demonstrate career progression from programming and data engineering to ML, multimodal AI, RAG, and agentic AI.

## Non-negotiable rules
1. Do not use or mention employer/client names, internal architectures, proprietary code, private datasets, credentials, screenshots, metrics, prompts, or documentation.
2. Use publicly licensed data or deterministic synthetic generators. Document the source and license.
3. Do not fabricate historical commits or claim a repository was built in its represented career year. Use wording such as "career timeline project" where appropriate.
4. Every repository must be runnable and must include tests, type hints, input validation, structured logging, `.env.example`, `.gitignore`, and a clear license.
5. Prefer small, maintainable implementations over oversized demos.
6. Never commit secrets, tokens, model credentials, large model artifacts, generated databases, or private user data.
7. All APIs must expose health checks and useful error responses.
8. All ML/AI projects must include evaluation, limitations, and reproducibility notes.
9. Use synthetic examples by default so every demo works without private access.
10. Make changes in reviewable commits and summarize tests executed.

## Standard repository sections
- Business/problem statement
- Architecture diagram (Mermaid)
- Capabilities
- Tech stack and design decisions
- Repository structure
- Local setup and quickstart
- Sample inputs and outputs
- Testing
- Evaluation/results
- Security/privacy
- Limitations
- Roadmap
- Public-safe portfolio disclaimer

## Standard engineering baseline
- Python 3.11+
- `pyproject.toml`
- Ruff and mypy where practical
- pytest
- GitHub Actions for lint and tests
- Dockerfile for medium/large services
- Makefile or task commands
- Pre-commit hooks where practical
- Dependabot configuration
