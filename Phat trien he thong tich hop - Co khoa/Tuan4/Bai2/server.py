import socket

# Định nghĩa cổng mà server sẽ lắng nghe
PORT = 12345

# Tạo một socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Liên kết socket với địa chỉ và cổng
server_socket.bind(('localhost', PORT))

# Lắng nghe kết nối từ client (tối đa 1 kết nối đồng thời)
server_socket.listen(1)
print(f"Đang lắng nghe trên cổng {PORT}...")

while True:
    # Chấp nhận kết nối từ client
    client_socket, client_address = server_socket.accept()
    print(f"Kết nối từ {client_address}")

    # Nhận dữ liệu từ client
    data = client_socket.recv(1024).decode('utf-8')
    print(f"Nhận từ client: {data}")

    # Chuyển đổi chuỗi thành chữ hoa
    data = data.upper()

    # Gửi dữ liệu chuyển đổi lại cho client
    client_socket.send(data.encode('utf-8'))

    # Đóng kết nối với client
    client_socket.close()
