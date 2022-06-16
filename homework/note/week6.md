## 程式的編譯、組譯、連結及載入流程
```
    高階語言(系統程式)
       ↓
    編譯器(系統軟體)
       ↓
    組合語言(系統程式)
       ↓
    組譯器(系統軟體)
       ↓
    目的檔
       ↓
    連結器(系統軟體)
       ↓
    執行檔
       ↓
    載入器(系統軟體)
       ↓
    記憶體

```
## 組合語言
### 編譯成執行檔
```
gcc foobar.c -o foobar
```
### 使用方法
```
./foobar
```
### 結果
```
r=740740
```

### 產生.s檔更詳細的列出
```
gcc -S --verbose-asm foobar.c -o foobar_mac.s
```
### 05-asm/02-gnu內的.s檔看組合語言語法

## 目的檔 (objdump)

### 只編譯不連結
```
gcc -c add.c -o add.o
```
#### objdump 是在類 Unix 作業系統上顯示關於目的檔的各種資訊的命令行程式

### 反組譯目的檔
```
objdump -d add.o
```

## 堆疊段
```
#include <stdio.h>
int power2(int n){
    if(n==0) return 1;
    return power2(n-1)*2;
}
int main(){
    int p = power2(3);
    printf("p=%d\n", p);
}

```
