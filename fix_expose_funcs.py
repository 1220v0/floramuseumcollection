content = open('index.html', encoding='utf-8').read()
content = content.replace(
    'function showDesc() {',
    'window.showDesc = function showDesc() {'
)
content = content.replace(
    'function hideDesc() {',
    'window.hideDesc = function hideDesc() {'
)
content = content.replace(
    "ghost.addEventListener('click', function(e) {\n                        e.stopPropagation();\n                        if (descOpen) { hideDesc(); } else { showDesc(); }\n                    });",
    "ghost.addEventListener('click', function(e) {\n                        e.stopPropagation();\n                        if (window.descOpen) { window.hideDesc(); } else { window.showDesc(); }\n                    });"
)
open('index.html', 'w', encoding='utf-8').write(content)
print('Done')
