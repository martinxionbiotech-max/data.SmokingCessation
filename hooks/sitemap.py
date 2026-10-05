"""MkDocs hook: 构建后生成 sitemap.xml（替代第三方 mkdocs-sitemap 插件）

为什么不用插件：CF Pages 构建环境没有安装 mkdocs-sitemap，导致
`Config value 'plugins': The "sitemap" plugin is not installed` → 构建失败。
本钩子只用标准库，随仓库分发，构建环境无需额外依赖。
"""

import os
from xml.sax.saxutils import escape


def on_post_build(config, **kwargs):
    site_dir = config["site_dir"]
    site_url = (config.get("site_url") or "").rstrip("/")
    urls = []
    for root, dirs, files in os.walk(site_dir):
        # 跳过 MkDocs 自身的资源目录
        dirs[:] = [d for d in dirs if d not in {"assets", "stylesheets", "javascripts", "search"}]
        for fn in files:
            if not fn.endswith(".html") or fn == "404.html":
                continue
            rel = os.path.relpath(os.path.join(root, fn), site_dir).replace(os.sep, "/")
            if rel == "index.html":
                loc = f"{site_url}/"
            elif rel.endswith("/index.html"):
                loc = f"{site_url}/{rel[: -len('index.html')]}"
            else:
                loc = f"{site_url}/{rel}"
            urls.append(loc)

    urls = sorted(set(urls))
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]
    lines += [f"  <url><loc>{escape(u)}</loc></url>" for u in urls]
    lines.append("</urlset>")

    out = os.path.join(site_dir, "sitemap.xml")
    with open(out, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")
    print(f"[sitemap-hook] wrote {len(urls)} URLs -> {out}")
