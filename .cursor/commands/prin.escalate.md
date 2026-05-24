# /prin.escalate — escalation request для blocker/deadlock и visible sabotage

Сформировать проверяемую escalation request, когда текущий owner не может закрыть вопрос: нет authority, другой role блокирует validation, objection повторяется без evidence, sync deadlock, believability/authority mismatch, или decision path застрял. Для visible sabotage — применить Anti-Sabotage Protocol и blocker role map.

**source_principles:** Life-03-03, Life-03-04, Work-04-02, Work-04-03, Work-05-02, Work-05-05, Work-06-03, Work-06-06, Work-10-12, Work-10-13, Work-16, Work-16-01, Work-16-02, Meta-Recursive-01, Work-16-01-c, Life-03-03-f

## Trigger

- Current owner lacks authority, information, or capability to close blocked outcome (`Work-10-13`).
- Same blocker repeats without new evidence (artifact, tool output, metric, demo).
- Validation blocked by another role without named invariant, owner, or pass/fail criteria.
- Believability mismatch: decision rests on authority/intuition while higher-believability evidence exists and override authority missing.
- Sync deadlock: parties claim agreement but observable outcome unchanged (`Work-06-03`).
- Vague objection or «all options bad» persists after `/prin.sync` or `/prin.situation` handoff — governance failure, not technical debate.

**Do not trigger:** solo reversible edits; informational governance query; blocker already fully specified with clear next action within current owner authority; new evidence arrived since last block.

## Input

Обязательно: blocker или deadlock (что заблокировано, кем, как часто). Опционально: current owner, escalation owner, blocked artifact, known stakeholders, deadline, prior attempts, matched sabotage pattern from `/prin.situation`.

## Canonical Sources

**Portfolio fallback:** если `principles_sot/` или derivation docs отсутствуют — использовать rules `05–08_dalio_*.mdc` и steps этой команды как behavioral SoT; machine slice (`principles_sot/*.yaml`) — optional (канон в Meta.Dalio.LogicModel).

1. Disagreement / believability: `Life-03-03.yaml`, `Life-03-04.yaml`, `Work-04-02.yaml`, `Work-04-03.yaml`, `Work-05-02.yaml`, `Work-05-05.yaml`
2. Escalation / governance: `Work-06-03.yaml`, `Work-06-06.yaml`, `Work-10-12.yaml`, `Work-10-13.yaml`, `Work-16.yaml`, `Work-16-01.yaml`, `Work-16-02.yaml`, `Meta-Recursive-01.yaml`
3. Rules: `.cursor/rules/07_dalio_work_management.mdc`, `.cursor/rules/28_bridgewater_reasoning.mdc` (Anti-Sabotage Protocol)
4. Workflow pair: `/prin.governance` для stakeholder map, `/prin.situation` для pattern classification, `/prin.sync` для pre-escalation disagreement map, `/prin.decide` для final decision log.

## Steps

1. **Escalation gate:** подтвердить trigger; если kill criteria met (см. ниже) — не эскалировать, вернуть next action.
2. **Blocker class (MECE):** technical, security, deploy, review, product, people/process, governance, or out of scope.
3. **Anti-Sabotage Protocol fields (`28_bridgewater_reasoning.mdc`):**
   - **Objection class:** из шага 2.
   - **Invariant:** what must remain true; if none named → `no named invariant — no mechanism`.
   - **Evidence level:** artifact/log, tool output, metric, demo, or intuition/authority.
   - **Owner:** who can validate, waive, or decide.
   - **Next experiment:** one check that would resolve or reduce the objection (если escalation ещё не финальный шаг).
4. **Blocked outcome:** что именно нельзя завершить без escalation (release, merge, decision, budget, hire, architecture choice).
5. **Evidence gap:** что отсутствует или повторяется без update; ссылка на artifact если есть.
6. **Authority check (`Work-10-13`):** почему current owner не может решить вопрос сам.
7. **Blocker role map:** reviewer | security | deploy | manager | architecture | governance — для каждой relevant role: can block? | owner name/role | can waive? | escalation path.
8. **Group input (`Work-16-02`):** если escalation требует higher authority — involve leadership group, не только single executive.
9. **Requested decision:** один yes/no или bounded choice (max 3 options); не open-ended «разберитесь».
10. **Success metric (`Work-10-12`):** observable signal после decision — не activity, а progress toward blocked outcome.
11. **Kill criteria for escalation:** когда escalation **не** нужна или **останавливается**:
    - Blocker предоставил named invariant + evidence ≥ demo и owner в рамках authority current owner.
    - New evidence arrived since last block — вернуть к `/prin.sync` или `/prin.decide`, не эскалировать как repeat.
    - Outcome reversible и current owner имеет authority — local fix path достаточен.
    - Objection class `out of scope` с named reason — redirect, не escalate.
12. **Fallback:** если owner неизвестен — first engagement: кто может назвать blocker owner и decision owner (one addressee, one question).

## Evidence Requirements

- Нельзя escalation без named blocked outcome.
- Нельзя blocker без owner hypothesis или explicit owner unknown gap.
- Vague objection эскалируется только как governance failure: нет invariant, evidence или owner.
- Repeated blocker требует evidence gap statement: «same invariant, no new artifact since [date/attempt]».

## Output

- **Escalation request:** blocker class, blocked outcome, evidence gap, current owner, blocker owner, escalation owner.
- **Anti-Sabotage Protocol row:** objection class | invariant | evidence level | owner | next experiment (if applicable before decision).
- **Blockers by role:** reviewer, security, deploy, manager, architecture, governance — block? | owner | waive authority? | notes.
- **Decision needed:** exact yes/no or bounded choice (max 3 options).
- **Success metric / deadline:** observable signal and timing if known.
- **Kill criteria check:** why escalation proceeds OR why stopped.
- **Next engagement:** один адресат, один вопрос, один artifact request if evidence gap.

## Exit Criteria

- Trigger confirmed; kill criteria evaluated explicitly.
- Blocked outcome, blocker owner (or unknown gap), and requested decision are bounded and testable.
- Anti-Sabotage Protocol fields complete or `N/A — evidence-backed blocker`.
- Blockers by role map filled for relevant roles.
- Success metric ties to outcome, not ceremony (`Work-10-12`).
- Next engagement is single-threaded (one addressee, one question).

## Constraints

- Не эскалировать solo reversible edits.
- Не использовать escalation как способ обойти valid evidence requirement.
- Не продолжать локальные попытки, если issue requires higher authority.
- Не предлагать «ещё один sync» как единственный шаг при repeated blocker без new evidence — sync уже failed; escalate or bounded decide.
- Не эскалировать informational queries («кто owner X?») без blocked outcome.
