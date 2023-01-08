### 一、WebSocket原理
1. 定义：WebSocket可以实现客户端和服务端的永久双向连接，相比于http协议，WebSocket可以实现服务端主动向客户端推送信息。http必须定期轮询，浪费资源。

<img decoding="async" src="../../images/websorck.png" >

> WebSocket提供client和server的处理模块

2. 优势

```shell
# WebSocket 没有跨源限制
# 浏览器对 WebSocket 支持很好
# 可以发送/接收字符串和二进制数据
```


### 二、常用事件及方法
1. 客户端常用方法

```javascript
/*
   常规事件
    open:连接已建立
    message:接收到数据
    error:WebSocket 错误
    close:连接已关闭
*/

let socket = new WebSocket("wss://javascript.info/article/websocket/demo/hello");

socket.onopen = function(e) {
  alert("[open] Connection established");
  alert("Sending to server");
  socket.send("My name is John"); // 发送数据
};

socket.onmessage = function(event) {
  alert(`[message] Data received from server: ${event.data}`);
};

socket.onclose = function(event) {
  if (event.wasClean) {
    alert(`[close] Connection closed cleanly, code=${event.code} reason=${event.reason}`);
  } else {
    // 例如服务器进程被杀死或网络中断
    // 在这种情况下，event.code 通常为 1006
    alert('[close] Connection died');
  }
};

socket.onerror = function(error) {
  alert(`[error] ${error.message}`);
};

```

2. 服务端常用方法
```javascript
/*
    核心：
    1. 绑定服务
    2. 监听message事件
*/
var WebSocketServer = require('websocket').server;
var http = require('http');

var server = http.createServer(function(request, response) {
    console.log((new Date()) + ' Received request for ' + request.url);
    response.writeHead(404);
    response.end();
});
server.listen(8080, function() {
    console.log((new Date()) + ' Server is listening on port 8080');
});

/*
    监听请求服务
*/
wsServer = new WebSocketServer({
    httpServer: server,        
    autoAcceptConnections: false
});

function originIsAllowed(origin) {
  return true;
}

wsServer.on('request', function(request) {
    if (!originIsAllowed(request.origin)) {
      request.reject();
      console.log((new Date()) + ' Connection from origin ' + request.origin + ' rejected.');
      return;
    }
    
    var connection = request.accept('echo-protocol', request.origin);
    console.log((new Date()) + ' Connection accepted.');
    /*
        message事件
    */
    connection.on('message', function(message) {
        if (message.type === 'utf8') {
            console.log('Received Message: ' + message.utf8Data);
            connection.sendUTF(message.utf8Data);
        }
        else if (message.type === 'binary') {
            console.log('Received Binary Message of ' + message.binaryData.length + ' bytes');
            connection.sendBytes(message.binaryData);
        }
    });
    connection.on('close', function(reasonCode, description) {
        console.log((new Date()) + ' Peer ' + connection.remoteAddress + ' disconnected.');
    });
});
```