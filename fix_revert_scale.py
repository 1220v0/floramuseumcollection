content = open('index.html', encoding='utf-8').read()
import re
old = r"                            var panelW = Math\.min\(window\.innerWidth \* 0\.22, 300\);.*?g\._shift = \(panelW \+ gap\) / 2;"
new = """                            var panelW = Math.min(window.innerWidth * 0.22, 300);
                            var shift = (panelW + 16) / 2;
                            g.style.transform = g.style.transform + ' translateX(-' + shift + 'px)';
                            g._shift = shift;"""
content = re.sub(old, new, content, flags=re.DOTALL)
open('index.html', 'w', encoding='utf-8').write(content)
print('Done')
