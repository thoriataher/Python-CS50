greet = input("greet the manager :) ").strip().lower()

if greet == "hello" or greet.startswith("hello"):
    print("$0")
elif greet != "hello" and greet.startswith("h"):
    print("$20")
else:
    print("$100")

greet = input("greet the manager :) ").strip().lower()

if greet.startswith("hello"):
    print("$0")
elif  greet.startswith("h"):
    print("$20")
else:
    print("$100")
