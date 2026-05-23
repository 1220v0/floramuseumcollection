content = open('index.html', encoding='utf-8').read()
old = '''window.showDesc = function showDesc() {
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
                descPanel.style.cssText = 'position:fixed; top:50%; left:' + (gr.right + gap) + 'px; width:' + panelW + 'px; transform:translateY(-50%); padding:40px 32px; color:white; z-index:10001; opacity:1; transition:opacity 300ms ease;';
                captionBar.style.opacity = '0';
                descOpen = true;
            }'''
new = '''window.showDesc = function showDesc() {
                if (!descPanel || !activeImg) return;
                descPanel.querySelector('.desc-title').textContent = activeImg.dataset.title || '';
                descPanel.querySelector('.desc-meta').textContent = (activeImg.dataset.artist || '') + (activeImg.dataset.year ? ' · ' + activeImg.dataset.year : '');
                descPanel.querySelector('.desc-body').textContent = activeImg.dataset.description || '';
                var panelW = Math.min(window.innerWidth * 0.28, 360);
                var gap = 28;
                var shift = (panelW + gap) / 2;
                ghost.style.transform = ghost.style.transform + ' translateX(-' + shift + 'px)';
                ghost._shift = shift;
                descPanel.style.cssText = 'position:fixed; top:50%; right:40px; width:' + panelW + 'px; transform:translateY(-50%); padding:40px 32px; color:white; z-index:10001; opacity:1; transition:opacity 300ms ease;';
                captionBar.style.opacity = '0';
                descOpen = true; window.descOpen = true;
            }'''
content = content.replace(old, new, 1)
open('index.html', 'w', encoding='utf-8').write(content)
print('Done')
