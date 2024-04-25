import requests


class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, endpoint):
        url = f"{self.base_url}/{endpoint}"
        response = requests.get(url)
        return response.json()

    def post(self, endpoint, data):
        url = f"{self.base_url}/{endpoint}"
        response = requests.post(url, json=data)
        return response.json()

    def put(self, endpoint, data):
        url = f"{self.base_url}/{endpoint}"
        response = requests.put(url, json=data)
        return response.json()

    def delete(self, endpoint):
        url = f"{self.base_url}/{endpoint}"
        response = requests.delete(url)
        return response.json()


# Example usage
if __name__ == "__main__":
    base_url = "https://api.weather.gov/gridpoints/SLC/103,150/forecast/hourly"
    api_client = APIClient(base_url)

    # Example GET request
    items_data = api_client.get("hourly")
    print(items_data)

    # Example POST request
    # new_item_data = {"name": "New Item", "description": "A new item"}
    # new_item = api_client.post("items/", new_item_data)
    # print(new_item)

    # Example PUT request
    # updated_item_data = {"name": "Updated Item",
    #                      "description": "An updated item"}
    # updated_item = api_client.put("items/1/", updated_item_data)
    # print(updated_item)

    # # Example DELETE request
    # deleted_item = api_client.delete("items/1/")
    # print(deleted_item)
