import requests
import json
def get_info(data):
    name=data.get("name")
    last=data["name"]["last"]
    first=data['name']['first']
    age=data['dob']['age']
    country=data['location']['country']
    gender=data['gender']
    data1={
        "first_name":first,
        "last_name": last,
        "age":age,
        "country":country,
        "gender":gender
        }
    return data1

def results(n):
    arr=[]
    while True:
        r = requests.get('https://randomuser.me/api/')
        if r.status_code == 200:
            
            m=r.json()
            data= m['results'][0]
            if data['gender'] == 'male':
                a=get_info(data)
                arr.append(a)
        dict1 = {'results':arr}
        if len(arr) > n - 1:
            break
    return dict1

dict1 = results(10)
data_json=json.dumps(dict1,indent=4)
f=open("data_json","w")
f.write(data_json)
f.close()