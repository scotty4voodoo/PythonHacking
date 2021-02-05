import sys
import io
import requests

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

#Response 출력
s = requests.Session()
r = s.get('http://httpbin.org/get')
#print(r.status_code) # == 200, 304, 500
#print(r.ok) # == 200일경우 True

#json parsing

r = s.get('https://jsonplaceholder.typicode.com/posts/1')
print(r.json())
print(r.json().keys())
print(r.json().values())
print(r.encoding)
print(r.content) #binary data
print(r.raw) #raw data
