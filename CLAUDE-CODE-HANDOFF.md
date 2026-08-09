# Prompt for Claude Code

Paste everything below the line into Claude Code, run from the repo folder.

---

You are doing the git work for `matthewignash-site`, the repo backing matthewignash.com.

`~/Documents/Claude/Projects/Publication Work/1-Projects/matthewignash-site`

**Your job is narrow: verify, commit, push, and prove the fetch targets resolve. Do not write or edit page content.** All eight pages and both walkthrough documents are already written. A separate content pass is queued, and mixing content edits into this migration would make a bad render impossible to diagnose.

## State of the repo right now

Already pushed in an earlier commit: `Contact-Page.html`, `CV-Page.html`, `Writing-Media-Page.html`.

Written but **not yet committed**:

- `pages/Home-Page.html` (container `mi-home`)
- `pages/About-Page.html` (`mi-about`)
- `pages/Work-Page.html` (`mi-work`)
- `pages/Case-Earth-Env.html` (`mi-case-earth-env`)
- `pages/Case-Theatre-Booking.html` (`mi-case-theatre`)
- `build.py`, extended from three entries to eight
- `SQUARESPACE-WALKTHROUGH.md` and `SQUARESPACE-WALKTHROUGH-PART-2.md`
- `drafts/Theatre-Wireframe.html`, the standalone wireframe kept for reference

`python3 build.py` has already been run, so `paste/` holds all eight.

## Context you need so you do not "fix" deliberate choices

- The standalone files in `Job-Search-2027-2028/Matthew Ignash Website/site/` use global CSS selectors (`*`, `html`, `body`, `a`) and would restyle the whole Squarespace page. They are **not** the source. Do not copy from them.
- **Home** is the eight `Squarespace-Blocks/01-Hero.html` … `08-Footer.html` blocks concatenated with `56px` spacer divs. The blocks relied on Squarespace section padding; concatenated they collided. The spacers replace it.
- **Work** is the five `Squarespace-Blocks/Work/*.html` blocks concatenated.
- **About** was written fresh with a `.mab-` prefix. No About block ever existed.
- **Eleven Work rows** were converted from `<a href="#">` to `<div>` with the `↗` arrow removed, because they linked nowhere and clicking one jumped to the top of the page. Exactly **two** rows are anchors: Earth and Env, and Theatre Booking Manager. **Do not restore the dead anchors.**
- The **theatre case study** is a new page at slug `booking-a-780-seat-theatre`, and the Work page links to it. That slug must not change without changing the Work page link too.
- The case study embeds an interactive wireframe with its own `<script>`. It is plain ES5-safe JS with no dependencies. Leave it alone.
- On the Earth and Env case study, a link to the course site pointed at `VERCEL_URL_HERE`. The anchor was unwrapped to plain text because the site is not deployed. That is intentional.

## Tasks

1. **Verify before committing.** Confirm `paste/` contains eight files and is newer than `pages/`. If not, run `python3 build.py`.
2. **Search `pages/` and `paste/` for leftovers** and report anything found: `href="#"`, `IMAGE_URL_HERE`, `VERCEL_URL_HERE`, `ESSAY_COUNT`, `TOOL_COUNT`, `12+`.
3. **Privacy check on the theatre case study.** `pages/Case-Theatre-Booking.html` must contain zero matches for `aischennai`, `csara`, or `Sara`. The source documents this was built from are full of real staff email addresses. If any appear, stop and report rather than pushing.
4. **Commit and push** to `main`. Suggested message: `Add Home, About, Work, and two case study pages`.
5. **Prove the fetch targets resolve.** After pushing, curl all eight raw URLs and confirm HTTP 200:

   `https://raw.githubusercontent.com/matthewignash/matthewignash-site/main/pages/<FILENAME>`

   Report the status of each. This is the most important step. A 404 on any one means that page silently runs on its frozen fallback forever and nothing on screen would reveal it.

6. **Report back** with the eight URL statuses and anything from steps 2 or 3.

## Do not

- Do not edit page content, copy, or styling.
- Do not touch `Job-Search-2027-2028/Squarespace-Blocks/`. It is retired and marked as such.
- Do not rewrite the walkthrough documents. They are current and cover all eight pages across two parts.
- Leave "15+ in-house tools built for staff and students" in the homepage stat strip. It contradicts a decision to name specific tools rather than count them, and it is first on the content-pass list, but it is content, not migration.

## Queued for the content pass, for context only

- Homepage stat strip still says "15+ in-house tools".
- Homepage featured projects: swap Parallel Design Labs out for AI Coding for Educators.
- Work page: six new rows, plus status upgrades on Earth and Env and Compass Point, plus a stronger Theatre Booking Manager description now that it has a case study behind it.
- About page: accreditation line, AI Leadership Council, Student Advisory Forum leadership role.

Reasoning for every content decision is in `Job-Search-2027-2028/Squarespace-Blocks/Pages/README-PASTE-AND-PUBLISH.md`.
