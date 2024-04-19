# bool 자료형
# True, False 반환- > 파이썬의 예약어
# 첫 문자를 항상 대문자로 작성.



a = True
b = False
type(a)
type(b)

1==1
True

2<1
False

#문자열, 리스트, 튜플, 딕셔너리 들의 값이 비어 있으면 ("", [], (), {})
# 비어있으면 거짓
# 숫자는 그 값이 0일 때 거짓, None도 거짓을 의미

a = [1,2,3,4]
while a:
    print(a.pop())

if []:
    print("참")
else: #else 뒤에도 [:]를 붙여야함.
    print("거짓")
    
    
if [1,2,3]:
    print("참")
else:
    print("거짓")


#불 연산 - bool함수를 사용하면 자료형의 참과 거짓을 식별가능
bool('')
bool('python')
