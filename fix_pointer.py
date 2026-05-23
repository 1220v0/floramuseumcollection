content = open('index.html', encoding='utf-8').read()
old = "#photo-description { position: fixed; top: 50%; right: -450px; transform: translateY(-50%); width: 35vw; max-width: 420px; padding: 48px 40px; z-index: 10001; transition: right 400ms cubic-bezier(0.16,1,0.3,1); color: white; }"
new = "#photo-description { position: fixed; top: 50%; right: -450px; transform: translateY(-50%); width: 35vw; max-width: 420px; padding: 48px 40px; z-index: 10001; transition: right 400ms cubic-bezier(0.16,1,0.3,1); color: white; pointer-events: none; }\n        #photo-description.visible, #photo-description[style*='opacity: 1'], #photo-description[style*='opacity:1'] { pointer-events: auto; }"
content = content.replace(old, new, 1)
open('index.html', 'w', encoding='utf-8').write(content)
print('Done')
