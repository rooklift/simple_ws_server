import random, threading, time
import SimpleWebSocketServer as swws


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


class Bkws(swws.WebSocket):

    def handleConnected(self):
        with clients_lock:
            clients.append(self)

    def handleClose(self):
        with clients_lock:
            clients.remove(self)


threading.Thread(target = we_send_messages).start()

# selectInterval is required in this next call, otherwise the server gets blocked at
# a select() call which only unblocks when there's a connection or disconnection...

server = swws.SimpleWebSocketServer('localhost', 8001, Bkws, selectInterval = 0.1)
server.serveforever()
