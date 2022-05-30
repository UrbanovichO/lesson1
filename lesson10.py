import requests
# response = requests.get("https://httpbin.org/get")
# print(response.text)
# print(f"Datatype - {type(response.text)}")

response = requests.post("https://httpbin.org/post",data="test data",
                         headers={"h1":"test title"})
print(response.text)