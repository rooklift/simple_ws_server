import threading, time
import SimpleWebSocketServer as swss


clients = []
clients_lock = threading.Lock()


def we_send_messages():
    n = 0
    while 1:
        n += 1
        with clients_lock:
            for c in clients:
                try:
                    c.sendMessage(str(n))
                except:
                    pass
        time.sleep(1)

def server_start():
    server = swss.SimpleWebSocketServer('localhost', 8001, MyWebsocketExample, selectInterval = 0.1)
    server.serveforever()

class MyWebsocketExample(swss.WebSocket):

    def handleConnected(self):
        with clients_lock:
            clients.append(self)

    def handleClose(self):
        with clients_lock:
            clients.remove(self)

    def handleMessage(self):
        print(self.data)


threading.Thread(target = we_send_messages).start()
threading.Thread(target = server_start).start()

