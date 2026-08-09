# Prompt for Claude Code

Paste everything below the line into Claude Code, run from the repo folder.

---

New work is sitting in the working tree of `matthewignash-site`. Review it, commit, push, and verify. **Do not rewrite page content.**

`~/Documents/Claude/Projects/Publication Work/1-Projects/matthewignash-site`

## What is new

**`pages/Case-Hall-Pass.html`** is a third case study, container `mi-case-hallpass`, slug **`replacing-the-paper-hall-pass`**. Title: "From a paper sheet to a system the IT department owns."

It embeds an interactive wireframe of the digital hall pass, `.mhp-` prefix, showing the classroom tablet and the admin dashboard. **CSS-only, no JavaScript**, using hidden radio inputs and `:checked ~` selectors, the same pattern as the theatre case study. Click-tested: correct screen, tab set and URL in all four states, zero JS errors.

Also changed:

- `build.py` extended from eight pages to nine.
- `pages/Work-Page.html`: the **Digital Hall Pass** row is now an anchor to the new slug with its `↗` arrow restored. Three rows link out now: Earth and Env, Theatre Booking Manager, Digital Hall Pass. The other nine stay plain with no arrow, deliberately.
- `pages/Case-Theatre-Booking.html`: removed a duplicated intro. The case section introduced the wireframe and then the wireframe introduced itself again. Content only, no structural change.
- `SQUARESPACE-WALKTHROUGH-PART-2.md`: new section 10 covering the new page.
- `drafts/Hallpass-Wireframe.html`: the standalone wireframe, kept for reference.

## Context so you do not "correct" deliberate choices

**Attribution on this page is load-bearing and was verified with Matthew directly.** Do not soften it, do not strengthen it:

- He built a **demonstrator**, in Apps Script and HTML. It was **never run with students**. The page says so explicitly, in a callout. That sentence stays.
- The demonstrator had a digital teacher-approval step. It was cut because it forced teachers into their email mid-lesson to formalise a decision they had already made out loud.
- **IT owns version two** and is actively building it on the RFID student ID cards the school deployed this year. He is still in the conversation with the Assistant Principal but is not writing the code.
- The status pill reads **"In development"**, not "In use". The theatre case study reads "In use". That difference is intentional and correct.

**Privacy.** The source mockups and the prototype spreadsheet contain real email addresses, a real student information system export, and named staff. None of it is on this page. Verified zero matches for `aischennai`, `Justyna`, `Chris`, and any six-digit student ID. Illustrative rows use "Student A" through "Student G" with no ID numbers, and no staff are named. **Keep it that way.**

## Tasks

1. Review `git diff`.
2. Run `python3 build.py`. Confirm `paste/` regenerates all **nine** pages.
3. Verify no scripts: `grep -c '<script' pages/*.html` should be 0 everywhere. The CV page reports 1, which is a false positive from the string `<script` inside a CSS comment. Confirm that is what it is and move on.
4. Verify privacy on the new page: zero matches for `aischennai`, `Justyna`, `Chris`, `csara`, and `\b1\d{5}\b`.
5. Verify the Work page has exactly three `<a class="mwk-row"` anchors and three `mwk-arrow` spans.
6. Commit and push. Suggested message: `Add the hall pass case study and link it from Work`.
7. **Curl all nine raw URLs** and report HTTP status for each:
   `https://raw.githubusercontent.com/matthewignash/matthewignash-site/main/pages/<FILENAME>`
8. Report the nine statuses plus anything from steps 3 to 5.

## Do not

- Do not add `<script>` to any page.
- Do not change the attribution wording, the "never run with students" callout, or the "In development" status.
- Do not name the Assistant Principal, the IT staff member, or any student.
- Do not touch `Job-Search-2027-2028/Squarespace-Blocks/`, which is retired.
- Leave "15+ in-house tools built for staff and students" in the homepage stat strip. Content pass, not this one.

## Still queued for the content pass

Homepage stat strip wording; swapping Parallel Design Labs for AI Coding for Educators in the homepage featured three; six new Work rows plus status upgrades; About page additions. Reasoning lives in `Job-Search-2027-2028/Squarespace-Blocks/Pages/README-PASTE-AND-PUBLISH.md`.
