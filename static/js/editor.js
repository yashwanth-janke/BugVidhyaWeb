let editor = ace.edit("editor");
editor.setShowPrintMargin(false);
let langTools = ace.require("ace/ext/language_tools");
setEditorSettings("ace/theme/cobalt", "ace/mode/python", true);
function setEditorSettings(theme, mode, enableAutoCompletion) {
  editor.setTheme(theme);
  editor.session.setMode(mode);
  if (enableAutoCompletion) {
    editor.setOptions({
      enableBasicAutocompletion: true,
      enableSnippets: true,
      enableLiveAutocompletion: true,
    });
  } else {
    editor.setOptions({
      enableBasicAutocompletion: false,
      enableSnippets: false,
      enableLiveAutocompletion: false,
    });
  }
}

function py() {
  setEditorSettings("ace/theme/cobalt", "ace/mode/python", true);
}

function jv() {
  setEditorSettings("ace/theme/cobalt", "ace/mode/java", true);
}

function kt() {
  setEditorSettings("ace/theme/cobalt", "ace/mode/kotlin", true);
}

function js() {
  setEditorSettings("ace/theme/cobalt", "ace/mode/javascript", true);
}

function sendCode() {
        var editor = ace.edit("editor");
        var pythonCode = editor.getValue();
        fetch('/run_code', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ code: pythonCode }),
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById("answer").innerText = data.output;
        })
        .catch(error => console.error('Error:', error));
    }
