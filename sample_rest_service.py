from flask import Flask, jsonify
import random
import string

app = Flask(__name__)

# Function to generate a random name
def generate_random_name():
    return ''.join(random.choices(string.ascii_uppercase, k=5))

# Function to generate a mysterious story
def generate_mysterious_story():
    characters = [generate_random_name() for _ in range(3)]
    locations = [generate_random_name() for _ in range(2)]
    artifacts = [generate_random_name() for _ in range(2)]

    story = (
        f"In the ancient lands of {locations[0]}, a mysterious figure known as {characters[0]} "
        f"discovered the forgotten city of {locations[1]}. Legends spoke of the {artifacts[0]}, "
        f"a powerful relic sought by many but found by few. {characters[1]}, a wanderer from the east, "
        f"joined forces with {characters[2]} to unravel the secrets of {artifacts[1]}, "
        f"hidden deep within the labyrinths of time. But as they drew closer, the shadows of the past "
        f"began to stir, revealing truths that could change the fate of all who dared to seek the unknown."
    )

    return story

@app.route('/mysterious-story', methods=['GET'])
def get_mysterious_story():
    story = generate_mysterious_story()
    return jsonify({'story': story})

if __name__ == '__main__':
    app.run(debug=True)

