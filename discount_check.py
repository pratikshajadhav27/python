role = input("Enter role: ")
age = int(input("Enter age: "))

eligible = (role == "student") and (age < 21)

print("Eligible :", eligible)