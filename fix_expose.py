content = open('index.html', encoding='utf-8').read()
content = content.replace(
    'let descOpen = false;',
    'let descOpen = false; window.descOpen = false;'
)
content = content.replace(
    'descOpen = true;',
    'descOpen = true; window.descOpen = true;'
)
content = content.replace(
    'descOpen = false;',
    'descOpen = false; window.descOpen = false;'
)
open('index.html', 'w', encoding='utf-8').write(content)
print('Done')
