#파이썬 패키지는 디렉터리와 파이썬 모듈로 이루어진다

import sys
print(sys.path)

sys.path.append("C:\\Users\\JH\\Desktop\\python\\DoIt\\Python-Practice")

print("++++++++++++++++++++start++++++++++++++++++++")
import game.sound.echo

game.sound.echo.echo_test()

print("+++++++++++++++++++++++++++++++++++++++++++++")
from game.sound.echo import echo_test
echo_test()


# __init__.py 용도
# __init__.py는 해당 디렉터리가 패키지의 일부임을 알려주는 역할
# 패키지에 포함된 디렉터리에 __init__.py파일이 없다면 패키지로 인식이 안됨.
# python 3.3 버전부터는 __init__.py가 없어도 패키지로 인식하나 
# 호환을 위해서 __init__.py를 생성하는것이 안전한 방법
# __init__.py 파일은 패키지 관련된 설정이나 초기화 코드를 포함할 수 있다.

print("+++++++++++++++++++++++++++++++++++++++++++++")

import game
print(game.VERSION)

game.render_test()

# #### __all__ ####
from game.sound import *
echo.echo_test()


##### relative #####
from game.graphic.render import render_test
render_test()

