
def validation(names):
    while True:
        name = input(names)
        if len(name) <= 10:

            return name
        else:

            print("Please Enter 10 letters or few .")


f_name = str(validation("Enter your First Name (10 letters or below ) : "))
l_name = str(validation("Enter Your Last Name (10 letters or below ) : "))
greetings = f"Hello {f_name} {l_name} ! You just developed into Python . "
print(greetings)
