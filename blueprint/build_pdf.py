"""Build the EVEglyphDesign Executive Blueprint PDF.

Cream/orange palette, Fraunces display + Inter body, sealed EVE Glyph mark
top-right of full diagrams and at foot of copyright page.
"""
from __future__ import annotations
import hashlib
import re
import textwrap
from datetime import datetime, timezone
from pathlib import Path

from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF

# --- paths ---
BLUEPRINT_DIR = Path("/home/user/workspace/sovereign-starter/blueprint")
FONTS_DIR = Path("/home/user/workspace/fonts")
OUT = BLUEPRINT_DIR / "EVEglyphDesign_Executive_Blueprint.pdf"
MD_PATH = BLUEPRINT_DIR / "blueprint.md"
LOGO_SVG = BLUEPRINT_DIR / "logo.svg"
DIAGRAM_FULL = BLUEPRINT_DIR / "diagram_full.svg"
DIAGRAM_MARG = BLUEPRINT_DIR / "diagram_marginal.svg"

# --- palette ---
CREAM = (0xfd/255, 0xfa/255, 0xf4/255)
CREAM2 = (0xf7/255, 0xf2/255, 0xe7/255)
INK = (0x1a/255, 0x1a/255, 0x1a/255)
LINE = (0xe7/255, 0xe1/255, 0xd3/255)
MUTE = (0x6b/255, 0x66/255, 0x5c/255)
ORANGE = (0xe8/255, 0x77/255, 0x22/255)

# --- fonts ---
pdfmetrics.registerFont(TTFont("Fraunces", str(FONTS_DIR / "Fraunces-Regular.ttf")))
pdfmetrics.registerFont(TTFont("Fraunces-Bold", str(FONTS_DIR / "Fraunces-Bold.ttf")))
pdfmetrics.registerFont(TTFont("Inter", str(FONTS_DIR / "Inter-Regular.ttf")))
pdfmetrics.registerFont(TTFont("Inter-Bold", str(FONTS_DIR / "Inter-Bold.ttf")))

# --- page geometry ---
PAGE_W, PAGE_H = LETTER
MARGIN_L = 0.9 * inch
MARGIN_R = 0.9 * inch
MARGIN_T = 0.9 * inch
MARGIN_B = 0.9 * inch
CONTENT_W = PAGE_W - MARGIN_L - MARGIN_R
BODY_SIZE = 10.5
BODY_LEAD = 15
H1_SIZE = 22
H2_SIZE = 14

# --- parse markdown into structured sections ---
def parse_markdown(md: str):
    """Return list of blocks: ('h1'|'h2'|'p'|'ul'|'diagram'|'meta', content).

    Blockquote-italic lines like `*[Full labelled ... top-right.]*` become 'diagram'
    markers, and the diagram type ('full' or 'marginal') and whether logo is required
    are inferred from the content.
    """
    blocks = []
    lines = md.split("\n")
    i = 0
    while i < len(lines):
        raw = lines[i]
        line = raw.rstrip()

        # skip horizontal rules
        if line.strip() == "---":
            i += 1
            continue

        # H1 (title)
        if line.startswith("# "):
            blocks.append(("h1", line[2:].strip()))
            i += 1
            continue

        # H2 (section)
        if line.startswith("## "):
            blocks.append(("h2", line[3:].strip()))
            i += 1
            continue

        # diagram markers
        if re.match(r"\s*\*?\[.*diagram.*\]\*?\s*$", line, re.I):
            content = line.strip().strip("*").strip("[]")
            dtype = "full" if "full" in content.lower() else "marginal"
            blocks.append(("diagram", (dtype, content)))
            i += 1
            continue

        # closing italic meta lines at end
        if line.startswith("*") and line.endswith("*") and len(line) > 2 and "diagram" not in line.lower():
            blocks.append(("meta", line.strip("*").strip()))
            i += 1
            continue

        # blank
        if line == "":
            i += 1
            continue

        # bullet list
        if line.lstrip().startswith("- "):
            items = []
            while i < len(lines) and lines[i].lstrip().startswith("- "):
                items.append(lines[i].lstrip()[2:].strip())
                i += 1
            blocks.append(("ul", items))
            continue

        # numbered list
        if re.match(r"\s*\d+\.\s", line):
            items = []
            while i < len(lines) and re.match(r"\s*\d+\.\s", lines[i]):
                items.append(re.sub(r"^\s*\d+\.\s", "", lines[i]).strip())
                i += 1
            blocks.append(("ol", items))
            continue

        # paragraph — gather consecutive non-blank lines that don't start a new block
        para = [line]
        i += 1
        while i < len(lines):
            nxt = lines[i]
            if nxt.strip() == "":
                break
            if nxt.startswith("#") or nxt.strip() == "---":
                break
            if nxt.lstrip().startswith("- ") or re.match(r"\s*\d+\.\s", nxt):
                break
            if re.match(r"\s*\*?\[.*diagram.*\]\*?\s*$", nxt, re.I):
                break
            para.append(nxt)
            i += 1
        blocks.append(("p", " ".join(para).strip()))
    return blocks


# --- inline markdown: **bold** and *italic* ---
_TOKEN = re.compile(r"(\*\*[^*]+\*\*|\*[^*]+\*|`[^`]+`)")

def tokenize_inline(text):
    out = []
    pos = 0
    for m in _TOKEN.finditer(text):
        if m.start() > pos:
            out.append(("r", text[pos:m.start()]))
        tok = m.group()
        if tok.startswith("**"):
            out.append(("b", tok[2:-2]))
        elif tok.startswith("`"):
            out.append(("c", tok[1:-1]))
        else:
            out.append(("i", tok[1:-1]))
        pos = m.end()
    if pos < len(text):
        out.append(("r", text[pos:]))
    return out

_FONT_FOR_STYLE = {
    "r": "Inter",
    "b": "Inter-Bold",
    "i": "Inter",   # italic surrogate: we don't have an italic file; use regular
    "c": "Inter",
}

def wrap_tokens(tokens, size, max_w):
    """Wrap a list of (style,text) tokens into lines that fit max_w."""
    lines = [[]]  # each line: list of (style, text, width)
    line_w = 0
    for style, text in tokens:
        # split into whitespace-preserving chunks (words + spaces)
        parts = re.findall(r"\S+|\s+", text)
        for part in parts:
            font = _FONT_FOR_STYLE[style]
            w = pdfmetrics.stringWidth(part, font, size)
            if part.isspace():
                # trailing space at line start -> drop
                if not lines[-1]:
                    continue
                lines[-1].append((style, part, w))
                line_w += w
                continue
            if line_w + w > max_w and lines[-1]:
                lines.append([])
                line_w = 0
            lines[-1].append((style, part, w))
            line_w += w
    return lines


# --- drawing helpers ---
class PageState:
    def __init__(self, c):
        self.c = c
        self.y = PAGE_H - MARGIN_T
        self.page_num = 1
        self.total_pages = 0

    def new_page(self, bg=CREAM):
        self.c.showPage()
        self.page_num += 1
        self._paint_bg(bg)
        self.y = PAGE_H - MARGIN_T

    def _paint_bg(self, bg):
        self.c.setFillColorRGB(*bg)
        self.c.rect(0, 0, PAGE_W, PAGE_H, stroke=0, fill=1)
        self.c.setFillColorRGB(*INK)

    def ensure(self, needed):
        if self.y - needed < MARGIN_B + 0.6 * inch:
            self.new_page()


def draw_svg(c, path, x, y, target_w, target_h=None):
    d = svg2rlg(str(path))
    if d is None:
        return
    scale_x = target_w / d.width
    scale_y = (target_h / d.height) if target_h else scale_x
    scale = min(scale_x, scale_y)
    d.scale(scale, scale)
    d.width *= scale
    d.height *= scale
    renderPDF.draw(d, c, x, y)


def draw_logo(c, x, y, size):
    draw_svg(c, LOGO_SVG, x, y, size, size)


def draw_wrapped(c, tokens, x, y, max_w, size=BODY_SIZE, lead=BODY_LEAD, color=INK):
    lines = wrap_tokens(tokens, size, max_w)
    c.setFillColorRGB(*color)
    for line in lines:
        cx = x
        for style, text, w in line:
            font = _FONT_FOR_STYLE[style]
            c.setFont(font, size)
            c.drawString(cx, y, text)
            cx += w
        y -= lead
    return y


def draw_footer(c, page_num, total, is_cover=False):
    c.setFillColorRGB(*MUTE)
    c.setFont("Inter", 8)
    if is_cover:
        return
    footer_y = MARGIN_B * 0.55
    c.drawString(MARGIN_L, footer_y, "EVEglyphDesign · Executive Blueprint · v4.2")
    c.drawRightString(PAGE_W - MARGIN_R, footer_y, f"page {page_num} of {total}")


def draw_cover(c, sha_placeholder="—", ts="—"):
    # background
    c.setFillColorRGB(*CREAM)
    c.rect(0, 0, PAGE_W, PAGE_H, stroke=0, fill=1)

    # logo top-right on cover
    draw_logo(c, PAGE_W - MARGIN_R - 0.9 * inch, PAGE_H - MARGIN_T - 0.9 * inch, 0.9 * inch)

    # title block
    c.setFillColorRGB(*INK)
    c.setFont("Fraunces-Bold", 34)
    c.drawString(MARGIN_L, PAGE_H - MARGIN_T - 2.2 * inch, "Executive Blueprint")

    c.setFont("Fraunces", 18)
    c.setFillColorRGB(*MUTE)
    c.drawString(MARGIN_L, PAGE_H - MARGIN_T - 2.8 * inch, "Sovereign Starter — one file, on a phone,")
    c.drawString(MARGIN_L, PAGE_H - MARGIN_T - 3.15 * inch, "in one session.")

    # accent bar
    c.setFillColorRGB(*ORANGE)
    c.rect(MARGIN_L, PAGE_H - MARGIN_T - 3.55 * inch, 1.2 * inch, 0.03 * inch, stroke=0, fill=1)

    # cover diagram
    dw = 4.6 * inch
    dh = 3.4 * inch
    dx = (PAGE_W - dw) / 2
    dy = MARGIN_B + 1.6 * inch
    draw_svg(c, DIAGRAM_FULL, dx, dy, dw, dh)

    # cover foot
    c.setFillColorRGB(*MUTE)
    c.setFont("Inter", 9)
    c.drawString(MARGIN_L, MARGIN_B + 0.6 * inch, "EVEglyphDesign · v4.2 · 2026-08-31")
    c.drawString(MARGIN_L, MARGIN_B + 0.4 * inch, f"UTC {ts}")
    c.drawRightString(PAGE_W - MARGIN_R, MARGIN_B + 0.6 * inch, "© 2026 EVEglyphDesign")
    c.drawRightString(PAGE_W - MARGIN_R, MARGIN_B + 0.4 * inch, f"SHA-256: {sha_placeholder}")


def render_blocks(c, blocks, state: PageState):
    for kind, content in blocks:
        if kind == "h1":
            # title already on cover — skip
            continue

        if kind == "h2":
            state.ensure(1.0 * inch)
            # accent rule above H2
            c.setFillColorRGB(*ORANGE)
            c.rect(MARGIN_L, state.y + 6, 0.5 * inch, 0.025 * inch, stroke=0, fill=1)
            c.setFillColorRGB(*INK)
            c.setFont("Fraunces-Bold", H2_SIZE)
            # wrap H2 if long
            words = content.split()
            line = ""
            lines = []
            for w in words:
                cand = (line + " " + w).strip()
                if pdfmetrics.stringWidth(cand, "Fraunces-Bold", H2_SIZE) > CONTENT_W - 1.2 * inch:
                    lines.append(line)
                    line = w
                else:
                    line = cand
            if line:
                lines.append(line)
            state.y -= 6
            for ln in lines:
                c.drawString(MARGIN_L, state.y - H2_SIZE, ln)
                state.y -= (H2_SIZE + 4)
            state.y -= 10
            continue

        if kind == "p":
            tokens = tokenize_inline(content)
            # estimate height
            lines = wrap_tokens(tokens, BODY_SIZE, CONTENT_W)
            needed = len(lines) * BODY_LEAD + 6
            state.ensure(needed)
            state.y -= BODY_SIZE
            state.y = draw_wrapped(c, tokens, MARGIN_L, state.y, CONTENT_W)
            state.y -= 4
            continue

        if kind in ("ul", "ol"):
            for idx, item in enumerate(content, 1):
                tokens = tokenize_inline(item)
                marker = f"{idx}." if kind == "ol" else "•"
                marker_w = pdfmetrics.stringWidth(marker, "Inter", BODY_SIZE) + 6
                lines = wrap_tokens(tokens, BODY_SIZE, CONTENT_W - marker_w - 4)
                needed = len(lines) * BODY_LEAD + 4
                state.ensure(needed)
                state.y -= BODY_SIZE
                c.setFillColorRGB(*ORANGE if kind == "ul" else INK)
                c.setFont("Inter" + ("-Bold" if kind == "ol" else ""), BODY_SIZE)
                c.drawString(MARGIN_L, state.y, marker)
                c.setFillColorRGB(*INK)
                state.y = draw_wrapped(c, tokens, MARGIN_L + marker_w + 4, state.y, CONTENT_W - marker_w - 4)
                state.y -= 2
            state.y -= 4
            continue

        if kind == "diagram":
            dtype, caption = content
            if dtype == "full":
                # dedicated space for full diagram in the flow
                needed = 3.4 * inch
                state.ensure(needed)
                state.y -= 0.1 * inch
                dw = 4.6 * inch
                dh = 3.0 * inch
                dx = (PAGE_W - dw) / 2
                dy = state.y - dh
                draw_svg(c, DIAGRAM_FULL, dx, dy, dw, dh)
                # logo top-right of diagram
                draw_logo(c, dx + dw - 0.6 * inch, dy + dh - 0.5 * inch, 0.5 * inch)
                # caption
                c.setFillColorRGB(*MUTE)
                c.setFont("Inter", 8)
                cap = "Circle — the repository, your boundary.  Triangle — boot contract (safety), canon (betterment), sin registry (enforcement).  Operator and objective outside the circle."
                # wrap caption
                cap_lines = []
                words = cap.split()
                l = ""
                for w in words:
                    cand = (l + " " + w).strip()
                    if pdfmetrics.stringWidth(cand, "Inter", 8) > CONTENT_W - 0.6 * inch:
                        cap_lines.append(l)
                        l = w
                    else:
                        l = cand
                if l:
                    cap_lines.append(l)
                cap_y = dy - 12
                for cl in cap_lines:
                    c.drawString(MARGIN_L + 0.3 * inch, cap_y, cl)
                    cap_y -= 10
                state.y = dy - (len(cap_lines) + 1) * 10 - 8
                c.setFillColorRGB(*INK)
            else:
                # marginal diagram: draw small at right margin at current y
                sz = 0.6 * inch
                x = PAGE_W - MARGIN_R - sz + 4
                y = state.y - sz + 0.2 * inch
                # only if there's room; if y is too low, skip
                if y > MARGIN_B + 0.6 * inch:
                    draw_svg(c, DIAGRAM_MARG, x, y, sz, sz)
            continue

        if kind == "meta":
            state.ensure(0.4 * inch)
            c.setFillColorRGB(*MUTE)
            c.setFont("Inter", 9)
            c.drawString(MARGIN_L, state.y - 12, content)
            state.y -= 22
            continue


def build():
    md = MD_PATH.read_text()
    blocks = parse_markdown(md)

    # PASS 1: compute page count by rendering to a throwaway canvas
    tmp = BLUEPRINT_DIR / ".tmp_count.pdf"
    c = canvas.Canvas(str(tmp), pagesize=LETTER)
    draw_cover(c)
    c.showPage()
    state = PageState(c)
    state.page_num = 2
    state._paint_bg(CREAM)
    render_blocks(c, blocks, state)
    c.save()
    # We don't need to inspect — but reportlab doesn't expose page count trivially post-save.
    # Read back via pypdf.
    from pypdf import PdfReader
    total_pages = len(PdfReader(str(tmp)).pages)
    tmp.unlink()

    # PASS 2: real build with footer showing total pages
    c = canvas.Canvas(str(OUT), pagesize=LETTER)
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    # cover first pass — we compute hash of markdown source as the "content hash"
    sha = hashlib.sha256(md.encode("utf-8")).hexdigest()[:16] + "…"
    draw_cover(c, sha_placeholder=sha, ts=ts)
    draw_footer(c, 1, total_pages, is_cover=True)  # no-op on cover
    c.showPage()

    state = PageState(c)
    state.page_num = 2
    state.total_pages = total_pages
    state._paint_bg(CREAM)

    # Hook: after each showPage we want to draw the footer.
    # Simpler: subclass by monkey-patching new_page.
    _orig_new_page = state.new_page
    def _wrapped():
        # draw footer on the page we're leaving
        draw_footer(c, state.page_num, total_pages)
        _orig_new_page()
        state._paint_bg(CREAM)
    state.new_page = _wrapped

    render_blocks(c, blocks, state)
    # footer on last content page
    draw_footer(c, state.page_num, total_pages)
    c.save()

    # verify
    from pypdf import PdfReader
    r = PdfReader(str(OUT))
    print(f"OUT: {OUT}")
    print(f"pages: {len(r.pages)}  (expected {total_pages})")
    print(f"size:  {OUT.stat().st_size} bytes")
    print(f"sha:   {sha}")


if __name__ == "__main__":
    build()
