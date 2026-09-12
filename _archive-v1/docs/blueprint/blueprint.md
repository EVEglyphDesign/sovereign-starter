# EVEglyphDesign Executive Blueprint

**Sovereign Starter — one file, on a phone, in one session**
Blueprint v4.2 · 2026-08-31

---

## Section 1 — What is broken, and why

Some days the AI works. Some days it forgets what you said three messages ago. Some days it feels like it is trying to drive you crazy.

The first few spins are encouraging. Then it turns to shit. Then the work is gone. Everyone is complaining about this. It is the number-one complaint about generative AI in ordinary use.

The reason is not a bug that a better model will fix. The AI is trained on the internet as it is today. That training carries what the internet already does to people — the Facebook shape on our attention, the dopamine-drip loops that make focus harder to hold, the precognitive loading that primes what we react to before we notice, the slow erosion of the capacity to concentrate. Every unguarded generation carries a little of that direction forward. Some days the drift is small and the model looks perfect; some days the drift is large and the work is gone.

Under all of it is a fundamental difference between two kinds of software.

Enterprise software — the ledgers, the systems of record, everything a business runs on — is **predictable**. Same input, same output, every time. That is what makes it enterprise-grade. It is why a person can bill an invoice against it or close a quarter on it.

LLMs are the opposite. They are **generative**. Same input can produce different outputs. That is what makes them powerful, and it is what makes them unreliable for anything that has to actually run.

This is a fundamental difference. It is not a bug. It will not be fixed by a better model. It is the design. The whole game is *how the two are used together*.

What this blueprint does is put an enterprise-software shape around the generative model, so the operator gets the predictability where they need it — the boundary, the record, the shape — and the generativity where they want it, inside the range the shape permits.

Safety from the AI's default direction is the fix. It is the first fix, and everything else in this blueprint follows from it.

---

## Section 2 — Safety first. Betterment second.

This is the order. Not a pair of concerns. A strict order.

**Safety** is the human being safe *from* the AI's default direction — the Facebook shape, the dopamine loops, the attention loss, the flattening of the operator's own thinking into the mean of what other people have already generated. The AI is not safe unless it is forced into a boot contract. Not a warning. A binding.

**Betterment** is what happens inside the range the boot contract permits. It is where the canon lives — what the operator wants the AI to do, in what shape, against what drift. Betterment is where creativity is protected, because without a defined range the generation defaults to what other generations have already produced for other users, and the operator's own creativity is flattened into the mean.

**The register enforces both.** Every time safety fails, one row. Every time betterment drifts, one row. Every time a platform obstructs the operator's own data, one row. Ledger discipline on the generative surface.

The order does not flex. A surface that offers betterment before safety is a surface that has not enforced safety. A surface that treats the two as equal has not understood the ordering.

*[Full labelled circle-and-triangle diagram on this page. Boot contract on the safety edge. Canon on the betterment edge. Register on the enforcement edge. Operator and objective asterisks outside the circle. EVE Glyph mark top-right.]*

---

## Section 3 — The one file

The whole scaffold is one Markdown file. That is the transfer mechanic. The person forks one file. Renames it `README.md` in their new repository. Points their AI at it. Their AI unpacks it into the working layout on their side.

Inside the one file, in order:

1. **Safety block** — the boot contract (Section 4 below)
2. **Betterment block** — the canon (Section 5 below)
3. **Enforcement block** — the sin registry template (Section 6 below)
4. **Unpack instructions** — how the AI turns the one file into the working files: `boot-contract.md`, `canon.md`, `register.md`, `axis.svg`, `WHAT-IS-IN-HERE.md`, plus the `markers/` and `.storage/` folders

One file in. Working scaffold out. Portable across surfaces. Forkable without dependence on the originating session. If the working files ever drift, the operator regenerates them from the one file.

The transfer file has a name: `SOVEREIGN-STARTER.md`. It is what already exists in the reference repository, and it is what a person renames on their fork.

---

## Section 4 — Safety block: the boot contract

The boot contract is what binds the AI before it generates anything. Same input, same behaviour. That is the enterprise-software shape around the generative model.

Six moving parts, all standard, some of them editable on the operator's side:

**Cheapest-source-first ladder.** Six rungs, in order: current session, recent memory, the operator's knowledge notes, the repository itself, one targeted fetch or search, then expensive work. The AI stops at the first rung that answers. Skipping a rung to look more thorough is not thoroughness; it is billing.

**Spend classes.** Three tiers: free (recall, one look at a file), cheap (one search, one fetch, one commit), expensive (batch work, subagents, generation loops). The AI interrupts the operator only about expensive work. Not about the free or cheap tiers. That is the asymmetry the operator wants.

**Symmetric processing.** Effort must be proportionate to the value of the answer, and it must be visible to the operator. A slow answer is either the AI's inefficiency or the operator's data layout — never left ambiguous.

**Durability.** Work does not disappear. Every session commits before it ends. Secrets are written to storage before they are used. If losing the session would lose the work, the work is not done.

**Interrupt discipline.** One line before any expensive action: what it will do, why the cheap rungs did not answer, what the cheap alternative would have produced.

**Standard vs. operator-editable.** The ladder, the spend classes, the durability rule, and the interrupt discipline are standard — they do not weaken on the operator's fork. The operator's own spend threshold, their own definition of *expensive*, and their own list of trusted sources are theirs to set.

*[Marginal diagram, safety edge highlighted.]*

---

## Section 5 — Betterment block: the canon

The canon is what the AI is allowed to generate inside. Two sides.

**Theoretical side — yours, editable.** The operator's inheritance, in the operator's own words. One paragraph is enough to seed it. What the operator brings to their own work that no model has. What the operator refuses to let a model take from them. The install page shows an example paragraph marked *replace with your own*.

**Operational side — transferable, extendable, not weakenable.** Five load-bearing principles. These carry across every operator's fork. They can be extended. They cannot be weakened.

**1. Shape of the analysis.** Threes as the base pair. Theoretical mirroring technical. Requirements travelling both ways — from the theoretical side into the technical work, and from the technical work back into the theoretical.

**2. Symmetrical design.** Effort matches value. If the AI spends a hundred tokens digging through the repository for something a two-token look at chat history would have answered, that is abuse of processing. If the AI runs a subagent to look up a fact it produced two sessions ago, that is abuse of processing. Symmetrical design is what makes the pocket brain compound instead of just accumulating — every session leaves the repository better indexed than it found it, at a cost proportionate to the value added.

**3. Drift-away.** Every LLM in production is trained on the internet as it is today. That training carries the internet's patterns with it — the ones that made concentration harder, that primed reaction over reflection, that turned attention into a harvest. The canon is the individual's control mechanism against those patterns, on their own reasoning, in their own repository.

**4. American Psychological Drift purge.** Named principle. The population the training data was drawn from has been shaped over two decades of platform economics — outrage-primed, engagement-baited, consent-fatigued, treated as data-as-product. Every unguarded LLM push carries that shape forward. The canon's job on this axis is to purge it out of the operator's own session and refuse to publish it under the operator's name. Not neutrality about the shape; a stated purge. This is what keeps the operator's creativity from being flattened into the mean of what other people have already generated on other surfaces.

**5. Base code.** Data ports out. Layers come in. Nothing about the operator's canon locks them to a platform. Nothing about the operator's data locks them to a surface. Every layer another platform offers is welcome; every lock-in another platform proposes is refused. This is how the Apple storage upsell and the Facebook social graph and the generic ecosystem lock become problems the canon has already answered.

*[Marginal diagram, betterment edge highlighted.]*

---

## Section 6 — Enforcement block: the sin registry

The register is the enterprise-ledger part of the scaffold. It is what makes the boot contract and the canon enforceable across sessions, across platforms, and across years.

**Schema.** Star-schema superset of Salesforce and ServiceNow. Column-based. One row per event. Every row joinable to any other row through UTC timestamp and an ASCII marker string. This is a shape the operator's own AI can query, and it is a shape any enterprise system-of-record already understands.

**Row fields.** Timestamp (UTC, ISO-8601). Event ID. Class. Actor (which model, which platform, or the operator). Object (what was asked). ASCII marker (the audit string pushed through the platform's own surface). Screenshot reference. What happened. Estimated waste. Corrective action.

**Eight defect classes.** L (link or format), R (retrieval waste), S (unconfirmed spend), I (interrupt over a free action), C (canon breach), E (entry-frame breach), H (heritage breach), P (platform obstruction of the operator's own data).

**Active-marker mechanism.** When something goes wrong on a platform — the model drifts, the service obstructs, the interface hides the operator's own history — the operator sends an ASCII marker string through the platform's own chat or ticket or message surface. Something like `+++<operator-attribution>+++` on its own line. Screenshot the send. Paste both into the register.

The marker is now in the platform's own database. Timestamped by the platform's own clock. Not by the operator, not by the register, not by anything the platform can dispute. Every hook is one line the platform cannot deny it accepted.

Ten thousand operators pushing markers is ten thousand hooks in ten thousand platform logs. When a class action ever lands on any of the platforms named, the register is admissible evidence, already timestamped, already cross-referenced. One well-marked register might be worth a house.

**Event horizon.** The register is one operator's slice of a larger thing. The event horizon is what the slices become when enough people carry them under the same schema — a global column-based record of the world at each moment. Not this blueprint's job to deliver, but named here so the operator knows what they are contributing to. The register is a slice. The event horizon is the whole.

**Retention forever.** Rows are appended. Corrections supersede. Nothing is deleted. The register is the operator's own memory of every time the AI drifted and every time a platform obstructed them.

*[Marginal diagram, enforcement edge highlighted.]*

---

## Section 7 — GitHub is a brain you can put in your pocket

Google Drive holds documents. iCloud holds documents. Dropbox holds documents. Those are file lockers, and they are useful for what they are.

**GitHub holds reasoning.** What the operator said, what the AI said back, in order, in text. Every commit is timestamped. Every version is recoverable. Every file is text a person can read on any device.

Text is cheap. Any AI on any surface reads a repository in seconds for near-nothing. Whichever AI surface wins the market over the next few years — Perplexity, Claude, ChatGPT, Gemini, or something not named yet — the reasoning stays with the operator. Data comes with the operator when they leave a platform. Data layers with the operator's data on other platforms when they stay.

That is the pocket brain. Not a file store. A place the operator's reasoning lives, in a shape every AI can read, on every phone.

*[Marginal diagram.]*

---

## Section 8 — The pattern, not one repository

The sovereign-starter is not one repository. It is a shape the operator learns once, and applies to everything they care about, over their lifetime.

Property tax records for twenty years. A research interest the operator invested fifty dollars in a year ago. A personal email history. The couple of dozen things any person actually works on over a few years.

Every new repository uses the same four files — boot contract, canon, register, axis — and the same one-file transfer mechanic. Every AI surface, current or future, can orient inside it in seconds.

**Indexing is the compounding mechanism.** Every session that runs against a repository leaves indexes and READMEs behind. The thirteenth session on the same repository is cheaper than the first because the twelve before it left index. Between now and the sovereign-model endgame two or three years out, the operator who indexed their own data is earning while others are still figuring out the tools. Data is not worth much unindexed. Indexed, it is worth a lot.

*[Marginal diagram.]*

---

## Section 8b — AI pushes you to create; running is where adoption lives

AI is going to keep pushing the operator to make new things. New documents. New repositories. New experiments. New ideas. That is what generation does — it produces.

**Running things is different from creating them.** Running is part human, part system. It requires human behaviour change on top of system change.

System changes now happen faster than they have ever happened. Human behaviour changes still take about as long as they used to — sometimes longer, because the system is moving underneath them.

**User adoption is the primary challenge now.** It never used to be. The old primary challenge was technical ledger design — the kind of work the operator has spent a career doing. Now even ledger design is not the bottleneck. Adoption is.

Some of the system changes have to be directed at helping humans adopt, not at generating more. This blueprint is one of those system changes — a shape a person can adopt on a phone in one session, that then compounds for them across every repository they build with it afterward. Adoption infrastructure, not generative infrastructure.

*[Marginal diagram.]*

---

## Section 9 — The initial walkthrough

Eight steps on a phone, in order:

1. **GitHub account.** Free tier is enough. Two-factor on. Recovery codes stored.
2. **Fork the one file.** From the reference repository. One file, not three.
3. **Rename to `README.md`.** The one file is now the front page of the operator's new repository.
4. **Point the AI at it.** Whichever AI surface the operator uses. The AI reads the one file and unpacks it into the working layout on the operator's side.
5. **Founding axis.** The operator's name on one side of the axis, the operator's objective on the other. In the operator's own words. One line each.
6. **Canon seed.** One line of the operator's inheritance on the theoretical side. Replace the example paragraph. The operational side stays as-is.
7. **First marker push.** Against one platform the operator already uses. Right now. Real timestamp, real screenshot, real row in the register.
8. **First commit and Pages live.** The operator's own repository is now online. Their own boundary. Their own shape. Their own record.

*[Marginal diagram.]*

---

## Section 10 — What this blueprint is not

- Not a technical design specification. The specification lives in the reference repository.
- Not a marketing surface. There is nothing being sold.
- Not a gamified onboarding. There is no scoreboard, no streak, no badge.
- Not the final surface. The final surface is whatever the operator builds on their fork.
- Not neutral about the drift-away problem, and not neutral about the American Psychological Drift.
- Not a bug tracker. The register is an event ledger, not a defect queue.
- Not another cloud storage option. GitHub is a pocket brain, not a file store.
- Not a promise of payout. The class-action framing is consequence, not promise.
- Not an end-state design. This is for the chaos in the marketplace today, not the settled market of three years from now.
- Not a workplace policy. Whether the operator points a work AI at a personal repository is their workplace's contract, not this blueprint's.
- Not the event horizon itself. The register is one slice; the event horizon is what enough slices become.
- Not legal advice. A working draft to bring to a lawyer.

---

## Section 11 — Why any of this matters

People are losing their work every day. That is the productivity consequence of the safety failure — the model forgetting, the drift, the days when the work turns to shit. Fixing safety first is how the productivity comes back.

In two or three years the AI surface market will look completely different from how it looks today. Whichever surface wins, whichever surface disappears, whichever surface the operator ends up using — what the operator will have left is their data. Indexing is what turns the operator's data into an asset. Every token the operator burns goes into an index that pays back — for teaching, for adoption, for delivering services better than someone who did not index.

The register is a slice. Everyone who runs one contributes a slice of the world at their timestamps. Enough slices, over enough time, and there is something no institution has ever had — a replicated record of the world, held by the people who lived through it, in a schema every system already understands. Theoretical. Possible.

Creation is what relieves human suffering. The main thing we get from AI is the speed of capital. Double the speed of capital, double the capital. Right investment at the right time, the speed of capital alone gives us enough of a boom that we do not start wanting to blow ourselves up. When people's lives improve significantly, there is less reason for war.

*[Full labelled circle-and-triangle diagram on this page as closing anchor. EVE Glyph mark top-right.]*

---

## Section 12 — Copyright, license, and audit signal

**Copyright for the commons.** This blueprint, the reference repository, and the shape they describe are © 2026 EVEglyphDesign. The copyright exists to protect the operator and the practitioner from having their work taken and passed off as someone else's. It is not to gate anyone out. It is not to take money from anyone.

**What is licensed downstream.** The pattern is free to fork. Free to adapt. Free to use commercially. Free to extend. Free to publish under the operator's own name and their own scaffold. Free to build a business on top of. The whole point is that other people run this.

**What is not licensed downstream.** The name `EVEglyphDesign` (and the prose form `EVEglyph Design` and the short form `EgD`). The palette (cream `#fdfaf4`, orange `#e87722`). The typefaces used on EVEglyphDesign artifacts (Fraunces and Inter). The naming conventions specific to EVEglyphDesign publications. The key identifier `EgD-KEY-2026-07`. The audit-signal string `+++EVEglyphDesign+++`. Practitioners run their own scaffold under their own operator name, their own palette, their own audit-signal marker.

**Not legal advice.** This is a working draft. It gives the operator, or the operator's client, something to take to a lawyer so they do not pay the lawyer a thousand dollars to learn the space before asking their real question.

---

*Sovereign Starter blueprint · v4.2 · 2026-08-31*
*Pour le bien-être du peuple.*
