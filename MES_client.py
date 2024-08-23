import requests
import json

# MES 1 sends a production order update to MES 2
def send_production_order_update(order_id, status):
    url = "http://127.0.0.1:5001/api/production-order/update"  # Local MES 2 API endpoint
    headers = {
        "Content-Type": "application/json"
    }

    # Payload with the production order data
    payload = {
        "order_id": order_id,
        "status": status,
        "timestamp": "2024-08-24T15:00:00Z"
    }

    # Sending a POST request to MES 2
    response = requests.post(url, data=json.dumps(payload), headers=headers)

    # Check response
    if response.status_code == 200:
        print(f"Order {order_id} update sent successfully.")
    else:
        print(f"Failed to send order update. Status Code: {response.status_code}, Response: {response.text}")


# Example of sending an order update
send_production_order_update(order_id="PO12345", status="Completed")
