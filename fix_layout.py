content = open('index.html', encoding='utf-8').read()

# Fix 1: reduce photo left shift
content = content.replace('translateX(-20vw)', 'translateX(-12vw)', 2)

# Fix 2: move description panel left
content = content.replace(
    '#photo-description.visible { right: 20px; }',
    '#photo-description.visible { right: 40px; width: 30vw; }'
)

# Fix 3: hide caption immediately on collapse, not animate back
old = "captionBar.classList.remove('visible');"
new = "captionBar.classList.remove('visible'); captionBar.style.opacity = '0';"
content = content.replace(old, new, 1)

open('index.html', 'w', encoding='utf-8').write(content)
print('Done')
