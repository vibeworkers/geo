#!/usr/bin/env python3
import json, re, ssl, urllib.request, urllib.error
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin, urlparse

SITES = [
    ("coupang", "https://www.coupang.com/"),
    ("gmarket", "https://www.gmarket.co.kr/"),
    ("musinsa", "https://www.musinsa.com/"),
    ("oliveyoung", "https://www.oliveyoung.co.kr/"),
]
OUT = Path(__file__).resolve().parent
CTX = ssl.create_default_context()
UA = "Mozilla/5.0 (compatible; GEOAuditBot/1.0; +https://example.local/geo-audit)"

class HeadParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_title = False
        self.title = ""
        self.meta = []
        self.links = []
        self.scripts = []
        self.html_lang = None
    def handle_starttag(self, tag, attrs):
        d = {k.lower(): (v or "") for k, v in attrs}
        if tag.lower() == "html":
            self.html_lang = d.get("lang")
        if tag.lower() == "title":
            self.in_title = True
        if tag.lower() == "meta":
            self.meta.append(d)
        if tag.lower() == "link":
            self.links.append(d)
        if tag.lower() == "script":
            self.scripts.append(d)
    def handle_endtag(self, tag):
        if tag.lower() == "title":
            self.in_title = False
    def handle_data(self, data):
        if self.in_title:
            self.title += data.strip() + " "

def fetch(url, max_bytes=600000):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "text/html,application/xhtml+xml,*/*"})
    try:
        with urllib.request.urlopen(req, timeout=15, context=CTX) as r:
            body = r.read(max_bytes)
            ctype = r.headers.get("content-type", "")
            text = body.decode("utf-8", errors="replace")
            return {"url": url, "ok": True, "status": r.status, "final_url": r.geturl(), "content_type": ctype, "headers": dict(r.headers), "bytes_read": len(body), "text": text}
    except Exception as e:
        return {"url": url, "ok": False, "error": f"{type(e).__name__}: {e}"}

def meta_content(meta, key, value):
    for m in meta:
        if m.get(key, "").lower() == value.lower():
            return m.get("content", "")
    return ""

def analyze(name, url):
    home = fetch(url)
    parsed = urlparse(url)
    root = f"{parsed.scheme}://{parsed.netloc}/"
    robots = fetch(urljoin(root, "robots.txt"), max_bytes=200000)
    sitemap = fetch(urljoin(root, "sitemap.xml"), max_bytes=200000)
    llms = fetch(urljoin(root, "llms.txt"), max_bytes=200000)
    hp = HeadParser()
    if home.get("ok"):
        hp.feed(home.get("text", ""))
    canonical = ""
    alternates = []
    for l in hp.links:
        rel = l.get("rel", "").lower()
        if "canonical" in rel:
            canonical = l.get("href", "")
        if "alternate" in rel and l.get("hreflang"):
            alternates.append({"hreflang": l.get("hreflang"), "href": l.get("href", "")})
    jsonld_count = sum(1 for s in hp.scripts if s.get("type", "").lower() == "application/ld+json")
    robots_text = robots.get("text", "") if robots.get("ok") else ""
    sitemap_lines = [line.strip() for line in robots_text.splitlines() if line.lower().startswith("sitemap:")]
    disallow_ai = []
    for bot in ["GPTBot", "ChatGPT-User", "ClaudeBot", "Claude-User", "PerplexityBot", "Google-Extended", "GoogleOther", "Applebot", "CCBot"]:
        if re.search(rf"(?im)^\s*user-agent:\s*{re.escape(bot)}\s*$", robots_text):
            disallow_ai.append(bot)
    return {
        "site": name,
        "url": url,
        "home": {k:v for k,v in home.items() if k != "text"},
        "robots": {k:v for k,v in robots.items() if k != "text"},
        "sitemap_xml": {k:v for k,v in sitemap.items() if k != "text"},
        "llms_txt": {k:v for k,v in llms.items() if k != "text"},
        "signals": {
            "html_lang": hp.html_lang,
            "title": hp.title.strip(),
            "meta_description": meta_content(hp.meta, "name", "description"),
            "og_title": meta_content(hp.meta, "property", "og:title"),
            "og_description": meta_content(hp.meta, "property", "og:description"),
            "canonical": canonical,
            "hreflang_count": len(alternates),
            "hreflang_samples": alternates[:10],
            "jsonld_count": jsonld_count,
            "robots_sitemap_lines": sitemap_lines[:10],
            "explicit_ai_user_agents_in_robots": disallow_ai,
        },
    }

for name, url in SITES:
    data = analyze(name, url)
    (OUT / f"{name}.json").write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
print(json.dumps({"ok": True, "sites": [n for n,_ in SITES], "out": str(OUT)}, ensure_ascii=False))
