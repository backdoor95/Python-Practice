'''
if 조건문:
    수행할_문장1
    수행할_문장2
    ...
else:
    수행할_문장A
    수행할_문장B
    ...
'''
# 조건문 뒤에 : 이 붙는다.
money = True

if money:
    print("돈은 True")

# 들여쓰기 오류 발생하는 경우 
# 들여쓰기를 할때 각각 들여쓰기 '깊이'를 다르게 했을 경우


# and , or, not
a , b = True, False
card = True
money = False

'''
>>> money = 2000
>>> card = True
>>> if money >= 3000 or card:
...     print("택시를 타고 가라")
... else:
...     print("걸어가라")
...
택시를 타고 가라
>>>
'''

# in, not in
'''
>>> 1 in [1, 2, 3]
True
>>> 1 not in [1, 2, 3]
False
'''

# 조건문에서 아무 일도 하지 않게 설정 => pass
pocket = ['paper', 'money', 'cellphone']
if 'money' in pocket:
    pass
else:
    print("카드 꺼내")
    


'''

if 조건문:
    수행할_문장1 
    수행할_문장2
    ...
elif 조건문:
    수행할_문장1
    수행할_문장2
    ...
elif 조건문:
    수행할_문장1
    수행할_문장2
    ...
...
else:
   수행할_문장1
   수행할_문장2
   ... 

'''


# if 문을 한 줄로 작성하기
if 'money' in pocket: pass
else: print("card")

#기존 if 문
score =90
if score >= 50:
    message = "success"
else:
    message = "failure"
    
# 조건부 표현식 예시 = 가독성에 유리하고 한 줄로 작성할 수 있어서 활용성 좋음.
message = "success" if score >= 60 else "failure"

    