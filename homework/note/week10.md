## 不動點定理
### 至少有一個點讓 F(X)=X
```
deno run 11_fixpoint.js

fixed_point(math_cos, 1)= 0.7390822985224023
fixed_point(y => math_sin(y) + math_cos(y), 1)= 1.2587315962971173
sqrt(2)= 1.4142135623746899
```
### pair
```
deno run pair_test.js

head(x)= 1
tail(x)= 2      
head(head(z))= 1
head(tail(z))= 3
```
### cond?a:b
```
if(cond) return a else b
```
```
m==0?a
    :m==1?b
    :erro
```
### return
```
return (m) => m(x,y)

return function(m){return m(x,y)}
```
