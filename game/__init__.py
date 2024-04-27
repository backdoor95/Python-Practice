from .graphic.render import render_test
VERSION = 3.5

def print_version_info():
  print(f"The version of this game is {VERSION}")


# 패키지 초기화 코드 작성
print("Initializing game...")
# 패키지 초기화 코드는 game 패키지 하위 모듈의 함수를 import할 경우에도 실행됨.
# 단, 초기화 코드는 한 번 실행된 후에는 다시import를 수행하더라도 실행되지 않음.
# 

# __all__ ?
# 특정 디렉터리의 모듈을 *을 사용하여import 할 때는  해당 디렉터리의 __init__.py파일에
# __all__ 변수를 설정하고 import할 수 있는 모듈을 정의해야함.

# __all__이 의미하는건 sound 디렉터리에서 *를 사용하여 import 할 경우, 