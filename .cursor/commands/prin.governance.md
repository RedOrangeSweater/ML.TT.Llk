# /prin.governance — stakeholder, owner и escalation review

Проверить governance перед масштабированием или org-dependent решением: кто решает, кто исполняет, кто эскалирует, кто может заблокировать. Подходит для cross-team, deploy, security, PR и process changes.

**source_principles:** Life-04-05, Meta-Recursive-01, Work-01-04, Work-03, Work-03-03, Work-03-04, Work-03-05, Work-04-03-d, Work-04-04, Work-04-04-a, Work-04-04-c, Work-04-04-l, Work-07, Work-07-01, Work-07-02, Work-07-03, Work-08, Work-08-01, Work-08-02, Work-08-03, Work-08-04, Work-08-05, Work-08-06, Work-08-07, Work-08-08, Work-10, Work-10-01, Work-10-03, Work-10-04, Work-10-05, Work-10-07, Work-10-08, Work-10-09, Work-10-10, Work-10-11, Work-10-13, Work-14, Work-15, Work-15-01, Work-16, Work-16-01, Work-16-02, Work-16-03, Work-13-05, Work-13-06, Work-13-09, Work-13-10, Work-08-04-a, Work-08-04-b, Work-15-01-b, Work-15-01-c, Work-01-03-a, Work-01-04-c, Work-01-04-d, Work-01-04-e, Work-07-01-a, Work-07-02-a, Work-13-05-a, Life-04-01-b, Work-08-01-a, Work-08-01-b, Work-08-01-c, Work-08-01-d, Work-08-01-e, Work-09-01-b, Work-09-03-f, Work-10-02-e, Work-10-04-b, Work-10-05-a, Work-12-08-l, Work-13-05-d, Work-13-09-a, Work-13-10-a, Work-15-01-a, Work-16-01-a, Work-16-01-g, Work-16-01-b, Work-16-01-c, Work-16-01-d, Work-16-01-e, Work-16-01-f, Work-16-01-h

## Input

Обязательно: описание решения или плана, затрагивающего людей, роли, approvals или deployment. Опционально: список известных stakeholders.

## Canonical Sources

**Portfolio fallback:** если `principles_sot/` или derivation docs отсутствуют — использовать rules `05–08_dalio_*.mdc` и steps этой команды как behavioral SoT; machine slice (`principles_sot/*.yaml`) — optional (канон в Meta.Dalio.LogicModel).

1. `principles_sot/Work-01-04.yaml`, `Work-07.yaml`, `Work-07-01.yaml`, `Work-07-02.yaml`, `Work-07-03.yaml`, `Work-10-13.yaml`, `Work-14.yaml`, `Work-15-01.yaml`, `Work-16.yaml`, `Work-16-01.yaml`, `Work-16-02.yaml`, `Work-16-03.yaml`, `Meta-Recursive-01.yaml`
2. Rule: `.cursor/rules/07_dalio_work_management.mdc` (`cursor.management.check_governance_before_scaling`)
3. Gap context: `docs/sdlc/00_Main/04_QA/GAP_ANALYSIS_ru.md` (Work 11–14/16)

## Steps

1. **Scope check:** решение зависит от org/people или это solo technical edit?
2. **Decision owner:** кто принимает финальное решение.
3. **Executors:** кто делает work после decision.
4. **Information & authority:** есть ли у responsible party данные и полномочия.
5. **Escalation path:** куда эскалировать при deadlock или blocker.
6. **Blocker map (MECE):** reviewer, security, deploy, manager, architecture, compliance — кто теоретически может stop the line.
7. **Principle-based tools (`Work-15-01`):** governance и decision path опираются на principle-aligned tooling, не ad-hoc process.
8. **Group leadership (`Work-16-02`):** для important decisions — group input, не single decision-maker без believable disagreement.
9. **Partnership balance (`Work-16-03`):** mechanism и rules дополняют, но не заменяют trust и genuine partnership.
10. **Anti-dismissal:** для каждого blocker — какой invariant/metric закрывает возражение, не vague «потом подумаем».
11. **Escalation ladder:** local owner → decision owner → blocker owner → documented unresolved decision.
12. **Mark N/A:** если solo reversible edit без delegation — явно governance not applicable.

## Evidence Requirements

- Named roles или teams, не только «команда».
- Явный escalation path или gap «escalation unknown» с next step to resolve.
- Список потенциальных blockers с owner для каждого approval.
- Для каждого blocker: что он может заблокировать, какой invariant он защищает, какая evidence может снять objection.

## Output

- **Governance table:** decides / executes / escalates / informs.
- **Blocker map:** role → what they can block → evidence needed → owner to engage.
- **Escalation ladder:** current owner → next owner → requested yes/no decision → deadline/metric.
- **Gaps:** missing authority, missing information, missing approver.
- **Next engagement:** кого спросить первым (yes/no friendly).
- **Commit surface:** TASK/ADR/decision log paths, если governance фиксируется в docs.

## Constraints

- Не полагаться на individual heroics, когда нужен mechanism.
- Не применять тяжёлый governance review к solo local typo/edit.
- Output должен быть role-neutral: понятен engineer, reviewer, manager, security, deploy.
