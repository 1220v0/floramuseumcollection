lines = open('index.html', encoding='utf-8').readlines()
start = None
end = None
for i, line in enumerate(lines):
    if 'const overlay = document.createElement' in line and start is None:
        start = i
    if '// Click hint logic' in line and start is not None:
        end = i
        break

new_code = open('new_interaction.js', encoding='utf-8').read()

if start is not None and end is not None:
    lines = lines[:start] + [new_code] + lines[end:]
    open('index.html', 'w', encoding='utf-8').writelines(lines)
    print('Done - replaced lines', start, 'to', end)
else:
    print('ERROR start:', start, 'end:', end)
