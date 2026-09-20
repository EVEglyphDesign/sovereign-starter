# The one-file method

One file. That is the whole method.

- **[`SOVEREIGN-STARTER.md`](./SOVEREIGN-STARTER.md)** — one file with
  three functions inside it:
  1. **Narrowing** — what you want the AI to do or not do, in your
     voice. The AI reads this first, before it acts for you.
  2. **Observations** — what actually happened. Every time the AI's
     work put something on your plate that it should not have, you log
     one row. Individual rows can be sloppy; the aggregate is what
     matters. **The pattern will not lie.**
  3. **Rule of three** — the mechanism that turns observations into
     rule changes. When three observations of the same shape stack up,
     a rule enters Part I. If the rule closes the shape, it was right.
     If the shape keeps repeating, the rule was under-specified.

That is the whole loop. No framework to adopt. No worldview to buy.
One file you write in your own words, and a habit of adding rows to
the register when the AI wastes your time.

The three functions are named inline so a team can read Parts I and II
together and see, on one page, what has been agreed and why.

## If you have to justify this to someone else

The description above is the mechanism. It is not the argument you make
to a partner, a general counsel or a finance director — they will want
to know why a text file is worth anyone's time.

**[`THE-CASE.md`](./THE-CASE.md)** is that argument, on three grounds:

- **Governing legislation around usage.** The EU AI Act has been in
  general application since 2 August 2026, and its AI literacy
  obligations since February 2025. GDPR Article 5(2) requires
  controllers to *demonstrate* compliance. The EU Data Act has applied
  since September 2025. ISO/IEC 42001 certifies an AI management
  system. Every one of them asks for the same thing: a contemporaneous,
  attributable record of how the AI was governed and what it actually
  did. You cannot demonstrate what you did not record.
- **Economics.** AI bought as seats looks like a fixed cost, so nobody
  measures the unit cost of AI-assisted work. The register measures
  rework rather than tokens, and the rule of three is the control that
  converts that evidence into a reduced unit cost.
- **Data as a capital asset.** The 2025 System of National Accounts
  recognises data as a produced asset; IAS 38 still keeps most
  internally generated intangibles off the balance sheet. The asset is
  real, growing and invisible. What makes data behave like capital —
  durable, attributable, controlled, transferable — is exactly what a
  versioned record with provenance produces, and exactly what a chat
  history in a vendor's product does not.

Read it before you take the method into a room where someone has to
approve it.

## Five-minute start

1. Download or copy the file into whatever surface you already use
   with your AI. Options in the next section.
2. Read Part I (Narrowing). Delete rules that do not apply to you.
   Rewrite the ones that do into your own words. The ten rules in the
   file are worked examples, not a fixed set.
3. Read Part II (Observations). Delete the example row.
4. Point your AI at the file. "Read `SOVEREIGN-STARTER.md` before you
   answer, and log any miss into its Part II register" is enough of an
   instruction.
5. Start using the AI normally. When it wastes your time, add one row.
   That is the loop.

## Where to keep the file

The file is plain Markdown. It works anywhere you can keep one
plain-text document your AI can read.

- **Claude project knowledge** — attach the file to a project.
  Reference it in the system prompt or the first turn.
- **ChatGPT project files** — upload the file to a project. Reference
  it in your first message.
- **Perplexity project files** — attach the file to a project. Point
  the project instructions at it.
- **A Notion page** — paste the file into a page. Copy the page URL
  into the AI's context.
- **A Google Doc** — one document. Copy the doc URL into the AI's
  context.
- **A folder on your computer** — `~/ai-notes/SOVEREIGN-STARTER.md`.
  Point the AI at the file.
- **A GitHub repository** — this repository is the reference layout,
  but you do not need a repository to use the method. A repository is
  useful when you have graduated past what a scratchpad can hold.

The method does not care which surface you pick. It cares that the
file exists, that the AI reads Part I before acting, and that you add
rows to Part II when the AI's work costs you.

One caveat worth reading `THE-CASE.md` for: the surfaces above are not
equivalent once the record has to be *defended* rather than merely
consulted. A file inside a vendor's product is not durable,
attributable, controlled or transferable in the sense a regulator or
an auditor means. Start wherever is easiest; know which properties you
are trading away while you do.

## Why one file instead of two

An earlier version of this starter shipped as two files
(`NARROWING.md` for the rules and `OBSERVATIONS.md` for the register).
Two files made the split between rules and evidence tidy on paper.
Uploaded into an AI surface — a Claude project, a ChatGPT project, a
Notion page — the split cost more than it paid: the AI had to be told
about both files, in the right order, on every session.

One file with three named parts keeps the split legible to a reader
without the coordination overhead. Part I stays short and scannable.
Part II grows freely as evidence accumulates. Part III is the short
mechanism that connects them. All three arrive together in one
attachment.

If the file ever grows past what one attachment can hold, the natural
next step is to move Part II into its own file or a repository and
leave a pointer at the bottom of Part I. The shape survives either
way.

## Why letters for classes and not names

Letters are cheap to add. A letter never has to be renamed because it
was a poor description; a name does. The Part II register starts with
ten classes (C, R, D, L, E, S, I, P, T, H) — you will add your own
when a new shape appears. The letters do not have to match anyone
else's letters. They only have to be stable for your register.

## Graduating past one file

When the one-file scratchpad stops holding what you need:

- **Add a script that reads Part II** and prints the distribution by
  class and fault. That is the first automation worth building; it
  turns "the pattern will not lie" from an assertion into a line of
  output.
- **Add a dashboard** that shows the register over time.
- **Add categories, tags, or a database** if you have outgrown a
  Markdown table.
- **Split Part II back into its own file or a repository** that carries
  the register, the read script, and a dashboard. Keep Part I as the
  first read; nothing about the split changes what the AI sees first.

At every stage, the AI reads one short first read. That is the
invariant.

## What is in this repository

- [`SOVEREIGN-STARTER.md`](./SOVEREIGN-STARTER.md) — the file. Three
  functions inline: Narrowing (Part I, ten worked example rules),
  Observations (Part II, register schema and one example row), Rule of
  three (Part III, the short mechanism). Copy, edit, delete as needed.
- [`THE-CASE.md`](./THE-CASE.md) — the enterprise argument for adopting
  it: the legislation governing AI usage, the economics of measured
  rework, and data as a capital asset. Written for the person who has
  to approve the method rather than the person who will run it.
- [`LICENSE-NOTICE.md`](./LICENSE-NOTICE.md) — you own what you write.
  This repository holds the method, not your notes.
- `docs/` — the public landing page at
  [eveglyphdesign.github.io/sovereign-starter](https://eveglyphdesign.github.io/sovereign-starter/).
- `_archive-v1/` — the earliest shape of this starter, kept so old
  links resolve. Ignore unless you were pointed at it.

That is the entire kit.
