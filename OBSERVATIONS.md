# Observations — what actually happened

This file is the evidence base for [`NARROWING.md`](./NARROWING.md).
Every row is an observation of the AI's operation from my perspective —
what the work put on my plate that the work should not have.

The register is not the point. Individual rows can be under-parsed,
mis-tagged, prose-drifting, or logged late — none of that changes what
the aggregate says. **The pattern will not lie.** Volume and repetition
swamp per-row noise.

I use the register to write and sharpen the rules in
[`NARROWING.md`](./NARROWING.md). When three observations of the same
class stack up, a rule is added or tightened. If the class keeps
stacking after the rule, the rule is under-specified. If the class
stops stacking, the rule was right.

## Schema

Each observation is a row with the columns below. Add columns if I
need them, drop columns if I don't. Keep the class and fault columns —
they are what makes the pattern legible.

| Column | What goes in it |
|---|---|
| `date` | ISO date, `YYYY-MM-DD` |
| `id` | Sequence in the day, e.g. `OBS-2026-09-12-01`. Never reused |
| `class` | Single letter — the shape of the miss. See classes below |
| `fault` | Who caused me to bear the cost — Agent, Instruction, Tooling, Upstream |
| `asked` | What I asked for, in one line |
| `done` | What was done instead, in one line |
| `cheaper` | The path that should have been taken |
| `waste` | The estimated cost — in time, in money, in trust |

## Class taxonomy

Classes are letters, not names, because letters are cheap to add and
never need to be renamed. Start with the ones below and add letters as
new shapes appear. Do not delete a letter once used; the register
depends on prior IDs staying stable.

| Letter | Shape of the miss |
|---|---|
| **C** | Canon breach — a stated rule was violated |
| **R** | Retrieval waste — re-derived a fact that was already held |
| **D** | Durability — worked in the session only, or spoke about state without fetching it |
| **L** | Link and format — bare URL, unclickable, or shallow deep-link |
| **E** | Equality drift — language read the AI and me as peers |
| **S** | Spend — expensive action taken without confirming first |
| **I** | Interrupt — asked permission for a free or cheap action |
| **P** | Processing drift — narrated the process, apologised, or restated the request |
| **T** | Timing — action was correct but late enough that it cost me |
| **H** | Handoff — the return did not survive being forwarded to the next reader |

Any letter I have not used yet is available. Add a new class the
moment I see a shape that does not fit an existing one.

## Fault ranks

Four ranks, from my perspective. The class names the *shape* of the
miss; the fault names *who caused* me to bear it.

| Rank | When it applies |
|---|---|
| **Agent** | The AI did it. Most rows will be this |
| **Instruction** | My ask was ambiguous, contradictory, or missing key context |
| **Tooling** | The platform, sandbox, or connector was the cause |
| **Upstream** | A third-party service, external data source, or network was the cause |

## The register

<!-- Add new rows at the top. Oldest at the bottom. -->

| Date | ID | Class | Fault | Asked | Done | Cheaper | Waste |
|---|---|---|---|---|---|---|---|
| 2026-09-12 | OBS-2026-09-12-01 | C | Agent | *Example row.* Deliver a two-page PDF with the palette I named | Delivered a three-page PDF with a different palette | Read the built PDF back before delivery, quote the palette hex in the return | About twenty minutes of correction cycle; my confidence in the check |

Delete the example row when I have logged one of my own.

## How to log a new observation

1. Pick the class (letter) and the fault (rank).
2. Write the four columns — asked, done, cheaper, waste — in one line
   each. Keep them terse; the point is the pattern, not the essay.
3. Add the row at the top of the register.
4. If this is the third observation of that class, sharpen the rule in
   [`NARROWING.md`](./NARROWING.md), or add a new one.

## When the file gets long

The register works at any size. A dozen rows already show a pattern; a
hundred rows show it sharply enough that individual rows do not need
to be perfect. When the file feels too long to scroll:

- **Do not delete old rows.** They are the evidence base.
- **Do not renumber.** IDs must be stable.
- **Do split the register into a top table of recent rows and a section-
  by-class deep dive below**, if that makes it easier to scan. Or move
  the older rows into an archive file and leave a pointer at the
  bottom. The two-file shape survives either way.

## What this file is not

- Not a to-do list. Rules for the AI go in `NARROWING.md`.
- Not a moral document. "Observation" is deliberately neutral; the
  register makes no claim about intent.
- Not a private log. This is what I use to convince myself, the AI,
  and anyone I hand my method to that the rules in `NARROWING.md` were
  earned, not invented.
