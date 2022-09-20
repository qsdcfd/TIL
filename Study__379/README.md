# 테스트와 디버깅

## Intro  

 파이썬은 컴파일 시점에 정적 타입 검사를 수행하지 않는다.
 
 파이썬 인터프리터가 컴파일 시점에 프로그램이 제대로 작동할 것이라고 확인할 수 있는 요소가 전혀 없다.
 
 파이썬은 선택적인 타입 애너테이션을 지원하여 정적 분석을 수행하여 감지 가능하다.
 
 디버깅을 해야 프로그램 실행 시 생길 위험을 방지할 수 있다.
 
 파이썬의 동적 기능을 사용하여 프로그램의 동작을 오버라이드함으로써 테스트를 구현하고 프로그램이 예상대로 작동하는지 확인한다.
 
 <br>
 
 ## 디버깅 출력에는 repr 문자열 사용
 
 - 파이썬 프로그램 디버깅
 
    - print함수
    	- 상태의 변화를 통해서 무엇이 잘못되었는지 확인
    
    - 형식화 문자열 사용
    
    - loggging 내장 모듈 사용하여 출력
 
 
```
'''
여러 방법 , 동일 결과

값을 print에 전달하기 전에 str 호출

% 연산자에. '%s' 형식화 문자열을 사용

f-문자열에서 값을 표시하는 기본 형식화 방식을 사용

format 내장 함수를 호출한다.

__format__ 특별 메서드를 명시적으로 호출

__str__ 특별 메서드를 명시적으로 호출
'''

#foo 뭐시기

print('foo 뭐시기')
myvalue = 'foo 뭐시기'
print(str(my_value)
print('%s' % my_value)
print(f'{my_value}')
print(format(my_value))
print(my_value.__format__('s'))
print(my_value.__str__())
```

<br>

**어떤 값을 사람이 읽을 수 있는 형식의 문자열로 바꿔도 이 값의 실제 타입과 구체적인 구성을 명확히 알기 어렵다**

```
#Print: 숫자 5와 문자 5를 구분하지 못한다

print(5)
print('5')

int_value = 5
str_value = '5'
print(f'{int_value} == {str_value} ?')
```

<br>

**디버깅 과정에서 print 사용 시 타입 문제로 제대로 되지 못한다. 그래서 이때 사용하는 방법이 repr을 활용하여 모든 문자를 나타내고, repr 내장 함수는 객체의 출력 가능한 표현을 반환하여 출력 가능한 표현은 반드시 객체를 분명하게 이해할 수 있는 문자열 표현**

```
#내장 타입에서 repr이 반환하는 문자열은 올바른 파이썬 식
a = '\x07'
print(repr(a)) # '\x07'

#repr이 돌려준 값을 eval 내장 함수에 넘기면 repr에 넘겼던 객체와 같은 객체가 생성 (eval호출은 조심스럽게 한다.)

b = eval(repr(a))
assert a ==b

#print사용해서 디버길할 때는 출력 전 repr을 호출하여 타입이 다른 경우에도 명확한 차이를 볼 수 있게 한다.

print(repr(5)) # 5
print(repr('5')) #'5'

#repr을 호출하는 것은 %연산자에 %r 형식화 문자열을 사용하는 것이나 f-문자열에 !r 타입 변환

print('%r" % 5) # 5
print('%r' % '5') # '5'

int_value = 5 
str_valure = '5'
print(f'{int_value!r} != {str_value!r}') # 5 ! = '5'
```

<br>

**클래스의 영우 사람이 읽을 수 있는 문자열 값은 repr값과 같고 print 넘기면 원하는 출력이 나와서 굳이 repr 호출 이유가 없다. 즉, object 상속한 하위 클래스 repr 기본 구현은 의미가 없다.**

```
class OpaqueClass:
	def __init__(self,x,y):
    	self.x = x
        self.y = y
        
obj = OpaqueClass(1, 'foo')
print(obj)

# eval 함수에 넘길 수도 없고, 객체의 인스턴스 필드 정보도 전혀 없다
```

<br>

### 해결 방법 1: 클래스 소스 코드를 변경할 수 있다면 다시 파이썬 식을 포하하는 문자열을 돌려주는 __repr__ 특별 메서드 정의


