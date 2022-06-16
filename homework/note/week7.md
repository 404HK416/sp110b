## 組合語言

### 執行
```
gcc svd1.c -o svd1
```

### 結果
```
svd1.c:6:10: fatal error: gsl/gsl_math.h: No such file or directory
 #include <gsl/gsl_math.h>
          ^~~~~~~~~~~~~~~~
compilation terminated.
```
### 需要wsl
```
wsl> sudo apt install libgsl-dev

wsl> gcc svd1.c -o svd1 -lgsl

wsl> ./svd1
```

## msys2安裝sqlite
```
pacman -S mingw-w64-x86_64-sqlite3
pkg-config --cflags sqlite3
pkg-config --libs sqlite3
```

## 執行
```
./sqlite_write
./sqlite_read
```
## 執行
```
./build.sh curl1
./sqlite_read
```
### make在msys2
## make安裝
```
pacman -S make
```

## 執行(先ls到資料夾後make)
### 結果
```
gcc -std=c99 -O0 sum.c main.c -o run
```
```
gcc -std=c99 -O0 -c sum.c -o sum.o
ar -r libstat.a sum.o
ar: creating libstat.a
gcc -std=c99 -O0 -c main.c -o main.o
gcc -std=c99 -O0 libstat.a main.o -L ./ -lstat -o run
```
## msys2安裝cmake
```
cd A-hello-cmake/
mkdir build && cd build
cmake ..
ninja
./hello_cmake
```
