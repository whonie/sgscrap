import requests
res = requests.get('http://www.google.com/')
res.raise_for_status()
# res = requests.get('http://www.nadocoding.tistory.com/')
print(len(res.text))
with open('mygoogle.html','w',encoding='utf-8') as f:
    f.write(res.text)