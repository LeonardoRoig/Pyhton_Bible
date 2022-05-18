email = input("What's your email?: ")

user_name = email[:email.index("@")]

domain = email[email.index("@") +1 :]

output = "Your username is {} and your domain is {}".format(user_name,domain)
# message = output.format(user_name,domain)

print(output)

