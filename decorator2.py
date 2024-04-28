# 데코레이터 함수는 기존함수의 입력인수에 상관없이 동작하도록 만들어야함.
# 
import time

def elapsed(original_func):
  def wrapper(*args, **kwargs):
    start = time.time()
    result = original_func(*args, **kwargs)
    end = time.time()
    print("함수 수행시간: %f 초" %(end-start))
    print("args = ", args)
    print("kwargs = ", kwargs)
    return result
  return wrapper

@elapsed
def myfunc(msg):
  print("'%s'을 출력합니다" %msg)
  
myfunc("You need python")
''''

*args와 kwargs
*args는 모든 입력 인수를 튜플로 변환하는 매개변수, **kwargs는 모든 ‘키=값’ 형태의 입력 인수를 딕셔너리로 변환하는 매개변수이다. 다음과 같은 형태의 호출을 살펴보자.

>>> func(1, 2, 3, name='foo', age=3)
func 함수가 입력 인수의 개수와 형태에 상관없이 모든 입력을 처리하려면 어떻게 해야 할까?

>>> def func(*args, **kwargs):
...     print(args)
...     print(kwargs)
... 
>>> func(1, 2, 3, name='foo', age=3)
(1, 2, 3)
{'age': 3, 'name': 'foo'}
이처럼 func 함수에 *args, **kwargs라는 매개변수를 지정하면 다양한 입력 인수를 모두 처리할 수 있다. 이렇게 하면 1, 2, 3 같은 일반 입력은 args 튜플, name = 'foo'와 같은 ‘키=값’ 형태의 입력은 kwargs 딕셔너리로 저장한다.


'''