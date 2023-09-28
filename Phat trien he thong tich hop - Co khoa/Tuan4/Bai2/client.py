import socket

# Định nghĩa cổng và địa chỉ máy chủ
SERVER_ADDRESS = 'localhost'
SERVER_PORT = 12345

# Tạo một socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Kết nối đến máy chủ
client_socket.connect((SERVER_ADDRESS, SERVER_PORT))

# Nhập chuỗi từ người dùng
message = input("Nhập chuỗi: ")

# Gửi chuỗi đến server
client_socket.send(message.encode('utf-8'))

# Nhận dữ liệu từ server
data = client_socket.recv(1024).decode('utf-8')
print(f"Nhận từ server: {data}")

# Đóng kết nối với server
client_socket.close()
