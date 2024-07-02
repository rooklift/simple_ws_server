import threading, time
import SimpleWebSocketServer as swss


clients = []
clients_lock = threading.Lock()


class Connection(swss.WebSocket):

	def handleConnected(self):
		with clients_lock:
			clients.append(self)
			print("Connected: {}".format(self.address))

	def handleClose(self):
		with clients_lock:
			clients.remove(self)
			print("Disconnected: {}".format(self.address))

	def handleMessage(self):
		print(self.data)


def server_start():
	server = swss.SimpleWebSocketServer('localhost', 8001, Connection, selectInterval = 0.1)
	server.serveforever()


def message_sender():
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


threading.Thread(target = server_start).start()
threading.Thread(target = message_sender).start()
