# Prompt for Claude Code

Paste everything below the line into Claude Code, run from the repo folder.

---

Three fixes are already applied in the working tree of `matthewignash-site`. Your job is to review them, commit, push, and verify. **Do not rewrite the page content.**

`~/Documents/Claude/Projects/Publication Work/1-Projects/matthewignash-site`

## What changed and why

**1. Both case studies are now JavaScript-free.**

`pages/Case-Theatre-Booking.html` and `pages/Case-Earth-Env.html` had interactive widgets driven by `<script>`. Those are now pure CSS, using hidden radio inputs and `:checked ~` sibling selectors. Both were click-tested: correct screen, tab set, URL, role highlight and result message in every state, with zero JS errors.

This supersedes the `enhance()` approach currently in `build.py`. That mechanism works, but it puts a page's JavaScript in the **pasted** block while the markup it controls lives in **GitHub**. Rename a class in `pages/`, push, and the frozen script silently stops matching, which shows up as a broken widget rather than an obviously stale page. CSS-only cannot drift, works in the Squarespace editor where the fetch never runs, and survives JavaScript being disabled.

**Leave the `enhance()` slot in `build.py`.** It is harmless, `page_script` is now empty for every page, and it stays available if something genuinely needs JS later. Do not delete it and do not reintroduce scripts into these two pages.

**2. The four "Read the CV" buttons are removed**, at Matthew's request. They were a second route to a page the nav already reaches, and the theatre one pointed at `/cv`, which 404s because the page actually lives at `/curriculum-vitae`.

Removed from `Home-Page.html`, `About-Page.html`, `Case-Earth-Env.html`, `Case-Theatre-Booking.html`. Each button group had two buttons, so the survivor was promoted to the solid style where needed. What remains: Home "See the work", About "Get in touch", Earth and Env "View the live course site", Theatre "Back to all work".

No page links to `/cv` or `/curriculum-vitae` any more, so the URL Mapping noted in the CV page header comment is no longer needed. That comment has been corrected.

**3. "Why it travels" is renamed to "Where else this fits"** on both case studies. Matthew disliked the phrase. Do not reintroduce it.

## Your tasks

1. Review `git diff`. The only changes should be: script removal plus CSS state rules on the two case studies, four anchor deletions plus two class promotions, one section heading on each case study, and the CV page header comment.
2. Run `python3 build.py`. Confirm `paste/` regenerates all eight pages.
3. **Verify no scripts crept back:** `grep -c '<script' pages/*.html` must be 0 for every page.
4. **Verify the buttons are gone:** `grep -rn 'Read the CV' pages/` should return only the CV page header comment.
5. **Verify no dead CV links:** `grep -rn 'href="/cv"' pages/` should return nothing.
6. Commit and push. Suggested message: `CSS-only case study widgets, drop the Read the CV buttons`.
7. **Curl all eight raw URLs** and report HTTP status for each:
   `https://raw.githubusercontent.com/matthewignash/matthewignash-site/main/pages/<FILENAME>`

## Then update the walkthrough

`SQUARESPACE-WALKTHROUGH-PART-2.md` has two statements that are now wrong. Fix only these:

- The Earth and Env section says the course site link "is now plain text rather than a broken link". It is now a real link to `https://hs-earth-env-site.vercel.app/`. Correct it.
- The theatre section's wireframe test says to check that clicking Manager view changes the tab count. Keep that test, but note the widget is CSS-only, so it also works in the Squarespace editor. That is a useful signal: if it works while editing, it will work published.

## Do not

- Do not reintroduce `<script>` into any page.
- Do not restore the "Read the CV" buttons.
- Do not touch `Job-Search-2027-2028/Squarespace-Blocks/`, which is retired.
- Leave "15+ in-house tools built for staff and students" in the homepage stat strip. It is on the content-pass list, but it is content, not this fix.
