content = open('index.html', encoding='utf-8').read()
old = "                    this.style.color = 'white';\n                    this.style.transition = 'color 50ms ease';\n                    var self = this;\n                    setTimeout(function() { self.style.color = ''; self.style.transition = ''; }, 250);"
new = "                    this.style.color = '#D4A853';\n                    this.style.transition = 'color 50ms ease';\n                    var self = this;\n                    setTimeout(function() { self.style.color = ''; self.style.transition = ''; }, 300);"
content = content.replace(old, new, 1)
open('index.html', 'w', encoding='utf-8').write(content)
print('Done')
