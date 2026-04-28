# Tech Laws

These documents are **non-negotiable** technical constraints for the project.
Strategy lives at the repo root. **Implementation rules live here.**

| Document                                              | Purpose                                                                 |
|-------------------------------------------------------|-------------------------------------------------------------------------|
| [PERFORMANCE_BUDGETS.md](PERFORMANCE_BUDGETS.md)      | Hard runtime limits. Saves the game from bloat.                          |
| [BLUEPRINT_STANDARDS.md](BLUEPRINT_STANDARDS.md)      | Naming, folders, hygiene. Prevents spaghetti.                            |
| [MULTIPLAYER_RULES.md](MULTIPLAYER_RULES.md)          | Replication-aware architecture from day one. Prevents Phase 6 rewrite.   |
| [PCG_RULESET.md](PCG_RULESET.md)                      | The procedural generator IS the game design.                             |

## Rule of thumb

If a feature violates a Tech Law, the **feature** is wrong. Not the law.
If a law must change, it changes **here, with a date and a reason** — never silently in code.
