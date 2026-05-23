content = open('index.html', encoding='utf-8').read()
old = "                        if (window.descOpen) {\n                            if (g._shift) { g.style.transform = g.style.transform.replace(' translateX(-' + g._shift + 'px)', ''); g._shift = null; }\n                            d.style.opacity = '0';\n                            if (cap) cap.style.opacity = '1';\n                            window.descOpen = false;\n                        } else {"
new = "                        if (window.descOpen) {\n                            window.hideDesc();\n                            return;\n                        } else {"
content = content.replace(old, new, 1)
open('index.html', 'w', encoding='utf-8').write(content)
print('Done')
