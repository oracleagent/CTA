import requests

class APIBase:
    """Base class for API clients."""

    def __init__(self, base_url, timeout=15):
        self.base_url = base_url
        self.timeout = timeout

    def get(self, endpoint, params=None):
        """Send a GET request to the specified endpoint."""
        try:
            response = requests.get(f"{self.base_url}{endpoint}", params=params, timeout=self.timeout)
            response.raise_for_status()  # Raises stored HTTPError, if one occurred.
            return response.json()
        except requests.exceptions.HTTPError as errh:
            print(f"Http Error: {errh}")
        except requests.exceptions.ConnectionError as errc:
            print(f"Error Connecting: {errc}")
        except requests.exceptions.Timeout as errt:
            print(f"Timeout Error: {errt}")
        except requests.exceptions.RequestException as err:
            print(f"OOps: Something Else: {err}")

    def post(self, endpoint, data=None):
        """Send a POST request to the specified endpoint."""
        try:
            response = requests.post(f"{self.base_url}{endpoint}", json=data, timeout=self.timeout)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as errh:
            print(f"Http Error: {errh}")
        except requests.exceptions.ConnectionError as errc:
            print(f"Error Connecting: {errc}")
        except requests.exceptions.Timeout as errt:
            print(f"Timeout Error: {errt}")
        except requests.exceptions.RequestException as err:
            print(f"OOps: Something Else: {err}")
