import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

test_dictionary = {"12345": 1}

while True:
    zip_code = socket.recv_string()

    fields_left = test_dictionary[zip_code]  # access a dictionary key of zip code, number,

    # if the value of the field is > 0, decrement and make reply successfully reserved
    if fields_left > 0:
        test_dictionary[zip_code] -= 1
        reply = "The reservation was successful."

    # if the value is 0, return "already reserved"
    else:
        reply = "Sorry, that park is already reserved."

    socket.send_string(reply)
