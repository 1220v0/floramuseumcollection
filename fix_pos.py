content = open('index.html', encoding='utf-8').read()
content = content.replace('translateX(-12vw)', 'translateX(-8vw)', 2)
content = content.replace(
    '#photo-description.visible { right: 40px; width: 30vw; }',
    '#photo-description.visible { right: 20px; width: 28vw; }'
)
open('index.html', 'w', encoding='utf-8').write(content)
print('Done')
