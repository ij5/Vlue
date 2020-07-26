# Blue - A hybrid programming language for web development.

Introduce
------------
이 언어는 보다 편리한 웹 개발을 목적으로 개발되었습니다.  
클라이언트와 서버의 경계가 뚜렷하지 않으며, 두 가지 스타일의 언어를 사용할 수 있는 하이브리드 언어입니다.  

Hello World!
-----------
test.bl 파일을 생성 후 다음과 같이 저장하세요.  
```javascript
log("Hello World!");
```
놀랍도록 간단합니다.
blue.exe가 있는 위치에서 커멘드 창을 열고 blue라고 입력하세요.  
파일명을 입력하라는 메시지가 나오면 아까 생성한 파일 이름을 넣습니다.   
```
result: Hello World!
```

Basic Grammar
---------------

### 1. Variable Declaration
변수를 정의하는 방법은 다음과 같습니다.  
```javascript
var v = 3+5;
var v2 = "Hello World!";
var v3 = [1,2,3,"a","b",'c'];
var v4 = true;
var v5 = 4<5;

function f(){
    log("hello");
}
var fv = f;
fv();       // result: hello

var fv2 = function(){
    log("world!");
}
fv2();      // result: world!
```
변수 앞에는 숫자가 올 수 없으며, 알파벳과 숫자만 사용할 수 있습니다.  
변수의 값에 넣을 수 있는 데이터타입은 다음과 같습니다.
- 계산식(변수 포함)
- 함수
- 배열
- 비교식
- Boolean

### 2. If Statement
if문은 다음과 같이 사용됩니다.
```javascript
var a = 4;
var b = 5;
if(a<b){
    log(a,b);
}
```
if식별자 뒤에 오는 괄호 안에 Expression이 올 수 있습니다.   
Expression은 N.Expression을 참고하세요.  

### 3. While Statement
while문은 다음과 같이 사용됩니다.
```javascript
var a = 0;
while(a<100){
    log(a);
    a = a + 1;
}
```

### 4. Function Declaration
함수 정의는 다음과 같이 사용됩니다.
```javascript
function hello(){
    log("Hello");
}
```

### 5. Function Call
함수 호출은 다음과 같이 사용됩니다.
```javascript
function myName(name){
    log("My name is "+name);
}
myName("Jaehee");       // result: Jaehee
```

### 6. Anonymous function
익명 함수를 변수에 대입하는 방법은 다음과 같습니다.
```javascript
var anonfunction = function(a,b,c){
    log(a+b+c);
};
anonfunction("a", "b", "c");        // result: abc
```
익명 함수 정의 후에는 세미콜론을 붙이는 게 원칙입니다.   
다만, 혼동을 방지하기 위하여 붙이지 않는 것을 제한적으로 허용하였습니다.


### 7. Expression
Expression은 다음과 같이 분류됩니다.
- 계산식(변수 포함)
- 함수 호출
- 배열
- 비교식  
- 클래스 호출


Other
------
**https://developer.mozilla.org/ko/docs/Web/Javascript 본 문서는 모질라에서 제공하는 자바스크립트 문서를 활용하였습니다.**
