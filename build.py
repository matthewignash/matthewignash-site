#!/usr/bin/env python3
"""Wrap each page fragment in a Squarespace Code Block that refreshes itself from GitHub.

The pasted block carries a full copy of the page as fallback, so the page renders
even if GitHub is unreachable. On a successful fetch the fallback is replaced with
whatever is currently on main. Run this after changing anything in pages/.
"""
from pathlib import Path

RAW_BASE = "https://raw.githubusercontent.com/matthewignash/matthewignash-site/main/pages"
CONTAINERS = {
    "Home-Page.html": "mi-home",
    "About-Page.html": "mi-about",
    "Work-Page.html": "mi-work",
    "Writing-Media-Page.html": "mi-writing",
    "CV-Page.html": "mi-cv",
    "Contact-Page.html": "mi-contact",
    "Case-Earth-Env.html": "mi-case-earth-env",
}

LOADER = """<script>
(function () {
  var mount = document.getElementById("__CONTAINER__");

  function scrubbed(markup) {
    var parsed = new DOMParser().parseFromString(markup, "text/html");
    [].forEach.call(parsed.querySelectorAll("script,iframe,object,embed"), function (node) {
      node.remove();
    });
    [].forEach.call(parsed.querySelectorAll("*"), function (node) {
      [].forEach.call([].slice.call(node.attributes), function (attr) {
        var unsafe = /^on/i.test(attr.name) || /^\\s*javascript:/i.test(attr.value);
        if (unsafe) node.removeAttribute(attr.name);
      });
    });
    return [].slice.call(parsed.head.childNodes).concat([].slice.call(parsed.body.childNodes));
  }

  fetch("__SOURCE__", { cache: "no-cache" })
    .then(function (response) {
      if (!response.ok) throw new Error(response.status);
      return response.text();
    })
    .then(function (markup) {
      var nodes = markup.trim() ? scrubbed(markup) : [];
      if (!nodes.length) return;
      mount.textContent = "";
      nodes.forEach(function (node) { mount.appendChild(document.importNode(node, true)); });
    })
    .catch(function () {});
}());
</script>
"""

root = Path(__file__).parent
paste_dir = root / "paste"
paste_dir.mkdir(exist_ok=True)

for filename, container in CONTAINERS.items():
    fragment = (root / "pages" / filename).read_text().rstrip()
    loader = LOADER.replace("__CONTAINER__", container).replace(
        "__SOURCE__", RAW_BASE + "/" + filename
    )
    header = (
        "<!-- " + filename + " for matthewignash.com. Paste into one Squarespace Code Block, once.\n"
        "     After that, edit pages/" + filename + " in the matthewignash-site repo and push.\n"
        "     This block picks the change up within about five minutes, no re-paste needed.\n"
        "     The copy below is a fallback, so the page is never blank if GitHub is unreachable.\n"
        "     Fetched markup is stripped of scripts and event handlers before it is inserted. -->\n"
    )
    body = '<div id="' + container + '">\n' + fragment + "\n</div>\n"
    (paste_dir / filename).write_text(header + body + loader)
    print("wrote paste/" + filename)
