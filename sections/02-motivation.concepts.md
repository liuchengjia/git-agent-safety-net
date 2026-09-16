# Motivation spine

## Claims
- A lower score can be caused by evaluator corruption.
- A checkpoint makes recorded code recoverable; tests and review determine acceptance.
- Git does not reverse external effects or record the whole runtime environment.

## Decisions
- Use cancellation of signed errors as the concrete failure throughout.
- State the limits before demonstrating destructive recovery.
- Distinguish history separation from process isolation.

## Open questions
- None blocking delivery.

## Not doing
- Credential remediation procedures or agent permission systems.
