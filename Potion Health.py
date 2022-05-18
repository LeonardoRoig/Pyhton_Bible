import random
from random import randint

difficulty = 1

health = 50

health_potion = int(random.randint(25,50) / difficulty)

health = health + health_potion

print (health)

message = "Health potion give Health points!"
print(message)

#