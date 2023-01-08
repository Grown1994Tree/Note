1. 更改文件server.py

2. 更改WebSocket的链接
```python
ws_server = "ws://soc-player.soccer.htb:9091" # 调整为目标
```

3. 调整参数值
```python
# 按照上传的payload进行调整
data = '{"id":"%s"}' % message
```

4. 启动
```shell
python server.py
```