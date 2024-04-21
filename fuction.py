
# 함수
def add(a,b):
   return a+b

print(add(3, 5))

def say():
   print("hello")
   
say()

def sub(a,b):
   return a-b

print(sub(40,-18))

# 매개변수를 지정하여 호출하기

result = sub(b=2, a=9)# 이렇게 지정하면, 순서에 상관없이 사용할 수 있다.

#입력값이 몇 개가 될지 모를때
def add_many(*args): #매개변수 이름 앞에 * 를 붙이면 입력값을 전부 모아 튜플로 만들어준다.
   result = 0 
   for i in args:
      result += i
   return result
# 관례적으로 arguments의 약자인 args를 많이 사용한다.
def add_many2(*qm):
   result = 0 
   for i in qm:
      result += i
   return result

print(add_many(1,2,5,7,9))
print(add_many2(1,2,3,4,5,6,7,8,9,10))

def add_mul(choice, *args):
   if choice == "add":
      result = 0
      for i in args:
         result += i
   elif choice == "mul":
      result = 1
      for i in args:
         result *= i
         
   return result

print(add_mul("mul", 1,2,3,4,5))

## 키워드 매개변수
## **kwargs
def print_kwargs(**kwargs): #이때 kwargs는 딕셔너리가 된다. - 딕셔너리는 key - value 이다.
   print(kwargs)
   
print_kwargs(a=1)
print_kwargs(name='foo', age=3)
'''
{'a': 1}
{'name': 'foo', 'age': 3}
'''
#함수의 리턴값은 오직 하나
def add_and_mul(a,b):
   return a+b, a*b
# 위에 처럼 return을 하게 된다는 오류는 안난다. 다만, 튜플 하나로 리턴하게 된다. (a+b, a*b)로 return

res = add_and_mul(3,4)
print(res) # (7, 12)

# 하나의 튜플을 2개의 값으로 분리해서 받고 싶을때
res1 , res2 = add_and_mul(4,5)
print(res1)
print(res2)

def say_nick(nick):
   if(nick == 'tomato'):
      return
   print("나의 별명은 %s 입니다." %nick)
   
say_nick("hihih")
say_nick("tomato")
      

### 매개변수에 초기값 미리 설정하기
def say_myself(name, age, man=True): # man 변수에 입력값을 주지 않으면 초기값 true을 갖게 됨.
   print("이름 = %s" %name)
   print("나이 = %d" %age)
   if(man):
      print("male")
   else:
      print("female")

say_myself("문호", 30)
say_myself("문호", 30, True) # 위에 코드와 동일한 결과


# def say_myself2(name, man=True, age): # 초기값을 설정한 매개변수의 위치를 마지막이 아닌 중간에 위치시킨다면 오류 발생함. ==>
#    #에러 메시지 = SyntaxError: parameter without a default follows parameter with a default
#    print("이름 = %s" %name)
#    print("나이 = %d" %age)
#    if(man):
#       print("male")
#    else:
#       print("female")
      
# 결론 초기화하고 싶은 매개변수는 항상 뒤에 놔야한다.

###### 함수 안에서 선언한 변수의 효력 범위

a = 1
def vartest(a):
   a = a+ 1
vartest(a)
print(a)


### 함수 안에서 함수 밖의 변수를 변경하는 방법
# 1.return 사용하기
a = 1
def vartest2(a):
   a = a+ 1
   return a
a = vartest2(a)
print(a)

# 2. global 명령어 사용하기
a = 1
def vartest3():
   global a# 함수 밖의 a 변수를 직접 사용하겠다는 의미. 코딩할 때는 global를 사용하지 않는 것이 좋다.
   #외부 변수에 종속적인 함수는 좋은 함수가 아니다.
   a = a+ 1 
   
##### lambda 예약어
# 함수이름 = lambda 매개변수1, 매개변수2 .... : 매개변수를 이용한 표현식
add = lambda a, b : a+b
result = add(3,4)
print(result)
