import sys
import io
import requests, json

#Rest : POST, GET, PUT:UPDATE, REPLACE(FETCH : UPDATE, MODIFY), DELETE

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')


payload1 = {'key1':'value1','key2':'values2'} #dict
payload2 = (('key1','values1'),('key2','values2')) #tuple
payload3 = {'some':'nice'} #json

#r = requests.put('http://httpbin.org/put',data=payload1)
#print(r.text)

#r = requests.put('https://jsonplaceholder.typicode.com/posts/1',data=payload1)
#print(r.text)

r = requests.delete('https://jsonplaceholder.typicode.com/posts/1')
print(r.text)
