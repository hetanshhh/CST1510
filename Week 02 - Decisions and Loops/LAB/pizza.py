
print("Welcome to Patel Pizza !")
size = input("What size pizza do you want? Small(S) , Medium(M) , or Large(L): ").upper()
add_pepperoni = input("Do you want pepperoni? Yes(Y) or No(N): ").upper()
extra_cheese = input("Do you want extra cheese? Yes(Y) or No(N): ").upper()

bill = 0


if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your bill is: ${bill}.")