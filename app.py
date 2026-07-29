from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
import random

app = Flask(__name__)

# MongoDB Configuration
# Ensure you have MongoDB running locally on default port 27017 or use Atlas URI
client = MongoClient('mongodb+srv://roopashree:roopashree05@cluster0.onlfr3u.mongodb.net/?appName=Cluster0')
db = client['bugify_db']
bugs_collection = db['bugs']

# Inject mock data if collection is empty (matches your screenshot)
def init_mock_data():
    if bugs_collection.count_documents({}) == 0:
        mock_bugs = [
            {"bug_id": "#BF-7730", "description": "UI Overlap Glitch #14", "severity": "Low", "status": "Resolved", "assignee": "Prem Ramya"},
            {"bug_id": "#BF-772F", "description": "Email Gateway Fail #13", "severity": "High", "status": "Resolved", "assignee": "Alice Dev"},
            {"bug_id": "#BF-772E", "description": "Database Timeout Issue", "severity": "Critical", "status": "Open", "assignee": "John Doe"},
            {"bug_id": "#BF-772D", "description": "Login Page CSS broken", "severity": "Medium", "status": "In Progress", "assignee": "Sarah Smith"},
        ]
        # Add some extra dummy bugs to make the total 31 like the image
        for i in range(27):
            mock_bugs.append({
                "bug_id": f"#BF-77{random.randint(0, 99):02d}",
                "description": f"Auto-generated bug report {i}",
                "severity": random.choice(["Low", "Medium", "High", "Critical"]),
                "status": random.choice(["Open", "In Progress", "Resolved"]),
                "assignee": random.choice(["Prem Ramya", "Alice Dev", "John Doe", "Unassigned"])
            })
        bugs_collection.insert_many(mock_bugs)

init_mock_data()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/bugs', methods=['GET'])
def get_bugs():
    bugs = list(bugs_collection.find({}, {'_id': 0}).sort("bug_id", -1))
    return jsonify(bugs)

@app.route('/api/bugs', methods=['POST'])
def add_bug():
    data = request.json
    # Generate a random ID format like #BF-XXXX
    new_id = f"#BF-{random.randint(1000, 9999)}"
    new_bug = {
        "bug_id": new_id,
        "description": data.get('description', 'No description'),
        "severity": data.get('severity', 'Low'),
        "status": data.get('status', 'Open'),
        "assignee": data.get('assignee', 'Unassigned')
    }
    bugs_collection.insert_one(new_bug)
    del new_bug['_id']
    return jsonify({"message": "Bug added successfully", "bug": new_bug}), 201

@app.route('/api/bugs/<bug_id>', methods=['PUT'])
def update_bug(bug_id):
    data = request.json
    bugs_collection.update_one({"bug_id": bug_id}, {"$set": data})
    return jsonify({"message": "Bug updated successfully"})

@app.route('/api/bugs/<bug_id>', methods=['DELETE'])
def delete_bug(bug_id):
    bugs_collection.delete_one({"bug_id": bug_id})
    return jsonify({"message": "Bug deleted successfully"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)