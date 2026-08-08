# Prompt for Claude Code

Paste everything below the line into Claude Code, run from the repo folder.

---

You are picking up work on `matthewignash-site`, the repo that backs matthewignash.com. Repo path:

`~/Documents/Claude/Projects/Publication Work/1-Projects/matthewignash-site`

## What already happened (do not redo)

Three pages were already built and pushed: `Contact-Page.html`, `CV-Page.html`, `Writing-Media-Page.html`. Those are live in the repo and are being pasted into Squarespace by hand, one time each.

In this session four more page fragments were written into `pages/` and `build.py` was extended from three entries to seven. `python3 build.py` has already been run, so `paste/` is current. Nothing has been committed or pushed yet.

New files in `pages/`:

- `Home-Page.html` (container `mi-home`)
- `About-Page.html` (container `mi-about`)
- `Work-Page.html` (container `mi-work`)
- `Case-Earth-Env.html` (container `mi-case-earth-env`)

## How these four were produced, so you know what to trust

They are **not** copies of the standalone files in `Job-Search-2027-2028/Matthew Ignash Website/site/`. Those use global CSS selectors (`*`, `html`, `body`, `a`) and would restyle the whole Squarespace page if pasted. They were rebuilt instead:

- **Home** = the eight `Squarespace-Blocks/01-Hero.html` … `08-Footer.html` blocks concatenated, with `56px` spacer divs between them. The blocks assumed Squarespace section padding; concatenated they collided, and the spacers replace that padding.
- **Work** = the five `Squarespace-Blocks/Work/*.html` blocks concatenated.
- **Case-Earth-Env** = `Squarespace-Blocks/Case-Earth-Env-AI-Literacy.html`.
- **About** = written fresh with a new `.mab-` prefix. No About block ever existed; the live page was assembled from loose fragments. Content was taken verbatim from `site/about.html`, which matches the live page.

Placeholders that were resolved, since the block files were pre-substitution templates:

- 10 `href="#"` on Home, 15 on Work, 2 on the case study, all mapped to real targets (`/cv`, `/work`, `/writing`, `/contact`, `/building-ai-literacy-in-a-science-course`, the Substack URL).
- `IMAGE_URL_HERE` replaced with the live Squarespace CDN headshot URL pulled off the published homepage.
- `VERCEL_URL_HERE` on the case study: the course site is not deployed, so the anchor was unwrapped and the text left in place. Re-link it when the Vercel deploy happens.
- Stale "12+ essays" on the homepage corrected to "63 posts".
- Eleven Work rows that linked nowhere but displayed a `↗` arrow were converted from `<a href="#">` to `<div>` with the arrow removed. Only Earth and Env still links, and it keeps its arrow. This was an explicit decision, not a bug. Do not restore the dead anchors.

## Your tasks

1. **Sanity check before committing.** Confirm `paste/` is newer than `pages/` and contains seven files. If not, run `python3 build.py`.
2. **Confirm no placeholders survive** anywhere in `pages/` or `paste/`: search for `href="#"`, `IMAGE_URL_HERE`, `VERCEL_URL_HERE`, `ESSAY_COUNT`, `TOOL_COUNT`, `12+`.
3. **Commit and push** to `main`. Message along the lines of `Add Home, About, Work and case study pages`.
4. **Verify the fetch targets resolve.** After pushing, curl each of the seven raw URLs and confirm HTTP 200:
   `https://raw.githubusercontent.com/matthewignash/matthewignash-site/main/pages/<FILENAME>`
   Report any that fail. This matters because a 404 means that page silently falls back forever.
5. **Extend `SQUARESPACE-WALKTHROUGH.md`** in the repo root to cover the four new pages. It currently documents only Contact, CV and Writing. Keep the same tone and level of detail: literal clicks, `pbcopy` command per page, Language = HTML, Display Source unchecked, select-all before pasting. Add the page-specific notes below.

## Page-specific notes for the walkthrough

**Home.** Currently eight separate Code Blocks. All eight get deleted and replaced by one. Warn that the hero headshot now comes from the HTML rather than a Squarespace image block, so if an image block remains it will duplicate.

**Work.** Currently five Code Blocks, all replaced by one.

**About.** This one is newly authored rather than ported. Tell him to open the live `/about` side by side and read it against the new version before deleting anything, because there was no saved source to diff against.

**Case study.** One block replaced by one block. Note the Vercel link is currently plain text.

**All four.** Set the section background to match `/work` and `/about`. If two footers appear after pasting, an old standalone footer block is still on the page; delete it.

## Do not do these

- Do not change any page content. A separate content pass is queued and mixing the two makes a bad render impossible to diagnose.
- Do not touch `Job-Search-2027-2028/Squarespace-Blocks/`. It is retired and marked as such.
- Leave "15+ in-house tools built for staff and students" in the homepage stat strip alone for now. It contradicts a decision to name specific tools instead of counting them, and it is first on the content-pass list, but it is content, not migration.

## Known content items for the next pass, for context only

- Homepage stat strip still says "15+ in-house tools".
- Homepage featured projects should swap Parallel Design Labs out for AI Coding for Educators.
- Work page needs six new rows: AI Coding for Educators, course launchpads, Reflection Tool, UDL Champions, AI Usage Survey and Policy Committee, DP curriculum documentation. Plus status upgrades on Earth and Env and Compass Point.
- About page needs an accreditation line, the AI Leadership Council, and the Student Advisory Forum leadership role.

Full reasoning for every content decision is in `Job-Search-2027-2028/Squarespace-Blocks/Pages/README-PASTE-AND-PUBLISH.md`.
