content = open('index.html', encoding='utf-8').read()
old = "                            var panelW = Math.min(window.innerWidth * 0.28, 360);\n                            var shift = (panelW + 28) / 2;"
new = "                            var panelW = Math.min(window.innerWidth * 0.22, 300);\n                            var shift = (panelW + 16) / 2;"
content = content.replace(old, new, 1)
old2 = "d.style.cssText = 'position:fixed; top:50%; right:40px; width:' + panelW + 'px; transform:translateY(-50%); padding:40px 32px; color:white; z-index:10001; opacity:1; transition:opacity 300ms ease;';"
new2 = "d.style.cssText = 'position:fixed; top:50%; right:24px; width:' + panelW + 'px; transform:translateY(-50%); padding:32px 24px; color:white; z-index:10001; opacity:1; transition:opacity 300ms ease;';"
content = content.replace(old2, new2, 1)
open('index.html', 'w', encoding='utf-8').write(content)
print('Done')
