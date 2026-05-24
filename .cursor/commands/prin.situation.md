# /prin.situation — оценка рабочей ситуации через Life/Work принципы

Описать ситуацию с работы (конфликт, сбой, решение, управление людьми) и получить structured assessment: позиция в Five Steps, релевантные принципы, что aligned/violated, состояние механизма, visible sabotage patterns (если есть), приоритетные next actions. Подходит для обучения принципам на реальных кейсах, ретроспектив и «разбор полётов» без немедленного fix.

**source_principles:** Life-01, Life-01-01, Life-01-02, Life-01-03, Life-01-04, Life-01-05, Life-01-06, Life-01-07, Life-01-08, Life-01-09, Life-01-10, Life-02, Life-02-01, Life-02-02, Life-02-07, Life-03, Life-03-03, Life-03-04, Life-04, Life-04-01, Life-04-02, Life-04-03, Life-04-05, Life-05-01, Meta-Recursive-01, Work-01-05, Work-02, Work-02-01, Work-02-02, Work-02-03, Work-02-04, Work-02-05, Work-04-02, Work-04-03, Work-05-02, Work-05-05, Work-06-03, Work-07, Work-07-01, Work-07-03, Work-08-02, Work-08-05, Work-08-07, Work-10-04, Work-10-07, Work-10-12, Work-10-13, Work-11, Work-12, Work-13, Work-14, Work-16, Life-04-04, Life-04-01-a, Life-04-01-b, Life-04-03-a, Life-04-03-b, Life-04-03-c, Life-04-03-d, Life-04-03-f, Life-04-04-e, Life-02-01-c, Life-02-03-c

## Trigger

- Narrative ситуации с работы: конфликт, сбой, решение, governance gap, recurring pain.
- Visible sabotage signals: vague objection, blocked validation без owner, authority/believability mismatch, repeated blocker, sync deadlock, «все варианты плохие» без counter-evidence.
- Запрос verdict по принципам, не только vent (trivial vent → empathy + один yes/no вопрос).

## Input

Обязательно: narrative ситуации (что произошло, контекст, роли, частота, stakes). Опционально: ваша роль, уже принятые действия, эмоции/боль (как signal, не как verdict).

## Canonical Sources

**Portfolio fallback:** если `principles_sot/` или derivation docs отсутствуют — использовать rules `05–08_dalio_*.mdc` и steps этой команды как behavioral SoT; machine slice (`principles_sot/*.yaml`) — optional (канон в Meta.Dalio.LogicModel).

1. Reasoning loop: `principles_sot/Life-02.yaml`, sub-principles `Life-02-01` … `Life-02-07`
2. Open-mindedness / disagreement: `Life-03-03.yaml`, `Life-03-04.yaml`, `Work-04-02.yaml`, `Work-04-03.yaml`, `Work-05-02.yaml`, `Work-05-05.yaml`
3. Work problem cycle: `Work-11` … `Work-16` chapter + sub-principles in `principles_sot/`
4. Escalation / action metrics: `Work-10-12.yaml`, `Work-10-13.yaml`, `Work-06-03.yaml`
5. Rules: `.cursor/rules/05_dalio_problem_solving.mdc`, `06_dalio_decisions.mdc`, `07_dalio_work_management.mdc`, `08_dalio_learning.mdc`, `28_bridgewater_reasoning.mdc` (Anti-Sabotage Protocol)
6. Handoffs: `/prin.diagnose`, `/prin.sync`, `/prin.decide`, `/prin.escalate`, `/prin.design`, `/prin.learn`, `/prin.teach`, `/prin.verify`, `/prin.governance`

## Steps

1. **Facts vs opinions (`Life-01-02`, `Life-05-02`, `Work-01-01`):** выделить наблюдаемые факты, assumptions, мнения участников.
2. **Reality lens (`Life-01`, `Life-01-01`, `Life-01-04`):** hyperrealism — plan grounded в causal reality; negative trends не замалчиваются.
3. **Five Steps map (`Life-02`):** где ситуация в цикле — goal, problem, root cause, plan, execution, outcome; что пропущено или перепутано по порядку.
4. **Life lens:** ego/blind-spot barriers (`Life-03-01`, `Life-03-02`); mental maps (`Life-02-07`); pain as signal (`Life-01-07`, `Life-02-06`); accountability (`Life-01-09`); higher-level view (`Life-01-10`).
5. **Work lens (MECE):**
   - Problem detection (`Work-11`) — проблема названа или замалчивается?
   - Diagnosis (`Work-12`) — root cause vs symptom?
   - Mechanism design (`Work-13`) — workaround vs системное улучшение?
   - Execution (`Work-14`) — follow-through после решения?
   - Governance (`Work-16`) — owner, authority, escalation?
6. **Sabotage pattern scan (MECE, `28_bridgewater_reasoning.mdc`):** если narrative содержит visible sabotage — классифицировать по одному primary pattern из библиотеки ниже; если pattern уже полностью разложен (class + invariant + evidence level + owner) — не разворачивать ceremony, перейти к next action.
7. **Consequence check (`Life-01-08`):** first vs 2nd/3rd order effects; short-term temptation vs long-term goal.
8. **Principle assessment table:** для каждого релевантного `PrincipleId` — **aligned / violated / unknown** + one-line evidence из narrative; не более 8 строк без запроса «развернуть».
9. **State verdict:** `healthy` / `at-risk` / `broken mechanism` + named biggest gap (skill, plan, process, context).
10. **Next actions (max 3):** owner, metric, one experiment; явный handoff command если нужен deep dive.
11. **Learning hook:** если pattern recurring → `/prin.learn`; если capability gap → `/prin.teach`.

## Sabotage Pattern Library (MECE)

Каждый pattern — closed set; новый сигнал попадает в класс или помечается `out of scope`. Для matched pattern заполнить все поля Anti-Sabotage Protocol и указать handoff.

| Pattern | Objection class | Invariant (если не назван) | Evidence level (типичный) | Owner (кто validate/waive) | Next experiment | Handoff |
| --- | --- | --- | --- | --- | --- | --- |
| **Vague objection** | people/process или governance | «не назван — нет механизма» | intuition / authority | role с authority на criteria pass/fail | Запросить named invariant + counter-evidence или bounded yes/no | `/prin.sync` → `/prin.decide` если sync не закрывает |
| **Blocked validation** | review, security, deploy, product | «не назван — нет механизма» | intuition или missing | named blocker owner по роли | Один artifact/log/metric/demo, который закрывает или falsifies block | `/prin.escalate` если owner unknown или waive недоступен |
| **Believability mismatch** | governance или product | decision quality / risk tolerance | authority vs artifact/tool/metric | decision owner с override authority | Сравнить believability rank: artifact > tool > metric > demo > intuition | `/prin.governance` или `/prin.decide` → `/prin.escalate` если нет authority |
| **Repeated blocker** | любой из MECE classes | prior invariant или «не обновлён» | same level без new item | blocker owner + escalation owner | Зафиксировать: что изменилось с прошлого блока? new evidence или repeat | `/prin.escalate` (`Work-10-13`, `Work-06-03`) |
| **Sync deadlock** | people/process или review | observable outcome vs «процесс соблюдён» | demo missing — compliance theater | decision owner для bounded choice | Один observable outcome metric после «согласия» | `/prin.sync` → `/prin.escalate` если deadlock persists |
| **Toxic «all options bad»** | product или governance | «не назван — нет механизма» | intuition без counter-evidence | decision owner | MECE option set (2–3) + per-option kill criterion или counter-evidence | `/prin.decide` если options готовы; `/prin.sync` если disagreement скрыт |

**Principle anchors:** `Life-03-03`, `Life-03-04` (productive disagreement, believability); `Work-04-02`, `Work-04-03` (get-in-sync, assertive + open); `Work-05-02`, `Work-05-05` (competent counter-evidence, decision competence); `Work-10-12` (action plan + progress metric); `Work-10-13` (escalate when blocked).

## Evidence Requirements

- Каждый violated/aligned claim привязан к фрагменту narrative или явному «unknown — need evidence».
- Verdict не строится только на эмоциях без observable signal.
- Sabotage pattern не присваивается без observable signal в narrative; иначе — `no pattern matched`.
- Next actions проверяемы (не «быть лучше»).

## Output

- **Situation summary:** facts, stakeholders, frequency, stakes.
- **Five Steps position:** current step + skipped steps.
- **Sabotage pattern (if matched):** pattern name | objection class | invariant | evidence level | owner | next experiment | handoff.
- **Principle assessment table:** PrincipleId | aligned/violated/unknown | evidence snippet.
- **State verdict:** healthy / at-risk / broken + biggest gap class.
- **Next actions:** up to 3 with owner, metric, suggested `/prin.*` handoff.
- **Blockers by role:** reviewer, security, deploy, manager, architecture, governance — кто может заблокировать validation или decision path.
- **Learning note:** один principle для углублённого изучения по этому кейсу.

## Exit Criteria

- Facts отделены от opinions; Five Steps position назван.
- Если sabotage visible — primary pattern classified с полным Anti-Sabotage Protocol row или explicit `no pattern matched`.
- Verdict + max 3 next actions с owner и metric; handoff указан когда validation/decision blocked.
- Blockers by role заполнены или явно `none identified`.
- Не moralize/blame — mechanism and skill gaps (`Life-02-06`).

## Constraints

- Не выдавать generic advice без привязки к `PrincipleId` из `principles_sot/`.
- Не подменять `/prin.diagnose` полным root-cause analysis — situation = orient + assess + prioritize; deep diagnosis → handoff.
- Не moralize/blame people — mechanism and skill gaps (`Life-02-06`).
- Не разворачивать full sabotage template, если blocker уже имеет class, invariant, evidence level и owner — перейти к next action.
- Trivial vent without ask for assessment — краткий empathy + один уточняющий yes/no вопрос.
