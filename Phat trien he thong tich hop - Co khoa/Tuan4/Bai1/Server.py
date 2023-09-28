#Bài 1: Từ thí dụ trên, sinh viên viết 1 echo-server theo yêu cầu sau:
#- Server: lắng nghe trên một port xác định (do sinh viên quy định), 
#chấp nhận yêu cầu kết nối từ một client, hiển thị thông tin client, 
#nhận một chuỗi từ client sau đó chuyển trả lại cho client
#- Client: kết nối tới server thông qua một port xác định (do sinh 
#viên quy định), gởi chuỗi đến server, nhận chuỗi mới từ server và 
#hiển thị trên màn hình của client

#server.py 

#SimpleServer.py
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

    # Gửi dữ liệu nhận được trở lại cho client (Echo)
    client_socket.send(data.encode('utf-8'))

    # Đóng kết nối với client
    client_socket.close()
