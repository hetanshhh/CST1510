first_name = "Hetansh patel"
first_name_followers = 439

second_name = "karm amin"
second_name_followers = 430

while True:
    print(f"\ncompare first : {first_name}")
    # Fixed: Changed {} to () for the print function
    print(f"compare second: {second_name}")

    guess = input("who has more followers? Type 'First' or 'Second' (or 'quit' to exit): ")

    if first_name_followers > second_name_followers:
        right_answer = "First"
    else:
        right_answer = "Second"

    
    if guess == right_answer:
        print("you got it right yayyyy!!:)")
    elif guess in ["First", "Second"]:
        print("wrong :(")
    
    elif guess == "quit":

        print("thanks for playing :)")
        break
    else:
        print("Invalid input, try again.")