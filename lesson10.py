import requests
# response = requests.get("https://httpbin.org/get")
# print(response.text)
# print(f"Datatype - {type(response.text)}")

# response = requests.post("https://httpbin.org/post",data="test data",headers={"h1":"test title"})
# print(response.text)
res_parse_list = []
response = requests.get("https://coinmarketcap.com/")
response_text = response.text
response_parse = response_text.split("<span>")
for parse_elem_1 in response_parse:
    if parse_elem_1.startswith("$"):
        for parse_elem_2 in parse_elem_1.split("</span>"):
            if parse_elem_2.startswith("$") and parse_elem_2[1].isdigit():
                res_parse_list.append(parse_elem_2)

        bitcoin_exchange_rate = res_parse_list[0]
        print(bitcoin_exchange_rate)