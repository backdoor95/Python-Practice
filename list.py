
odd = [1,3,5,7,9]

# 비어있는 리스트는 list()로 생성할 수 있다.
a = []
b = [1,2,3]
c = ['apple', 'samsung', 'nvida']
d = [1,2, 'life', 'google']

a = [1, 2, 3, ['a', 'b', 'c']]

print(a[0])
print(a[-1])
print(a[-1][0])

#리스트의 슬라이싱
a = [1,2,3,4,5]
print(a[0:2])

a = "54345"
print(a[0:2])

#리스트 연산하기
a = [1,2,3]
b = [4,5,6]
c = a + b
print(c)

#곱하기
c = a*4
print(c)

#길이 구하기
a = [1,2,3]
c = len(a)
print(c)


#c = a[0]+"hello" #이렇게 하면 타입이 맞지 않아서 오류
c = str(a[0]) + "hello"
print(c)


#리스트 값 수정
a = [1, 2, 3]
a[2] = 4
print(a)


# del 함수사용해서 요소 삭제
a = [1, 2, 3]
del a[1]
print(a)

del a[2:]
print(a)

#리스트 관련함수
a = [1, 2, 3]

# 요소 추가
a.append(7)
print(a)

a.append([8,9])
print(a)

#리스트 정렬

#TypeError: '<' not supported between instances of 'list' and 'int'
# a.sort()
# print(a)

a = ['z', 'c', 'i', 'q']
a.sort()
print(a)

# 리스트 뒤집기
a.reverse()
print(a)

# 인덱스 반환
a = [1,2,3]
# 리스트에 값이 있다면 해당 값의 인덱스값을 리턴
# 값이 없다면 에러발생
print(a.index(3))

#리스트에 요소 삽입 - insert
# insert(a,b) 리스트의 a번째 위치에 b를 삽입 = 파이썬은 숫자를 0부터 센다는것 기억
a = [1,2,3]
a.insert(0,4)
print(a)

a.insert(3,5)
print(a)

#리스트 요소 제거 = remove
# 리스트에서 첫번쨰로 나오는 x를 삭제하는 함수.

a = [1, 2, 3, 1, 2, 3]
a.remove(3)
print(a)

#리스트 요소 끄집어 내기 - pop
#맨 마지막 요소를 리턴하고 그 요소는 삭제
a = [1,2,3]
print(a.pop())
print(a)

#리스트에 포함된 요소의 개수 세기 - count
a = [1, 2, 3, 1]
b = a.count(1)
print(b)

#리스트 확장 - extend
a = [1,2,3]
a.extend([4,5])
print(a)
'''

a.extend([4, 5])는 a += [4, 5]와 동일 | append와 미세하게 다름.
>>> a = [1, 2, 3]
>>> a.extend([4, 5])
>>> a
[1, 2, 3, 4, 5]
>>> b = [6, 7]
>>> a.extend(b)
>>> a
[1, 2, 3, 4, 5, 6, 7]


'''

