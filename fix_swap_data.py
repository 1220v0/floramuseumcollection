content = open('index.html', encoding='utf-8').read()

line2 = 'data-title="Mona Lisa" data-artist="Juan Antonio Alonso del Canto" data-year="1791\u20131800" data-description="Displayed in the special In Focus section of Ages of Splendor at MAP. This pencil-on-paper study was made by a draughtsman working for a Spanish engraving company as a preparatory drawing for a printed reproduction of the painting."'

line3 = 'data-title="Find the Ideal Perspective (alternate perspective)" data-artist="Xu Bing" data-year="2021\u20132022" data-description="This black-ground print shows the character layout of the Gravitational Arena from another vantage point. The Square Word Calligraphy is excerpted from Ludwig Wittgenstein\'s Philosophical Investigations; the gravitational distortion of the text embodies Wittgenstein\'s argument that perspective shapes human cognition."'

content = content.replace(line2, 'TEMP_PLACEHOLDER', 1)
content = content.replace(line3, line2, 1)
content = content.replace('TEMP_PLACEHOLDER', line3, 1)

open('index.html', 'w', encoding='utf-8').write(content)
print('Done')
