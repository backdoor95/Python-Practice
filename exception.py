print("EXCEPTION!")

# FileNotFoundError, ZeroDivisionError,IndexError
# 오류 예외 처리 기법

'''

try:
  ...
except [발생오류 [as 오류변수]]: # []안 내용 생략 가능
  ...
  
'''

'''
1. try - except 만 사용
오류의 종류에 상관없이 오류가 발생하면 except 블록 수행

try:
  ...
except:
  ...
  
'''

'''
2. 발생 오류 포함한 except문
오류 발생시 except문에 미리 정해 놓은 오류와 동일한 오류일 경우에만 except 블록 수행

try:
  ...
except 발생오류:
  ...
  
'''

'''
3. 발생 오류와 오류 변수까지 포함한 except 문

try:
    ...
except 발생오류 as 오류변수:
    ...
  
'''
# # try_except.py
# try:
#     4 / 0
# except ZeroDivisionError as e:
#     print(e)
# #division by zero


'''
 finally 절은 try 문 수행 도중 예외 발생 여부에 상관없이 항상 수행된다. 보통 finally 절은 사용한 리소스를 close해야 할 때 많이 사용한다.
# try_finally.py
try:
    f = open('foo.txt', 'w')
    # 무언가를 수행한다.

    (... 생략 ...)

finally:
    f.close()  # 중간에 오류가 발생하더라도 무조건 실행된다.

'''

# 여러개의 오류 처리
'''
try:
    ...
except 발생오류1:
   ... 
except 발생오류2:
   ...

'''
try:
    a = [1,2]
    print(a[3])
    4/0
except (ZeroDivisionError, IndexError) as e:
    print(e)


# try - else 문
'''

try:
    ...
except [발생오류 [as 오류변수]]:
    ...
else:  # 오류가 없을 경우에만 수행
    ...

'''
ValueError
# try_else.py
try:
    age=int(input('나이를 입력하세요: '))
except:
    print('입력이 정확하지 않습니다.')
else:
    if age <= 18:
        print('미성년자는 출입금지입니다.')
    else:
        print('환영합니다.')

## 오류 회피
# error_pass.py
try:
    f = open("나없는파일", 'r')
except FileNotFoundError:
    pass


# 오류 일부러 발생시키기
# error_raise.py
class Bird:
    def fly(self):
        raise NotImplementedError
#NotImplementedError는 파이썬에 이미 정의되어 있는 오류로, 꼭 작성해야 하는 부분이 구현되지 않았을 경우 일부러 오류를 발생시키기 위해 사용한다.
#상속받는 클래스에서 메서드를 재구현하는 것을 ‘메서드 오버라이딩’이라고 한다

class Eagle(Bird):
    def fly(self):
        print("very fast")

eagle = Eagle()
eagle.fly()


# 예외 만들기
# error_make.py
# 오류 메시지를 출력했을 때 오류 메시지가 보이게 하려면
# 오류 클래스에 다음과 같은 __str__ 메서드를 구현해야 한다.
# __str__ 메서드는 print(e)처럼 오류 메시지를 print 문으로 출력할 경우에 호출되는 메서드이다.
class MyError(Exception):
    def __str__(self):
        return "허용되지 않는 별명입니다."

# 
def say_nick(nick):
    if nick == '바보':
        raise MyError()
    print(nick)
    

try:
    say_nick("천사")
    say_nick("바보")
except MyError as e:
    print(e)




