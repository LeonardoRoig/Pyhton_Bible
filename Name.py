
name = input("What's your name?: ")

age = int(input("How old are you?: "))

city = input("What city do you live in?: ")

love = input("What's do you love doing?: ")

message = "You name is {} and you are {} years old. You live {} and love {}!"
output = message.format(name,age,city,love)
print(output)
