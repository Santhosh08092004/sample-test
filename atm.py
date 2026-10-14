import calc as ca

USER_DATA = {
    "user_name" : "user_1",
    "acc_no"    : 13579012,
    "pin"       : 1234,
    "total_bal" : 1000000
}

def user_info():

    if USER_DATA and USER_DATA["user_name"]:
        return f"Hi Welcome User {USER_DATA['user_name']} Your acc.no is {USER_DATA['acc_no']}"
    else:
        False

def withdraw(withdrawl_amount):

    if  withdrawl_amount > USER_DATA["total_bal"]:
        return False
    else:
        amount = ca.withdraw_calc(USER_DATA["total_bal"],withdrawl_amount)
        USER_DATA["total_bal"]= amount
        return amount

def deposit(deposit_amount):

    if deposit_amount:
        amount = ca.deposit_calc(USER_DATA["total_bal"],deposit_amount)
        USER_DATA["total_bal"]= amount
        return amount

def check_bal():

    return USER_DATA["total_bal"]

def main():

    print("Welcome to ATM..")
    print("="*20)

    pin= int(input("Enter you pin to proceed: "))

    if pin == USER_DATA["pin"]:
        print(user_info())

        while True:
            choice = int(input("1. Withdrawl\n2. Deposit\n3. Check Balance\n4. Exist\nEnter your choice: "))

            match choice:
                case 1:
                    amount= int(input("Enter the amount to withdraw: "))
                    withdraw_resp = withdraw(amount)
                    if withdraw_resp:
                        print(f"Your Withdrawl Successful, your total balance is {withdraw_resp}")
                    else:
                        print("Insufficient Balance")

                case 2:
                    amount= int(input("Enter the amount to Deposit: "))
                    print(f"Dposit Successful, your total balance is {deposit(amount)}")

                case 3:
                    print(f"Total Balance is {check_bal()}")

                case 4:
                    print("Thanks you using ATM")
                    break

                case _:
                    print("Invalid Input, Please Enter between 1 to 4")

    else:
        print("Invalid pin no, please try again")
        return

if __name__ =="__main__":
    main()
                   

