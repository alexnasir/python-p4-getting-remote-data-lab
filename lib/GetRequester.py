import requests
import json

class GetRequester:
    def __init__(self, url: str):
        """Initialize with a URL."""
        self.url = url

    def get_response_body(self):
        """Send a GET request and return the body of the response as a string."""
        try:
            response = requests.get(self.url)
            response.raise_for_status()  # Raise an HTTPError for bad responses (4xx, 5xx)
            return response.text  # Return the body of the response as a string
        except requests.exceptions.RequestException as e:
            print(f"Error occurred: {e}")
            return None

    def load_json(self):
        """Use get_response_body to send a GET request and return the JSON data."""
        response_body = self.get_response_body()
        if response_body:
            try:
                return json.loads(response_body)  # Convert response body to Python data
            except json.JSONDecodeError:
                print("Error: Response is not valid JSON.")
                return None
        else:
            print("Error: No response body to parse.")
            return None

    def __str__(self):
        """Return the URL as a string when the object is printed."""
        return f"GetRequester({self.url})"
