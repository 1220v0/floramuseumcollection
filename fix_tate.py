content = open('index.html', encoding='utf-8').read()

# Line 898 - first photo (彩色格子 Mondrian)
content = content.replace(
    'data-title="London Fog" data-artist="Chris Ofili" data-year="2024" data-description=""',
    'data-title="Composition B (No.II) with Red" data-artist="Piet Mondrian" data-year="1935" data-description="One of a series composed of straight black lines and areas of primary colour, this work marks the culmination of Mondrian\'s efforts to create a purely spiritual form of modern painting — his style he called Neoplasticism. On close inspection, the rectangles of white are shot through with patches of grey and visible brushstrokes, making the surface more imperfect and alive than it first appears. Part of Tate Modern\'s permanent collection."'
)

# Line 901 - second photo (黑色装置 Beuys)
content = content.replace(
    'data-title="Tate Modern" data-artist="Anish Kapoor" data-year="2024" data-description=""',
    'data-title="Lightning with Stag in its Glare" data-artist="Joseph Beuys" data-year="1958\u20131985" data-description="The only monumental installation Beuys produced in bronze and other metals. The weighty triangular form represents a bolt of lightning, while the dark forms scattered on the floor are primordial animals cast from loam. The arrangement evokes a mythic forest clearing where animals are illuminated by a dramatic lightning strike."'
)

# Line 904 - third photo (黄色装置 Mike Kelley)
content = content.replace(
    'data-title="Thames Flow" data-artist="Rachel Whiteread" data-year="2024" data-description=""',
    'data-title="Hierarchical Figure & The Banana Man Costume" data-artist="Mike Kelley" data-year="1989 / 1981\u201382" data-description="Two works displayed in Mike Kelley: Ghost and Spirit at Tate Modern. The yellow suit is the Banana Man Costume worn by Kelley in his early performance work. The Banana Man was a character Kelley had only heard about second-hand, so he asked friends to recount their fragmented memories — making the performance an investigation into the fallibility of human memory."'
)

# Line 907 - fourth photo (一排照片 Mike Kelley)
content = content.replace(
    'data-title="City Lights" data-artist="David Hockney" data-year="2024" data-description=""',
    'data-title="Ahh...Youth!" data-artist="Mike Kelley" data-year="1991" data-description="A series of eight prints — seven portraits of stuffed animals and one of Kelley himself. These works, made from worn second-hand toys, undermine the first impression of innocent children\'s playthings to evoke thoughts about gender and familial power structures as well as an underlying sense of the sinister. The photographs became widely known as the cover of Sonic Youth\'s 1992 album Dirty."'
)

open('index.html', 'w', encoding='utf-8').write(content)
print('Done')
