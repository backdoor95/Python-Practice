class Mul:
  def __init__(self, m):
    self.m = m
    
  def __call__(self, n): # __call__ 함수는 Mul 클래스로 만든 객체에 인수를 전달하여 바로 호출하는 메서드.
    return self.m*n
  
if __name__ == "__main__":
  mul3 = Mul(3)
  mul5 = Mul(5)

print(mul3(10))
print(mul5(10))



