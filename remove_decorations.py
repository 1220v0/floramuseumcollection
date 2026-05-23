with open('index.html', 'r') as f:
    content = f.read()

# Patterns to remove
decorative_patterns = [
    r'<!-- Hand-drawn decorations -->\s*<svg.*?</svg>\s*<svg.*?</svg>\s*',
    r'<!-- Botanical decoration -->\s*<svg.*?</svg>\s*',
    r'<!-- Compass decoration -->\s*<svg.*?</svg>\s*',
    r'<!-- Camera decoration -->\s*<svg.*?</svg>\s*',
    r'<!-- Postcard decoration -->\s*<svg.*?</svg>\s*',
    r'<svg class="decoration.*?</svg>\s*',
    r'<div class="ornament">❧</div>\s*',
    r'<div class="final-ornament">✦</div>\s*',
]

import re

for pattern in decorative_patterns:
    content = re.sub(pattern, '', content, flags=re.DOTALL)

# Write back
with open('index.html', 'w') as f:
    f.write(content)

print("Decorative elements removed successfully!")
