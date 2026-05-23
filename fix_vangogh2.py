content = open('index.html', encoding='utf-8').read()

replacements = [
    ('data-title="The Bedroom (De slaapkamer)" data-artist="Vincent van Gogh" data-year="1888" data-description="Van Gogh painted the bedroom of his house in Arles, the Yellow House, which he had just moved into. He wrote to his brother Theo that the painting was meant to convey absolute rest. He made three versions: the first in October 1888, the second after flood damage in 1889, and a third as a gift for his mother. The bold flat colour, tilted perspective, and simplified forms reflect his deep engagement with Japanese printmaking."',
     'data-title="Almond Blossom" data-artist="Vincent van Gogh" data-year="1890" data-description="Painted in Saint-R\u00e9my to celebrate the birth of his nephew, also named Vincent Willem, to his brother Theo. The white blossoms against a vivid blue sky were directly inspired by Japanese woodblock prints, and it remains one of the most beloved works in the Van Gogh Museum\'s permanent collection."'),
    ('data-title="Woman Bathing (Badende vrouw)" data-artist="Edgar Degas" data-year="c. 1887" data-description="A pastel on paper depicting a nude woman from behind, bending to dry herself. Degas used only the towel and the sponge as the only clues that the model is washing. The vertical structure of parallel pastel marks creates a refined, shimmering surface that Van Gogh studied closely."',
     'data-title="Woman Bathing (Badende vrouw)" data-artist="Edgar Degas" data-year="c. 1887" data-description="A pastel on paper depicting a nude woman from behind, bending to dry herself. Degas used only the towel and the sponge as the only clues that the model is washing. The vertical structure of parallel pastel marks creates a refined, shimmering surface that Van Gogh studied closely."'),
    ('data-title="View of a Butcher\'s Shop" data-artist="Vincent van Gogh" data-year="1888" data-description="Painted in Arles, this small oil shows a view through a window frame looking out at a butcher\'s shop on the street below, and a passing woman in a green hat visible through the glass. It demonstrates Van Gogh\'s intense curiosity about the everyday life and street scenes surrounding his Yellow House."',
     'data-title="View of a Butcher\'s Shop" data-artist="Vincent van Gogh" data-year="1888" data-description="Painted in Arles, this small oil shows a view through a window frame looking out at a butcher\'s shop on the street below, and a passing woman in a green hat visible through the glass. It demonstrates Van Gogh\'s intense curiosity about the everyday life and street scenes surrounding his Yellow House."'),
    ('data-title="Self-Portrait with Straw Hat" data-artist="Vincent van Gogh" data-year="1887" data-description="One of the many self-portraits Van Gogh painted during his Paris years (1886\u201388), when he had access to a mirror and used himself as a free model. The straw hat and the impressionistic blue-grey background of small dabs reflect his direct absorption of Impressionist and Pointillist technique after encountering works by Seurat, Signac, and their circle."',
     'data-title="Self-Portrait with Straw Hat" data-artist="Vincent van Gogh" data-year="1887" data-description="One of the many self-portraits Van Gogh painted during his Paris years (1886\u201388), when he had access to a mirror and used himself as a free model. The straw hat and the impressionistic blue-grey background of small dabs reflect his direct absorption of Impressionist and Pointillist technique after encountering works by Seurat, Signac, and their circle."'),
    ('data-title="Almond Blossom" data-artist="Vincent van Gogh" data-year="1890" data-description="Painted in Saint-R\u00e9my to celebrate the birth of his nephew, also named Vincent Willem, to his brother Theo. The white blossoms against a vivid blue sky were directly inspired by Japanese woodblock prints, and it remains one of the most beloved works in the Van Gogh Museum\'s permanent collection."',
     'data-title="The Bedroom (De slaapkamer)" data-artist="Vincent van Gogh" data-year="1888" data-description="Van Gogh painted the bedroom of his house in Arles, the Yellow House, which he had just moved into. He wrote to his brother Theo that the painting was meant to convey absolute rest. He made three versions: the first in October 1888, the second after flood damage in 1889, and a third as a gift for his mother. The bold flat colour, tilted perspective, and simplified forms reflect his deep engagement with Japanese printmaking."'),
]

lines = content.split('\n')
result = []
replacements_done = [False] * len(replacements)
img_count = 0

for line in lines:
    if 'Weixin Image_20260523033431' in line or 'Weixin Image_20260523033432' in line or 'Weixin Image_20260523033433' in line or 'Weixin Image_20260523033434' in line or 'Weixin Image_20260523033435' in line:
        idx = img_count
        if idx < len(replacements):
            old, new = replacements[idx]
            line = line.replace(old, new)
        img_count += 1
    result.append(line)

content = '\n'.join(result)
open('index.html', 'w', encoding='utf-8').write(content)
print('Done, replaced', img_count, 'images')
