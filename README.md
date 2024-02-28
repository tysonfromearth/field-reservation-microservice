# field-reservation-microservice

Communication Contract: 
How to request data: use pyZMQ's socket.send_string() method with a zip code as the argument, e.g., socket.send_string("12345")

How to receive data: use pyZMQ's socket.recv_string() method and assign the response to a variable, e.g., reply = socket.recv_string()

![image](https://github.com/tysonfromearth/field-reservation-microservice/assets/40677874/fa35bdcf-479d-403d-8487-30b7d1a042fd)
