#!/usr/bin/env python3
"""
Merge DIP_Lectures.txt into DIP_Term_Paper.md according to user rules:
- Keep only Markdown sections whose headings appear in the lecture text (case-insensitive)
  OR whose content contains keywords: tip, tips, trick, technique (case-insensitive).
- Remove other sections unless they contain tips/tricks/techniques.
- Append lecture paragraphs not present in the MD under 'Additional content from DIP_Lectures.txt'.

Creates a backup DIP_Term_Paper.md.bak before writing.
"""
from pathlib import Path
import re
import sys

ROOT = Path(r"D:/MIST/DIP/term paper")
TXT = ROOT / "DIP_Lectures.txt"
MD = ROOT / "DIP_Term_Paper.md"
BAK = ROOT / "DIP_Term_Paper.md.bak"

def read_text(p):
    return p.read_text(encoding='utf-8')

def split_sections(md_text):
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

def heading(sec):
    for ln in sec.splitlines():
        if ln.strip().startswith('#'):
            return re.sub(r'^#+\s*', '', ln).strip()
    return ''

def has_tip_keywords(sec):
    return bool(re.search(r'\b(tip|tips|trick|technique|techniques)\b', sec, re.I))

def normalize(s):
    return re.sub(r'\s+', ' ', s).strip().lower()

def main():
    if not TXT.exists():
        print(f"Lecture text not found: {TXT}")
        sys.exit(1)
    if not MD.exists():
        print(f"Markdown not found: {MD}")
        sys.exit(1)

    lecture = read_text(TXT)
    lecture_norm = normalize(lecture)

    md = read_text(MD)
    BAK.write_text(md, encoding='utf-8')

    sections = split_sections(md)
    kept = []
    dropped = []
    for sec in sections:
        h = heading(sec)
        if not h:
            kept.append(sec)
            continue
        # If heading words appear in lecture text, keep
        h_words = [w for w in re.split(r'\W+', h.lower()) if w]
        found = any(w in lecture_norm for w in h_words[:3])
        if found or h.lower() in lecture_norm or has_tip_keywords(sec):
            kept.append(sec)
        else:
            dropped.append(h)

    # Find additional lecture paragraphs not in markdown
    md_concat = normalize('\n'.join(kept))
    paras = [p.strip() for p in re.split(r'\n\s*\n', lecture) if len(p.strip())>40]
    additional = []
    for p in paras:
        n = normalize(p)
        if n and n not in md_concat:
            additional.append(p.strip())

    new_md = '\n\n'.join(kept)
    if additional:
        new_md += '\n\n## Additional content from DIP_Lectures.txt\n\n'
        for a in additional:
            new_md += a + '\n\n'

    MD.write_text(new_md, encoding='utf-8')
    print(f"Merge complete. Backup saved to {BAK}. Dropped sections: {dropped}")

if __name__ == '__main__':
    main()
