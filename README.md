# Markdown Analysis API

This API allows potential buyers for our client ABC to access an AI-generated analysis of synergies between the buyer's business and ABC. Clients can also add to this analysis via the post method in the API.

## How to run and test the API locally

1. Clone the repository and navigate to project directory
2. Install the required packages:
pip install requirements.txt
3. Run the `app.py` file
4. Use postman or curl to test the following API endpoints OR run the `api_tester.py` file after `app.py` is up and running:

## GET:
url: `http://127.0.0.1:5000/get`

- Returns a json object with the markdown response formatted as follows:
`{"markdown": "markdown text here"}`

## POST:
url: `http://127.0.0.1:5000/post`

Parameters:

    headers = {
        'Content-Type': 'application/json',
    }

    body = {
        'text': 'sentence to add here'
    }

- Updates the markdown by adding a new sentence to the end of it in a new line



