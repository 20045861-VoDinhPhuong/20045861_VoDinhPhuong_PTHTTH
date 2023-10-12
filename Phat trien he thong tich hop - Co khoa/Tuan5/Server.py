import socket
import threading

def reverse_string_and_capitalize_first_word(string):
    words = string.split()
    reversed_string = ' '.join(words[::-1])
    capitalized_string = reversed_string.title()
    return capitalized_string

def calculate_integer_sum(numbers):
    numbers_list = numbers.split()
    try:
        integer_numbers = [int(num) for num in numbers_list]
        return sum(integer_numbers)
    except ValueError:
        return "Invalid input. Please enter only integers."

def handle_client_connection(client_socket):
    while True:
        request = client_socket.recv(1024).decode()
        if not request:
            break
        if request == "1":
            client_socket.sendall("Enter a string: ".encode())
            string = client_socket.recv(1024).decode()
            result = reverse_string_and_capitalize_first_word(string)
            client_socket.sendall(result.encode())
        elif request == "2":
            client_socket.sendall("Enter a series of integers separated by spaces: ".encode())
            numbers = client_socket.recv(1024).decode()
            result = calculate_integer_sum(numbers)
            client_socket.sendall(str(result).encode())
        elif request == "3":
            break
    client_socket.close()

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(5)
    print("Server started and listening on port 12345.")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"New client connected: {addr[0]}:{addr[1]}")
        client_thread = threading.Thread(target=handle_client_connection, args=(client_socket,))
        client_thread.start()

start_server()