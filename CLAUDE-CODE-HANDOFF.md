# Prompt for Claude Code

Paste everything below the line into Claude Code, run from the repo folder.

---

New work is in the working tree of `matthewignash-site`. Review it, commit, push, verify. **Do not rewrite page content.**

`~/Documents/Claude/Projects/Publication Work/1-Projects/matthewignash-site`

## What is new

**`pages/Case-IA-Moderation.html`** is a fourth case study, container `mi-case-ia`, slug **`a-shared-standard-for-science-ias`**. Title: "One rubric, both sides of the desk."

It covers the IB Diploma science internal assessment programme as one arc: four workshops across five meetings that taught the standard to students, then department-wide moderation that applied it, then the measured outcome. It embeds an interactive wireframe of the moderation tool, `.mia-` prefix, with a reviewer role and a moderator role, four screens. **CSS-only, no JavaScript.** Click-tested, zero JS errors.

Also changed:

- `build.py` extended to ten pages.
- `pages/Work-Page.html`: the **IA Moderation Tool** row is now an anchor to the new slug with its arrow restored. Four rows link out now: Earth and Env, IA Moderation Tool, Theatre Booking Manager, Digital Hall Pass. The other eight stay plain.
- `SQUARESPACE-WALKTHROUGH-PART-2.md`: new section 11.
- `drafts/Moderation-Wireframe.html`: standalone wireframe for reference.

## Facts on this page were verified with Matthew directly. Do not adjust them.

- **Four workshop decks, five meetings.** The fifth meeting has no deck: students read a complete IA as a group, marked it against the rubric themselves, discussed which strands were easy or hard to evidence, and only then saw the real marks. If you see "four sessions" anywhere, that is wrong; it is four workshops across five meetings.
- **Middle school teachers genuinely read diploma IAs** as readers whose marks counted, not as observers. The page says so in a callout. That is accurate and deliberate.
- **Two to three readers per IA**, cross-subject and cross-division, blind to each other until both submit.
- **The AI pass is named openly.** The tool runs an AI pass over each IA producing per-strand scores. The page shows it as a third column and states plainly that it never sets a mark and exists to make disagreement visible; the agreed column is always human. Matthew chose to disclose this rather than obscure it. **Do not remove the column and do not soften the disclosure.**
- **Evaluation drew the most reader disagreement**, research design almost none, and that finding fed the next workshop sequence. This is the page's argument. Leave it.

## Privacy, and check this before pushing

The source spreadsheet `Science IA Moderation V2.xlsx` contains **real student first names, staff email addresses, Google Drive file IDs and real IA titles**. The source mockups and workshop decks contain more of the same. None of it is on this page.

Verify zero matches in `pages/Case-IA-Moderation.html` for: `aischennai`, `Airi`, `Archisha`, `Dheeban`, `imatthew`, `msagaya`, `fadam`, `prebecca`, and the pattern `\b1[A-Za-z0-9_-]{25,}` for Drive IDs. Illustrative rows use "Candidate 01" style with invented investigation titles. **If anything matches, stop and report rather than pushing.**

## Tasks

1. Review `git diff`.
2. `python3 build.py`. Confirm `paste/` regenerates all **ten** pages.
3. `grep -c '<script' pages/*.html` must be 0 everywhere. The CV page reports 1, a false positive from the string inside a CSS comment.
4. Run the privacy checks above.
5. Confirm `pages/Work-Page.html` has exactly four `<a class="mwk-row"` anchors and four `mwk-arrow` spans.
6. Commit and push. Suggested message: `Add the IA moderation case study and link it from Work`.
7. **Curl all ten raw URLs** and report status for each:
   `https://raw.githubusercontent.com/matthewignash/matthewignash-site/main/pages/<FILENAME>`
8. Report the ten statuses plus anything from steps 3 to 5.

## One duplication to be aware of, but leave alone

The IA outcome table now appears on two pages: `pages/CV-Page.html` and `pages/Case-IA-Moderation.html`, with the same figures and the same caption. That is intentional. Do not try to factor it out; the loader has no include mechanism and a shared fragment would break the one-block-per-page model. Just know that revising the figures means editing both.

## Do not

- Do not add `<script>` to any page.
- Do not remove or reword the AI pass disclosure, the middle school callout, or the five-meetings detail.
- Do not name any student, candidate, or member of staff.
- Do not touch `Job-Search-2027-2028/Squarespace-Blocks/`, which is retired.
- Leave "15+ in-house tools built for staff and students" in the homepage stat strip. Content pass, not this one.
