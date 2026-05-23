content = open('index.html', encoding='utf-8').read()

js = '<script>(function(){var d=document.getElementById("photo-description");function s(i){if(!d||!i)return;d.querySelector(".desc-title").textContent=i.dataset.title||"";d.querySelector(".desc-meta").textContent=(i.dataset.artist||"")+(i.dataset.year?" · "+i.dataset.year:"");d.querySelector(".desc-body").textContent=i.dataset.description||"";d.classList.add("visible");var c=document.querySelector(".photo-caption-bar");if(c)c.style.opacity="0";if(window.ghost)window.ghost.style.transform+=" translateX(-20vw)";window.descriptionOpen=true;}function h(){if(!d)return;d.classList.remove("visible");var c=document.querySelector(".photo-caption-bar");if(c)c.style.opacity="1";if(window.ghost)window.ghost.style.transform=window.ghost.style.transform.replace(" translateX(-20vw)","");window.descriptionOpen=false;}document.addEventListener("click",function(e){if(!window.ghost)return;var r=window.ghost.getBoundingClientRect();var inside=e.clientX>=r.left&&e.clientX<=r.right&&e.clientY>=r.top&&e.clientY<=r.bottom;if(inside){window.descriptionOpen?h():s(window.activeImg);}else if(window.descriptionOpen){h();}},true);})();</script>'

content = content.replace('</body>', js + '</body>', 1)
open('index.html', 'w', encoding='utf-8').write(content)
print('Done')
