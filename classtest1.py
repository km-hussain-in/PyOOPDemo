class Interval:
  
  def __init__(self, min, sec):
    self.__min = min + sec // 60
    self.__sec = sec % 60
    
  def time(self): return 60 * self.__min + self.__sec
  
  def __add__(self, other):
    return Interval(self.__min + other.__min, self.__sec + other.__sec)
    
  def __str__(self):
    return f'{self.__min}:{self.__sec:02d}'
  

def speed(distance, duration):
  return (3.6 * distance) / duration.time()

a = Interval(1, 65)
print('First Interval =', a)
print(f'Speed of first = {speed(500, a):.1f}')

b = Interval(3, 20)
print('Second Interval =', b)
print(f'Speed of second = {speed(500, b):.1f}')

c = a + b
print('Total Interval =', c)




	
	
