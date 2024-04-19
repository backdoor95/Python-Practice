
# 집합 자료형
#리스트 넣기
s1 = set([1,2,3])
print(s1)
#문자열 넣기
s2 = set("hello")
print(s2)
# 비어있는 집합
s_empty = set()



#set 자료형의 특징
# 1. 중복 허용 x
# 2. 순서가 없다. => 인덱싱 불가능
# 인덱싱을 하려면 리스트나 튜플로 변환 후에 사용해야함.
li = list(s1)
li[0]  
tp = tuple(s1)
tp[0]



# 교집합, 합집합, 차집합 구하기
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

#교집합
s1&s2
s1.intersection(s2)
s2.intersection(s1)

#합집합
s1|s2
s1.union(s2)
s2.union(s1)

#차집합
s1-s2 
s1.difference(s2)

s2-s1
s2.difference(s1)


#집합 자료형 관련 함수
#add
s1 = set([1,2,3])
s1.add(4)
print(s1)
#update : 여러 개의 값을 한번에 추가할 때.
s1 = set([1,2,3])
s1.update([4,5,6])
print(s1)
#remove : 특정값 제거
s1 = set([1,2,3])
s1.remove(2)
print(s1)