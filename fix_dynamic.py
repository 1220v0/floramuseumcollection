content = open('index.html', encoding='utf-8').read()

# Remove the fixed translateX shift from showDescription JS
content = content.replace(
    'if(window.ghost)window.ghost.style.transform+=" translateX(-8vw)";',
    '''if(window.ghost){
    var gr = window.ghost.getBoundingClientRect();
    var panelW = Math.min(window.innerWidth * 0.28, 420);
    var gap = 24;
    var totalW = gr.width + gap + panelW;
    var shift = (window.innerWidth - totalW) / 2 - gr.left + gr.width/2 - gr.width/2;
    var photoShift = -(panelW + gap) / 2;
    window.ghost.style.transform = window.ghost.style.transform + " translateX(" + photoShift + "px)";
    window.ghost._descShift = photoShift;
  }'''
)

# Remove fixed translateX from hideDescription
content = content.replace(
    'if(window.ghost)window.ghost.style.transform=window.ghost.style.transform.replace(" translateX(-8vw)","");',
    '''if(window.ghost && window.ghost._descShift){
    window.ghost.style.transform=window.ghost.style.transform.replace(" translateX("+window.ghost._descShift+"px)","");
    window.ghost._descShift = null;
  }'''
)

open('index.html', 'w', encoding='utf-8').write(content)
print('Done')
