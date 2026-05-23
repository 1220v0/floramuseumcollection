content = open('index.html', encoding='utf-8').read()
old = "            window.hideDesc = function hideDesc() {\n                if (!descPanel) return;\n                if (ghost && ghost._origTransform) {\n                    ghost.style.transform = ghost._origTransform;\n                    ghost._origTransform = null;\n                    ghost._shift = null;\n                }"
new = "            window.hideDesc = function hideDesc() {\n                var dp = document.getElementById('photo-description');\n                if (!dp) return;\n                var g = window.ghost || document.querySelector('.photo-spotlight');\n                if (g && g._origTransform) {\n                    g.style.transform = g._origTransform;\n                    g._origTransform = null;\n                    g._shift = null;\n                }\n                dp.style.opacity = '0';\n                window.descOpen = false;\n                var cap = document.querySelector('.photo-caption-bar');\n                if (cap) cap.style.opacity = '1';\n                return;"
content = content.replace(old, new, 1)
open('index.html', 'w', encoding='utf-8').write(content)
print('Done')
