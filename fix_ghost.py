content = open('index.html', encoding='utf-8').read()
content = content.replace(
    'ghost = document.createElement(\'img\');',
    'ghost = document.createElement(\'img\'); window.ghost = ghost;',
    1
)
open('index.html', 'w', encoding='utf-8').write(content)
print('Done')
