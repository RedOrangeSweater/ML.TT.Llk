# /prin.portable — audit переносимого principles bundle

Определить, какие principles-related files копировать в другой проект, что адаптировать, что не копировать вслепую. Подходит перед переносом Dalio-derived rules/commands в новый repo.

**source_principles:** Meta-Recursive-01, Meta-Recursive-03, Meta-Recursive-05

## Input

Опционально: путь целевого проекта, нужные behavior families (problem solving, decisions, governance, learning, git workflow). Пусто → полный portable bundle audit.

## Canonical Sources

**Portfolio fallback:** если `principles_sot/` или derivation docs отсутствуют — использовать rules `05–08_dalio_*.mdc` и steps этой команды как behavioral SoT; machine slice (`principles_sot/*.yaml`) — optional (канон в Meta.Dalio.LogicModel).

1. `.cursor/rules/04_meta_dalio_logicmodel.mdc` (§Portable principles-related bundle)
2. `docs/sdlc/00_Main/04_QA/CURSOR_RULES_INVENTORY_ru.md`
3. `principles_sot/README.md`
4. Test cases: `docs/sdlc/00_Main/04_QA/CURSOR_RULE_TESTCASES_ru.md`

## Steps

1. **List groups:** Core derived rules, Machine SoT slice, Support rules, Git workflow, Commands.
2. **Per group — copy list:** exact file paths from inventory (verify on disk).
3. **Adapt list:** project overlay (`00_core.mdc`, domain overlay), Run configs, push policy, repo-specific paths.
4. **Do-not-copy:** `04_meta_dalio_logicmodel.mdc`, corpus paths, MDLM-specific tasks unless adapted.
5. **Blocker roles map:** для каждой behavior family назвать роли, которые могут заблокировать перенос или validation (reviewer, security, deploy, manager, architecture). Если роль не применима в solo repo — явно «N/A».
6. **Traceability check:** каждый copied rule/command имеет `source_principles` или `portfolio_common`; нужные YAML в `principles_sot/` для выбранного slice.
7. **Smoke checklist:** после copy — `/prin.audit`, `validate_cursor_artifact_traceability.py --strict` (if present), `validate_cursor_rule_testcases.py`, one positive test case per behavior family.

## Copy manifest (default bundle)

| Group | Paths | Purpose |
| --- | --- | --- |
| Core derived rules | `.cursor/rules/05_dalio_problem_solving.mdc`, `06_dalio_decisions.mdc`, `07_dalio_work_management.mdc`, `08_dalio_learning.mdc` | Problem loop, decisions, ownership, learning |
| Support rules | `25_karpathy_guidelines.mdc`, `28_bridgewater_reasoning.mdc`, `19_plans_detailed_execution.mdc`, `14_rules_feedback_loop.mdc` | Reasoning quality, plans, feedback loop |
| Git workflow (optional) | `02_atomic_git.mdc`, `15_commit_push_shortcuts.mdc` | Atomic commits / push policy — adapt to target repo |
| Commands | `.cursor/commands/prin.audit.md` … `prin.portable.md` (14 files) | `/prin.*` workflows |
| Machine SoT slice | `principles_sot/README.md` + YAML referenced by copied artifacts' `source_principles` | Traceability backing |

## Adapt manifest (always review)

| Artifact | What to change in target |
| --- | --- |
| `00_core.mdc` | SoT entrypoints, language, project purpose |
| Domain overlay | Replace `04_meta_dalio_logicmodel.mdc` with target-specific overlay |
| `.vscode/tasks.json` | Prefix, script paths, venv location |
| Push policy | Align `15_commit_push_shortcuts.mdc` with target git workflow |
| Local QA | Copy or adapt `29_local_qa_no_ci.mdc` + `scripts/pre_push_check.sh` when CI absent |

## Exclude manifest

- `principy-dalio-2018/` corpus (not portable as bundle)
- `04_meta_dalio_logicmodel.mdc` without rewrite
- MDLM-only scripts/reports unless target adopts same SoT layout
- Full `principles_sot/*.yaml` (210 records) when only a behavior subset is needed

## Evidence Requirements

- Inventory table matches actual files on disk.
- Target project constraints named (git policy, language, no Dalio corpus, CI vs local QA).
- Blocker roles named per family or marked N/A with reason.

## Output

- **Copy manifest:** group → files → purpose.
- **Adapt manifest:** file → what to change in target repo.
- **Exclude manifest:** files not to copy blindly.
- **Blocker roles:** family → role → what blocks → escalation owner.
- **Post-copy verification:** commands to run (`/prin.audit`, traceability `--strict`, testcase validator, one positive case per family).
- **Commit surface:** if updating source repo inventory only — doc paths.

## Constraints

- Не копировать весь `principy-dalio-2018/` как часть portable bundle.
- Не копировать project overlay без адаптации SoT entrypoints.
- Output role-neutral: понятен тому, кто настраивает Cursor в любом проекте.
