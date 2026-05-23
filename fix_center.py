content = open('index.html', encoding='utf-8').read()
old = "                            var panelW = Math.min(window.innerWidth * 0.20, 260);\n                            var shift = (panelW + 8) / 2;\n                            g.style.transform = g.style.transform + ' translateX(-' + shift + 'px)';\n                            g._shift = shift;\n                            var gr2 = g.getBoundingClientRect(); d.style.cssText = 'position:fixed; top:50%; left:' + (gr2.right + 2) + 'px; width:' + panelW + 'px; transform:translateY(-50%); padding:24px 20px; color:white; z-index:10001; opacity:1; transition:opacity 300ms ease;';"
new = """                            var panelW = Math.min(window.innerWidth * 0.20, 240);
                            var gap = 12;
                            var photoW = g.offsetWidth * parseFloat((g.style.transform.match(/scale\\(([^)]+)\\)/) || [0,'1'])[1]);
                            var totalW = photoW + gap + panelW;
                            var leftStart = (window.innerWidth - totalW) / 2;
                            var currentLeft = parseFloat((g.style.transform.match(/translateX\\(([^)]+)px\\)/) || [0,0])[1]);
                            var photoCenterX = g.getBoundingClientRect().left + g.getBoundingClientRect().width / 2;
                            var targetPhotoCenterX = leftStart + photoW / 2;
                            var shift = photoCenterX - targetPhotoCenterX;
                            g.style.transform = g.style.transform.replace(/translateX\\([^)]+px\\)/, 'translateX(' + (currentLeft - shift) + 'px)');
                            g._shift = shift;
                            d.style.cssText = 'position:fixed; top:50%; left:' + (leftStart + photoW + gap) + 'px; width:' + panelW + 'px; transform:translateY(-50%); padding:24px 20px; color:white; z-index:10001; opacity:1; transition:opacity 300ms ease;';"""
content = content.replace(old, new, 1)
open('index.html', 'w', encoding='utf-8').write(content)
print('Done')
