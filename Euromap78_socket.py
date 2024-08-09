import socket

# Configuration
IMM_IP = '192.168.1.100'  # Replace with your IMM's IP address
IMM_PORT = 12345  # Replace with your IMM's port number


def connect_to_imm():
    # Create a socket object
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Connect to the IMM
        sock.connect((IMM_IP, IMM_PORT))
        print("Connected to IMM")

        # Send a request (example)
        request_data = b'YOUR_REQUEST_DATA'  # Replace with actual request data
        sock.sendall(request_data)

        # Receive response
        response_data = sock.recv(4096)  # Adjust buffer size as needed
        print("Received data:", response_data.decode())

    except socket.error as e:
        print("Socket error:", e)

    finally:
        # Close the connection
        sock.close()


if __name__ == "__main__":
    connect_to_imm()
