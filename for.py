
# for 문의 기본 구조
'''

for 변수 in 리스트(또는 튜플, 문자열):
    수행할_문장1
    수행할_문장2
    ...


'''

# 전형적인 for문
# 1
test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)
    
#2
a = [(1,2), (3,4), (5,6)]
for (first, last) in a:
    print(first + last)

#3 for문의 응용
marks = [90, 25, 67, 45, 80]

number = 0
for mark in marks:
    number += 1
    if mark >= 60:
        print("%d번 학생은 합격" %number)
    else:
        print("%d번 학생은 불합격" % number)
        


# marks2.py
marks = [90, 25, 67, 45, 80]
# for문과 continue문
number = 0 
for mark in marks: 
    number = number +1 
    if mark < 60:
        continue 
    print("%d번 학생 축하합니다. 합격입니다. " % number)


# for문과 함께 자주 사용하는 range함수

r = range(10)
print(r) # range(10)은 0부터 10 미만의 숫자를 포함하는 range 객체를 만들어 준다.


add = 0
for i in range(1,11):
    add = add + i
    
print(add)

# marks3.py
marks = [90, 25, 67, 45, 80]
#range(5)가 될 것이다. number 변수에는 차례로 0부터 4까지의 숫자가 대입
for number in range(len(marks)):
    if marks[number] < 60 :
        continue
    print("%d번 학생 축하합니다. 합격!" %(number+1))
    

for i in range(2,10):        # 1번 for문
     for j in range(1, 10):   # 2번 for문
         print(i*j, end=" ") 
     print('') 
     
# print(i*j, end=" ")와 같이 print 함수에 end 파라미터를 설정한 이유는 해당 결괏값을 출력할 때 다음 줄로 넘기지 않고 그 줄에 계속 출력하기 위해서이다. 
# print 문의 end 매개변수에는 줄바꿈 문자(\n)가 기본값으로 설정되어 있다.


#리스트 컴프리헨션 사용
# 사용 x
'''
>>> a = [1,2,3,4]
>>> result = []
>>> for num in a:
...     result.append(num*3)
...
>>> print(result)
[3, 6, 9, 12]
'''
# 사용 o
a = [1,2,3,4]
result = [num * 3 for num in a]
print(result)


a = [1,2,3,4]
result = [num*3 for num in a if num%2 == 0]

''' [표현식 for 항목 in 반복_가능_객체 if 조건문] '''