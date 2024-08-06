# pip install cryptography ( to clear cryptography is not installed error)
from opcua import Client

# Define the OPC UA server URL
#server_url = "opc.tcp://your-opcua-server-url:4840"
server_url = "opc.tcp://172.18.207.71:48010"

# Create an OPC UA client
client = Client(server_url)

try:
    # Connect to the OPC UA server
    client.connect()
    print(f"Connected to {server_url}")

    # Get the root node
    root = client.get_root_node()
    print("Root node is:", root)

    # Browse the address space
    objects = client.get_objects_node()
    print("Objects node is:", objects)

    # Read a variable (replace 'ns=2;i=2' with the actual node id of your variable)
    var = client.get_node("ns=3;i=6041")
    value = var.get_value()
    print(f"Value of the variable is: {value}")

    # Read a variable (replace 'ns=2;i=2' with the actual node id of your variable)
    var = client.get_node("ns=3;i=6044")
    value = var.get_value()
    print(f"Value of the variable is: {value}")

    # Read a variable (replace 'ns=2;i=2' with the actual node id of your variable)
    var = client.get_node("ns=3;i=6015")
    value = var.get_value()
    print(f"Value of the variable is: {value}")


except Exception as e:
    print(f"An error occurred: {e}")

#except KeyboardInterrupt:
#    print("Keyboard interrupted")


finally:
    # Disconnect from the server
    client.disconnect()
    print("Disconnected from the server")