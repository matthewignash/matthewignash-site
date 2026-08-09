# Squarespace walkthrough, part 2: the remaining five pages

Part 1 covered Contact, CV, and Writing and Media. This covers everything else.

**Repo folder** (called THE FOLDER below):
`~/Documents/Claude/Projects/Publication Work/1-Projects/matthewignash-site`

**Do part 1 first.** Nothing here depends on it technically, but Contact and CV are the pages actively costing you credibility, and this part is longer.

---

## The same three rules as before

1. **The editor will show old content.** Squarespace does not run JavaScript while editing, so every block shows its built-in copy until the page is published. Not a bug.
2. **Copy with Terminal, never TextEdit.** TextEdit can convert HTML to rich text and corrupt it.
3. **In every Code Block:** click inside, **Cmd+A**, then paste. Set **Language = HTML**. Leave **Display Source unchecked**.

---

## What is different about these five

Contact, CV and Writing were mostly empty pages you filled. These five **replace existing content**, and two of them replace *many* blocks with one.

| Page | What is there now | What you do |
|---|---|---|
| Home | **Eight** Code Blocks | Delete all eight, add one |
| Work | **Five** Code Blocks | Delete all five, add one |
| About | Assorted blocks | Delete them, add one |
| Earth and Env case study | One Code Block | Replace it |
| Theatre case study | **Does not exist yet** | Create the page from scratch |

---

## 4. Home page

```
cat ~/Documents/Claude/Projects/Publication\ Work/1-Projects/matthewignash-site/paste/Home-Page.html | pbcopy
```

1. **Pages** → **Home** → **Edit**.
2. Delete all eight existing Code Blocks. Work top to bottom: hero, stat strip, what I do, green themes box, selected work, wellbeing quote, writing and media, footer.
3. **If there is a separate image block holding your headshot, delete that too.** The photo is now inside the HTML. Leaving the old one gives you two.
4. Add one Code Block. **Cmd+A**, paste. Language = HTML, Display Source unchecked.
5. Set the section background to match `/work`.
6. **Save.**

**Check after publishing:** the headshot appears in the hero. It loads from your existing Squarespace image URL, which I pulled off the live page, so it should be identical to what is there now.

## 5. Work page

```
cat ~/Documents/Claude/Projects/Publication\ Work/1-Projects/matthewignash-site/paste/Work-Page.html | pbcopy
```

1. **Pages** → **Work** → **Edit**.
2. Delete all five existing Code Blocks: header, systems, curriculum, co-design, AI practice.
3. Add one Code Block, **Cmd+A**, paste, Language = HTML, Display Source unchecked.
4. Background, **Save**.

**One change you will notice.** Eleven of the twelve project rows used to show a `↗` arrow and link nowhere. Clicking one jumped you to the top of the page. Those are now plain rows with no arrow. Two rows keep the arrow because they genuinely go somewhere: Earth and Env, and Theatre Booking Manager. As more projects get real destinations, their arrows come back.

## 6. About page

```
cat ~/Documents/Claude/Projects/Publication\ Work/1-Projects/matthewignash-site/paste/About-Page.html | pbcopy
```

**Read this one before you delete anything.** About is the only page with no saved source file. It was assembled from loose fragments that were never consolidated, so I rebuilt it from `site/about.html`, which matches the live page as far as I can tell.

1. Open the live `/about` in a second tab and read it against the new version.
2. If anything on the live page is missing from the new one, tell me before going further. That would mean an edit was made in Squarespace and never made it back to a file.
3. Once it matches: **Edit** → delete the existing blocks → add one Code Block → **Cmd+A** → paste → Language = HTML → Display Source unchecked.
4. Background, **Save**.

## 7. Earth and Env case study

```
cat ~/Documents/Claude/Projects/Publication\ Work/1-Projects/matthewignash-site/paste/Case-Earth-Env.html | pbcopy
```

Page already exists at `/building-ai-literacy-in-a-science-course`. Replace its single Code Block. Background, **Save**.

**The course site link works.** It points at `https://hs-earth-env-site.vercel.app/`, the deployed Earth and Env course site. It sat as plain text for a while, because a link to a site that had not been deployed would have been a broken one. That is resolved.

## 8. Theatre case study, a brand new page

This is the only page you have to create.

```
cat ~/Documents/Claude/Projects/Publication\ Work/1-Projects/matthewignash-site/paste/Case-Theatre-Booking.html | pbcopy
```

1. **Pages** panel → **+** → **Blank Page**.
2. Name it **Booking a 780-seat theatre**.
3. **Move it out of the main navigation.** In the Pages panel, drag it into the **Not Linked** section. Case studies are reached from the Work page, not the top nav. Your Earth and Env case study already sits this way, so match it.
4. **Set the URL slug to `booking-a-780-seat-theatre`.** Gear icon → URL Slug. This must match exactly, because the Work page links to it.
5. **Edit** → add a Code Block → **Cmd+A** → paste → Language = HTML → Display Source unchecked.
6. Background, **Save**.

**Then check the wireframe works.** This one you can test **in the editor**, unlike everything else in this guide. The wireframe is pure CSS, no JavaScript, so it does not depend on the GitHub fetch that never runs while you are editing. That makes it a useful early signal: **if it works while editing, it will work published.**

- Click **Manager view**. The tab row underneath should change from three tabs to four.
- Click through the tabs. The little URL in the grey bar should change with each one.
- On the teacher **Seating** tab, you should see the coloured seat map with a partly filled orange block.

If the role buttons do nothing, it is not JavaScript, because there is none. Check Display Source is unchecked and that you pasted from `paste/` rather than `pages/`.

---

## 9. Final pass once everything is published

- **Remove Cart** from the navigation if you have not already. Edit → click the header → **Edit Site Header** → **Elements** → toggle Cart off.
- **Click every link on the Work page.** Two should open case studies. The rest should not be clickable at all.
- **Click "Read the CV" on the homepage.** It should land on `/cv`, not a 404.
- **Check for double footers.** Each page now carries its own footer. If you see two, an old standalone footer block is still sitting on that page.
- **Open the site on your phone.** Every page is responsive, but the seat map is the one thing built for a laptop. It scrolls sideways inside its box, which is expected.

---

## From here on

Eight pages, one command:

```
cd ~/Documents/Claude/Projects/Publication\ Work/1-Projects/matthewignash-site && python3 build.py && git commit -am "describe what changed" && git push
```

Live in about five minutes, no Squarespace login.

**And the standing habit:** every few months, or after a big content change, re-paste all eight blocks. The copy baked into each block is a frozen snapshot that only updates when you paste. Visitors with JavaScript never see it, but search engines can, and you do not want Google indexing a year-old CV.

---

## Do not publish these

Two files in the Theatre Management Dashboard folder are good internal documents and should stay internal:

- `FAC-Theatre-Booking-Manager_How-to-Use.docx`
- `Documentation/Theatre-Booking-Manager_IT-Handoff.docx`

Both contain real staff email addresses throughout. The case study page carries none, and no individual is named on it.

---

## 10. Hall pass case study, a second new page

Same shape as the theatre case study. This page does not exist yet, so you create it.

```
cat ~/Documents/Claude/Projects/Publication\ Work/1-Projects/matthewignash-site/paste/Case-Hall-Pass.html | pbcopy
```

1. **Pages** panel → **+** → **Blank Page**.
2. Name it **From a paper sheet to a system IT owns**.
3. Drag it into **Not Linked**, alongside the other two case studies. It is reached from the Work page, not the top nav.
4. **Set the URL slug to `replacing-the-paper-hall-pass`.** It must match exactly, because the Work page links to it.
5. **Edit** → add a Code Block → **Cmd+A** → paste → **Language = HTML** → **Display Source unchecked**.
6. Set the section background to match `/work`. **Save**.

**Test the wireframe.** It is CSS-only, so unlike everything else here it also works inside the Squarespace editor. That is a useful shortcut: if the role buttons work while you are editing, they will work published.

- Click **In the office**. The tab row should change from "Open a pass / Close a pass" to "Live now / History".
- On **Live now** you should see the coloured donut and the block bars, with Period 3 as the tallest.

**Three Work page rows now link out.** Earth and Env, Theatre Booking Manager, and Digital Hall Pass. Each carries the `↗` arrow. The other nine rows are plain and have no arrow, which is deliberate.

### A note on this page's honesty

This case study says plainly that the prototype was a demonstrator and was never run with students, and that IT owns version two. That is not modesty, it is the thing that makes the rest of the page credible. If a reference call ever comes, everything on this page will match what the Assistant Principal and IT would say about it.

---

## 11. IA moderation case study, a third new page

```
cat ~/Documents/Claude/Projects/Publication\ Work/1-Projects/matthewignash-site/paste/Case-IA-Moderation.html | pbcopy
```

1. **Pages** panel → **+** → **Blank Page**.
2. Name it **One rubric, both sides of the desk**.
3. Drag it into **Not Linked**, with the other case studies.
4. **Set the URL slug to `a-shared-standard-for-science-ias`.** Must match exactly; the Work page links to it.
5. **Edit** → Code Block → **Cmd+A** → paste → **Language = HTML** → **Display Source unchecked**.
6. Background to match `/work`. **Save**.

**Test:** click **As the moderator**. Tabs should change from "My queue / Score an IA" to "Compare and agree / Department view". On **Compare and agree** the Data analysis row should be highlighted with "readers differ by 2".

**Four Work rows now link out:** Earth and Env, IA Moderation Tool, Theatre Booking Manager, Digital Hall Pass. The other eight are plain, deliberately.

### Two things on this page worth knowing before you publish

**It names the AI pass.** The comparison table has an "AI pass" column alongside the two human readers, and the caption states that it never sets a mark and exists only to make disagreement visible. You chose to show this rather than hide it. It is the right call, but expect it to come up in an IB-facing interview, so have the sentence ready: the agreed column is always human, always from the conversation.

**It carries the IA outcome table**, in the same format and with the same caption as the CV page. If you ever revise those figures, they now live in two places: `pages/CV-Page.html` and `pages/Case-IA-Moderation.html`.
