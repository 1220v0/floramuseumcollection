content = open('index.html', encoding='utf-8').read()
old = '''                img.addEventListener('click', function(e) {
                    e.stopPropagation();
                    if (ghost) return;'''
new = '''                img.addEventListener('click', function(e) {
                    if (ghost) {
                        if (descOpen) { hideDesc(); } else { showDesc(); }
                        return;
                    }'''
content = content.replace(old, new, 1)
open('index.html', 'w', encoding='utf-8').write(content)
print('Done')
