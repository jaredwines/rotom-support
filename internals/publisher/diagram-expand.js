(() => {
  function addControls() {
    document.querySelectorAll('div.mermaid').forEach((diagram) => {
      if (diagram.dataset.expandControl) return;
      diagram.dataset.expandControl = 'true';
      const button = document.createElement('button');
      button.type = 'button';
      button.className = 'diagram-expand';
      button.textContent = 'Expand diagram';
      button.addEventListener('click', () => {
        const placeholder = document.createComment('diagram position');
        diagram.before(placeholder);
        const dialog = document.createElement('dialog');
        dialog.className = 'diagram-dialog';
        dialog.setAttribute('aria-label', 'Expanded diagram');
        const close = document.createElement('button');
        close.type = 'button';
        close.textContent = 'Close';
        close.className = 'diagram-close';
        const view = document.createElement('div');
        view.className = 'diagram-view';
        view.append(diagram);
        dialog.append(close, view);
        document.body.append(dialog);
        close.addEventListener('click', () => dialog.close());
        dialog.addEventListener('close', () => {
          placeholder.replaceWith(diagram);
          dialog.remove();
          button.focus();
        });
        dialog.showModal();
      });
      diagram.before(button);
    });
  }
  function start() {
    addControls();
    new MutationObserver(addControls).observe(document.body, { childList: true, subtree: true });
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', start);
  else start();
})();
