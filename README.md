# Blue - A hybrid programming language for web development.

Introduce
------------
이 언어는 보다 편리한 웹 개발을 목적으로 개발되었습니다.  
클라이언트와 서버의 경계가 뚜렷하지 않으며, 두 가지 스타일의 언어를 사용할 수 있는 하이브리드 언어입니다.  

Basic Grammar
---------------
### 1. Variable Declaration
변수를 정의하는 방법은 다음과 같습니다.  
```javascript
var v = 3+5;
var v2 = "Hello World!";
var v3 = [1,2,3,"a","b",'c'];
```
변수 앞에는 숫자가 올 수 없으며, 알파벳과 숫자만 사용할 수 있습니다.  
변수의 값에 넣을 수 있는 데이터타입은 다음과 같습니다.
- 계산식(변수 포함)
- 함수
- 배열
- 비교식
- Boolean

### If Statement
if문은 다음과 같이 사용됩니다.
```javascript
a = 4;
b = 5;
if(a<b){
    print(a,b);
}
```
if식별자 뒤에 오는 괄호 안에 Expression이 올 수 있습니다.   
Expression은 N.Expression을 참고하세요.  

### While Statement
while문은 다음과 같이 사용됩니다.
```javascript
a = 0;
while
```

### N. Expression
Expression은 다음과 같이 분류됩니다.
- 계산식(변수 포함)
- 함수 호출
- 배열
- 비교식  
