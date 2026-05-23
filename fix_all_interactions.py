import re

content = open('index.html', encoding='utf-8').read()

# Remove any extra description script tags appended before </body>
content = re.sub(r'\n<script>\n\(function\(\).*?\}\)\(\);\n</script>\n</body>', '\n</body>', content, flags=re.DOTALL)
content = re.sub(r'<script>\(function\(\)\{var d=document\.getElementById\("photo-description"\).*?\}\)\(\);</script>', '', content, flags=re.DOTALL)

# Find and replace the entire photo interaction block
old_pattern = r'(// Photo spotlight interaction.*?)(// Click hint logic)'
new_interaction = '''// Photo spotlight interaction
            (function() {
                var ghost = null;
                var activeImg = null;
                var justOpened = false;
                var descOpen = false;
                var overlay = document.getElementById('scene-overlay');
                var captionBar = document.querySelector('.photo-caption-bar');
                var descPanel = document.getElementById('photo-description');

                function collapse() {
                    if (!ghost) return;
                    captionBar.classList.remove('visible');
                    captionBar.style.opacity = '0';
                    if (descOpen) {
                        descPanel.classList.remove('visible');
                        descPanel.style.left = '';
                        descOpen = false;
                    }
                    ghost.style.transform = ghost.style.transform
                        .replace(/ translateX\(-[0-9.]+px\)/, '')
                        .replace(/translateX\([^)]+\) translateY\([^)]+\) scale\([^)]+\)/, function(m) { return m; });
                    ghost.style.transform = 'translateX(0px) translateY(0px) scale(1)';
                    overlay.style.opacity = '0';
                    overlay.style.pointerEvents = 'none';
                    ghost.addEventListener('transitionend', function() {
                        if (ghost) { ghost.remove(); ghost = null; }
                        if (activeImg) {
                            activeImg.style.objectFit = '';
                            activeImg.style.height = '';
                            activeImg = null;
                        }
                    }, { once: true });
                }

                function showDesc() {
                    if (!descPanel || !activeImg) return;
                    descPanel.querySelector('.desc-title').textContent = activeImg.dataset.title || '';
                    descPanel.querySelector('.desc-meta').textContent = (activeImg.dataset.artist || '') + (activeImg.dataset.year ? ' · ' + activeImg.dataset.year : '');
                    descPanel.querySelector('.desc-body').textContent = activeImg.dataset.description || '';
                    var panelW = Math.min(window.innerWidth * 0.28, 360);
                    var gap = 28;
                    var shift = (panelW + gap) / 2;
                    ghost.style.transform = ghost.style.transform + ' translateX(-' + shift + 'px)';
                    ghost._shift = shift;
                    var gr = ghost.getBoundingClientRect();
                    descPanel.style.cssText = 'position:fixed; top:50%; left:' + (gr.right + gap) + 'px; width:' + panelW + 'px; transform:translateY(-50%); padding:40px 32px; color:white; z-index:10001; transition:opacity 300ms ease;';
                    descPanel.style.opacity = '1';
                    captionBar.style.opacity = '0';
                    descOpen = true;
                }

                function hideDesc() {
                    if (!descPanel) return;
                    if (ghost && ghost._shift) {
                        ghost.style.transform = ghost.style.transform.replace(' translateX(-' + ghost._shift + 'px)', '');
                        ghost._shift = null;
                    }
                    descPanel.style.opacity = '0';
                    descOpen = false;
                    captionBar.style.opacity = '1';
                }

                document.querySelectorAll('.photo-item img').forEach(function(img) {
                    img.addEventListener('click', function(e) {
                        e.stopPropagation();
                        if (ghost) return;
                        var r = img.getBoundingClientRect();
                        var vw = window.innerWidth;
                        var vh = window.innerHeight;
                        var maxW = vw * 0.85;
                        var maxH = vh * 0.70;
                        var scaleX = maxW / r.width;
                        var scaleY = maxH / r.height;
                        var scale = Math.min(scaleX, scaleY);
                        var ghostCenterY = vh * 0.45;
                        var tx = (vw/2) - (r.left + r.width/2);
                        var ty = ghostCenterY - (r.top + r.height/2);
                        ghost = document.createElement('img');
                        ghost.src = img.src;
                        ghost.className = 'photo-spotlight';
                        ghost.style.cssText = 'position:fixed; left:' + r.left + 'px; top:' + r.top + 'px; width:' + r.width + 'px; height:' + r.height + 'px; object-fit:cover; z-index:9999; cursor:pointer; transition:transform 380ms cubic-bezier(0.34,1.0,0.64,1);';
                        document.body.appendChild(ghost);
                        img.style.objectFit = 'cover';
                        img.style.height = r.height + 'px';
                        overlay.style.opacity = '1';
                        overlay.style.pointerEvents = 'auto';
                        var finalH = r.height * scale;
                        var title = img.dataset.title || '';
                        var artist = img.dataset.artist || '';
                        var year = img.dataset.year || '';
                        captionBar.textContent = title + (artist ? ' ｜ ' + artist : '') + (year ? ' ｜ ' + year : '');
                        captionBar.style.top = (ghostCenterY + (finalH/2) + 16) + 'px';
                        captionBar.style.opacity = '1';
                        captionBar.classList.add('visible');
                        activeImg = img;
                        justOpened = true;
                        requestAnimationFrame(function() {
                            ghost.style.transform = 'translateX(' + tx + 'px) translateY(' + ty + 'px) scale(' + scale + ')';
                        });
                    });
                });

                document.addEventListener('click', function(e) {
                    if (!ghost) return;
                    if (justOpened) { justOpened = false; return; }
                    var gr = ghost.getBoundingClientRect();
                    var insideGhost = e.clientX>=gr.left && e.clientX<=gr.right && e.clientY>=gr.top && e.clientY<=gr.bottom;
                    var pr = descPanel ? descPanel.getBoundingClientRect() : null;
                    var insidePanel = pr && descOpen && e.clientX>=pr.left && e.clientX<=pr.right && e.clientY>=pr.top && e.clientY<=pr.bottom;
                    if (insideGhost || insidePanel) {
                        if (descOpen) { hideDesc(); } else { showDesc(); }
                    } else {
                        if (descOpen) { descPanel.style.opacity='0'; descOpen=false; }
                        collapse();
                    }
                });
            })();

            // Click hint logic'''

content = re.sub(old_pattern, new_interaction, content, flags=re.DOTALL)
open('index.html', 'w', encoding='utf-8').write(content)
print('Done')
