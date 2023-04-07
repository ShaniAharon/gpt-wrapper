# My Flask OpenAI API App

This is a simple Python Flask application that demonstrates a backend with two routes, one GET and one POST. The POST route sends a message to the OpenAI API, and the GET route shows the responses.

## Getting Started

### Prerequisites

To run this project, you'll need:

- Python 3.7 or higher
- Flask
- OpenAI Python library

### Installation

1. Clone the repository:
   git clone https://github.com/username/my-flask-openai-api-app.git

2. Change into the project directory:
   cd my-flask-openai-api-app

3. Set up a virtual environment:
   python3 -m venv venv

4. Activate the virtual environment:

- On Linux/macOS:
  source venv/bin/activate
- On Windows:
  venv\Scripts\activate

5. Install the required dependencies:
   pip install -r requirements.txt

### Configuration

Create a `.env` file in the project root directory with the following content:

OPENAI_API_KEY=<your_openai_api_key>

Replace `<your_openai_api_key>` with your actual OpenAI API key.

## Running the Application

Start the Flask development server:
flask run

The application will be accessible at `http://127.0.0.1:5000`.

## API Endpoints

### GET `/responses`

Retrieve the list of responses from the OpenAI API.

### POST `/send-message`

Send a message to the OpenAI API.

#### Request

````json
{
  "message": "Your message here"
}

```response
{
  "response": "OpenAI API response here"
}


````
