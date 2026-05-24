# /prin.design — mechanism design после diagnosis

Спроектировать изменение mechanism/plan после named root cause: mechanism вместо workaround, systematized principles, iterative design, verification metric. Подходит после `/prin.diagnose` или когда root cause уже известна с evidence.

**source_principles:** Life-02-04, Meta-Recursive-01, Work-04-04-e, Work-13, Work-13-01, Work-13-02, Work-13-03, Work-13-04, Work-13-05, Work-13-06, Work-13-07, Work-13-08, Work-13-09, Work-13-10, Work-13-11, Work-15, Work-15-01, Life-05-11, Work-12-04, Work-16-01, Work-16, Work-10-01-b, Work-10-01-c, Work-15-01-b, Work-10-02-c, Work-13-05-a, Work-10-02-b, Work-10-02-d, Work-12-08-m, Work-13-05-c, Work-13-05-d, Work-13-09-b, Life-02-04-a, Life-02-04-b, Life-02-04-c, Life-02-04-d, Life-02-04-e, Life-02-04-f, Life-03-01-c-b

## Input

Обязательно: root-cause hypothesis (или явная assumption) и контекст проблемы. Опционально: diagnosis summary из `/prin.diagnose`, constraints, stakeholders, уже предложенный local fix.

## Canonical Sources

**Portfolio fallback:** если `principles_sot/` или derivation docs отсутствуют — использовать rules `05–08_dalio_*.mdc` и steps этой команды как behavioral SoT; machine slice (`principles_sot/*.yaml`) — optional (канон в Meta.Dalio.LogicModel).

1. Chapter: `principles_sot/Work-13.yaml`
2. Work sub-principles: `Work-13-01.yaml` … `Work-13-11, Work-15, Work-15-01.yaml`
3. Five Steps design step: `principles_sot/Life-02-04.yaml`
4. Rule: `.cursor/rules/05_dalio_problem_solving.mdc` (`cursor.problem.design_mechanism`)
5. Support: `.cursor/rules/28_bridgewater_reasoning.mdc` (MECE options, falsification)
6. Derivation: `docs/sdlc/00_Main/02_Architecture/CURSOR_RULE_DERIVATION_ru.md`

## Steps

1. **Gate (`Life-02-04`):** root cause named или explicit assumption; если нет — stop и `/prin.diagnose`.
2. **Mechanism not patch (`Work-13`, `Work-13-01`):** предложить mechanism change, не one-off local fix; root cause должна быть обойдена или устранена.
3. **Workaround vs real fix:** отделить временный workaround от durable mechanism; workaround — только с named lesson и path к mechanism (`/prin.learn` если нужен feedback loop).
4. **Systematize principles (`Work-13-02`):** если mechanism не repeatable — codify principles и how-to-apply (rules, commands, checklists).
5. **Film scenario plan (`Work-13-03`):** plan как scenario — who, what, when, expected outcomes, owners, metrics.
6. **Iterative build (`Work-13-04`):** улучшать mechanism iteratively; не big-bang perfect system.
7. **Goals not tasks (`Work-13-05`):** привязать mechanism к целям, не только к task list.
8. **Org clarity (`Work-13-06`, `Work-13-10`):** если org-dependent — clear reporting lines, responsibilities, job descriptions; no unclear dual reporting.
9. **Minimize guides (`Work-13-07`):** новые rules/guides только когда needed; prefer simpler mechanism.
10. **Strategic anchor (`Work-13-08`):** tactical changes сохраняют strategic vision.
11. **Control integrity (`Work-13-09`):** если есть metrics — design control против gaming/cheating.
12. **Realistic buffers (`Work-13-11, Work-15, Work-15-01`):** time/cost buffers в plan.
13. **Verification metric (`Work-13`):** как проверить, что новый mechanism работает; kill criteria для design.
14. **Handoff:** owner + next step → `/prin.decide` (если choice между options), `/prin.verify` (verification), `/prin.governance` (org blockers).

## Evidence Requirements

- Named root-cause hypothesis или explicit assumption с next experiment.
- Связь mechanism change → root cause (claim → evidence).
- Verification metric или observable signal успеха mechanism.
- Для org design: named roles и reporting clarity.

## Output

- **Design summary:** root cause, proposed mechanism change, workaround vs durable fix.
- **Plan scenario:** tasks, owners, timeline, metrics (`Work-13-03`).
- **Principles/systematization:** что codified для repeatability (`Work-13-02`).
- **Verification:** metric, smoke check, `/prin.verify` hook.
- **Blockers by role:** reviewer, security, deploy, manager, architecture — кто может veto или delay mechanism rollout.
- **Commit surface:** paths для plan doc, rule/command update, ADR/TASK.

## Constraints

- Не проектировать plan/mechanism до root-cause diagnosis (`Life-02-04`); trivial one-off — кратко указать skip.
- Не предлагать только local patch для recurring problem без mechanism path.
- Не big-bang redesign без iterative steps (`Work-13-04`).
- Не добавлять guides/rules без necessity check (`Work-13-07`).
