import re
from collections import defaultdict

LINK_RE = re.compile(r"\[\[([^\]]+)\]\]")

class BacklinksPlugin:
    def on_files(self, files, config):
        self.links = defaultdict(list)

        for f in files:
            if not f.src_path.endswith(".md"):
                continue

            with open(f.abs_src_path, encoding="utf-8") as fp:
                content = fp.read()

            for target in LINK_RE.findall(content):
                self.links[target].append(f)

        return files

    def on_page_markdown(self, markdown, page, config, files):
        name = page.file.name
        backlinks = self.links.get(name, [])

        if backlinks:
            page.meta["backlinks"] = [
                {
                    "title": p.page.title or p.file.name,
                    "url": p.page.url,
                }
                for p in backlinks
                if p.page
            ]

        return markdown

