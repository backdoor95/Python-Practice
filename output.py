### 사용자 입력 활용하기
# input 사용
a = input()
print(a)

# 프롬프트를 띄워 사용자 입력받기 
# input("안내 문구")
number = input("숫자 입력 : ") #주의 input은 모든것을 문자열로 취급하기 때문에 number는 숫자가 아닌 문자열이라는 것에 주의
print(number)
type(number)

# 큰따옴표로 둘러싸인 문자열은 +연산과 동일
print("life" " is " "too short")
print("life"+" is "+"too short")
print("life","is","too short")


for i in range(10):
  print(i, end = ' ')