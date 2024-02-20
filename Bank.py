user_passwords = {
    "bob":"1234"

}


user = {
    "bob":1200,


}


def deposit(name):

    print("Current amount: ",user[name])
    deposit_amount = int(input("What amount do you want to deposit? : "))
    new_amount =  user[name] + deposit_amount
    user.update({name: new_amount})
    print("New amount: ", user[name])

def withdraw(name):
    
    print("Current amount: ",user[name])
    withdraw_amount = int(input("What amount do you want to withdraw? : "))
    new_amount =  user[name] - withdraw_amount
    user.update({name: new_amount})
    print("New amount: ", user[name])

def check_balance(name):
    print("Current amount: ",user[name])


def new_user_add() :
    new_user_name = input("what is your name for your account? : ")
    new_user_passowrd  = input("what is your password you want to set for your account? : ")
    user.update({new_user_name: 0})
    user_passwords.update({new_user_name: new_user_passowrd})


new_user = input("Are u a new user? y or n: ")

if new_user == 'y':
    new_user_add()

else:
    pass

all_availible_accounts = list(user.keys())


while True:
    name = input("login - what is your name? : ")
    password  = input("What is your password : ")

   

    if name in all_availible_accounts:
        
        if password != user_passwords[name]:
            print("incorrect password")
        
        else:
            break

    else:
         print("incorrect name")
while True:

    action = input("what do you want to do? deposit(d) , withdraw(w), check balance(cb) or Quit(q) :")

    if action == 'd':
        deposit(name)

    elif action == 'w':
        withdraw(name)

    elif action == 'cb':
        check_balance(name)

    elif action == 'q':
        print("Thanks for using our bank?")
        break

    else:
        print("incorrect input")


