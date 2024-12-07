print("WELCOME TO TODO LIST APP")
print("*" * 25)

new_list = []
removed_list = []

while True:
    for a in range(len(new_list)):
        print(f"{a + 1}) {new_list[a]}")
    print("*"*30)
    print("Enter a command. Type 'h' for todo help")
    user_input = input(">" )

    if user_input == 'q':
         break

    elif user_input == 'h':
        print("TODO LIST HELP")
        print( "*" * 14 )
        print("Type 'q' to quit")
        print("To add a todo to the list, type it and hit enter ")
        print("to complete a todo enter is number")
        
    elif user_input.isnumeric():
        if int(user_input) <= len(new_list):
            removed_Data = new_list.pop(int(user_input)-1)
            removed_list.append(removed_Data)
            
        else:
            print("Removed task is not in list")
        
    else:
         new_list.append(user_input)


print(f"You Completed {len(removed_list)} todos today")
for a in removed_list:
    print(f"{a}")
