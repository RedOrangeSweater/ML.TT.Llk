# /prin.sync — get-in-sync через claim, evidence и next experiment

Довести разногласие до ясного состояния: agreement, unresolved item, decision owner или next experiment. Подходит для технических, архитектурных, процессных и org-дискуссий, где стороны говорят мимо друг друга или спорят без нового evidence.

**source_principles:** Life-01-03, Life-02-07, Life-03-01, Life-03-02, Life-03-03, Life-03-04, Life-03-05, Life-03-06, Life-04, Life-04-03, Life-04-04, Life-05-10, Meta-Recursive-01, Work-01, Work-01-02, Work-01-03, Work-01-05, Work-03, Work-03-01, Work-03-02, Work-03-04, Work-04, Work-04-01, Work-04-01-a, Work-04-02, Work-04-02-a, Work-04-02-b, Work-04-02-c, Work-04-03, Work-04-03-a, Work-04-03-b, Work-04-03-c, Work-04-03-d, Work-04-03-e, Work-04-03-f, Work-04-03-g, Work-04-03-h, Work-04-04, Work-04-04-a, Work-04-04-b, Work-04-04-c, Work-04-04-d, Work-04-04-e, Work-04-04-f, Work-04-04-g, Work-04-04-h, Work-04-04-i, Work-04-04-j, Work-04-04-k, Work-04-04-l, Work-04-05, Work-04-05-a, Work-04-05-b, Work-04-06, Work-04-07, Work-05-02, Work-05-05, Work-05-05-a, Work-06, Work-06-01, Work-06-02, Work-06-03, Work-08-07, Life-04-01, Life-04-02, Life-04-05, Life-04-01-a, Life-03-01-c, Life-03-03-a, Life-02-06-b-b, Life-03-01-b-b, Life-03-01-c-c, Life-03-03-b, Life-03-03-c, Life-03-03-d, Life-03-02-c, Life-03-02-d, Life-03-02-e

## Input

Обязательно: спорный вопрос или disagreement. Опционально: known claims, stakeholders, deadline, current decision owner.

## Canonical Sources

**Portfolio fallback:** если `principles_sot/` или derivation docs отсутствуют — использовать rules `05–08_dalio_*.mdc` и steps этой команды как behavioral SoT; machine slice (`principles_sot/*.yaml`) — optional (канон в Meta.Dalio.LogicModel).

1. Life open-mindedness: `Life-02-07.yaml` (mental maps, assumptions, humility), `Life-03-01.yaml` (ego/blind-spot barriers), `Life-03-02.yaml` (radical open-mindedness), `Life-03-03.yaml`, `Life-03-04.yaml`, `Life-03-05.yaml` (recognize biased people), `Life-03-06.yaml` (practice open-mindedness)
2. Work sync/disagreement: `Work-04-02.yaml`, `Work-04-03.yaml`, `Work-05-02.yaml`, `Work-05-05.yaml`, `Work-06.yaml`, `Work-06-01.yaml`, `Work-06-02.yaml`, `Work-06-03.yaml`
2. Rules: `.cursor/rules/06_dalio_decisions.mdc`, `.cursor/rules/28_bridgewater_reasoning.mdc`
3. Workflow pair: `/prin.decide` для commitment, `/prin.escalate` для blocked decision path.

## Steps

1. **Disagreement scope:** назвать один конкретный question, по которому нет sync.
2. **Barrier check (`Life-03-01`):** проверить ego barrier и blind-spot barrier; не принимать «они не понимают» без evidence.
3. **Claim split:** для каждой стороны отделить claim, evidence, assumption и desired outcome.
4. **Mental maps (`Life-02-07`):** явно назвать assumptions и mental models каждой стороны; что их falsifies; не equate own map с reality; проверять карту реальности evidence, не только авторитет.
5. **Open-mindedness (`Life-03-02`, `Life-03-06`):** активно искать, что собственное мнение может быть неверным; после спора — lesson и behavior experiment.
6. **Believability check (`Life-03-05`, `Work-05-02`, `Life-05-10`):** кто имеет track record, causal explanation, access to facts, observable curiosity vs defensiveness; align principles before action dispute.
7. **Strongest opposing view:** сформулировать самую сильную позицию против recommended path.
8. **Invariant:** для objection указать, что должно остаться true; если invariant нет, objection не блокирует.
9. **Next experiment:** назвать один artifact/log/metric/demo, который меняет belief или закрывает disagreement.
10. **Decision path:** agreement, unresolved item with owner, `/prin.decide`, или `/prin.escalate`.

## Evidence Requirements

- Минимум один concrete claim и один evidence item на активное разногласие.
- Vague objection должен быть преобразован в invariant + evidence request или помечен как no mechanism.
- Если нужен commitment, есть decision owner или yes/no вопрос о владельце решения.

## Output

- **Sync state:** agreed / unresolved / escalated / no mechanism.
- **Disagreement map:** claim → evidence → opposing view → invariant → next experiment.
- **Believability notes:** кто believable и почему.
- **Owner:** decision owner или owner следующей проверки.
- **Next action:** один проверяемый шаг.
- **Blockers by role:** reviewer, security, deploy, manager, architecture — кто может заблокировать sync или decision path.

## Constraints

- Не превращать любое обсуждение в ceremony: для простого вопроса ответить напрямую.
- Не принимать авторитет, статус или раздражение как evidence.
- Не продолжать debate без нового evidence, owner или escalation path.
