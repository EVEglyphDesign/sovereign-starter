# The two-file method

Two files. That is the whole method.

- **[`NARROWING.md`](./NARROWING.md)** — what you want the AI to do or
  not do. In your voice. The AI reads this first, before it acts for
  you.
- **[`OBSERVATIONS.md`](./OBSERVATIONS.md)** — what actually happened.
  Every time the AI's work put something on your plate that it should
  not have, you log one row. Individual rows can be sloppy; the
  aggregate is what matters. The pattern will not lie.

The two files talk to each other. `OBSERVATIONS.md` is the evidence.
`NARROWING.md` is the response. When three observations of the same
shape stack up, a rule enters `NARROWING.md`. If the rule closes the
shape, it was right. If the shape keeps repeating, the rule was
under-specified.

That is the whole loop. No framework to adopt. No worldview to buy.
Just two files you write in your own words, and a habit of adding rows
to the register when the AI wastes your time.

## Five-minute start

1. Download or copy both files into whatever surface you already use
   with your AI. Options in the next section.
2. Read `NARROWING.md`. Delete rules that do not apply to you. Rewrite
   the ones that do into your own words. The ten rules in the file are
   worked examples, not a fixed set.
3. Read `OBSERVATIONS.md`. Delete the example row.
4. Point your AI at the two files. "Read `NARROWING.md` before you
   answer, and log any miss to `OBSERVATIONS.md`" is enough of an
   instruction.
5. Start using the AI normally. When it wastes your time, add one row.
   That is the loop.

## Where to keep the two files

The files are plain Markdown. They work anywhere you can keep two
plain-text documents your AI can read.

- **ChatGPT project files** — upload both files to a project.
  Reference them in your first message: "Read `NARROWING.md` first."
- **Claude project knowledge** — attach both files to a project.
  Reference `NARROWING.md` in the system prompt or the first turn.
- **A Notion page** — paste each file into its own page inside a
  parent page. Copy the parent page URL into the AI's context.
- **A Google Doc** — one document per file, in a shared Drive folder.
  Copy the folder URL into the AI's context.
- **A folder on your computer** — `~/ai-notes/NARROWING.md` and
  `~/ai-notes/OBSERVATIONS.md`. Point the AI at the folder.
- **A GitHub repository** — this repository is the reference layout,
  but you do not need a repository to use the method. A repository is
  useful when you have graduated past what a scratchpad can hold.

The method does not care which surface you pick. It cares that both
files exist, that the AI reads `NARROWING.md` before acting, and that
you add rows to `OBSERVATIONS.md` when the AI's work costs you.

## Why two files instead of one

One file collapses the two questions into one: *what do I want* and
*why do I want it*. That works for a week. It stops working the moment
you have more than a page of rules, because the rules and the
evidence for the rules cannot both be scannable on the same page.

Splitting the two lets `NARROWING.md` stay short — a page or two, a
first read — while `OBSERVATIONS.md` grows freely as the evidence
accumulates. The AI reads only the short file every session. The long
file exists to be read once when a rule feels wrong, or when I add
a new one.

## Why letters for classes and not names

Letters are cheap to add. A letter never has to be renamed because it
was a poor description; a name does. The register in
`OBSERVATIONS.md` starts with ten classes (C, R, D, L, E, S, I, P, T,
H) — you will add your own when a new shape appears. The letters do
not have to match anyone else's letters. They only have to be stable
for your register.

## Graduating past two files

When the two-file scratchpad stops holding what you need:

- **Add a script that reads `OBSERVATIONS.md`** and prints the
  distribution by class and fault. That is the first automation worth
  building; it turns "the pattern will not lie" from an assertion into
  a line of output.
- **Add a dashboard** that shows the register over time.
- **Add categories, tags, or a database**, if you have outgrown a
  Markdown table.
- **Replace `OBSERVATIONS.md` with a repository** that carries the
  register, the read script, a dashboard, and forwarding pointers
  from the old file names to the new ones. Keep `NARROWING.md` as the
  first read; nothing about the repository changes what the AI sees
  first.

At every stage, the AI reads one short file first. That is the
invariant.

## What is in this repository

- [`NARROWING.md`](./NARROWING.md) — the AI's first read. Ten worked
  example rules, each citing the observation class it responds to.
  Copy, edit, delete as needed.
- [`OBSERVATIONS.md`](./OBSERVATIONS.md) — the register. Schema at the
  top, one example row, delete it and start logging.
- [`LICENSE-NOTICE.md`](./LICENSE-NOTICE.md) — you own what you write.
  This repository holds the method, not your notes.
- `_archive-v1/` — the previous shape of this starter, kept so old
  links resolve. Ignore unless you were pointed at it.

That is the entire kit.
