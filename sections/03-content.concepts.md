# Content spine

## Claims
- Explicit staging and both diffs make acceptance inspectable.
- Fixed valid-input tests catch squared-error removal; contract tests validate guards.
- Restore, revert, and reset act on different scopes.
- An experimental branch earns integration through review and validation.

## Decisions
- Generate a separate disposable lab; never reset the tutorial manuscript.
- Use Python standard library only; proposals are deterministic simulations, not actual model outputs.
- Use explicit HEAD in file recovery to avoid the staged-mistake trap.
- Show reset as a scoped alternative; verify it only in an automatically generated temporary repository.
- Keep PySR to a plan, and label that limitation in the prose and demo.
- Use --ff-only so divergence fails visibly rather than silently adding a merge.
- A before/after commit graph shows both labels on the same chain; the main label alone moves during the fast-forward.
- Keep expected status in a literal block so Pandoc preserves its meaningful leading blank.

## Open questions
- The real PySR exercise is deferred to a later course activity.

## Not doing
- Claims that five checks prove general numerical correctness; the contract is finite numeric lists.
- Live remote creation, authentication, conflict resolution, or force pushing.
