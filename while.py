treeHit = 0
while treeHit < 10:
    treeHit += 1
    print("나무를 %d번 찍음" %treeHit)
    if treeHit == 10:
        print("나무 쓰러짐.")
        
prompt = """
... 1. Add
... 2. Del
... 3. List
... 4. Quit
...
... Enter number: """

number = 0
while number != 4:
    print(prompt)
    number = int(input()) #사용자의 숫자 입력을 받아들이는 것.

# while문 강제로 빠져나가기
