## 三種虛擬機架構
```
記憶體機(Memory Machine): 可直接對記憶體變數進行運算
暫存器機(Register Machine): 必須將變數載入暫存器中，才能進行運算
堆疊機(Stack Machine): 會取出堆疊上層元素進行運算，並將結果存回堆疊中
```
## 編譯成執行檔
```
gcc -w c6.c -o c6
```

## 使用方法
```
./c6 test/fib.c  
```

## 執行結果
```
./c6 test/fib.c  
```

## 印出執行的過程
```
./c6 -s test/hello.c
```

## 執行結果
```
1: #include <stdio.h>
2: 
3: int main()
4: {
5:   printf("hello, world\n");
    1:930098     ENT  0
    3:9300A8     ADDR 0:9700A0
    5:9300B8     PSH #堆疊
    6:9300C0     PRTF #printf
    7:9300C8     ADJ  1
6:   return 0;
    9:9300D8     IMM  0
    B:9300E8     LEV
7: }
    C:9300F0     LEV #離開
```

# 列印目的檔

## 產生目的檔
```
./c6 test/sum.c -o test/sum.o
```

## 可以直接執行
```
./c6 -r test/sum.o
```

## 執行 + 執行過程
```
結果與上面一樣
./c6 -d -r test/sum.o
```
