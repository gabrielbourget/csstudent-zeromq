import zmq

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://localhost:2000")

socket.setsockopt(zmq.SUBSCRIBE, b"")

LISTENERS = [0, 1, 2, 3, 4, 5, 6, 7]

while True:
  message = socket.recv_pyobj()
  message_index = list(message.keys())[0]
  if message_index in LISTENERS:
    print(message.get(LISTENERS[message_index]))
