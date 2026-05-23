with open('index.html', 'r') as f:
    lines = f.readlines()

lines_to_delete = set()

i = 0
while i < len(lines):
    line = lines[i]
    if any(selector in line for selector in ['.gallery-page', '.photo-collage', '.photo-item']):
        if '{' in line:
            lines_to_delete.add(i)
            brace_count = line.count('{') - line.count('}')
            j = i + 1
            while j < len(lines) and brace_count > 0:
                lines_to_delete.add(j)
                brace_count += lines[j].count('{') - lines[j].count('}')
                j += 1
    i += 1

new_lines = [line for i, line in enumerate(lines) if i not in lines_to_delete]

style_close_idx = None
for i, line in enumerate(new_lines):
    if '</style>' in line:
        style_close_idx = i
        break

if style_close_idx:
    new_rules = """
        /* Gallery Layout - Fresh Rules */
        .gallery-page {
            height: 100vh;
            padding: 24px 80px 16px;
            display: flex;
            flex-direction: column;
            overflow: hidden;
        }

        .photo-collage {
            flex: 1;
            columns: 3 !important;
            column-gap: 10px;
            overflow: hidden;
        }

        .photo-item {
            break-inside: avoid;
            margin-bottom: 10px;
            overflow: hidden;
        }

        .photo-item img {
            width: 100%;
            display: block;
            object-fit: cover;
            filter: sepia(30%) contrast(95%) brightness(97%);
        }

        .photo-item:nth-child(1) img { height: 195px !important; }
        .photo-item:nth-child(2) img { height: 260px !important; }
        .photo-item:nth-child(3) img { height: 175px !important; }
        .photo-item:nth-child(4) img { height: 220px !important; }
        .photo-item:nth-child(5) img { height: 150px !important; }

        .right-heavy .photo-item:nth-child(1) img { height: 155px !important; }
        .right-heavy .photo-item:nth-child(2) img { height: 175px !important; }
        .right-heavy .photo-item:nth-child(3) img { height: 265px !important; }
        .right-heavy .photo-item:nth-child(4) img { height: 155px !important; }
        .right-heavy .photo-item:nth-child(5) img { height: 220px !important; }

        /* Only switch to 2 columns on genuinely small screens */
        @media (max-width: 600px) {
            .photo-collage { columns: 2 !important; }
            .photo-item img { height: 130px !important; }
        }
"""
    new_lines.insert(style_close_idx, new_rules)

with open('index.html', 'w') as f:
    f.writelines(new_lines)

print(f"Deleted {len(lines_to_delete)} lines and added new rules")
