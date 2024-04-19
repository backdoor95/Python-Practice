# 딕셔너리 
# key : value
# 딕셔너리는 사전
# { }으로 둘러싸여 있다.
# 문자열은 작은따옴표(''), 큰따옴표("")으로 만들수 있다.

dic = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}

a = {1: 'hi'}


a = {'a': [1, 2, 3]}

#딕셔너리 쌍 추가
# 주의 [ ]안에 들어가는것은 key 값이다. 인덱스가 아니다.
a = {1:'a'}
a[2] = 'b'
print(a)
# output = {1: 'a', 2: 'b'}

a['name'] = 'pey'
print(a)
# output = {1: 'a', 2: 'b', 'name': 'pey'}

a[3] = [1,2,3]
print(a)
#output = {1: 'a', 2: 'b', 'name': 'pey', 3: [1, 2, 3]}



## del 
# del를 사용하면 {Key: Value} 쌍이 삭제

del a[1]
print(a)
#output = {2: 'b', 'name': 'pey', 3: [1, 2, 3]}


#딕셔너리에서 key를 사용해 value얻기
grade = {'pey': 10, 'julliet': 99}
v = grade['pey']
print(v)
v = grade['julliet']
print(v)

# 딕셔너리 만들 때 주의점.
# key는 고유한 값, 중복되는 key 값을 설정해 놓으면 하나를 제외한 나머지 것들이 모두 무시됨.

a = {1:'a', 1:'b'}
print(a)
#output = {1: 'b'}

# 주의!! : TypeError: unhashable type: 'list' key에는 리스트가 못들어간다. 단, 튜플은 들어갈수 있다.
# 이런 차이가 발생하는 이유는 key가 가변(list)/불변(tuple)에 따라서 달라진다.
# a = {[1,2] : 'hello'}
# print(a)

#튜플은 key가 될수 있다.
a = {(5,7):"tuple test"}
print(a)


#딕셔너리 관련함수
# 1) key 리스트 만들기 - keys
# dict_keys 객체를 리턴한다.
# 만약에 객체를 리스트로 변경하고 싶으면, list(a.keys()) 를 사용하자.
a = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
print(a.keys()) #output = dict_keys(['name', 'phone', 'birth'])

# value 리스트 만들기 -values
print(a.values())
#output = dict_values(['pey', '010-9999-1234', '1118'])
# dict_values 객체를 리턴한다.

#key, value 쌍 얻기 -items
print(a.items())
# dict_items([('name', 'pey'), ('phone', '010-9999-1234'), ('birth', '1118')])
# items함수는 key, value의 쌍을 튜플(tuple)로 묶은 값을 dict_items객체로 리턴


