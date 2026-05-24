# /prin.derive — вывести или обновить Cursor rule/command из PrincipleId

Создать proposal для principles-related `.cursor/rules/*.mdc` или `.cursor/commands/prin.*.md` из canonical principle records. Цель — получить самодостаточный artifact, который можно перенести в другой проект без знания всего corpus.

**source_principles:** Meta-Recursive-02, Meta-Recursive-03

## Input

Обязательно: один или несколько `PrincipleId` из `principles_sot/` или описание gap. Примеры: `Life-02`, `Work-12`, `Meta-Recursive-03`, `gap: stakeholder decision log`.

## Canonical Sources

**Portfolio fallback:** если `principles_sot/` или derivation docs отсутствуют — использовать rules `05–08_dalio_*.mdc` и steps этой команды как behavioral SoT; machine slice (`principles_sot/*.yaml`) — optional (канон в Meta.Dalio.LogicModel).

## Derivation Steps

1. Найти source record в `principles_sot/` или зафиксировать missing record в `GAP_ANALYSIS_ru.md`.
2. Сформулировать operational intent:
   - trigger: когда правило включается;
   - obligation/prohibition: что сделать и чего нельзя делать;
   - evidence: какие факты нужны;
   - exit criteria: как понять, что действие завершено;
   - fallback: один yes/no question или explicit assumption.
3. Выбрать artifact:
   - `.cursor/rules/05–08_dalio_*.mdc` для always-on behavior;
   - `.cursor/commands/prin.*.md` для explicit workflow;
   - `docs/sdlc/00_Main/04_QA/CURSOR_RULE_TESTCASES_ru.md` для regression cases.
4. Проверить overlap с `28_bridgewater_reasoning.mdc`, `25_karpathy_guidelines.mdc`, `19_plans_detailed_execution.mdc`.
5. Обновить `CURSOR_RULES_INVENTORY_ru.md` и `GAP_ANALYSIS_ru.md`.

## Output

- **Source principles:** IDs and files.
- **Artifact target:** exact path.
- **Draft content:** complete rule/command snippet.
- **Test cases:** positive + negative.
- **Gap update:** what coverage changed.

## Constraints

Не плодить rule на каждый snippet. Группировать by behavior family: problem solving, decisions, work management, learning, audit/review workflow.
