from bs4 import BeautifulSoup
import requests
Dollar_Grn = "https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B4%D0%BE%D0%BB%D0%B0%D1%80%D0%B0+%D0%B4%D0%BE+%D0%B3%D1%80%D0%B8%D0%B2%D0%BD%D1%96&sxsrf=ALiCzsYMniigGccscK9PdSRd4JCLvMLkYg%3A1654360804853&ei=5IqbYojMM76n9u8PsuA-&ved=0ahUKEwiIzumgnpT4AhW-k_0HHTKwDwAQ4dUDCA4&uact=5&oq=%D0%BA%D1%83%D1%80%D1%81+%D0%B4%D0%BE%D0%BB%D0%B0%D1%80%D0%B0+%D0%B4%D0%BE+%D0%B3%D1%80%D0%B8%D0%B2%D0%BD%D1%96&gs_lcp=Cgdnd3Mtd2l6EAMyDQgAEIAEELEDEEYQggIyBQgAEIAEMggIABCABBDJAzIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQ6CggAEEcQsAMQyQM6BwgAEEcQsAM6BwgAELADEEM6EgguEMcBEKMCEMgDELADEEMYAToSCC4QxwEQ0QMQyAMQsAMQQxgBOgsIABCABBCxAxCDAToICAAQsQMQgwE6CAgAEIAEELEDOg4IABCABBCxAxCDARDJAzoFCAAQkgM6BQgAEMsBSgQIQRgASgQIRhgAUIsBWL4dYNQfaAFwAXgAgAFniAHPB5IBAzguMpgBAKABAcgBDMABAdoBBAgBGAg&sclient=gws-wiz"
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}
full_page = requests.get(Dollar_Grn,headers=headers)
soup = BeautifulSoup(full_page.content, 'html.parser')
soup_list = soup.findAll("span", {"class": "DFlfde", "class":"SwHCTb", "data-precision":2})
USD = soup_list[0].text
print(USD)

