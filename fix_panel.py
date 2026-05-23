content = open('index.html', encoding='utf-8').read()
old = "                if (e.target.closest('#photo-description')) return;"
new = "                if (window.descOpen && e.target.closest('#photo-description')) return;"
content = content.replace(old, new, 1)
open('index.html', 'w', encoding='utf-8').write(content)
print('Done')
