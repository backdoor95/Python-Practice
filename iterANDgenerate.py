print("test")
# for a in [1,2,3]:
#   print(a)
print("Iter & Generate")
# # [1,2,3]을 for문으로 차례대로 하나씩 출력하는 예제
# # for 문과 같은 반복 구문에 적용할 수 있는 리스트와 같은 객체를 
# # '반복 가능(iterable) 객체'라고 함.

# b = [1,2,3]
# print(type(b))
# ib = iter(b) # iter함수를 사용해서 이터레이터로 만들기
# print(type(ib))


# print(next(ib))
# print(next(ib))
# print(next(ib))
# print(next(ib))

# 이터레이터의 값을 가져오는 가장 일반적인 방법은 for문을 이용하는 것
# 이터레이터는 재사용 불가

# 이터레이터 만들기
# 1. __iter__
# 2. __next__ 2개의 메서드 구현 2개를 같이 구현해야한다. 반드시!!
# class MyItertor:
#   def __init__(self, data):
#     self.data = data
#     self.position = 0
    
#   def __iter__(self):
#     return self
  
#   def __next__(self):
#     if self.position >= len(self.data):
#       raise StopIteration
#     result = self.data[self.position]
#     self.position += 1
#     return result
  

# i = MyItertor([1,2,3])
# for item in i:
#   print(item)