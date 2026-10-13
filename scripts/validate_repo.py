"""Validate Skill structure and flag non-anonymous/historical publication content."""
from pathlib import Path
import re
import sys

root = Path(__file__).resolve().parents[1]
skills = sorted((root / 'skills').glob('*/SKILL.md'))
errors = []
if len(skills) != 11:
    errors.append(f'Expected 11 Skill definitions; found {len(skills)}')
for skill in skills:
    text = skill.read_text(encoding='utf-8')
    match = re.search(r'\A---\n(.*?)\n---\n', text, flags=re.S)
    if not match:
        errors.append(f'Missing YAML frontmatter: {skill}')
    else:
        header = match.group(1)
        if not re.search(r'^name:\s*' + re.escape(skill.parent.name) + r'\s*$', header, re.M):
            errors.append(f'Skill name does not match directory: {skill}')
        if not re.search(r'^description:\s*\S', header, re.M):
            errors.append(f'Missing description: {skill}')
    for companion in ['references/METHOD.md', 'assets/PRACTICE.md', 'references/DECISION_PROMPTS.md']:
        if not (skill.parent/companion).exists() and skill.parent.name != 'study-coach':
            errors.append(f'Missing {companion}: {skill.parent.name}')

# Detect accidental uploads of identifiable material and date-specific content.
forbidden = [
    r"\b20(?:2\d|3\d)\b",
    r"\b[A-Za-z]{2,5}\.F?\d{3}\b",
    r"\b[A-Z][a-z]{3,}\s+University\b",
]
for item in root.rglob('*'):
    if not item.is_file() or '.git' in item.parts: continue
    if item.suffix.lower() in {'.pdf','.docx','.pptx','.xlsx'}:
        errors.append(f'Restricted document type in public package: {item.relative_to(root)}')
    if item.suffix.lower() in {'.md','.txt','.py','.yml','.yaml','.svg'}:
        data = item.read_text(encoding='utf-8')
        for pat in forbidden:
            # Avoid flagging the validator's own quoted detection patterns
            if item.name == 'validate_repo.py': continue
            if re.search(pat, data, flags=re.I):
                errors.append(f'Potential historical reference {pat!r}: {item.relative_to(root)}')
print(f'Checked {len(skills)} Skills and all public text files.')
if errors:
    print('\n'.join('FAIL: '+e for e in errors)); sys.exit(1)
print('PASS: structure and public-content checks')
