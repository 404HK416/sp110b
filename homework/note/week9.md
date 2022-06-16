## 作業系統
```
五大功能
1. 行程管理:打造一個環境讓任何程式能不受干擾的執行
2. 記憶體管理:打造一個記憶體配置環境，當程式向系統請求記憶體時，就能獲得所需空間，且不需考慮其他程式
3. 輸出入系統:能將輸出入裝置包裝成系統函數，讓輸出入作業變容易使用
4. 檔案系統:能讓程式師及使用者輕鬆存取永久儲存裝置中的檔案
5. 使用者介面:讓程式師及使用者能輕鬆操作的環境
```
### 執行
```
 gcc forever.c -o forever
./forever
```
### 陷入無限迴圈(ctrl+c跳出)

## 行程
### 查看行程
```
ps
```
### 終止行程
```
kill + 行程代碼
```

### 行程VS執行緒
```
行程:傳統的兩個行程通常擁有不同的記憶空間，在具有記憶體管理單元(MU:Memory Management Unit)的作業係中，兩個行程的記憶空間是完全獨立的，各自擁有自己的記憶體映射表。所以在行程切換的同時也必須更換映射表，這樣的動作會消耗許多時間。

執行緒:
    1.執行緒之間共用記憶體空間
    2.切換時不須映射表
    3.切換動做非常快速
```
### thread(兩個執行緒)
```
gcc georgeMary.c -o georgeMary 
./georgeMary
```

### 結果
george一秒一次 mary 2秒一次
```
George
----------------
Mary
George
----------------
George
----------------
Mary
George
```
### 行程代碼(linux)
```
./georgeMary &
```
### 行程代碼
```
gcc race.c -o race
./race
```

### 結果(非0代表有競爭情況)
```
counter=4570963
```
```
counter=4254466
```
```
counter=-3411833
```

### 行程代碼(加了互斥鎖鎖定)
```
gcc norace.c -o norace
./norace
```

### 結果
```
counter=0
```
### 死結(deadlock)
```
gcc deadlock.c -o deadlock
./deadlock
```
### 結果(中間進入死結無法完整輸出訊息)
```
A lock x
B lock y
```
## 生產者消費者
```
gcc -w producerConsumer.c -o producerConsumer 
./producerConsumer
```
## 結果
```
Consumer 1 Just consumed item 1174 from slot 2
Producer 2. Put 1181 in slot 9
incremented in!
Consumer 3 Just consumed item 1175 from slot 3
Producer 0. Put 1182 in slot 0
incremented in!
.
.
```

## 哲學家進餐問題
```
[維基百科](https://zh.wikipedia.org/zh-tw/%E5%93%B2%E5%AD%A6%E5%AE%B6%E5%B0%B1%E9%A4%90%E9%97%AE%E9%A2%98)
```



