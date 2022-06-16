## 安裝軟體

1.codeblocks  
2.msys2  
3.WSL

## ms2使用
1.安裝gcc >>pacman -S gcc  
2.cd 到目的資料夾  
3.進行操作

## gdb
r: run  
n: next  (空白也行)  
p: print (p x=1 會把 x 設成 1 後再印出)  
c:continue  
p:print  
s:step  
q:quit  

## 編譯四步驟
前置處理、編譯、組譯、連結

## gcc指令的含意
gcc -c sum.c -o sum
其中-c代表只激活預處理、編譯和彙編，sum.c為檔名
-o為參數，sum為指定檔名

gcc -S sum.c -o fib.s
-S的s必須為大寫，表示只激活預處理和編譯
fib.s表示為組合語言檔
如果fib.s的s為大寫，表示為須做前置處理的組合語言檔

## 補充
ar是gcc底下壓縮函式庫程式
.o靜態函式庫
.so動態函式庫
皆可壓縮到ar中
