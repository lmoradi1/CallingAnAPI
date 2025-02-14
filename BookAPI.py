import requests
api_url = "https://www.dbooks.org/api/book/1503212300"
response = requests.get(api_url)
print(response.json())