import requests
response = requests.get("https://httpbin.org/get")
print(response.content)
print(f"Datatype - {type(response.content)}")