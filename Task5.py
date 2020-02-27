#Perform Get and Display 200OK
import requests
url = "http://172.17.50.43/spicyx"
r = requests.get(url)
print("Status code:\n*******")
print(r.status_code)
print("*******")
#Show Website Display
h = requests.head(url)
print("Header:\n*******")
for lines in h.headers:
    print(lines,":",h.headers[lines])
print("*******")
#Modify Header
url2 = "http://httpbin.org/headers"
fake_headers = {
    "User-Agent":"Mobile"
}
r2 = requests.get(url2, headers=fake_headers)
print(r2.text)