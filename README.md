# matthewignash-site

Page blocks for [matthewignash.com](https://matthewignash.com), a Squarespace site.

`pages/` holds the live source for three pages. Each one is pasted into Squarespace once,
inside a Code Block that then re-fetches this repo on every page load. Editing a file here
and pushing updates the live site within about five minutes. No re-paste.

## Layout

| Path | What it is |
|---|---|
| `pages/` | **The source of truth.** Edit here. |
| `paste/` | Generated. The Code Block payload, pasted into Squarespace once per page. |
| `build.py` | Regenerates `paste/` from `pages/`. |

## Changing a page

```bash
# edit pages/CV-Page.html
python3 build.py
git commit -am "CV: <what changed>" && git push
```

The live site picks it up on the next page load once GitHub's five-minute cache expires.
Running `build.py` is only strictly needed when you want the pasted fallback refreshed too,
but doing it every time keeps the fallback from drifting.

## How the Code Block behaves

Each block contains a full copy of its page as fallback, then tries to fetch the current
version from `raw.githubusercontent.com`. On success the fallback is replaced. On any
failure the fallback stays. The page is therefore never blank, and search engines see real
markup rather than an empty container.

Fetched markup is parsed with `DOMParser` and stripped of `script`, `iframe`, `object` and
`embed` elements plus any `on*` or `javascript:` attributes before it is inserted. That is
defence in depth: this repo is the only source, but content crossing a network boundary onto
the live domain should not be injected raw.

The fetch uses `cache: "no-cache"`, which forces a revalidation against GitHub on every page
load. Without it the browser honours `max-age=300` and a repeat visitor can sit on a stale
copy for five minutes after a push. Revalidation is cheap, since an unchanged file comes back
as a 304 with no body.

## When a push is not enough

A push updates what visitors *see*. It does not update the fallback copy sitting in the pasted
Code Block, which stays as it was on the day you pasted. That is fine for ordinary edits.

It is not fine when the point of the change is that the old content must stop existing, for
example removing a personal detail. The fallback still carries it, in the page source, whether
or not the fetch succeeds. **For that kind of change, run `build.py` and re-paste the block.**


## Why this repo is public

Squarespace fetches these files from a visitor's browser, so they have to be publicly
readable. They contain only what already appears on the public website. Everything else
about the site, including drafts, planning and anything personal, lives in a separate
private repo.
