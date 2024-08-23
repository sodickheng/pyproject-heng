from flask import Flask, request, jsonify

app = Flask(__name__)


# Endpoint to receive production order updates
@app.route('/api/production-order/update', methods=['POST'])
def receive_production_order_update():
    data = request.get_json()  # Parse the JSON payload

    # Extract data from the request
    order_id = data.get('order_id')
    status = data.get('status')
    timestamp = data.get('timestamp')

    # Log the received data (In practice, update MES 2's database or system)
    print(f"Received update for Order ID: {order_id}, Status: {status}, Timestamp: {timestamp}")

    # Respond with a success message
    return jsonify({"message": "Order update received successfully."}), 200


# Running the MES 2 API
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
