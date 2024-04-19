
a = 1
b = "python"
c = [1,2,3]

# 파이썬에서 사용하는 변수는 객체를 가리키는 것.
a = [1,2,3]
id(a) # 메모리 주소확인


#리스트를 복사할때
#얕은 복사
a = [1,2,3]
b = a
id(a)
id(b)
## 서로 동일한 결과가 나온다.

a is b # is : a와 b가 가리키는 객체가 같을지 확인하는 명령어


#깊은 복사
#방법 1 : [:] 사용하기
a = [1,2,3] 
b = a[:]
a[1] = 4
print(a)
print(b)
print(id(a))
print(id(b))
print(a is b)

from copy import copy
a = [1,2,3]
b = copy(a)
b = a.copy()

print(id(a))
print(id(b))
print(a is b)

# tuple로 a, b에 값을 대입
# 튜플은 괄호를 생략해도됨.
c, d = ('python', 'life')
(c, d) = 'python', 'life'
c = 100

#리스트로 변수 만들기
[a, b] = ['python', 'life']

#변수의 값을 간단하게 바꾸는 법
a = 3
b = 5
a, b = b, a

