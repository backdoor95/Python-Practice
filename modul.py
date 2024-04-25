
import mod1
print(mod1.add(3,4))
print(mod1.sub(5,2))


## import 모듈_이름
# from 모듈_이름 import 모듈_함수

# 
from mod1 import add
from mod1 import add, sub
from mod1 import * # 모든 함수를 불러와서 사용하겠다는 의미


# 다른 디렉터리에 있는 모듈을 불러오는 방법
#                    1. sys.path.append 사용하기
import sys
# sys모듈을 사용하면 파이썬 라이브러리가 설치되어 있는 디렉터리 확인가능
print(sys.path)

sys.path.append("C:\\Users\\JH\\Desktop\\python\\DoIt\\Python-Practice\\mymod") ## 경로표시할때 \\ 해야함. 한개(\)로는 안됨.
# 이렇게 추가하면 파이썬 모듈을 어디에서든 바로 불러서 사용가능
print(sys.path)

import mod2
print(mod2.PI)
a = mod2.Math()
print(a.solv(2))
print(mod2.add(mod2.PI,4.4))


#                  2. PYTHONPATH 환경 변수 사용하기
set PYTHONPATH = C:\\Users\\JH\\Desktop\\python\\DoIt\\Python-Practice\\mymod

