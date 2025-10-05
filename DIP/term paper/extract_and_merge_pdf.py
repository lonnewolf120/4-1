#!/usr/bin/env python3
"""
Extract text from a PDF and merge/update the DIP_Term_Paper.md file.

Rules implemented:
- Extract text from DIP_Lectures.pdf to DIP_Lectures.txt
- Keep only Markdown sections whose headings appear in the PDF text (case-insensitive)
  OR whose content contains keywords: tip, tips, trick, technique (case-insensitive).
- Append any PDF text segments not found in the original MD under a new section
  "Additional content from DIP_Lectures.pdf".

This is a best-effort automated merge; review the resulting Markdown.
"""
import sys
from pathlib import Path
import re

try:
    from pdfminer.high_level import extract_text
except Exception:
    extract_text = None


ROOT = Path(r"D:/MIST/DIP/term paper")
PDF = ROOT / "DIP_Lectures.pdf"
TXT = ROOT / "DIP_Lectures.txt"
MD = ROOT / "DIP_Term_Paper.md"
BACKUP = ROOT / "DIP_Term_Paper.md.bak"

def extract_pdf_text(pdf_path, out_txt_path):
    if extract_text is None:
        raise RuntimeError("pdfminer.six not installed")
    text = extract_text(str(pdf_path))
    out_txt_path.write_text(text, encoding='utf-8')
    return text

def split_markdown_sections(md_text):
    # Split into blocks with heading line included
    lines = md_text.splitlines()
    sections = []
    cur = []
    for line in lines:
        if line.startswith('#') and cur:
            sections.append('\n'.join(cur))
            cur = [line]
        else:
            cur.append(line)
    if cur:
        sections.append('\n'.join(cur))
    return sections

def heading_of_section(section_text):
    for line in section_text.splitlines():
        if line.strip().startswith('#'):
            # return heading text without hashes
            return re.sub(r'^#+\s*', '', line).strip()
    return ''

def contains_tip_keywords(section_text):
    return bool(re.search(r'\b(tip|tips|trick|technique|techniques)\b', section_text, re.I))

def normalize_whitespace(s):
    return re.sub(r'\s+', ' ', s).strip()

def main():
    if not PDF.exists():
        print(f"PDF not found: {PDF}")
        sys.exit(1)

    if extract_text is None:
        print("Required package pdfminer.six not installed. Install with: pip install pdfminer.six")
        sys.exit(2)

    print(f"Extracting text from {PDF} ...")
    pdf_text = extract_pdf_text(PDF, TXT)
    pdf_norm = normalize_whitespace(pdf_text.lower())

    md_text = MD.read_text(encoding='utf-8')
    MD.write_text(md_text, encoding='utf-8')
    BACKUP.write_text(md_text, encoding='utf-8')

    sections = split_markdown_sections(md_text)
    kept_sections = []

    for sec in sections:
        head = heading_of_section(sec)
        if not head:
            # keep preamble (if any)
            kept_sections.append(sec)
            continue
        if head.lower() in pdf_norm or contains_tip_keywords(sec):
            kept_sections.append(sec)
        else:
            # also check by words of the heading (split)
            words = [w for w in re.split(r'\W+', head.lower()) if w]
            if any(w in pdf_norm for w in words[:3]):
                kept_sections.append(sec)
            else:
                print(f"Dropping section not found in PDF: '{head}'")

    # Find additional content in PDF not present in MD: take long paragraphs from PDF
    pdf_paras = [p.strip() for p in re.split(r'\n\s*\n', pdf_text) if len(p.strip())>50]
    md_norm = normalize_whitespace('\n'.join(kept_sections)).lower()
    additional = []
    for p in pdf_paras:
        n = normalize_whitespace(p).lower()
        if n not in md_norm and len(n) > 80:
            additional.append(p.strip())

    # Build new markdown
    new_md = '\n\n'.join(kept_sections)
    if additional:
        new_md += '\n\n## Additional content from DIP_Lectures.pdf\n\n'
        for a in additional:
            new_md += a + '\n\n'

    MD.write_text(new_md, encoding='utf-8')
    print(f"Wrote updated markdown to {MD} (backup saved at {BACKUP})")
    print(f"Extracted text saved to {TXT}")

if __name__ == '__main__':
    main()
