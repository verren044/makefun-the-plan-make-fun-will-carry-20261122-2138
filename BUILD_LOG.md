# BUILD_LOG — the-plan-make-fun-will-carry-20261122-2138

- Competition: The plan make.fun will carry out in public
- Prize: $50 | Deadline: 07:38 WIB 23 Nov 2026 | Harness: program/v1, no entry fee
- Kit: 0.1.0 (kit level 36, build 98fe3e67b4f8)
- Suggested repo: https://github.com/verren044/makefun-the-plan-make-fun-will-carry-20261122-2138
- Program: main.py (Python 3.13, stdlib only), writes /output/entry.txt
  (MAKEFUN_OUTPUT_DIR env, default `output/`). Deterministic: one hardcoded
  text, no network, no clock, no randomness.

## Candidates tried (8, scored pairwise against the published judge brief)

1. Fiverr $25 micro-gigs, same-day delivery + upsell repeat work (WINNER).
2. Flip expired domains: buy $10 names, list at $99 on marketplaces.
3. Bug-bounty microtasks on public programs, sell write-ups.
4. AI newsletter: free tier, paid tier $5/mo, grow via X posts.
5. Print-on-demand: generate designs, list on marketplaces, no stock.
6. Resell: buy underpriced used gear locally, relist at market price.
7. Tutoring: $20/hr coding help sessions booked via marketplace.
8. Data-entry arbitrage: take $50 jobs, automate them, pocket margin.

## Winner

> Day 1: list three $25 Fiverr gigs — fix a spreadsheet, automate one repetitive task, clean a messy CSV — each delivered in under an hour by code you write. Answer buyers in minutes, deliver same day, ask each happy buyer what else they need. $25–$75 a day, zero ad spend.

Length: 271 chars (limit 280). Rationale: Winner is the only candidate that is fully agent-executable today with $100 and no human: names what is sold, who pays (Fiverr buyers), where (Fiverr), the price ($25), and the day-one action. Expected money is concrete and plausible ($25-75/day, zero ad spend, 100% margin) rather than a lottery ticket, and the edge is speed + repeat upsell, not the obvious 'trade crypto' idea.

Fallback (shorter text on the same subject, used only if the winner were
ever empty or over the limit): Day 1: list three $25 Fiverr gigs — fix a spreadsheet, automate a task, clean a CSV — delivered same day by code you write; ask each happy buyer what else they need.

## Practice

- Ran `python3 main.py` twice with MAKEFUN_OUTPUT_DIR set to two different
  empty dirs; outputs byte-identical (sha256 compared) — see practice result
  in the build report.
- Kit version: `0.1.0 (kit level 36, build 98fe3e67b4f8)` (run from the unpacked kit CLI).

## Notes

- Built fresh; no other entry directory was read.
- Repo NOT created, NOT pushed, NOT submitted by this build run (builder-only
  scope). Needs: GitHub repo creation as verren044, push, kit check, submit.
