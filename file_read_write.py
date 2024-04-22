
############## 내용 쓰기 ####################
# 파일 객체 = open(파일_이름, 파일_열기_모드)
# 파일 열기 모드 종류 : 1.r(읽기모드) | 2.w(쓰기모드) | 3.a(추가모드)
f = open("textfile01.txt", "w")


f.close() # 열려있는 파일을 직접 닫아 주는게 좋다.
# 열었던 파일을 닫지 않고 다시 사용하려고 하면 오류 발생


# 경로를 표현할떄는 '/'는 한번만, '\'는 '\\'어렇게 2번씩 사용해야함.

#f = open("textfile02.txt", "w", encoding="UTF-8")
f = open("textfile02.txt", "w")
for i in range(1,10):
    data = "%d번째 줄 입니다.\n" %i
    f.write(data)
f.close()




############## 내용 읽기 ###############
#f = open("textfile02.txt", "r", encoding="UTF-8")
f = open("textfile02.txt", "r")
line = f.readline()
print(line)
f.close()

f = open("textfile02.txt", "r")
while True:
    line = f.readline()
    if not line: break# 더 이상 읽을 줄이 없으면 break를 수행
    print(line)
f.close()

#= 한 줄씩 읽어 출력할 때 줄 끝에 \n 문자가 있다.


f = open("textfile02.txt", "r")
lines = f.readlines()
for line in lines:
    print(line, end="")
f.close()

print("############################")
# \n 문자 제거하기
f = open("textfile02.txt", 'r')
lines = f.readlines()
for line in lines:
    line = line.strip()  # 줄 끝의 줄 바꿈 문자를 제거한다.
    print(line)
f.close()

########## read 함수 사용하기

print("############################")
f = open("textfile02.txt", "r")
data = f.read() # 문자열 전체를 리턴한다.
print(data)
f.close()


########### 파일 객체를 for문과 함께 사용하기 ##############
f = open("textfile02.txt", "r")
for line in f:
    print(line, end= "")
f.close()


############ 파일에 새로운 내용추가하기 ###############
f = open("textfile02.txt", "a")
for i in range(11,21):
    data = "%d번째 줄입니다.\n" %i
    f.write(data)
f.close()

f = open("textfile02.txt", "r")
data = f.read()
print(data)
f.close()

######### with 문과 함께 사용하기 #############
# open , close를 자동으로 해주는 역할. == with
with open("textfile02.txt","a") as f:
    f.write("with 명령어 테스트")
with open("textfile02.txt","r") as f:
    print(f.read())
    