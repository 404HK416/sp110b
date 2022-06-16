## 01-basic(要在msys2上跑)

### fork1.c
```
gcc fork1.c
./a
 
1918  : Hello world!
1920  : Hello world!
1919  : Hello world!
1921  : Hello world!
```
### fork2.c
```
gcc fork2.c
./a
 
1934  : enter
1934  : after 1st fork
1935  : after 1st fork
1934  : Hello world!
1937  : Hello world!
1935  : Hello world!
1936  : Hello world!
```
### fork3.c
```
gcc fork3.c
./a
 
1943  : enter
1943  : after 1st fork
1944  : after 1st fork
1944  : Hello world!
1943  : Hello world!
1946  : Hello world!
1945  : Hello world!
```
## 02-child(要在msys2上跑)
### fork2.c
```
gcc fork2.c
./a
 
1953 : I am parent!
1956 : I am child!
1954 : I am parent!
1955 : I am child!
```
## 03-exec
### 
```
gcc execvp1.c
./a
 
execvp():before
total 65
-rwxr-xr-x 1 user user 62735 Apr 27 15:41 a.exe
drwxr-xr-x 1 user user     0 Mar 23 14:35 backup
-rw-r--r-- 1 user user   185 Mar 23 14:35 execvp1.c
```
## 04-system(要在msys2上跑)
### system1.c
```
gcc system1.c
./a
 
total 67
-rwxr-xr-x 1 user user 62223 Apr 27 15:45 a.exe
-rw-r--r-- 1 user user   274 Mar 23 14:35 mysystem0.c
-rw-r--r-- 1 user user   351 Mar 23 14:35 mysystem1.c
-rw-r--r-- 1 user user   106 Mar 23 14:35 system1.c
main end!
```
### mysystem0.c
```
gcc system0.c
./a
 
total 67
-rwxr-xr-x 1 user user 62241 Apr 27 15:46 a.exe
-rw-r--r-- 1 user user   274 Mar 23 14:35 mysystem0.c
-rw-r--r-- 1 user user   351 Mar 23 14:35 mysystem1.c
-rw-r--r-- 1 user user   106 Mar 23 14:35 system1.c
```
### mysystem1.c
```
gcc system1.c
./a
 
total 67
-rwxr-xr-x 1 user user 62623 Apr 27 15:47 a.exe
-rw-r--r-- 1 user user   274 Mar 23 14:35 mysystem0.c
-rw-r--r-- 1 user user   351 Mar 23 14:35 mysystem1.c
-rw-r--r-- 1 user user   106 Mar 23 14:35 system1.c
main end!
```
