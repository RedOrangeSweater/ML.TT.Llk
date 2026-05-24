# /prin.diagnose — диагностика проблемы до fix

Провести diagnosis до design/fix: symptom → owner/mechanism → root-cause hypothesis → next experiment. Подходит для любой роли, когда есть повторяющийся или нетривиальный сбой, а не для тривиальной правки.

**source_principles:** Life-01, Life-01-04, Life-01-06, Life-01-10, Life-02, Life-02-01, Life-02-02, Life-02-03, Life-03-01, Work-10-01, Work-11, Work-12, Work-11-01, Work-11-02, Work-11-03, Work-11-04, Work-12-01, Work-12-02, Work-12-04, Work-12-05, Work-12-03, Work-10-01-b, Life-04-03-b, Life-04-03-c, Life-03-01-a, Life-03-01-b, Work-09-03-c, Work-10-02-b, Work-11-04-a, Work-11-04-b, Work-11-05-a, Work-12-05-a, Work-12-06-a, Life-02-02-a, Life-02-03-a, Life-02-02-b, Life-02-02-c, Life-02-03-b, Life-02-03-c, Life-02-02-d, Life-02-02-e, Life-02-02-f, Life-03-01-b-a, Life-03-06-c

## Input

Обязательно: описание проблемы (symptom, контекст, частота). Опционально: логи, артефакты, owner, уже предложенный fix.

## Canonical Sources

**Portfolio fallback:** если `principles_sot/` или derivation docs отсутствуют — использовать rules `05–08_dalio_*.mdc` и steps этой команды как behavioral SoT; machine slice (`principles_sot/*.yaml`) — optional (канон в Meta.Dalio.LogicModel).

1. Chapter: `principles_sot/Life-02.yaml`, `Work-11.yaml`, `Work-12.yaml`
2. Life Five Steps subs: `Life-02-01.yaml` (clarify goal), `Life-02-02.yaml` (identify problem), `Life-02-03.yaml` (diagnose root cause); barrier check: `Life-03-01.yaml` (ego/blind-spot)
3. Work sub-principles: `Work-11-01.yaml` (worry when complacent), `Work-11-02.yaml` (QC mechanism), `Work-11-03.yaml` (specific not general), `Work-11-04.yaml` (tackle hard problems); `Work-12-01.yaml` (three diagnostic questions), `Work-12-02.yaml` (continuous analysis), `Work-12-04.yaml` (drill-down 80/20), `Work-12-05.yaml` (quality diagnosis)
4. Rule: `.cursor/rules/05_dalio_problem_solving.mdc` (`cursor.problem.diagnose_before_fix`)
5. Derivation: `docs/sdlc/00_Main/02_Architecture/CURSOR_RULE_DERIVATION_ru.md`

## Steps

1. **Clarify goal (`Life-02-01`):** какой measurable outcome и verification metric, если проблемы не было.
2. **Observe reality:** что наблюдается сейчас (факты, логи, метрики, частота).
3. **Name problem (`Life-02-02`, `Work-11-03`, `Work-11-04`):** отделить symptom от named problem; не начинать с обобщений — конкретный bad outcome между goal и reality; не откладывать сложные проблемы без diagnosis.
4. **Complacency check (`Work-11-01`):** если нет беспокойства при видимых рисках — проверить скрытые проблемы; не успокаиваться без evidence.
5. **QC mechanism (`Work-11-02`):** назвать механизм или личный контроль качества; owner контроля.
6. **Barrier check (`Life-03-01`):** если counter-evidence отвергается как «они не понимают» — назвать ego/blind-spot barrier и запросить concrete evidence.
7. **Owner/mechanism hypothesis:** кто или какой процесс отвечает за механизм.
8. **Root-cause hypothesis:** skill / plan / process / context / mechanism failure.
9. **Continuous analysis (`Work-12-02`):** отслеживать trends и negative outcomes во времени — улучшается или ухудшается.
10. **Work-12-01 diagnostic ladder:** базовые три вопроса; затем по контексту lettered subs 12.1.a (кто/что иначе), 12.1.b (какой Five Step), 12.1.g (characteristic vs action), 12.1.i (manager failure modes); 12.1.d/e/f — не hindsight, не mix circumstances/approach, problem≠diagnosis.
11. **Drill-down (`Work-12-04`):** list problems → root causes → plan → execution; фокус на ~20% причин, дающих ~80% bad outcomes.
12. **Quality diagnosis (`Work-12-05`):** open-minded diagnosis; связь с прогрессом и отношениями.
13. **Classify failure type:** ошибка человека, неподходящая роль, плохой механизм (Work-12).
14. **Next experiment:** один проверяемый шаг, который подтвердит или опровергнет гипотезу.
15. **Stop before design:** не предлагать fix, пока diagnosis не ссылается на root cause или explicit assumption.

## Evidence Requirements

- Минимум одно конкретное наблюдение сбоя (лог, trace, метрика, воспроизводимый шаг).
- Частота или признак recurring vs one-off.
- Именованный owner или mechanism, если известен.

## Output

- **Diagnosis summary:** goal, observed reality, problem, owner/mechanism, root-cause hypothesis.
- **Failure classification:** skill / plan / process / context / mechanism.
- **Next experiment:** claim → expected evidence → kill criteria.
- **Blockers by role:** кто может заблокировать validation (reviewer, security, deploy, manager, architecture).
- **Commit surface:** если diagnosis ведёт к doc update — пути файлов для atomic commit.

## Constraints

- Не переходить к implementation plan, пока root cause не назван или не помечен как assumption.
- Не лечить symptom как root cause.
- Для тривиальной one-off правки (typo, label) — кратко указать, что full diagnosis не нужен, и остановиться.
