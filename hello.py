# animal package
# dog, cat modules
# dog, cat modules can say "hi"

#from animal import dog
#from animal import cat
from animal import * # animal package가 가지고 있는 모듈을 전부 불러옴

d = dog.Dog() # instance
d.hi()

c = cat.Cat()
c.hi()
