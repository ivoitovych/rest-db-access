# Sample REST Service for LLM Integration

This project provides a simple REST service to demonstrate the integration of a Language Learning Model (LLM) with an external data source. The service allows the LLM to request additional information using a specific pattern and receive unique, mysterious stories from a JSON-based database.

## Project Structure

- **PromptForDataSystemAccess.txt**: Contains instructions for the LLM to request and incorporate external data.
- **sample_rest_service.py**: The Flask-based REST service that reads data from a JSON file and provides specific stories based on queries.
- **stories.json**: A JSON file containing a database of fictional entities and their corresponding stories.

## Prerequisites

- Python 3.x
- Flask

## Setup Instructions

1. **Install Flask**:
   ```bash
   pip install Flask
   ```

2. **Prepare the JSON Database**:
   Ensure `stories.json` is available in the project directory or specify a path to your own JSON file with a similar structure.

3. **Run the Flask Service**:
   Start the Flask application by providing the path to the JSON file as a command-line argument:
   ```bash
   python sample_rest_service.py stories.json
   ```

   This starts the service on `http://127.0.0.1:5000` with the `/data-request` endpoint.

## Usage

### LLM Data Request Pattern

The LLM can request data by using the following pattern in its output:
```
Data request: [Your Query Here] End of data request.
```

### Querying the Service

The service listens on the `/data-request` endpoint and expects a `query` parameter. It returns the story associated with the queried entity name.

Example query:
```
GET /data-request?query=Zorblex%20the%20Quantum%20Whisperer
```

### Available Records

The following entities can be queried using their exact names:
- Zorblex the Quantum Whisperer
- The Chronomantic Loom of Eon
- Lumina Voidheart
- The Whispers of Nyx
- Ekos, the Living Planet

### Handling Responses

- **Successful Query**: Returns the story of the requested entity.
- **Unsuccessful Query**: Returns a message indicating that no story was found.

## Additional Information

- **Error Handling**: If there is an issue retrieving data, the system will notify with a "REQUEST ERROR" message.
- **Data Management**: Both the data request and the received data are cleared from the chat history to maintain context brevity and manage computational resources.

This project serves as an example for integrating LLMs with external data sources, demonstrating how to enhance conversational capabilities with dynamic content.