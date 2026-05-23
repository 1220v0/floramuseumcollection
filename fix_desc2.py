content = open('index.html', encoding='utf-8').read()
old = "window.descriptionOpen = false;"
new = "window.descriptionOpen = false;\n                    window.activeImg = img;"
content = content.replace(old, new, 1)
open('index.html', 'w', encoding='utf-8').write(content)
print('Done')
