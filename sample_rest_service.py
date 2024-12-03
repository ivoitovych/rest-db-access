from flask import Flask, jsonify, request
import json
import sys

app = Flask(__name__)

# Load the database from a JSON file passed as a command-line argument
def load_database(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

# Load the database
if len(sys.argv) != 2:
    print("Usage: python sample_rest_service.py <path_to_json_file>")
    sys.exit(1)

database = load_database(sys.argv[1])

@app.route('/data-request', methods=['GET'])
def get_story():
    # Get the query parameter for the name
    query_name = request.args.get('query', '').strip()
    
    # Find the story for the given name
    for item in database:
        if item['name'].lower() == query_name.lower():
            return jsonify({'story': item['story']})
    
    return jsonify({'story': 'No story found for the requested entity.'})

if __name__ == '__main__':
    app.run(debug=True)

