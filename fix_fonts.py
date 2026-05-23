import base64

# Read the font files
with open('AnticallyRegular-OVox8.ttf', 'rb') as f:
    antically_data = base64.b64encode(f.read()).decode('utf-8')

with open('LoniaLatterCursiveSignature-nAW30.otf', 'rb') as f:
    lonia_data = base64.b64encode(f.read()).decode('utf-8')

# Read the HTML file
with open('index.html', 'r') as f:
    content = f.read()

# Replace the font faces
old_font1 = "@font-face {\n            font-family: 'Antically';\n            src: url('./AnticallyCursiveSignature-nAW30.otf') format('opentype');\n            font-weight: normal;\n            font-style: normal;\n        }"

new_font1 = "@font-face {\n            font-family: 'LoniaLatter';\n            src: url('data:font/opentype;base64," + lonia_data + "') format('opentype');\n            font-weight: normal;\n            font-style: normal;\n        }"

old_font2 = "@font-face {\n            font-family: 'Antically';\n            src: url('./AnticalllyRegular-OVox8.ttf') format('truetype');\n            font-weight: normal;\n            font-style: normal;\n        }"

new_font2 = "@font-face {\n            font-family: 'Antically';\n            src: url('data:font/truetype;base64," + antically_data + "') format('truetype');\n            font-weight: normal;\n            font-style: normal;\n        }"

content = content.replace(old_font1, new_font1)
content = content.replace(old_font2, new_font2)

# Write the updated HTML file
with open('index.html', 'w') as f:
    f.write(content)

print("Fonts embedded successfully!")
