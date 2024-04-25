class Calculator:
  def __init__(self):
    self.result = 0
  
  def add(self, num):
    self.result += num
    return self.result
  
  def sub(self, num):
    self.result -= num
    return self.result
  
cal1 = Calculator()
cal2 = Calculator()

# vscode에서 단어 찾기 = ctrl shift f


# Cookie 클래스는 아무런 기능도 가지고 있지않는 클래스임.
class Cookie:
  pass

a = Cookie()
b = Cookie()


'''
점프 투 파이썬
객체와 인스턴스의 차이
클래스로 만든 객체를 ‘인스턴스’라고도 한다. 그렇다면 객체와 인스턴스의 차이는 무엇일까? 이렇게 생각해 보자. a = Cookie()로 만든 a는 객체이다. 그리고 a 객체는 Cookie의 인스턴스이다. 즉, 인스턴스라는 말은 특정 객체(a)가 어떤 클래스(Cookie)의 객체인지를 관계 위주로 설명할 때 사용한다. ‘a는 인스턴스’보다 ‘a는 객체’라는 표현이 어울리며 ‘a는 Cookie의 객체’보다 ‘a는 Cookie의 인스턴스’라는 표현이 훨씬 잘 어울린다.
'''





#### 사칙연산 클래스 만들기

#  클래스 안에 구현된 함수는 다른 말로 메서드(method)라고 부른다.
# self는 해당 메서드를 호출한 객체를 의미한다.


##### 생성자
# 생성자란 객체가  객체가 생성될 때 자동으로 호출되는 메서드를 의미함.
# 파이썬에서는 __init__를 사용하면 해당 메서드는 생성자가 된다.

class FourCal:
  
  def __init__(self, first, second):
    self.first = first
    self.second = second
  
  def setdata(self, first, second):
    self.first = first
    self.second = second
  
  def add(self):
    result = self.first + self.second
    return result

  def mul(self):
    result = self.first * self.second
    return result
  
  def sub(self):
    result = self.first - self.second
    return result
  
  def div(self):
    result = self.first / self.second
    return result
  
a = FourCal(7,8)
type(a)


# 메서드를 호출하는 방법은 2가지 있다.
a = FourCal(10,11)

# 1
a.setdata(4,2)
# 2
FourCal.setdata(a,4,2)


b = FourCal(55,55)
b.setdata(3,7)

a.add()


###### 클래스의 상속
#      class 클래스_이름(상속할_클래스_이름)
# 기존 클래스가 라이브러리 형태 or 수정이 허용되지 않는 상황
class MoreFourCal(FourCal):
  def pow(self):
    result = self.first**self.second
    return result


## 메서드 오버라이딩
class SafeFourCal(FourCal):
  def div(self):
    if self.second == 0: # 분모가 0일 경우(나누는 값이 0일 경우) 0을 리턴
      return 0
    else:
      return self.first/self.second
    


#       클래스 변수
class Family:
  lastname = "문"

print(Family.lastname)

j = Family()
k = Family()
print(j.lastname)
print(k.lastname)

Family.lastname = "MUN"
j.lastname = "jjjjj"
k.lastname ="kkkkk"
print(Family.lastname)
print(j.lastname)
print(k.lastname)
