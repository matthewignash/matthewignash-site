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
4. Go to the **Storage** tab → choose **Email** → enter **matthew.ignash@gmail.com**.
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

**Do 2a before 2b.** Changing the URL first means you only publish once, and it fixes a link that is broken right now: your homepage has a "Read the CV" button pointing at `/cv`, and `/cv` currently returns a 404 for every visitor.

### 2a. Change the URL first

1. Left sidebar → **Pages**.
2. Hover over the **CV** page → click the **gear / settings icon** that appears on the right.
3. Find **URL Slug**. It currently says `583544494043`.
4. Delete that and type `cv`.
5. Click **Save**.

Your CV page is now at `matthewignash.com/cv` and the homepage button works.

### 2b. Copy the code

```
cat ~/Documents/Claude/Projects/Publication\ Work/1-Projects/matthewignash-site/paste/CV-Page.html | pbcopy
```

### 2c. Paste it

Same as step 1c: **Edit** → **+** → search **code** → **Code** → click in the box → **Cmd+A** → **Cmd+V** → **Language = HTML** → **Display Source unchecked** → click outside.

### 2d. Background, then Save

Same as 1e and 1f.

**About the three buttons on this page:** they open a pre-filled email asking for the CV rather than downloading a PDF. That is deliberate, because the PDFs do not exist yet and a working email request beats a broken download. When the PDFs are ready, the replacement code is already sitting commented out just below them.

---

## STEP 3. Writing and Media page

This page is currently completely empty.

```
cat ~/Documents/Claude/Projects/Publication\ Work/1-Projects/matthewignash-site/paste/Writing-Media-Page.html | pbcopy
```

Then: **Pages** → **Writing** → **Edit** → **+** → **Code** → **Cmd+A** → **Cmd+V** → **Language = HTML** → **Display Source unchecked** → set background → **Save**.

---

## STEP 4. Remove "Cart" from the navigation

It is a Squarespace commerce default and it currently shows on every page.

1. Click **Edit** on any page.
2. Click on the **header area** at the top.
3. Click **Edit Site Header**.
4. Click **Elements**.
5. Toggle **Cart** **off**.
6. **Save**.

---

## STEP 5. Prove the GitHub connection actually works

The editor cannot tell you this. You have to test on the live page.

Right now the built-in copy and the GitHub copy are identical, so you need to create a visible difference on purpose.

1. Make sure all three pages are published.
2. Open THE FOLDER, and in `pages/CV-Page.html` find the line with `Curriculum vitae`. Change it to `Curriculum vitae TEST`.
3. In Terminal:

```
cd ~/Documents/Claude/Projects/Publication\ Work/1-Projects/matthewignash-site && python3 build.py && git commit -am "fetch test" && git push
```

4. Wait five minutes.
5. Open `matthewignash.com/cv` in a **new tab**, then hard-reload with **Cmd+Shift+R**.

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

Every few months, or after any big content change, **re-paste all three blocks** using the same Terminal copy commands from steps 1a, 2b and 3.

Here is why. The code you paste contains a snapshot of the page. Visitors normally see the fresh GitHub version, so the snapshot stays invisible. But if the fetch ever fails, and for search engines that do not run JavaScript, that snapshot is what gets read. It never updates on its own, no matter how many times you push.

Running `build.py` refreshes the snapshot **in the file on your computer**. Only pasting it into Squarespace refreshes the one on the live site.

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
