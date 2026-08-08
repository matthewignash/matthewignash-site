# Getting the GitHub blocks onto Squarespace

Step by step. Roughly 40 minutes. Do it in this order.

**Repo folder** (referred to below as THE FOLDER):
`~/Documents/Claude/Projects/Publication Work/1-Projects/matthewignash-site`

---

## How this works, in two sentences

You paste each page's code into Squarespace **once**. From then on you edit the file in THE FOLDER, push to GitHub, and the live page picks up the change on its own in about five minutes.

The thing you paste already contains a full copy of the page, so the page works even if the GitHub part fails. That is why the file you paste is bigger than the one you edit.

---

## Before you start: two things that will confuse you

**1. The editor will look wrong. That is correct.**
Squarespace does not run JavaScript while you are editing. So inside the editor you will always see the built-in copy, never the GitHub version. Only the published page fetches from GitHub. Do not go hunting for a bug.

**2. Copy with Terminal, not TextEdit.**
Opening an HTML file in TextEdit can turn it into rich text and quietly corrupt it. Use the Terminal commands below. Each one puts the file on your clipboard, ready to paste.

---

## STEP 0. Check you can add a Code Block (1 minute)

Code Blocks need the Squarespace **Business** or **Core** plan or above.

Open any page in Squarespace, click **Edit**, click a **+** to add a block, and type "code" in the search. If **Code** appears, you are fine. If it is missing or greyed out, stop here and tell me, because none of this works on a lower plan.

---

## STEP 1. Contact page (do this first, it is the worst thing live)

Right now your Contact page says **"Request a Private Consultation"** with **"a dedicated advisor will connect with you shortly to discuss how our curated programs can advance your educational goals."** That is Squarespace demo copy for a tutoring business.

### 1a. Copy the code

Open Terminal and paste this, then press Return:

```
cat ~/Documents/Claude/Projects/Publication\ Work/1-Projects/matthewignash-site/paste/Contact-Page.html | pbcopy
```

Nothing will appear. That is normal. The code is on your clipboard.

### 1b. Delete the stock copy

1. In Squarespace, left sidebar → **Pages** → click **Contact**.
2. Click **Edit** (top left of the page preview).
3. Click the heading **"Request a Private Consultation"** → click the **trash icon** → confirm.
4. Click the paragraph starting **"We invite you to complete the form below"** → **trash icon** → confirm.
5. If there is a placeholder image, delete that too.

### 1c. Add the Code Block

1. Still in Edit mode, hover near the top of the page content. A **blue line with a + on it** appears.
2. Click the **+**.
3. In the search box type **code**, click **Code**.
4. A code block appears containing `<p>Hello, World!</p>` or similar.
5. **Click inside the code box, press Cmd+A to select everything, then Cmd+V to paste.** You must select-all first or you will end up with the placeholder text still in there.
6. Below the code box, find the **Language** dropdown → set it to **HTML**.
7. Find the **Display Source** checkbox → make sure it is **UNCHECKED**. If it is checked, Squarespace prints your code as visible text instead of rendering it.
8. Click outside the block to close it.

### 1d. Add the contact form

1. Hover just **below** the Code Block → click the **+**.
2. Search **form** → click **Form**.
3. Click the form → **Edit** → set the fields to: **Name, Email, Organisation (optional), Message**.
4. Go to the **Storage** tab → choose **Email** → enter your own address there.

   Type it into Squarespace only. It is deliberately not written down in this repo, which is public, and it is deliberately absent from the Contact and CV pages. The form is the only route now.
5. Close the form editor.

Use the native Form Block, not a coded one. Squarespace forms actually deliver mail and keep working regardless of the GitHub part.

### 1e. Set the background

1. Hover over the section → on the left edge, click the **paintbrush / Edit Section** icon.
2. Go to **Background** → **Colour**.
3. Pick the same section theme that `/work` and `/about` already use. Those pages are already on the right warm paper tone, so matching them is more reliable than hunting for the hex code `#FAF7F2`.

### 1f. Save

Click **Save** (top left). Done.

---

## STEP 2. CV page

### 2a. The URL — mostly done, one piece still missing

The page now lives at **`matthewignash.com/curriculum-vitae`**. Squarespace refused the shorter `cv`, which is normal rather than a fault: the field shows the `/` separately, so typing `/cv` produces `//cv` and is rejected.

**Still to do, and it matters.** Your homepage has a **"Read the CV"** button hardcoded to `/cv`, and `/cv` still returns a 404 for every visitor. Your header nav is fine, it points at the real page. To fix the button:

1. Left sidebar → **Settings** → **Advanced** → **URL Mappings**.
2. Add this line exactly:

```
/cv -> /curriculum-vitae 301
```

3. **Save**, then open `matthewignash.com/cv` in a new tab. The point of the test is that `/cv` now lands on the CV page instead of 404ing.

### 2b. Copy the code

```
cat ~/Documents/Claude/Projects/Publication\ Work/1-Projects/matthewignash-site/paste/CV-Page.html | pbcopy
```

### 2c. Paste it

Same as step 1c: **Edit** → **+** → search **code** → **Code** → click in the box → **Cmd+A** → **Cmd+V** → **Language = HTML** → **Display Source unchecked** → click outside.

### 2d. Background, then Save

Same as 1e and 1f.

**About the four buttons on this page.** They are an emphasis switch, not downloads. Clicking **Leadership & Operations**, **Curriculum & Innovation** or **IB Programme** moves the most relevant rows to the top of Leadership and impact; **Full record** puts them back. Nothing is ever hidden, and no row is removed in any state. Asking for the actual CV is the plain **Request the full CV** link underneath.

They work without JavaScript, which is why they are radio buttons under the hood rather than a script. If you tab into them, the arrow keys move between them.

**This page also has a sticky section nav** below the buttons. It pins to the top as you scroll so a reader can jump to Experience or Education without hunting.

**Why this page used to scroll forever.** It was 18 screens tall for about 4 screens of content. Squarespace's Fluid Engine sizes a section by the number of grid rows it declares, and this one declared 439, so it reserved roughly 16,000px whatever was inside it. The pasted block now collapses those rows itself. If you ever see a page with a vast blank space below the content, that is the cause, and re-pasting the current block fixes it.

---

## STEP 3. Writing and Media page

This page is currently completely empty.

```
cat ~/Documents/Claude/Projects/Publication\ Work/1-Projects/matthewignash-site/paste/Writing-Media-Page.html | pbcopy
```

Then: **Pages** → **Writing** → **Edit** → **+** → **Code** → **Cmd+A** → **Cmd+V** → **Language = HTML** → **Display Source unchecked** → set background → **Save**.

---

## STEP 4. The Cart — nothing to do. Skip this.

An earlier version of this guide told you to remove **Cart** from the navigation. **That was wrong, and you were right that you could not find it.**

The mistake came from spotting `href="/cart"` in the page source without checking whether it renders. The actual markup is:

```
<div id="floatingCart" class="floating-cart hidden">
```

That `hidden` class is the whole story. Squarespace 7.1 puts that div on every site whether or not you sell anything, and it stays hidden until you have products. It is not in your header nav either. There is no cart on your site and nothing to switch off.

## STEP 4b. The four remaining pages

Home, About, Work and the case study all work exactly like the ones above: copy, add one Code Block, **Cmd+A**, **Cmd+V**, **Language = HTML**, **Display Source unchecked**, set the background, **Save**.

Two things apply to all four. Set the section background to match `/work` and `/about`, which are already on the right tone. And if **two footers** appear after pasting, an old standalone footer block is still sitting on the page below your new one — delete it.

### 4b-i. Home page

**This one replaces eight Code Blocks with one.** The homepage was built as eight separate blocks, hero through footer. Delete all eight, then paste this single block in their place.

```
cat ~/Documents/Claude/Projects/Publication\ Work/1-Projects/matthewignash-site/paste/Home-Page.html | pbcopy
```

**Watch for a duplicated headshot.** The hero image now comes from inside the HTML rather than from a Squarespace image block. If an image block is still on the page, you will see the photo twice. Delete the image block, not the code.

### 4b-ii. Work page

**Replaces five Code Blocks with one.** Delete all five first.

```
cat ~/Documents/Claude/Projects/Publication\ Work/1-Projects/matthewignash-site/paste/Work-Page.html | pbcopy
```

Eleven rows on this page used to show a `↗` arrow while linking nowhere. They are now plain text with no arrow. Only Earth and Env still links out, and it keeps its arrow. That is deliberate, not something to put back.

### 4b-iii. About page

**Read this one before you delete anything.** Unlike the others, the About page was never saved as a source file anywhere; the live page was assembled from loose fragments. This version was written fresh from what is currently published.

So: open `matthewignash.com/about` in one tab, paste the new block into a **draft** or simply compare on screen, and read the two side by side first. If a line is missing or reworded in a way you do not want, tell me before you delete the old blocks.

```
cat ~/Documents/Claude/Projects/Publication\ Work/1-Projects/matthewignash-site/paste/About-Page.html | pbcopy
```

### 4b-iv. Earth and Env case study

One block replaced by one block, on `/building-ai-literacy-in-a-science-course`.

```
cat ~/Documents/Claude/Projects/Publication\ Work/1-Projects/matthewignash-site/paste/Case-Earth-Env.html | pbcopy
```

The link to the course site is currently **plain text rather than a link**, because that site is not deployed yet. Once it is on Vercel, tell me the URL and I will wire it up.

---

## STEP 5. Prove the GitHub connection actually works

The editor cannot tell you this. You have to test on the live page.

Right now the built-in copy and the GitHub copy are identical, so you need to create a visible difference on purpose.

1. Make sure the pages you have pasted are published.
2. Open THE FOLDER, and in `pages/CV-Page.html` find the line with `Curriculum vitae`. Change it to `Curriculum vitae TEST`.
3. In Terminal:

```
cd ~/Documents/Claude/Projects/Publication\ Work/1-Projects/matthewignash-site && python3 build.py && git commit -am "fetch test" && git push
```

4. Wait five minutes.
5. Open `matthewignash.com/curriculum-vitae` in a **new tab**, then hard-reload with **Cmd+Shift+R**.

**If you see "Curriculum vitae TEST"** the connection is live. Change it back, run the same Terminal command again with a different message, and you are done.

**If you do not see it after five minutes**, the page is running on the built-in copy. Tell me. The likely cause is Squarespace blocking the request to GitHub, and if that is what is happening you need to know now rather than in three months.

---

## STEP 6. From now on, this is the whole loop

To change anything on Contact, CV, or Writing and Media:

1. Edit the file in **`pages/`** in THE FOLDER. Not `paste/`. Not the old `Squarespace-Blocks` folder.
2. Run this one line in Terminal:

```
cd ~/Documents/Claude/Projects/Publication\ Work/1-Projects/matthewignash-site && python3 build.py && git commit -am "describe what changed" && git push
```

3. Wait about five minutes. The live site updates itself. **No Squarespace login, no re-pasting.**

That is the whole point of this setup.

---

## One habit that protects you

Every few months, or after any big content change, **re-paste every block** using the Terminal copy commands above. There are seven now.

Here is why. The code you paste contains a snapshot of the page. Visitors normally see the fresh GitHub version, so the snapshot stays invisible. But if the fetch ever fails, and for search engines that do not run JavaScript, that snapshot is what gets read. It never updates on its own, no matter how many times you push.

Running `build.py` refreshes the snapshot **in the file on your computer**. Only pasting it into Squarespace refreshes the one on the live site.

### The one case where a push is not enough, and you must re-paste

If the *point* of a change is that the old content stops existing, pushing does not achieve it. The snapshot in Squarespace still carries the old version, in the page source, where scrapers read it.

**This applies to you right now.** Your email address was removed from the Contact and CV pages, but the blocks currently pasted on your site still contain it: three times on `/contact`, five times plus four `mailto:` links on `/curriculum-vitae`. Visitors do not see it, because the fetch replaces it. Bots reading the source do.

Re-pasting Contact and CV is what actually removes it. Those two blocks have changed several times since you pasted, so do them both.

Left alone for a year, Google could end up indexing a year-old version of your CV. Re-pasting quarterly costs ten minutes and removes the problem.

---

## If something looks wrong

| What you see | What it means | Fix |
|---|---|---|
| Your code showing as visible text on the page | **Display Source** is checked | Edit the block, uncheck it |
| Page looks unstyled or plain | Only part of the code pasted | Click in the code box, Cmd+A, re-copy and re-paste |
| Old content still there | The old blocks were not deleted | Edit the page, delete the leftover text blocks |
| Editor shows the old wording after you pushed | Normal, the editor never fetches | Check the published page in a new tab instead |
| Nothing changes on the live page after pushing | The fetch is being blocked | Do step 5, then tell me the result |
| Section colour looks off against other pages | Wrong section theme | Match the theme `/work` and `/about` use |

---

## Where things live now

| Folder | What it is |
|---|---|
| `matthewignash-site/pages/` | **The real files. Edit these.** |
| `matthewignash-site/paste/` | Auto-generated. Copy from here into Squarespace. Never edit by hand. |
| `matthewignash-site/build.py` | Regenerates `paste/` from `pages/`. Run before every push. |
| `Job-Search-2027-2028/Squarespace-Blocks/Pages/` | **Retired.** Editing it changes nothing. Its README is still worth reading for why the content says what it says. |
