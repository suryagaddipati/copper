const { TextEncoder, TextDecoder } = require('util');

global.TextEncoder = TextEncoder;
global.TextDecoder = TextDecoder;

global.Worker = class {
  constructor(stringUrl) {
    this.url = stringUrl;
    this.onmessage = () => {};
    this.onmessageerror = () => {};
    this.onerror = () => {};
  }

  postMessage(msg) {
    this.onmessage(msg);
  }

  addEventListener(type, listener) {
    if (type === 'message') {
      this.onmessage = listener;
    }
  }

  removeEventListener(type, listener) {
    if (type === 'message') {
      this.onmessage = () => {};
    }
  }

  terminate() {
    // Do nothing
  }
};