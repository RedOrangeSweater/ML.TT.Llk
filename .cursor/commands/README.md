# Canonical .cursor/commands (shared across portfolio)

Shared slash-commands set for portfolio projects. Source: RulesEngineUniverse workflow (commands-first: curs.*, sdlc.*, hat.*, release.aaa). Project-specific commands (e.g. game.extract for REU only) live in `docs/projects/<project>/.cursor/commands/` and are overlaid when syncing that project.

- **Propagation**: `tools/sync_portfolio_to_upstreams.py` copies this folder to each upstream `.cursor/commands`.
- **Update**: When REU or another project improves commands, snapshot into `docs/projects/<project>/commands.upstream-*`, then copy the chosen set here and re-run propagation.

**SDLC layout** (новая структура `docs/sdlc/00_Main/`):
- `/sdlc.newrepo` — пустой проект с полной структурой: копировать template в целевой репо, затем вызвать `/sdlc.main` (target, path, subProjects).
- `/sdlc.main` — создать/привести основной SDLC (00_Main) и sub‑SDLC.
- `/sdlc.create` — завести новый sub‑SDLC (01_*, 02_*, …).
- `/sdlc.migrate` — перейти со старой плоской структуры `docs/NN_Name/` на `docs/sdlc/00_Main/` (запускать вручную по репо, затем коммит/пуш).
- `/sdlc.status`, `/sdlc.audit` — снимок статуса и аудит согласованности.

**Principles namespace** (`prin.*.md` в корне commands):
- `/prin.audit` — покрытие principles → Cursor rules/commands/test cases.
- `/prin.derive` — proposal для нового principles-derived rule/command из `PrincipleId`.
- `/prin.gap` — обновить gap tracker пополнения Cursor artifacts из принципов.
- `/prin.diagnose` — diagnosis до fix (symptom → root cause → next experiment).
- `/prin.design` — mechanism design после diagnosis.
- `/prin.decide` — decision log: options, evidence, owner, metric, kill criteria.
- `/prin.governance` — stakeholder/owner/escalation и blocker map.
- `/prin.sync` — get-in-sync по disagreement: claim, evidence, opposing view, invariant, next experiment.
- `/prin.escalate` — escalation request для blocker/deadlock с requested yes/no decision.
- `/prin.learn` — error/feedback → lesson → mechanism change.
- `/prin.teach` — teach-in-context (not doing-for).
- `/prin.verify` — outcome/mechanism verification.
- `/prin.situation` — situation assessment/coaching (Five Steps map).
- `/prin.portable` — audit переносимого principles bundle в другой проект.
