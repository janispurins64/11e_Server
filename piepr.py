import requests
response = requests.get('http://www.delfi.lv') #http://127.0.0.1:5000/dati
if response.status_code == 200:
    print('Success!')
    print(response.headers)
    print("------------>")
    print(response.content)
elif response.status_code == 404:
    print('Not Found.')
json_response = response.json()
print("---------------->")
print(json_response)