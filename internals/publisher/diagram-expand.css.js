.diagram-expand, .diagram-close {
  background: var(--md-primary-fg-color);
  border: 0;
  border-radius: .25rem;
  color: var(--md-primary-bg-color);
  cursor: pointer;
  font: inherit;
  padding: .45rem .8rem;
}
.diagram-expand { display: block; margin: 1rem 0 .35rem auto; }
.diagram-dialog {
  background: var(--md-default-bg-color);
  border: 1px solid var(--md-default-fg-color--lightest);
  border-radius: .5rem;
  color: var(--md-default-fg-color);
  height: 92vh;
  max-height: 92vh;
  max-width: 96vw;
  padding: 1rem;
  width: 96vw;
}
.diagram-dialog::backdrop { background: rgba(0, 0, 0, .75); }
.diagram-close { display: block; margin-left: auto; }
.diagram-view { height: calc(100% - 3rem); overflow: auto; text-align: center; }
.diagram-view svg { height: auto; max-width: none !important; min-width: 100%; width: max(100%, 1000px); }
.diagram-expand:focus-visible, .diagram-close:focus-visible { outline: 3px solid var(--md-accent-fg-color); outline-offset: 3px; }
