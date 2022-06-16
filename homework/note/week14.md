## 08-ipcchat fifo(msys2)
```
gcc chat.c -o chat
//機器1
./chat 1
hi

receive: hi2

//機器2
./chat 0
hi2

receive: hi
```
## 08-ipcchat fifo(msys2)
```
gcc chat.c -o chat
//機器1
./chat 1
hi

receive: hi2

//機器2
./chat 0
hi2

receive: hi
```
## 08-ipcchat mmap(共用記憶體)
### 將檔案放在記憶體內,然後共用
```
gcc chat.c -o chat
//機器1
./chat 1
hi

receive: hi2

//機器2
./chat 0
hi2

receive: hi
```
## 08-ipcchat udp
### 利用socket 帶參數是用戶,不帶是server
```
gcc chat.c -o chat
//機器1
./chat
hi

I am server...
receive: <connect request> from client addr 127.0.0.1
//機器2
./chat 127.0.0.1
hi2

I am client...
```
## 08-ipcchat tcp(比起udp有接收和連接和listen)
```
gcc chat.c -o chat
//機器1
./chat
accept: cfd=4 client addr 127.0.0.1

I am server...
receive: <connect request> from client addr 127.0.0.1
//機器2
./chat 127.0.0.1

I am client...
connect success: sfd=3 server addr=127.0.0.1
```
