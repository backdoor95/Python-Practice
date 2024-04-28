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

# '''
# 1
# 2
# 3
# Traceback (most recent call last):
#   File "c:\Users\JH\Desktop\python\DoIt\Python-Practice\iter_generate.py", line 19, in <module>
#     print(next(ib))
#           ^^^^^^^^
# StopIteration
# '''

# 이터레이터의 값을 가져오는 가장 일반적인 방법은 for문을 이용하는 것
# 이터레이터는 재사용 불가

# 이터레이터 만들기
# 1. __iter__
# 2. __next__ 2개의 메서드 구현 2개를 같이 구현해야한다. 반드시!!
class MyItertor:
  def __init__(self, data):
    self.data = data
    self.position = 0
    
  def __iter__(self):
    return self
  
  def __next__(self):
    if self.position >= len(self.data):
      raise StopIteration
    result = self.data[self.position]
    self.position += 1
    return result
  

i = MyItertor([1,2,3])
for item in i:
  print(item)
  
# reviterator.py
class ReverseItertor:
    def __init__(self, data):
        self.data = data
        self.position = len(self.data) -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.position < 0:
            raise StopIteration
        result = self.data[self.position]
        self.position -= 1
        return result

if __name__ == "__main__":
    i = ReverseItertor([1,2,3])
    for item in i:
        print(item)


## 제너레이터
# -> 이터레이터를 생성해 주는 함수.
# return 대신에 yield 키워드 사용
def mygen():
  yield 'a'
  yield 'b'
  yield 'c'
  
  # 제너레이터는 yield라는 문장을 만나면 그 값을 리턴하되 현재 상태를 그대로 기억한다는 것이다. 이것은 마치 음악을 재생하다가 일시 정지 버튼으로 멈춘 것과 비슷한 모양새이다.
  
# generator.py
def mygen():
    for i in range(1, 1000):
        result = i * i
        yield result

gen = mygen()

print(next(gen))
print(next(gen))
print(next(gen))

gen = (i * i for i in range(1, 1000))

# 제너레이터 vs 이터레이터

# generator2.py
import time

def longtime_job():
    print("job start")
    time.sleep(1)  # 1초 지연
    return "done"

list_job = [longtime_job() for i in range(5)]
print(list_job[0])
print(list_job[1])
print(list_job[2])
print(list_job[3])
print(list_job[4])

# job start
# job start
# job start
# job start
# job start
# done
# done
# done
# done
# done

#######################################
# generator2.py
import time

def longtime_job2():
    print("job start")
    time.sleep(1)
    return "done"

list_job = (longtime_job2() for i in range(5))
print(next(list_job))
