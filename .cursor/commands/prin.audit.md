# /prin.audit — аудит покрытия Principles → Cursor artifacts

Проверить, насколько `.cursor/rules/` и `.cursor/commands/` покрывают canonical principles и помогают человеку действовать: понять ситуацию, проверить корректность reasoning, выбрать следующий шаг, назначить owner и metric.

**source_principles:** Meta-Recursive-01, Meta-Recursive-03

## Input

Опционально: `all`, `rules`, `commands`, `gap`, `portable`, путь к principle record или путь к rule/command. Пусто → audit всего principles-related слоя.

## Canonical Sources

**Portfolio fallback:** если `principles_sot/` или derivation docs отсутствуют — использовать rules `05–08_dalio_*.mdc` и steps этой команды как behavioral SoT; machine slice (`principles_sot/*.yaml`) — optional (канон в Meta.Dalio.LogicModel).

1. Human canonical examples: `docs/sdlc/00_Main/03_Specs/CANONICAL_EXAMPLES_ru.md`.
2. Machine slice: `principles_sot/*.yaml`.
3. Derivation contract: `docs/sdlc/00_Main/02_Architecture/CURSOR_RULE_DERIVATION_ru.md`.
4. Gap tracker: `docs/sdlc/00_Main/04_QA/GAP_ANALYSIS_ru.md`.
5. Inventory: `docs/sdlc/00_Main/04_QA/CURSOR_RULES_INVENTORY_ru.md`.

## Audit Checklist

- **Traceability:** каждый principles-related rule/command имеет `source_principles` или явно помечен как `portfolio_common`.
- **Self-contained behavior:** rule/command говорит trigger, action, evidence, exit criteria, fallback; ссылка не заменяет объяснение.
- **Role-neutral usability:** инструкция годится для человека любой роли: engineer, reviewer, manager, security, deploy, architecture; нет предположения «только разработчик».
- **Decision discipline:** есть owner, metric, next experiment, kill criteria для нетривиальных решений.
- **Blocker roles:** output называет, какие роли могут заблокировать decision или validation (reviewer, security, deploy, manager, architecture).
- **Portable bundle:** ясно, какие files копировать в другой проект и что адаптировать.
- **Coverage gaps:** все новые gaps записаны в `GAP_ANALYSIS_ru.md` с next artifact.
- **Command workflows:** `prin.diagnose`, `prin.design`, `prin.decide`, `prin.governance`, `prin.sync`, `prin.escalate`, `prin.learn`, `prin.teach`, `prin.verify`, `prin.situation`, `prin.portable` покрывают diagnosis, mechanism design, decision log, governance, get-in-sync, escalation, learning, teach-in-context, verification, situation coaching, portability.

## Output

- **Verdict:** покрытие достаточное / есть blockers.
- **Coverage table:** principle family → current rule/command → missing behavior.
- **Findings:** ordered by severity, each as claim → evidence → fix.
- **Next actions:** конкретные file-level edits.
- **Commit surface:** какие файлы должны попасть в atomic commit.

## Constraints

Не выводить rules из raw Haskell snippets напрямую. Если нужен новый behavior, сначала указать `PrincipleId` из `principles_sot/` или добавить gap в `GAP_ANALYSIS_ru.md`.
