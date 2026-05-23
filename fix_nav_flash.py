content = open('index.html', encoding='utf-8').read()
old = "                item.addEventListener('click', function() {\n                    const targetSectionNum = parseInt(this.dataset.section);"
new = "                item.addEventListener('click', function() {\n                    this.style.opacity = '1';\n                    this.style.color = 'white';\n                    var self = this;\n                    setTimeout(function() { self.style.opacity = ''; self.style.color = ''; }, 300);\n                    const targetSectionNum = parseInt(this.dataset.section);"
content = content.replace(old, new, 1)
open('index.html', 'w', encoding='utf-8').write(content)
print('Done')
