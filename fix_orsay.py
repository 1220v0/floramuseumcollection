content = open('index.html', encoding='utf-8').read()

content = content.replace(
    'data-title="Parisian Light" data-artist="Pierre Bonnard" data-year="2024" data-description=""',
    'data-title="Poppies" data-artist="Claude Monet" data-year="1873" data-description="Painted while Monet lived in Argenteuil after returning from England, this was shown at the very first Impressionist exhibition in 1874. He constructed the field through blobs of paint, including the disproportionately large poppies in the foreground asserting the primacy of visual impression over realistic description. Donated to the French state by \u00c9tienne Moreau-N\u00e9laton in 1906."'
)

content = content.replace(
    'data-title="Orsay Clock" data-artist="\u00c9douard Manet" data-year="2024" data-description=""',
    'data-title="Blue Dancers (Danseuses bleues)" data-artist="Edgar Degas" data-year="c. 1890" data-description="One of the most celebrated works at the Mus\u00e9e d\'Orsay. Degas captures four ballerinas in blue tutus from behind in a moment before or after rehearsal, enveloped by a shimmering background of greens and pinks. Executed in pastel, the work exemplifies his late technique of layering colour to achieve rich, luminous surfaces."'
)

content = content.replace(
    'data-title="Seine Walk" data-artist="Pierre-Auguste Renoir" data-year="2024" data-description=""',
    'data-title="Study of a Figure Outdoors: Woman with a Parasol, Turning Right" data-artist="Claude Monet" data-year="1886" data-description="Painted in the summer of 1886 at Giverny, the model was Suzanne Hosch\u00e9d\u00e9, the stepdaughter of the artist. Monet painted two pendant works of the same figure exploring how a figure could be treated as a series subject just as he had done with landscapes. Gift of Michel Monet, 1927."'
)

content = content.replace(
    'data-title="Modern Study" data-artist="Henri Matisse" data-year="2024" data-description=""',
    'data-title="Dancers Ascending a Staircase" data-artist="Edgar Degas" data-year="c. 1886\u20131890" data-description="Part of Degas\'s series of elongated horizontal tableaux en long. The diagonal line, abrupt cropping, and off-centre viewpoint all reflect his deep interest in Japanese prints and photography. Bequest of Comte Isaac de Camondo, 1911."'
)

content = content.replace(
    'data-title="Blue Period" data-artist="Pablo Picasso" data-year="2024" data-description=""',
    'data-title="Narcissi and Tulips" data-artist="Henri Fantin-Latour" data-year="1862" data-description="Fantin-Latour is best known for his flower paintings and group portraits of Parisian artists and writers. This early still life already shows the meticulously observed, quiet realism that would make him one of the 19th century\'s foremost flower painters. Also from the Donation \u00c9tienne Moreau-N\u00e9laton, 1906."'
)

open('index.html', 'w', encoding='utf-8').write(content)
print('Done')
