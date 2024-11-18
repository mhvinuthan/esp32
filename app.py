from flask import Flask, render_template, request, jsonify
from datetime import datetime
import json

app = Flask(__name__)

# Store activity logs
user_activities = []

# Root route to show the dashboard
@app.route('/')
def home():
    return render_template('index.html', activities=user_activities)

# Route to receive and store user activity data (from JavaScript)
@app.route('/activity', methods=['POST'])
def activity():
    activity_data = request.json
    if activity_data:
        activity_data['time_received'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        user_activities.append(activity_data)
        return jsonify({"message": "Activity data received!"}), 200
    return jsonify({"message": "Invalid activity data!"}), 400

# Run the Flask app on all available network interfaces and port 5000
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)