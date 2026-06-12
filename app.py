from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for ticket service
state = {
    "tickets": 10
}

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"}), 200

@app.route('/api/v1/ticket', methods=['POST'])
def buy_ticket():
    if state["tickets"] <= 0:
        return jsonify({
            "status": "fail",
            "message": "No tickets left"
        }), 400
    
    state["tickets"] -= 1
    return jsonify({
        "status": "success",
        "message": "Ticket purchased successfully",
        "remaining_tickets": state["tickets"]
    }), 200

@app.route('/api/v1/ticket', methods=['GET'])
def get_tickets():
    return jsonify({
        "status": "success",
        "remaining_tickets": state["tickets"]
    }), 200

if __name__ == '__main__':
    print("Starting Ticket Microservice on http://127.0.0.1:5002")
    app.run(host="127.0.0.1", port=5002, debug=False)
