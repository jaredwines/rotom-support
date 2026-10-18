(() => {
  function addControls() {
    document.querySelectorAll('pre.mermaid').forEach((diagram) => {
      if (diagram.dataset.expandControl) return;
      diagram.dataset.expandControl = 'true';
      const button = document.createElement('button');
      button.type = 'button';
      button.className = 'diagram-expand';
      button.textContent = 'Expand diagram';
      button.addEventListener('click', () => {
        const svg = diagram.querySelector('svg');
        if (!svg) return;
        const dialog = document.createElement('dialog');
        dialog.className = 'diagram-dialog';
        dialog.setAttribute('aria-label', 'Expanded diagram');
        const close = document.createElement('button');
        close.type = 'button';
        close.textContent = 'Close';
        close.className = 'diagram-close';
        const view = document.createElement('div');
        view.className = 'diagram-view';
        const copy = svg.cloneNode(true);
        copy.removeAttribute('id');
        view.append(copy);
        dialog.append(close, view);
        document.body.append(dialog);
        close.addEventListener('click', () => dialog.close());
        dialog.addEventListener('close', () => { dialog.remove(); button.focus(); });
        dialog.showModal();
      });
      diagram.before(button);
    });
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', addControls);
  else addControls();
})();
