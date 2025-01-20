import pyzmq as zmq
from time import sleep

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://localhost:2000")

messages = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
CURRENT_MESSAGE = 0

while True:
  sleep(1)
  socket.send_pyobj({ CURRENT_MESSAGE: messages[CURRENT_MESSAGE] })
  if CURRENT_MESSAGE < len(messages) - 1:
    CURRENT_MESSAGE += 1
  else: CURRENT_MESSAGE = 0
