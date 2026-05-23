content = open('index.html', encoding='utf-8').read()
js = """
<script>
(function() {
  var descPanel = document.getElementById('photo-description');
  function showDesc(img) {
    if (!descPanel || !img) return;
    descPanel.querySelector('.desc-title').textContent = img.dataset.title || '';
    descPanel.querySelector('.desc-meta').textContent = (img.dataset.artist || '') + (img.dataset.year ? ' · ' + img.dataset.year : '');
    descPanel.querySelector('.desc-body').textContent = img.dataset.description || '';
    descPanel.classList.add('visible');
    var c = document.querySelector('.photo-caption-bar');
    if (c) c.style.opacity = '0';
    if (window.ghost) window.ghost.style.transform += ' translateX(-20vw)';
    window.descriptionOpen = true;
  }
  function hideDesc() {
    if (!descPanel) return;
    descPanel.classList.remove('visible');
    var c = document.querySelector('.photo-caption-bar');
    if (c) c.style.opacity = '1';
    if (window.ghost) window.ghost.style.transform = window.ghost.style.transform.replace(' translateX(-20vw)','');
    window.descriptionOpen = false;
  }
  document.addEventListener('click', function(e) {
    if (!window.ghost) return;
    var r = window.ghost.getBoundingClientRect();
    var inside = e.clientX>=r.left && e.clientX<=r.right && e.clientY>=r.top && e.clientY<=r.bottom;
    if (inside) { window.descriptionOpen ? hideDesc() : showDesc(window.activeImg); }
    else if (window.descriptionOpen) { hideDesc(); }
  }, true);
})();
</script>
"""
content = content.replace('</body>', js + '</body>', 1)
open('index.html', 'w', encoding='utf-8').write(content)
print('Done')
