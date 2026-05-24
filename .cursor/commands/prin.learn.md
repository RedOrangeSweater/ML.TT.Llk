# /prin.learn — error/feedback → lesson → mechanism change

Превратить боль, ошибку или негативный feedback в observable signal, lesson и при необходимости mechanism change (rule, script, Run config, process). Подходит после incident, review, recurring agent/process failure.

**source_principles:** Life-01, Life-01-05, Life-01-06, Life-01-07, Life-02-06, Life-03-06, Work-08-08, Work-09-03, Work-09-04, Work-09-05, Work-09-09, Work-10-08, Work-13, Meta-Recursive-03, Work-09-03-e, Work-10-02-a, Life-02-06-a, Life-02-01-g-a, Life-02-06-b, Life-03-01-c-a, Life-03-06-a, Life-03-06-b

## Input

Обязательно: описание painful outcome или failure. Опционально: частота, уже сделанный one-time fix, затронутые artifacts.

## Canonical Sources

**Portfolio fallback:** если `principles_sot/` или derivation docs отсутствуют — использовать rules `05–08_dalio_*.mdc` и steps этой команды как behavioral SoT; machine slice (`principles_sot/*.yaml`) — optional (канон в Meta.Dalio.LogicModel).

1. `principles_sot/Life-01-05.yaml`, `Life-01-06.yaml`, `Life-01-07.yaml`, `Life-02-06.yaml`, `Life-03-06.yaml`, `Work-09-03.yaml`, `Work-09-04.yaml`, `Work-09-05.yaml`, `Work-09-09.yaml`, `Work-13.yaml`, `Meta-Recursive-03.yaml`
2. Rule: `.cursor/rules/08_dalio_learning.mdc` (`cursor.learning.convert_pain_to_mechanism_change`)
3. Feedback loop: `.cursor/rules/14_rules_feedback_loop.mdc`

## Steps

1. **Signal:** что именно пошло не так (observable, не blame).
2. **Recurrence check:** one-off vs likely to recur.
3. **Accurate feedback:** если есть people/process аспект, отделить observed behavior/outcome от generalized judgment.
4. **Lesson:** короткий вывод, что система должна была сделать иначе; не фиксироваться на blame или fixed traits (`Life-02-06`).
5. **Open-mindedness practice (`Life-03-06`):** если урок из painful disagreement — behavior experiment и signal успеха practice.
6. **Mechanism change:** rule update, command update, script, Run config, checklist — что предотвратит повтор.
7. **Verification:** как проверить, что mechanism работает (test, smoke, audit command).
8. **Skip over-engineering:** если recurrence unlikely — lesson only, без mechanism redesign.

## Evidence Requirements

- Конкретный failure signal (лог, повтор, user correction, CI fail).
- Явная связь lesson → proposed mechanism artifact path.
- Для feedback по людям/процессу: конкретное наблюдение или outcome, не «он плохой/они саботируют» без evidence.

## Output

- **Lesson:** one paragraph, actionable.
- **Mechanism proposal:** file path(s) и minimal change scope.
- **Verification step:** command or manual check.
- **Gap update:** если нужен новый principle record или rule — entry для `GAP_ANALYSIS_ru.md`.
- **Blockers by role:** reviewer, security, deploy, manager, architecture — кто может заблокировать mechanism change или validation.
- **Commit surface:** atomic paths (rule, command, test case).

## Constraints

- Не останавливаться на apology или blame.
- Не делать workaround без named lesson.
- Не over-engineer mechanism для one-off already-fixed issue.
