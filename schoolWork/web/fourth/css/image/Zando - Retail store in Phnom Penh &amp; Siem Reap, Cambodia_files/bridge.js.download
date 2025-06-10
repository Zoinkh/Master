"use strict";
var exports = { __esModule: true };

Object.defineProperty(exports, "__esModule", {
  value: true,
});
exports["default"] = void 0;

function _classCallCheck(instance, Constructor) {
  if (!(instance instanceof Constructor)) {
    throw new TypeError("Cannot call a class as a function");
  }
}

function _defineProperties(target, props) {
  for (var i = 0; i < props.length; i++) {
    var descriptor = props[i];
    descriptor.enumerable = descriptor.enumerable || false;
    descriptor.configurable = true;
    if ("value" in descriptor) descriptor.writable = true;
    Object.defineProperty(target, descriptor.key, descriptor);
  }
}

function _createClass(Constructor, protoProps, staticProps) {
  if (protoProps) _defineProperties(Constructor.prototype, protoProps);
  if (staticProps) _defineProperties(Constructor, staticProps);
  Object.defineProperty(Constructor, "prototype", { writable: false });
  return Constructor;
}

/**
 * VueJsBridgePlugin
 */
var getDeviceInfo = function getDeviceInfo() {
  var device = {};
  var ua = navigator.userAgent;
  var windows = ua.match(/(Windows Phone);?[\s\/]+([\d.]+)?/);
  var android = ua.match(/(Android);?[\s\/]+([\d.]+)?/);
  var ipad = ua.match(/(iPad).*OS\s([\d_]+)/);
  var ipod = ua.match(/(iPod)(.*OS\s([\d_]+))?/);
  var iphone = !ipad && ua.match(/(iPhone\sOS|iOS)\s([\d_]+)/);
  device.ios = device.android = device.windows = device.iphone = device.ipod = device.ipad = device.androidChrome = false; // Windows

  if (windows) {
    device.os = "windows";
    device.osVersion = windows[2];
    device.windows = true;
  } // Android

  if (android && !windows) {
    device.os = "android";
    device.osVersion = android[2];
    device.android = true;
    device.androidChrome = ua.toLowerCase().indexOf("chrome") >= 0;
  }

  if (ipad || iphone || ipod) {
    device.os = "ios";
    device.ios = true;
  } // iOS

  if (iphone && !ipod) {
    device.osVersion = iphone[2].replace(/_/g, ".");
    device.iphone = true;
  }

  if (ipad) {
    device.osVersion = ipad[2].replace(/_/g, ".");
    device.ipad = true;
  }

  if (ipod) {
    device.osVersion = ipod[3] ? ipod[3].replace(/_/g, ".") : null;
    device.iphone = true;
  } // iOS 8+ changed UA

  if (device.ios && device.osVersion && ua.indexOf("Version/") >= 0) {
    if (device.osVersion.split(".")[0] === "10") {
      device.osVersion = ua.toLowerCase().split("version/")[1].split(" ")[0];
    }
  }

  device.iphonex = device.ios && screen.height === 812 && screen.width === 375; // Webview

  device.webView = (iphone || ipad || ipod) && ua.match(/.*AppleWebKit(?!.*Safari)/i);
  return device;
};

var deviceInfo = getDeviceInfo();

var VueJsBridgePlugin = /*#__PURE__*/ (function () {
  function VueJsBridgePlugin() {
    var options = arguments.length > 0 && arguments[0] !== undefined ? arguments[0] : {};

    _classCallCheck(this, VueJsBridgePlugin);

    this.options = { debug: false, delay: 200 };
  }
  /**
   * Initialize the core bridge plugin
   * @param {function} callback
   * callback Returns an instance of the bridge plugin
   */

  _createClass(VueJsBridgePlugin, [
    {
      key: "init",
      value: function init(callback) {
        if (deviceInfo.android) {
          // The following is the source code of [JsBridge](https://github.com/lzyzsd/JsBridge) -- android
          if (window.WebViewJavascriptBridge) {
            callback(window.WebViewJavascriptBridge);
          } else {
            document.addEventListener(
              "WebViewJavascriptBridgeReady",
              function () {
                callback(window.WebViewJavascriptBridge);
              },
              false
            );
          }
        } else {
          // The following is the source code of [WebViewJavascriptBridge](https://github.com/marcuswestin/WebViewJavascriptBridge) -- ios
          if (window.WebViewJavascriptBridge) {
            return callback(window.WebViewJavascriptBridge);
          }

          if (window.WVJBCallbacks) {
            return window.WVJBCallbacks.push(callback);
          }

          window.WVJBCallbacks = [callback];
          var WVJBIframe = document.createElement("iframe");
          WVJBIframe.style.display = "none";
          WVJBIframe.src = "wvjbscheme://__BRIDGE_LOADED__";
          document.documentElement.appendChild(WVJBIframe);
          setTimeout(function () {
            document.documentElement.removeChild(WVJBIframe);
          }, 0);
        }
      },
      /**
       * Register a method that provides native calls
       * @param {string} name is method name
       * @param {function} fn callback method, two parameters data, callback
       * The first parameter is the data passed by native
       * The second parameter is the callback function callback provided by the native. After the front-end processing is completed, the native can be notified through the callback
       */
    },
    {
      key: "registerHandler",
      value: function registerHandler(name, fn) {
        var _this = this;

        var delay = this.options.delay; // bridge initialization takes time, delay processing registration method

        setTimeout(function () {
          _this.init(function (bridge) {
            bridge.registerHandler(name, function (data, callback) {
              var parseData = typeof data === "string" ? JSON.parse(data) : data;
              fn(parseData, callback);
            });
          });
        }, delay);
      },
      /**
       * The front end calls the native method
       * @param {any} payload
       * The payload parameter is defined by negotiating with native
       * @example
       * {
       *    type: 'handlerName',
       *    data: 'data from front'
       * }
       */
    },
    {
      key: "callHandler",
      value: function callHandler() {
        console.log("callll.....");
        var name = arguments.length > 0 && arguments[0] !== undefined ? arguments[0] : this.options.nativeHandlerName;
        var payload = arguments.length > 1 ? arguments[1] : undefined;
        var debug = this.options.debug;

        var _resolve;

        var _reject; // Generate a promise object, keep resolve, rejectt

        var readyPromise = new Promise(function (resolve, reject) {
          _resolve = resolve;
          _reject = reject;
        });
        debug && console.info("[VueJsBridge] Start calling NativeHandler with payload:", payload);
        this.init(function (bridge) {
          try {
            bridge.callHandler(name, payload, function (response) {
              debug && console.info("[VueJsBridge] Success response:", typeof response === "string" ? JSON.parse(response) : response); // The call succeeds, using the reserved resolve to change the state of the returned promise
              // protect android response with string content

              _resolve(typeof response === "string" ? JSON.parse(response) : response);
            });
          } catch (e) {
            debug && console.info("[VueJsBridge] Failed error:", typeof e === "string" ? JSON.parse(e) : e); // The call is successful, use the retained reject to change the state of the returned promise

            _reject(e);
          }
        });
        return readyPromise;
      },
    },
  ]);

  return VueJsBridgePlugin;
})();

exports["default"] = VueJsBridgePlugin;
