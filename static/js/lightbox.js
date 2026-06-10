document.addEventListener('DOMContentLoaded', function () {
  // Inject modal into DOM
  const modal = document.createElement('div');
  modal.id = 'lightbox-modal';
  modal.setAttribute('role', 'dialog');
  modal.setAttribute('aria-modal', 'true');
  modal.setAttribute('aria-label', 'Image viewer');
  modal.innerHTML =
    '<button id="lightbox-close" aria-label="Close">\u00d7</button>' +
    '<img id="lightbox-img" src="" alt="">' +
    '<p id="lightbox-caption"></p>';
  document.body.appendChild(modal);

  const lbImg     = document.getElementById('lightbox-img');
  const lbCaption = document.getElementById('lightbox-caption');
  const lbClose   = document.getElementById('lightbox-close');

  function openLightbox(src, alt, caption) {
    lbImg.src = src;
    lbImg.alt = alt || '';
    lbCaption.textContent = caption || '';
    lbCaption.style.display = caption ? '' : 'none';
    modal.classList.add('active');
    document.body.style.overflow = 'hidden';
    lbClose.focus();
  }

  function closeLightbox() {
    modal.classList.remove('active');
    document.body.style.overflow = '';
    setTimeout(function () { lbImg.src = ''; }, 200);
  }

  // Event delegation — works for dynamically-added figures too
  document.addEventListener('click', function (e) {
    const trigger = e.target.closest('.lightbox-trigger');
    if (trigger) {
      e.preventDefault();
      const triggerImg = trigger.querySelector('img');
      openLightbox(
        trigger.href,
        triggerImg ? triggerImg.alt : '',
        trigger.dataset.caption || ''
      );
    }
  });

  lbClose.addEventListener('click', closeLightbox);

  // Click backdrop to close
  modal.addEventListener('click', function (e) {
    if (e.target === modal) closeLightbox();
  });

  // Escape key to close
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && modal.classList.contains('active')) closeLightbox();
  });
});
