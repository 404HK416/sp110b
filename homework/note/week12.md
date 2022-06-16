#### io1.c
#### 內部0644
#### 0代表8進位
#### 6代表rw
#### 4代表r沒有wx
```
gcc io1.c -o io1
./io1

n=10
```
### echo.c(讀入字,回應兩次)
```
gcc echo1.c -o echo1
./echo1
d

d
d
```
### fecho1.c(將a讀入輸出到b,再將ab印出來)
```
gcc fecho1.c -o fecho1
./fecho1
```
### stderr1.c
```
gcc stderr1.c -o stderr1
./stderr1

Some message!
Warning: xxx
Error: yyy
```
### stderr2.c
```
gcc stderr2.c -o stderr2
./stderr2
(印到log.txt內)
```
### myshell.c
```
gcc myshell.c -o myshell
./myshell

myshell:D:\sp\sp\09-posix\05-myshell\v1 $ 
```
### time.c
```
gcc time.c -o time
./time

Wed May 04 15:19:56 2022
Wed May 04 15:19:57 2022
Wed May 04 15:19:58 2022
Wed May 04 15:19:59 2022
```
### client.c(server將時間傳給client)p.s:需要在兩個msys內執行
```
make
機器1:./server
機器2:./client

Wed May  4 15:26:53 2022
```
### telnet1.c(遠端操控server)p.s:需要在兩個msys內執行
```
make
機器1:./server
機器2:./client

connect to server 127.0.0.1 success!
127.0.0.1 $ ls
cmd=ls
Makefile
README.md
client.c
client.exe
server.c
server.exe
```
