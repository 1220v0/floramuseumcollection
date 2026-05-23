content = open('index.html', encoding='utf-8').read()

old = "                if (justOpened) {\n                    justOpened = false;\n                    return;\n                }\n                collapse();"

new = "                if (justOpened) {\n                    justOpened = false;\n                    return;\n                }\n                if (window.descriptionOpen) return;\n                var ghostEl = document.querySelector('.photo-spotlight');\n                if (ghostEl) {\n                    var gr = ghostEl.getBoundingClientRect();\n                    var ins = e.clientX>=gr.left && e.clientX<=gr.right && e.clientY>=gr.top && e.clientY<=gr.bottom;\n                    if (ins) return;\n                }\n                collapse();"

content = content.replace(old, new, 1)
open('index.html', 'w', encoding='utf-8').write(content)
print('Done')
