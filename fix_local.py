content = open('index.html', encoding='utf-8').read()
old = "                    if (ghost) {\n                        if (descOpen) { hideDesc(); } else { showDesc(); }\n                        return;\n                    }"
new = "                    if (ghost) {\n                        if (window.descOpen) { window.hideDesc(); } else { window.showDesc(); }\n                        return;\n                    }"
content = content.replace(old, new, 1)
open('index.html', 'w', encoding='utf-8').write(content)
print('Done')
