import zmq

context = zmq.Context()

print("Connecting to reservation microservice server...")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

# send test string
while True:
    zip_code = input("What is the zip code where you want to reserve a park?\n")
    socket.send_string(zip_code)

    reply = socket.recv_string()
    print(reply)
