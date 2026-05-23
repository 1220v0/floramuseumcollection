content = open('index.html', encoding='utf-8').read()

# Save original transform before shifting
old = "                            g.style.transform = g.style.transform.replace(/translateX\\([^)]+px\\)/, 'translateX(' + (currentLeft - shift) + 'px)');\n                            g._shift = shift;"
new = "                            g._origTransform = g.style.transform;\n                            g.style.transform = g.style.transform.replace(/translateX\\([^)]+px\\)/, 'translateX(' + (currentLeft - shift) + 'px)');\n                            g._shift = shift;"
content = content.replace(old, new, 1)

# Fix hideDesc to restore original transform
old2 = "            window.hideDesc = function hideDesc() {\n                if (!descPanel) return;\n                if (ghost && ghost._shift) {\n                    ghost.style.transform = ghost.style.transform.replace(' translateX(-' + ghost._shift + 'px)', '');\n                    ghost._shift = null;\n                }"
new2 = "            window.hideDesc = function hideDesc() {\n                if (!descPanel) return;\n                if (ghost && ghost._origTransform) {\n                    ghost.style.transform = ghost._origTransform;\n                    ghost._origTransform = null;\n                    ghost._shift = null;\n                }"
content = content.replace(old2, new2, 1)

open('index.html', 'w', encoding='utf-8').write(content)
print('Done')
