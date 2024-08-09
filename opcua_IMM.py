# connect through Europmap IMM machines
from opcua import Client
import time

# Define the OPC-UA server endpoint URL
OPC_UA_SERVER_URL = "opc.tcp://<IP_ADDRESS>:<PORT>"  # Replace with your server IP and port

def connect_to_server(url):
    client = Client(url)
    try:
        client.connect()
        print("Connected to OPC-UA Server")
    except Exception as e:
        print(f"Failed to connect to OPC-UA Server: {e}")
        return None
    return client

def collect_data(client):
    try:
        # Replace with the actual node ID you want to monitor
        node_id = "ns=2;i=2"  # Example Node ID
        node = client.get_node(node_id)
        data = node.get_value()
        print(f"Data from node {node_id}: {data}")
    except Exception as e:
        print(f"Failed to collect data: {e}")

def main():
    client = connect_to_server(OPC_UA_SERVER_URL)
    if client:
        try:
            while True:
                collect_data(client)
                time.sleep(10)  # Adjust the sleep time as needed
        finally:
            client.disconnect()
            print("Disconnected from OPC-UA Server")

if __name__ == "__main__":
    main()
