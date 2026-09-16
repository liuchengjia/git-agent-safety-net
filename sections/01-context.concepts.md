# Context spine

## Claims
- A commit identifies a selected file snapshot and links it to history.
- Working files, staging, and HEAD are distinct states.
- A branch is a movable commit reference; Git does not require GitHub.

## Decisions
- Define the objects before arguing for agent safety.
- Use a monospaced state diagram: commands label transitions, diffs label comparisons.
- Introduce HEAD now because recovery commands use it later.

## Open questions
- None for the declared audience.

## Not doing
- Git object storage, hashing algorithms, or detached HEAD recovery.
