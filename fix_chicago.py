content = open('index.html', encoding='utf-8').read()

content = content.replace(
    'data-title="Windy City" data-artist="Jeff Koons" data-year="2024" data-description=""',
    'data-title="The Red Armchair" data-artist="Pablo Picasso" data-year="1931" data-description="Painted in preparation for an exhibition at the Galeries Georges Petit in Paris, this is the first in a large series of portraits of Marie-Th\u00e9r\u00e8se Walter, Picasso\'s secret mistress at the time. He mixed industrial Ripolin house paint with oil to produce a wide range of surface effects. The Cubist device of showing both frontal and profile views simultaneously reflects the double life he and Walter were discreetly leading."'
)

content = content.replace(
    'data-title="Urban Grid" data-artist="Robert Rauschenberg" data-year="2024" data-description=""',
    'data-title="P.5. Outside-Inside" data-artist="Serge Chermayeff" data-year="1949" data-description="One of five prints from a portfolio by the British-American architect and designer, produced during his tenure as director of Chicago\'s Institute of Design. The overlapping and nested rectangles explore the Bauhaus tension between exterior structure and interior space, a key preoccupation of his architectural thinking."'
)

content = content.replace(
    'data-title="Skyline" data-artist="Gordon Matta-Clark" data-year="2024" data-description=""',
    'data-title="Tall Figure" data-artist="Alberto Giacometti" data-year="1947" data-description="After first producing work associated with Surrealism, Giacometti began making his distinctive elongated, skeletal bronze sculptures in Paris in the late 1940s. His works struck a powerful chord with the Existentialist writer Jean-Paul Sartre, who saw the isolated figures as a visualization of his own ideas about the loneliness and ultimate absurdity of the human condition after World War II."'
)

content = content.replace(
    'data-title="Reflections" data-artist="Ed Paschke" data-year="2024" data-description=""',
    'data-title="Untitled (Match-Woman I)" data-artist="Francis Picabia" data-year="1920" data-description="The tipped matchsticks convey with precision the prinked and permed appearance of a fashionable woman of the time, reflecting Picabia\'s simultaneous movement in the worlds of Parisian high society and Dada. The work relates most closely to a group of collages from roughly 1923 to 1926. Part of the Lindy and Edwin Bergman Collection at the Art Institute of Chicago."'
)

open('index.html', 'w', encoding='utf-8').write(content)
print('Done')
