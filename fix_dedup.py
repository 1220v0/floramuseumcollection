content = open('index.html', encoding='utf-8').read()
# Remove duplicate activeImg lines, keep only first occurrence
import re
count = 0
def replacer(m):
    global count
    count += 1
    if count == 1:
        return m.group(0)
    return ''
content = re.sub(r'\n\s+window\.activeImg = img;', replacer, content)
open('index.html', 'w', encoding='utf-8').write(content)
print('Done, remaining:', content.count('window.activeImg = img'))
