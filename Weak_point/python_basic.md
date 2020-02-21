# Python( 파이썬 )     

    - 융통성이 있는 언어      
    - 동적 타입 변화    
      
### 파이썬을 실행시키는 3가지      

    - 1. 명령 프롬프트 -> python.exe 실행      
    - 2. IDLE -> 파이썬 자체 에디터      
        - 파이썬 쉘을 실행 후 사용      
    - 3. 에디터로 코드작성 후 실행     
    
### 메모리와 변수 

- 변수는?     
    - 메모리(RAM)에 위치 => 특정한 값을 저장할 수 있는 장소    
    - 저장된 위치 값인 주소(address)를 가짐      
    - 비어있는 위치에 값을 할당하여 사용      
    
- 변수 이름     
    - 알파벳(첫글자는 소문자)    
        - 대소문자 구분     
            - 주로 대문자는 클래스 명 앞에 사용    
            - 일반 변수는 주로 소문자 사용     
    - 언더스코어(가능한 중간이나 맨뒤에 사용하기를 권장)    
    - 숫자(단독 사용은 비추)     
    - 의미있는 단어로 표기     
        - ex) teacher_name = 'Kim'    
    - 프로그램에서 이미 사용하고 있는 예약어는 사용금지    
        -  for, if , range, etc...     
     
    \*\* 컴퓨터가 처리하는 데이터는 램위에 올라가 있는 데이터      
    
- 기본 자료형      
    - **수치 자료형(정수, 실수)**      
        - 정수 : lnteger ( data = 1 )     
        - 실수 : float ( data = 9.0 )     
    - **문자형**      
        - String : ( data = 'ME?' ),(  data = "OR ME? " )    
    - **논리 / 불린 자료형( 첫 글자는 대문자 T/F )**    
        - Boolean : Ture , False ( data = True)    

- 연산자 그리고 피연산자    
    - +, -, \*, / 같은 기호 연산자    
    - 연산자에 의해 계산 되는 문자나 숫자를 피연산자    
    - 3+2 =>  3과 2는 피연산자 , + 는 연산자    
    - 수식에서 연산자의 역활과 순서는 수학에서 연산자와 동일     
    - 문자간 연산도 가능     
    
## 내가 가장 헷갈리는거 
- indexing & slicing (문자열 index 추출)     
    - index    : 한가지 문자만 -> 명시한 문자만     
                - 문자열의 각 문자는 순서가 있음      
                => a[0]  => '숫자'만 넣을 경우 => 이 숫자는 문자열의 인덱스 넘버를 말함 
                => 앞에서부터 순차적으로 나열되어 있음      

        > a 라는  a = 'hellow word' 문자열에서 요청한 그문자만 콕 찝어서 명시한 아이만 출력      

    ㄴ slicing : 문자열에서 사용자가 명시한부분만 부분적으로 잘라온다.  => [ 시작 : 끝 ]     
                => 시작과 끝을 명시해서 그사이의 값을 가지고 옴     
---
### 이터레이터 
    반복 가능한 객체를 말한다 
    객체에 .next가 가능하다면 이터레이터가 맞음 
    list는 반복 가능하지만 이터레이터는 아니다 
    명시적으로 반복가능란 객체로 만들어서 사용해야한다.

- **이터러블** 
    반복 가능하다는 뜻 => 반복(loop)연산이 가능하여 
    해당 위치를 이동해가면서 값을 사용할수 있는지를 말함

    a라는 dict를 생성하여 class 확인을 하면 a는 dict일뿐 이터레이터는 아니다. 

- 이터레이션 
반복가능한 객체에사 해당 값을 가져오는 행위 

- 이터 함수 
    list나 dict를 이터레이터로 만들어 주는 함수
    dict를 생성하여  iter함수를 통하여 b라는 이터레이터를 만듬
    이터러블 하기때문에 for문과 짝을 이루어 사용한다. 


### 제너레이터 
    이터레이터를 만들어주는것을 말함 
    = 반복 가능한 객체를 만들어 주는 행위 

- yield
    function에서 return과 동일한 역할을 수행 = 반환값

```py
# def generator(n):
#     print "get_START"
#     i = 0
#     while i < n:
#         yield i
#         print "yield 이후 %d" % i
#         i += 1
#     print "get_END"

# for i in generator(4):
#     print "for_START %d" % i
#     print i
#     print "for_END %d" % i

```    
<hr />
< 참고 자료 >      
    1. [fastcampus](www.fastcampus.co.kr)    
    2. [A Byte of Python](http://byteofpython-korean.sourceforge.net/byte_of_python.html)    
    3. [codecademy](https://www.codecademy.com/)    