content = open('index.html', encoding='utf-8').read()
old = "                            g._origTransform = g.style.transform;\n                            g.style.transform = g.style.transform.replace(/translateX\\([^)]+px\\)/, 'translateX(' + (currentLeft - shift) + 'px)');"
new = "                            if (!g._origTransform) g._origTransform = g.style.transform;\n                            g.style.transform = g.style.transform.replace(/translateX\\([^)]+px\\)/, 'translateX(' + (currentLeft - shift) + 'px)');"
content = content.replace(old, new, 1)
open('index.html', 'w', encoding='utf-8').write(content)
print('Done')
