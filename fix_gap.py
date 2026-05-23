content = open('index.html', encoding='utf-8').read()
old = "                            var panelW = Math.min(window.innerWidth * 0.22, 300);\n                            var shift = (panelW + 16) / 2;"
new = "                            var panelW = Math.min(window.innerWidth * 0.20, 260);\n                            var shift = (panelW + 8) / 2;"
content = content.replace(old, new, 1)
old2 = "d.style.cssText = 'position:fixed; top:50%; right:24px; width:' + panelW + 'px; transform:translateY(-50%); padding:32px 24px; color:white; z-index:10001; opacity:1; transition:opacity 300ms ease;';"
new2 = "var gr2 = g.getBoundingClientRect(); d.style.cssText = 'position:fixed; top:50%; left:' + (gr2.right + 8) + 'px; width:' + panelW + 'px; transform:translateY(-50%); padding:24px 20px; color:white; z-index:10001; opacity:1; transition:opacity 300ms ease;';"
content = content.replace(old2, new2, 1)
open('index.html', 'w', encoding='utf-8').write(content)
print('Done')
