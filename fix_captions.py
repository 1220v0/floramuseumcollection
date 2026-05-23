content = open('index.html', encoding='utf-8').read()

replacements = [
    ('[PLACEHOLDER: personal notes and feelings] Walking through the spacious halls of MAP',
     'Standing beside the Oriental Pearl Tower, I spent four hours walking through four of the five floors. Every exhibition featured newly emerging works by contemporary independent artists, all executed to a high standard. A place I will return to on every visit to Shanghai.'),
    ("[PLACEHOLDER: personal notes and feelings] Tate Modern's Turbine Hall",
     'The first museum I walked into upon arriving in London, carrying my earliest memories of overseas university life. Before this I knew almost nothing about how modern art expressed itself. Tate Modern gave me a vivid and memorable introduction to it.'),
    ('[PLACEHOLDER: personal notes and feelings] The Art Institute of Chicago houses',
     'A museum I passed through in a rush. My impression of Chicago was so warm that my affection for the city extended naturally to this place. It remains a fond memory, and I will find the time to explore it properly one day, I know I will.'),
    ("[PLACEHOLDER: personal notes and feelings] The Musée d'Orsay transformed",
     "I consider myself fortunate to have discovered the Musée d'Orsay, and even more so to have spent an entire afternoon there during the brief four days in Paris. Intimate and refined yet deeply immersive, I would personally rank it even slightly above the Louvre."),
    ("[PLACEHOLDER: personal notes and feelings] Walking through the medieval streets of Barcelona",
     'It was still cold in Barcelona in February, and I spent a long time searching for the entrance early that morning -- such an experience that left a strong impression. The collection is remarkably rich. My thanks to the generosity of Jaume Sabartés.'),
    ("[PLACEHOLDER: personal notes and feelings] The Van Gogh Museum in Amsterdam",
     "A museum I was determined to finish before catching my flight. The space is compact but the circulation is cleverly designed, the interpretive materials were thorough, and the content was so so rich. Walking through felt like living Van Gogh's entire life, that makes me deeply moved."),
]

for old, new in replacements:
    if old in content:
        content = content.replace(old, new)
        print('Replaced:', old[:40])
    else:
        print('NOT FOUND:', old[:40])

open('index.html', 'w', encoding='utf-8').write(content)
print('Done')
