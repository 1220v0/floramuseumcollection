content = open('index.html', encoding='utf-8').read()
old = """                            var panelW = Math.min(window.innerWidth * 0.22, 300);
                            var shift = (panelW + 16) / 2;
                            g.style.transform = g.style.transform + ' translateX(-' + shift + 'px)';
                            g._shift = shift;"""
new = """                            var panelW = Math.min(window.innerWidth * 0.22, 300);
                            var gap = 20;
                            var totalW = g.offsetWidth * 0.75 + gap + panelW;
                            var startX = (window.innerWidth - totalW) / 2;
                            var currentScale = parseFloat((g.style.transform.match(/scale\\(([^)]+)\\)/) || [0,'1'])[1]);
                            var newScale = currentScale * 0.75;
                            g._origTransform = g.style.transform;
                            g._origScale = currentScale;
                            var newTx = startX - parseFloat((g.style.transform.match(/translateX\\(([^)]+)px\\)/) || [0,0])[1]) + g.offsetWidth * 0.75 / 2 - g.offsetWidth / 2;
                            g.style.transform = g.style.transform.replace(/scale\\([^)]+\\)/, 'scale(' + newScale + ')').replace(/translateX\\([^)]+px\\)/, 'translateX(' + (parseFloat((g.style.transform.match(/translateX\\(([^)]+)px\\)/) || [0,0])[1]) - (panelW + gap) / 2) + 'px)');
                            g._shift = (panelW + gap) / 2;"""
content = content.replace(old, new, 1)
open('index.html', 'w', encoding='utf-8').write(content)
print('Done')
