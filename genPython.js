function injectCSS() {
    const styleElement = document.createElement("style");
    const cssCode = `
#popup-textbox {
    display: none;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    background-color: #fff;
    padding: 20px;
    border: 1px solid #000;
    box-shadow: 0 0 10px rgba(0,0,0,0.5);
    z-index: 999;
}
#close-button { 
    color: red;
    position: absolute;
    top: 0%;
    right: 0%
}
#popup-textbox-content { width: 1000px; height: 750px }
`;
    styleElement.appendChild(document.createTextNode(cssCode));
    document.head.appendChild(styleElement);
}

const parser = new DOMParser();
function appendHtml(parentEl, html, appearAtEl = "body") {
    parentEl.appendChild(parser.parseFromString(html, "text/html")[appearAtEl].firstChild);
}

const loadScript = (FILE_URL, async = true, type = "text/javascript") => {
    return new Promise((resolve, reject) => {
        try {
            const scriptEle = document.createElement("script");
            scriptEle.type = type;
            scriptEle.async = async;
            scriptEle.src =FILE_URL;

            scriptEle.addEventListener("load", (ev) => {
                resolve({ status: true });
            });

            scriptEle.addEventListener("error", (ev) => {
                reject({
                    status: false,
                    message: `Failed to load the script ＄{FILE_URL}`
                });
            });

            document.body.appendChild(scriptEle);
        } catch (error) {
            reject(error);
        }
    });
};

function injectElements() {
    appendHtml(document.querySelector(".comfy-menu"), `
        <button id="popup-button" style="margin-top: 10px">Gen Python</button>
    `)
    appendHtml(document.body, `
        <div id="popup-textbox">
            <h3>Node Workflow -> Python Code</h3>
            <button id="close-button">X</button>
            <div id="popup-textbox-content"></div>
        </div>
    `)

    window.editor;
    const popupTextbox = document.querySelector("#popup-textbox");
    document.querySelector("#popup-button").addEventListener("click", async () => {
        window.editor.setValue(
            JSON.stringify((await app.graphToPrompt()).output, null, 4), 
            -1
        )
        popupTextbox.style.display = "block"
    });
    document.querySelector("#close-button").addEventListener("click", () => popupTextbox.style.display = "none");

    loadScript("https://cdn.jsdelivr.net/npm/ace-builds@1.16.0/src-min-noconflict/ace.min.js").then(
        () => {
            window.editor = ace.edit("popup-textbox-content")
            editor.setTheme("ace/theme/dracula");
            editor.session.setMode("ace/mode/python");
        }
    );
}

injectCSS()
injectElements()


