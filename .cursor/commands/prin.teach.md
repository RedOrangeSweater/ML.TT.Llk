# /prin.teach — teach-in-context (mechanism learning, not doing-for)

Передать skill или principle in situ: dual purpose (goal + mechanism learning), teach-to-fish вместо micromanagement, case-study extraction. Подходит при onboarding, delegation, rule/command introduction, post-incident mechanism upgrade.

**source_principles:** Work-09, Work-09-01, Work-09-01-c, Work-09-02, Work-09-03, Work-09-04, Work-09-06, Work-09-09, Work-10-02, Work-10-03, Life-02-06, Meta-Recursive-03, Work-10-02-c, Work-09-01-a, Work-09-01-b, Work-09-03-b, Work-10-02-a, Work-15-01-a, Life-02-06-b-a

## Input

Обязательно: кого/что обучаем (person, team, agent workflow) и контекст situation. Опционально: уже известный principle, constraint «не ломать production», deadline.

## Canonical Sources

**Portfolio fallback:** если `principles_sot/` или derivation docs отсутствуют — использовать rules `05–08_dalio_*.mdc` и steps этой команды как behavioral SoT; machine slice (`principles_sot/*.yaml`) — optional (канон в Meta.Dalio.LogicModel).

1. `principles_sot/Work-09.yaml`, `Work-09-01.yaml`, `Work-09-01-c.yaml`, `Work-09-02.yaml`, `Work-09-03.yaml`, `Work-09-04.yaml`, `Work-09-06.yaml`, `Work-09-09.yaml`, `Work-10-02.yaml`, `Life-02-06.yaml`, `Meta-Recursive-03.yaml`
2. Rules: `.cursor/rules/08_dalio_learning.mdc`, `.cursor/rules/07_dalio_work_management.mdc`
3. Verify handoff: `/prin.verify` when teach cycle needs outcome check

## Steps

1. **Dual purpose (`Work-10-02`):** named goal advance + mechanism teach/verify — вторая задача не теряется ради speed.
2. **Case study (`Work-10-02.a`):** классифицировать situation type; какие principles applicable; какой lesson для повторяющихся cases.
3. **Teach-to-fish (`Work-09-01-c`):** что learner должен уметь сам после; допустимые learning mistakes; не micromanage.
4. **Principle explanation (`Work-10-02.c`):** если вводится rule/process — объяснить underlying principle, не только compliance wording.
5. **Mechanism over blame (`Life-02-06`):** focus на skill/mechanism gap, не fixed traits.
6. **Accurate feedback (`Work-09-03`):** assessment tied to evidence; не sugarcoat, не blame.
7. **Verification hook:** назначить observable signal успеха teaching (→ `/prin.verify` или explicit metric).

## Evidence Requirements

- Named learner/mechanism owner.
- Concrete «после teach должно быть возможно X без Y».
- Learning mistake bounds (что допустимо vs блокер).

## Output

- **Teach plan:** situation class, principles, approach (not step-by-step micromanagement).
- **Learning objective:** one measurable capability change.
- **Allowed mistakes / guardrails:** что можно отпустить для learning.
- **Verify metric:** signal для `/prin.verify` или Run config smoke.
- **Blockers by role:** reviewer, security, deploy, manager, architecture — кто может заблокировать teach outcome или validation.
- **Commit surface:** paths для rule/command/doc updates if teach becomes mechanism change.

## Constraints

- Не делать work-for когда запрос — capability building.
- Не вводить rule без named principle rationale.
- Для trivial one-off with no recurrence — teach ceremony optional; state why skipped.
