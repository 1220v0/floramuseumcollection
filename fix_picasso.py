content = open('index.html', encoding='utf-8').read()

content = content.replace(
    'data-title="Gaud\u00ed\'s Dream" data-artist="Joan Mir\u00f3" data-year="2024" data-description=""',
    'data-title="La Revue Blanche" data-artist="Henri de Toulouse-Lautrec" data-year="1895" data-description="A lithographic poster depicting Misia Natanson ice-skating at the Palais de Glace in Paris. Printed in four colors on two joined sheets of wove paper, the work is considered one of Lautrec\'s finest individual pieces. Displayed at the Museu Picasso as a primary influence on the young Picasso, who absorbed Lautrec\'s bold graphic language on his first trip to Paris in 1900."'
)

content = content.replace(
    'data-title="Mediterranean" data-artist="Salvador Dal\u00ed" data-year="2024" data-description=""',
    'data-title="Early works from Barcelona (group display)" data-artist="Pablo Picasso" data-year="1895\u20131897" data-description="A cluster of small oil sketches made by Picasso between ages 13 and 16, shortly after his family moved to Barcelona. The seascapes, landscapes, and a bearded man\'s portrait show rapid naturalistic development in the academic tradition. Picasso came to Barcelona in 1895 and the city had a lasting effect on him more than any other place."'
)

content = content.replace(
    'data-title="Picasso\'s Youth" data-artist="Pablo Picasso" data-year="2024" data-description=""',
    'data-title="Las Meninas series" data-artist="Pablo Picasso" data-year="1957" data-description="Between August and December 1957, Picasso embarked on a comprehensive analysis of Vel\u00e1zquez\'s Las Meninas, producing 58 oil paintings. In 1968, he donated the entire series to the Museu Picasso in memory of his lifelong friend Jaume Sabart\u00e9s. The grisaille palette in several works heightens the analytic, almost x-ray quality of Picasso\'s dialogue with Vel\u00e1zquez."'
)

content = content.replace(
    'data-title="Catalan Light" data-artist="Antoni T\u00e0pies" data-year="2024" data-description=""',
    'data-title="The Wait (Margot)" data-artist="Pablo Picasso" data-year="1901" data-description="One of the most visually arresting works in the museum: a young woman in extravagant headdress, face flushed and eyes narrowed in a vacant stare. The free, almost frenzied brushstrokes and expressionistic use of vibrant colour draw from Seurat, Van Gogh, and Toulouse-Lautrec. It was one of the most praised works at Picasso\'s landmark first solo exhibition at the Vollard Gallery, Paris, in June 1901."'
)

open('index.html', 'w', encoding='utf-8').write(content)
print('Done')
