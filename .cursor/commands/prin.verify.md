# /prin.verify — dedicated outcome / mechanism verification

Проверить expected vs observed outcome после decision, deploy, teach cycle или mechanism change. Отделить progress metric от mere activity; continuous mechanism test.

**source_principles:** Life-02-05, Work-09, Work-09-02, Work-09-03, Work-09-06, Work-09-07, Work-10-02, Work-10-06, Work-10-10, Work-10-12, Meta-Recursive-04, Life-05-12, Work-14-03, Work-08-04-a, Work-10-01-a, Work-10-01-c, Work-01-02-a, Work-01-04-d, Work-05-05-a, Work-08-01-a, Work-08-01-b, Work-09-03-a, Work-09-03-b, Work-09-03-c, Work-09-03-d, Work-09-03-f, Work-10-04-a, Work-10-04-b, Work-13-09-a, Work-13-09-b, Work-14-03-a, Life-02-05-b, Work-16-01-g, Life-02-05-c, Work-16-01-h

## Input

Обязательно: что проверяем (decision, mechanism, teach objective) и когда/где смотреть signal. Опционально: уже заданные metrics из `/prin.decide` handoff или `/prin.teach`.

## Canonical Sources

**Portfolio fallback:** если `principles_sot/` или derivation docs отсутствуют — использовать rules `05–08_dalio_*.mdc` и steps этой команды как behavioral SoT; machine slice (`principles_sot/*.yaml`) — optional (канон в Meta.Dalio.LogicModel).

1. `principles_sot/Work-09.yaml`, `Work-09-02.yaml`, `Work-09-03.yaml`, `Work-09-06.yaml`, `Work-09-07.yaml`, `Work-10-02.yaml`, `Work-10-06.yaml`, `Work-10-12.yaml`, `Meta-Recursive-04.yaml`
2. Rules: `.cursor/rules/07_dalio_work_management.mdc` (`cursor.work.assign_owner_and_metric`)
3. Run configs: matching `MDLM:` task if verification is scripted

## Steps

1. **Expected state:** что mechanism/decision должен был дать (behavior + metric).
2. **Observed state:** artifact, log, metric, demo — believability ≥ demo.
3. **Deviation check (`Work-10-06`):** expected vs observed; named deviation или confirm aligned.
4. **Understanding gate (`Work-10-06.a`):** если understanding insufficient — block further decisions, gather evidence first.
5. **Progress vs activity (`Work-10-12`):** metric показывает движение к goal, не только busy work.
6. **Dual-purpose verify (`Work-10-02`):** если был teach cycle — проверить и goal outcome, и mechanism learning signal.
7. **Accurate assessment (`Work-09-03`):** feedback по evidence, не kindness blur.
8. **Next action:** continue / adjust mechanism / escalate / `/prin.learn` if recurring gap.

## Evidence Requirements

- Observable signal (command output, metric, log field, smoke test).
- Explicit pass/fail или deviation class.
- Owner для follow-up если verify failed.

## Output

- **Verification report:** expected, observed, verdict (pass / partial / fail).
- **Deviation diagnosis:** если fail — symptom, plausible mechanism owner.
- **Kill criteria check:** falsifies ли результат chosen option из decision log.
- **Next experiment:** one check или fix step.
- **Blockers by role:** reviewer, security, deploy, manager, architecture — кто может заблокировать verification или follow-up fix.
- **Commit surface:** test case, script, Run config if verify exposed gap.

## Constraints

- Не принимать «кажется работает» без named signal.
- Не путать verification с blame — focus на mechanism.
- Trivial already-confirmed edit — lightweight verify или skip with reason.
