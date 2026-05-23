content = open('index.html', encoding='utf-8').read()
import re
content = re.sub(
    r'#photo-description\s*\{[^}]*\}',
    '#photo-description { position: fixed; top: 50%; right: -450px; transform: translateY(-50%); width: 35vw; max-width: 420px; padding: 48px 40px; z-index: 10001; transition: right 400ms cubic-bezier(0.16,1,0.3,1); color: white; }',
    content,
    count=1
)
content = re.sub(
    r'#photo-description\.visible\s*\{[^}]*\}',
    '#photo-description.visible { right: 20px; }',
    content,
    count=1
)
open('index.html', 'w', encoding='utf-8').write(content)
print('Done')
