
print("Python's favorite food is perl")

# 작은따옴표 안에 사용된 큰 따옴표는 무나자열을 만드는 기호로 인식되지 않음.
print('"Python is very easy." he says')

# 이 부분은 에러가 남.
##print('Python's favorite food is perl')

food = 'Python\'s favorite food is perl'
say = "\"Python is very easy.\" he says."
print(food)
print(say)

#  \n = 이스케이프 코드
multiline = "Life is too short\nYou need python"
print(multiline)

multiline = '''
 Life is too short
 You need python
 '''
print(multiline)


# \n 대신에 '''abcd''' or """abcd"""

#문자열 더하기
#문자열 더해서 연결
head = "Python"
tail = " is fun!"
str = head + tail
print(str)

#문자열 곱하기
a = "python "
b = a * 2
print(b)

#문자열 곱하기 응용
# multistring.py

print("=" * 50)
print("My Program")
print("=" * 50)

print("한글 깨짐 테스트 출력")

len(a)
print(len(a))

# 파이썬은 0부터 인덱싱
a = "Life is too short, You need Python"

# 0은 기호를 붙여도 그냥 0
print(a[-0])
print(a[+0])

'''
슬라이싱 기법으로 a[시작_번호:끝_번호]를 지정할 때
끝 번호에 해당하는 문자는 포함하지 않기 때문이다.
즉, a[0:3]을 수식으로 나타내면 다음과 같다.
>>> a[0:3]
'Lif'
0 <= a < 3
'''

print(a[19:])
print(a[:17])

#a[시작_번호:끝_번호]에서 시작 번호와 끝 번호를 생략하면 문자열의 처음부터 끝까지 뽑아 낸다.
print(a[:])


#슬라이싱 문자열 나누기
a = "20240416"


# 문자열 포맷팅

num = 3
print("난 사과 %d개를 가지고 있다." %num)

numStr = "다섯"
print("난 전공책 %s개 가지고 있다." %numStr)

#2개 이상의 값을 넣으려면 마지막 % 다음 괄호 안에 쉼표(,)로 구분하여 각각의 값을 넣어 주면 된다.
print("난 사과 %d개, 전공책 %s개 소유중이다." %(num, numStr))

# %s 포맷 코드는 실수, 정수 전부 문자열로 바꾸어 표현함.

# 만약에 %d와 %를 같이 쓸때 [%%]를 사용한다.
print("%d%% 확률" %num)


#format함수

str10 = "I eat {0} cookies.".format(8)
print(str10)

'''
2개 이상의 값을 넣을 경우,
문자열의 {0}, {1}과 같은 인덱스 항목이 format 함수의 입력값으로 순서에 맞게 바뀐다.
위 예에서 {0}은 format 함수의 첫 번째 입력값인 number, {1}은 format 함수의 두 번째 입력값인 day로 바뀐다
'''
number = 10
day = "three"
str11 = "I ate {0} apples. so I was sick for {1} days.".format(number, day)
print(str11)


#정렬

# 왼쪽 정렬
print("{0:<10}".format("hi"))
# 오른쪽 정렬
print("{0:>10}".format("hi"))
# 가운데 정렬
print("{0:^10}".format("hi"))

# 정렬하면서 공백 채우기
# [=]으로 공백 채우기
print("{0:=^10}".format("hi"))
# [!]으로 공백 채우기
print("{0:!<10}".format("hi"))

# 소수점 표현법
print("%0.5f" %3.413679)#이렇게 하면 반올림을 한다.
print("%.5f" %3.413679)#이렇게 하면 반올림을 한다.
print("%10.5f" %3.413679)#이렇게 하면 반올림을 한다.

y = 3.42134234
print("{0:0.4f}".format(y))


# 문자열 관련 함수

#문자 개수 세기
a = "hobby"
print(a.count('b'))

#위치 알려주기1- find == 문자 or 문자열 둘다 가능
# 만약에 찾고자하는 문자 또는 문자열이 없다면 -1 반환
# 파이썬은 0부터 세기 때문에 실제 위치는 출력값에서 1을 더해주면 된다.
a = "Python is the best choice bye bound bbq"
num = a.find("bbq") # b가 처음나온 위치
print("a의 길이는 = %d" %len(a))
print(num)


#위치 알려주기2 - index
# find와 다른점은 존재하지 않는 문자인덱스를 찾으면 에러가 발생 나머지는 동일
a = "Life is too short apple candy"
num = a.index("candy")
print(num)

#문자열 삽입 - join
#join 함수는 문자열뿐만 아니라 앞으로 배울 리스트나 튜플도 입력으로 사용할 수 있다
s = ",".join('abcd')
print(s)
s = ",".join(['a', 'b', 'c', 'd'])
print(s)

# 소문자|대문자 변환
a = "hi"
a = a.upper()
print(a)

a = "HI"
a=a.lower()
print(a)

#공백 지우기
b = "     strip test  ssetterewwdfsjls                     "
print(b.lstrip())
print(b.rstrip())
print(b.strip())

#문자열 바꾸기
a = "Life is too short"
a = a.replace("Life", "money")
print(a)

#문자열 나누기 - split
# split() 이렇게 한다면 space, tab, enter 을 기준으로 문자열을 나눈다.
a = "Life is too short"
print(a.split())

b = "a:b:c:d"
print(b.split(':'))
