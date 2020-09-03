(function () {
    var SCRIPT_URL = window.location.hostname ? '//rum.ngenix.net/js/userscript.js' : '../build/userscript.js';

    function listen(evnt, elem, func) {
        if (elem.addEventListener) { // W3C DOM
            elem.addEventListener(evnt, func, false);
        } else if (elem.attachEvent) { // IE DOM
            elem.attachEvent('on' + evnt, func);
        }
    }

    function hasNecessaryFeatures() {
        var hasJson = typeof window.JSON === 'object';
        var hasXhr = window.XMLHttpRequest !== 'undefined';

        return hasJson && hasXhr;
    }

    function loadScript() {
        window.setTimeout(function () {
            var script = document.createElement('script');
            script.src = SCRIPT_URL + '?_time=' + new Date().getTime();
            document.body.appendChild(script);
        }, 1000);
    }

    if (hasNecessaryFeatures()) {
        if (document.readyState === 'complete') {
            loadScript();
        } else {
            listen('load', window, loadScript);
        }
    }

}());
