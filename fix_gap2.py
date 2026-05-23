content = open('index.html', encoding='utf-8').read()
old = "var gr2 = g.getBoundingClientRect(); d.style.cssText = 'position:fixed; top:50%; left:' + (gr2.right + 8) + 'px;"
new = "var gr2 = g.getBoundingClientRect(); d.style.cssText = 'position:fixed; top:50%; left:' + (gr2.right + 2) + 'px;"
content = content.replace(old, new, 1)
open('index.html', 'w', encoding='utf-8').write(content)
print('Done')
