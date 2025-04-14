class SimpleEditor {
    constructor(selector) {
        this.editor = document.querySelector(selector);
        if (this.editor) {
            this.setupToolbar();
            this.setupEventListeners();
        }
    }

    setupToolbar() {
        const toolbar = document.createElement('div');
        toolbar.className = 'editor-toolbar';
        toolbar.innerHTML = `
            <button type="button" data-command="bold">Bold</button>
            <button type="button" data-command="italic">Italic</button>
            <button type="button" data-command="underline">Underline</button>
            <button type="button" data-command="createLink">Link</button>
            <button type="button" data-command="insertImage">Image</button>
        `;
        this.editor.parentNode.insertBefore(toolbar, this.editor);
    }

    setupEventListeners() {
        document.querySelectorAll('.editor-toolbar button').forEach(button => {
            button.addEventListener('click', () => {
                const command = button.dataset.command;
                if (command === 'createLink') {
                    const url = prompt('Enter URL:');
                    if (url) document.execCommand(command, false, url);
                } else if (command === 'insertImage') {
                    const url = prompt('Enter image URL:');
                    if (url) document.execCommand(command, false, url);
                } else {
                    document.execCommand(command, false, null);
                }
            });
        });
    }
}