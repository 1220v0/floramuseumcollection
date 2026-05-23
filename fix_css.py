content = open('index.html', encoding='utf-8').read()
old = '#photo-description {\n            position: fixed;\n            top: 50%;\n            right: 0;\n            transform: translateY(-50%) translateX(100%);\n            width: 35vw;\n            max-width: 420px;\n            padding: 48px 40px;\n            z-index: 10001;\n            transition: transform 400ms cubic-bezier(0.16, 1, 0.3, 1);\n            background: transparent;\n            color: white;\n        }\n        #photo-description.visible {\n            transform: translateY(-50%) translateX(0);\n        }'
new = '#photo-description { position: fixed; top: 50%; right: -420px; transform: translateY(-50%); width: 35vw; max-width: 420px; padding: 48px 40px; z-index: 10001; transition: right 400ms cubic-bezier(0.16,1,0.3,1); color: white; }\n        #photo-description.visible { right: 20px; }'
content = content.replace(old, new, 1)
open('index.html', 'w', encoding='utf-8').write(content)
print('Done')
