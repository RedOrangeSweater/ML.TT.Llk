# /prin.decide — decision log с evidence и owner

Отделить analysis от commitment: собрать options, evidence, counter-evidence, believable disagreement, owner, metric и kill criteria. Подходит для архитектурных, процессных и org-решений любой роли.

**source_principles:** Life-01-01, Life-01-04, Life-01-08, Life-01-09, Life-01-10, Life-02-05, Life-03, Life-03-02, Life-03-04, Life-03-05, Life-03-06, Life-05, Life-05-01, Life-05-02, Life-05-03, Life-05-04, Life-05-05, Life-05-06, Life-05-07, Life-05-08, Life-05-09, Life-05-10, Work-04-05-b, Work-05, Work-05-01, Work-05-01-a, Work-05-01-b, Work-05-02, Work-05-02-a, Work-05-02-b, Work-05-02-c, Work-05-02-d, Work-05-02-e, Work-05-02-f, Work-05-03, Work-05-03-a, Work-05-03-b, Work-05-04, Work-05-04-a, Work-05-04-b, Work-05-04-c, Work-05-04-d, Work-05-05, Work-05-05-a, Work-05-05-b, Work-05-05-c, Work-05-05-d, Work-05-06, Work-05-06-a, Work-05-06-b, Work-05-06-c, Work-05-07, Work-06-04, Work-07-01, Work-08-04, Work-10-07, Work-10-09, Work-10-12, Work-14, Work-14-01, Work-14-02, Work-14-03, Work-14-04, Work-14-05, Life-05-11, Life-05-12, Work-13-08, Life-02-01-g, Life-05-02-c, Work-05-02-g, Work-08-04-b, Work-15-01-c, Work-01-02-b, Work-01-04-e, Work-08-01-d, Life-05-02-a, Life-05-02-b, Life-05-02-d, Work-10-02-e, Life-05-06-a, Work-14-01-a, Work-14-01-b, Work-14-01-c, Life-05-07-a, Life-02-04-c, Life-02-05-a, Life-02-01-a, Work-16-01-f, Life-02-01-b, Life-02-01-d, Life-02-01-e, Life-02-01-f, Life-02-01-g-b, Life-02-01-h, Life-03-03-e, Life-03-02-a, Life-03-02-b, Life-03-02-f, Life-03-02-g

## Input

Обязательно: decision topic и контекст. Опционально: уже известные options, constraints, stakeholders, deadline.

## Canonical Sources

**Portfolio fallback:** если `principles_sot/` или derivation docs отсутствуют — использовать rules `05–08_dalio_*.mdc` и steps этой команды как behavioral SoT; machine slice (`principles_sot/*.yaml`) — optional (канон в Meta.Dalio.LogicModel).

1. `principles_sot/Life-02-05.yaml`, `Life-05-01.yaml`, `Life-05-02.yaml`, `Life-05-03.yaml`, `Life-05-04.yaml`, `Life-05-06.yaml`, `Life-05-07.yaml`, `Life-05-10.yaml`, `Life-03.yaml`, `Life-03-04.yaml`, `Life-03-05.yaml`, `Work-05.yaml`, `Work-05-02.yaml`, `Work-05-02-b.yaml`, `Work-05-05.yaml`, `Work-06-04.yaml`, `Work-07-01.yaml`, `Work-10-12.yaml`, `Work-14.yaml`, `Work-14-01.yaml` … `Work-14-05.yaml`
2. Rules: `.cursor/rules/06_dalio_decisions.mdc`, `.cursor/rules/07_dalio_work_management.mdc`
3. Support: `.cursor/rules/28_bridgewater_reasoning.mdc` (MECE, falsification)

## Steps

1. **Phase gate (`Life-05-01`):** явно разделить analysis phase и decision phase; не смешивать.
2. **Objective view (`Life-05-02`):** facts vs opinions; competent sources (5.2.a); не over-weight single data points (5.2.e).
3. **Long-term outlook (`Life-05-03`):** trajectory A/B; rate vs target (5.3.a); 80/20 key factors (5.3.c).
4. **Multi-level check (`Life-05-04`, `Life-01-10`):** decision level + cross-level alignment; above/below the line (5.4.a).
5. **Consequence orders (`Life-01-08`):** 1st vs 2nd/3rd order effects; short-term temptation vs long-term goal.
6. **Analysis phase:** перечислить 2–3+ options с trade-offs; не выбирать сразу.
7. **Expected value (`Life-05-06`):** probability × payoff; improve probability when cheap (5.6.a); net pros/cons (5.6.c).
8. **Information vs delay (`Life-05-07`):** gather more info vs decide now; goals before desires (5.7.a).
9. **Evidence:** для каждого option — supporting facts, believability источника.
10. **Believability matrix (`Life-05-10`, `Life-03-05`, `Work-05-02`):** competent advisors; observable open-mindedness, не status.
11. **Counter-evidence:** strongest opposing view или risk; кто believable и почему.
12. **Rejection protocol:** отвергнутый option — counter-evidence, invariant или kill criterion.
13. **Uncertainty:** что неизвестно; какие данные изменят выбор.
14. **Decision phase:** recommendation, decision owner, expected outcome, verification metric.
15. **Kill criteria:** что falsifies выбранный option.
16. **Execution handoff (`Life-02-05`, `Life-01-09`, `Work-10-12`, `Work-14`):** owner, next step, progress metric; stop debating.
17. **Follow-through (`Work-14-01` … `Work-14-05`):** inspiring goal link; prioritize under overload; checklists for complex steps; sustainable rest; celebrate milestones.

## Evidence Requirements

- Минимум два рассмотренных option для нетривиального решения.
- Явный decision owner или yes/no вопрос «Вы принимаете финальное решение?»
- Metric или observable signal успеха.
- Для каждого rejected option: counter-evidence или invariant; vague «плохой вариант» не считается evidence.

## Output

- **Decision log:** topic, options table, evidence, counter-evidence, uncertainty.
- **Believability matrix:** source, evidence level, track record, causal explanation, access to facts, conflict of interest.
- **Recommendation:** chosen option (или defer), owner, metric, kill criteria.
- **Roles that can block:** reviewer, security, deploy, manager, architecture — кто может veto или delay.
- **Next action:** один concrete step после commitment.
- **Commit surface:** paths для decision doc / ADR / TASK, если нужно зафиксировать.

## Constraints

- Не смешивать analysis и final commitment в одном undifferentiated блоке.
- Не представлять confidence без stated uncertainty.
- Для уже согласованного small edit — не устраивать decision ceremony; выполнить или кратко подтвердить scope.
