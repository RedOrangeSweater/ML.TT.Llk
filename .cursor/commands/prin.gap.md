# /prin.gap — обновить gap tracker Principles → Cursor rules/commands

Вести `docs/sdlc/00_Main/04_QA/GAP_ANALYSIS_ru.md` как backlog пополнения Cursor rules и commands из principles SoT.

**source_principles:** Meta-Recursive-01, Meta-Recursive-05

## Input

Опционально: новый gap, principle family, command/rule path или audit output. Пусто → пересмотреть текущий gap tracker по фактическим `.cursor/rules/`, `.cursor/commands/`, `principles_sot/` (если есть).

## Canonical Sources

**Portfolio fallback:** если `principles_sot/` или derivation docs отсутствуют — использовать rules `05–08_dalio_*.mdc` и steps этой команды как behavioral SoT; machine slice (`principles_sot/*.yaml`) — optional (канон в Meta.Dalio.LogicModel).

## What To Track

- canonical records coverage: какие `principles_sot/*.yaml` уже имеют derived artifacts;
- book coverage: какие Life/Work chapters ещё не нормализованы в `principles_sot/`;
- behavior coverage: какие human workflows ещё не покрыты самодостаточными rules/commands;
- command UX: есть ли короткий `prin.*` entrypoint для частого workflow;
- portability: понятно ли, какие files брать в другой проект.

## Update Format

Каждый gap записывать как:

- **Gap ID**
- **Claim**
- **Evidence**
- **Missing artifact**
- **Next experiment/fix**
- **DoD**
- **Owner / metric**

## Output

- **Changed tracker sections**
- **New / closed gaps**
- **Next 1–3 derivation targets**
- **Commit note:** files that should be staged

## Constraints

Не закрывать gap без evidence: file path, rule_id, command path, test case or validation command.
