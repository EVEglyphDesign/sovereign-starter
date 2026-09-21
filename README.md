# The Sovereign Starter

One file. It is the harness itself — not a summary of one, not a pointer
to one.

**[`SOVEREIGN-STARTER.md`](./SOVEREIGN-STARTER.md)** carries everything
needed to put an AI surface under an operating contract: the contract,
the skills that make it load, the economics that justify it, the
register that proves it, and the mechanism that changes it.

| Part | What it is |
|---|---|
| **0 — Fitting** | Six capabilities, the onboarding probe, what to do when one is missing |
| **I — Narrowing** | The contract. Thirteen worked rules, in your voice |
| **II — Skills** | The contract in the form a machine actually picks up |
| **III — Economics** | Why it is worth the time, for the person who has to approve it |
| **IV — Observations** | The evidence register |
| **V — Rule of three** | How evidence becomes rule changes |
| **VI — Client overlays** | One core, many clients |
| **Annex A** | Per-surface notes. Dated, and expected to go stale |

Parts I, II and III are one contract with three faces: what the machine
is told, how the telling is made to load, and why someone signs off on
the cost. Remove one and the other two stop working.

## The design rule that matters most

**The core is written against capabilities. The annex is written against
products.**

Products churn. A harness whose rules are phrased in product names dies
with them. So every rule in Parts I–V is phrased against a *capability*
— can this surface write to the record, can it reach the repository, can
it see what it costs — and never against a product name. When a surface
changes, you re-run the probe in §0.3, which asks the surface itself
what it can do. You do not wait for someone to update a table.

The six capabilities:

| | Capability | The question it answers |
|---|---|---|
| **C1** | Instruction persistence | Does the contract load itself every session, or must someone attach it? |
| **C2** | Record write | Can the AI append to the register without you pasting? |
| **C3** | Authoritative reach | Can it query the record of truth rather than its own context? |
| **C4** | External fetch | Can it fetch a URL or search in-session? |
| **C5** | Spend visibility | Can it read what it is costing, in the units you are billed in? |
| **C6** | Artifact read-back | Can it open what it just built and inspect it? |

Model quality, context length and speed are deliberately not on that
list. They change constantly and change nothing about how the harness is
fitted.

## Five-minute start

1. **Copy the file** into whatever surface you use with your AI.
2. **Run the probe** in §0.3 — six questions, one turn. "Not sure"
   counts as No until demonstrated. Then verify C2 and C3 rather than
   trusting the answers: ask for a test row to be written and read back,
   and ask for a named fact from the record.
3. **Fill a capability card** (§0.2) and apply the degradation rules in
   §0.4 for whatever is missing.
4. **Make it yours** (§0.6). Replace the document ID. Delete the Part I
   rules that do not describe your practice and rewrite the rest in your
   own words — rules you did not write will not survive contact with
   your own work. Delete the example register row, keep the schema.
5. **Point the AI at it.** "Read `SOVEREIGN-STARTER.md` before you act,
   acknowledge with the §0.8 signature, and log misses after my request
   is satisfied, never instead of it."
6. **Verify the load.** Ask for the signature. It carries the Part I
   rule count, the top register ID and the live capability list — things
   only a reader can produce. "Contract read and acknowledged" is a line
   any model emits whether or not the file arrived.

## Logging depends on C2, and this is where harnesses die

The single most common way this method fails quietly: the operator waits
for register rows that never come, and concludes the method did not
work.

On a **C2-capable** surface the AI appends rows itself. On a
**C2-absent** surface it cannot, and the instruction is different:

> When you miss, state the row in the register's table format at the end
> of your return. I will paste it in.

Then paste it. If you will not paste, do not pretend that surface
carries the register — name the surface that does. §0.4 has the honest
degradation for each of the six.

## Where to keep the file

Anywhere you can keep one plain-text document your AI can read: a
project's attached files, a notes page, a document, a folder on your
machine, or a repository.

They are not equivalent, and the difference is not convenience. A
repository with a write-scoped connector gives you C1, C2 and C3 in one
move — the contract loads itself, the register closes its own loop, and
the AI can reach the record of truth. A file attached to a vendor
project gives you none of the three and leaves the record inside someone
else's product.

Start wherever is easiest. Know which capabilities you are trading away,
and record them on the card. Part III §3 is the longer argument for why
custody is worth the setup.

## If you have to justify this to someone

Part III is the working version of that argument, and
**[`THE-CASE.md`](./THE-CASE.md)** is the long form with sources — for
partners, programme directors, general counsel and finance:

- **Usage is a regulated activity.** The EU AI Act has been in general
  application since 2 August 2026 and its AI literacy obligations since
  2 February 2025. GDPR Article 5(2) requires controllers to
  *demonstrate* compliance. The EU Data Act has applied since
  12 September 2025. ISO/IEC 42001 certifies an AI management system.
  Every one asks for the same artefact: a contemporaneous, attributable
  record of how the AI was governed and what it did. You cannot
  demonstrate what you did not record.
- **Unit cost, not seat cost.** Seats look fixed, so nobody measures what
  an AI-assisted deliverable costs. The register measures rework, and
  the rule of three is the control that reduces it. Note the honest
  limit stated in Part III §2: a miss-only register shows *composition*,
  not *rate*, unless you keep the denominator line — and it is
  selection-biased by construction, so it is a rework register, never a
  quality metric.
- **Data as a capital asset.** The 2025 System of National Accounts
  recognises data as a produced asset; IAS 38 still keeps most
  internally generated intangibles off the balance sheet. The asset is
  real, growing and invisible. Durable, attributable, controlled,
  transferable is what makes data behave like capital, and a versioned
  record with provenance has all four where a chat history has none.

Read it before taking the method into a room where someone has to
approve it.

## Across more than one client

Part VI is the boundary. The core — Parts I, II, III, V and the class
taxonomy — is shared and never forks per client. Per client you keep an
overlay: their canon values, their systems of record, their operator
policy and its tier-1 constraints, their capability cards, their
register.

**Registers never merge.** What crosses from an engagement back into
your core is the rule, never the rows. Rows carry client facts; rules do
not.

## Why letters for the classes

Letters are cheap to add and never need renaming for having described
something poorly. The harder rule is in Part IV: **do not silently
reassign a letter.** A reassigned letter is worse than a deleted one —
old rows stay readable and now mean the wrong thing. Add freely,
reassign none. Across clients the letters are the only thing that makes
two registers comparable.

## What is in this repository

- [`SOVEREIGN-STARTER.md`](./SOVEREIGN-STARTER.md) — the harness. Parts
  0–VI and Annex A. Copy, edit, delete as needed.
- [`THE-CASE.md`](./THE-CASE.md) — the long-form argument with sources
  and dates, for the person who has to approve the method rather than
  the person who will run it.
- [`LICENSE-NOTICE.md`](./LICENSE-NOTICE.md) — MIT. You own what you
  write; this repository holds the method, not your notes.
- `docs/` — the public landing page at
  [eveglyphdesign.github.io/sovereign-starter](https://eveglyphdesign.github.io/sovereign-starter/),
  carrying a mirrored copy of the harness.
- `_archive-v1/` — the earliest shape, kept so old links resolve. Ignore
  unless you were pointed at it.

That is the entire kit.
