content = open('index.html', encoding='utf-8').read()
old = "                    document.body.appendChild(ghost);\n                    window.ghost = ghost;"
new = """                    document.body.appendChild(ghost);
                    window.ghost = ghost;
                    ghost.addEventListener('click', function(e) {
                        e.stopPropagation();
                        if (descOpen) { hideDesc(); } else { showDesc(); }
                    });"""
content = content.replace(old, new, 1)
open('index.html', 'w', encoding='utf-8').write(content)
print('Done')
