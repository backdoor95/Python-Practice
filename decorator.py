import time

def elapsed(original_func):
  def wrapper():
    start = time.time()
    result = original_func()# 기존함수 수행
    end = time.time()
    print("함수 수행시간: %f 초" %(end - start))
    return result
  return wrapper

# 파이썬은 함수 위에 [@+함수명] 있으면 데코레이터 함수로 인식한다.
@elapsed 
def myfunc():
  print("함수가 실행됩니다.")


decorated_myfunc = elapsed(myfunc)



