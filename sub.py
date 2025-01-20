import zmq

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://localhost:2000")

socket.setsockopt(zmq.SUBSCRIBE, b"")

LISTENER = 0

while True:
  message = socket.recv_pyobj()
  # if message.get(LISTENER) is not None:
  #   print(message.get(LISTENER))
  print(message)