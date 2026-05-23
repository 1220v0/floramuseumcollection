content = open('index.html', encoding='utf-8').read()

# Remove active color change, keep only diamond
content = content.replace(
    '.nav-item.active .nav-diamond { opacity: 1; } .nav-item.active { opacity: 1; color: #A07830; }',
    '.nav-item.active .nav-diamond { opacity: 1; }'
)

# Fix hover - only show diamond at 0.5, no text change
content = content.replace(
    '.nav-item:hover { opacity: 1; } .nav-item:hover .nav-diamond { opacity: 0.5; }',
    '.nav-item:hover .nav-diamond { opacity: 0.5; }'
)

open('index.html', 'w', encoding='utf-8').write(content)
print('Done')
