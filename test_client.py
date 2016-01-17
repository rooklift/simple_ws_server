from websocket import create_connection         # pip install websocket-client

URL = "ws://127.0.0.1:8001/foo/bar"


ws = create_connection(URL)

while 1:
    try:
        result = ws.recv()
        print(result)
    except:
        ws = create_connection(URL)

ws.close()

input()
