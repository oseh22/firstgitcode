# data=("read me")
# print (data)
# import random
# reng = random.randrange (10, 100, 3)
# print(reng) 



import random

def lottery_gen():
    # Generate a random number between 0 and 50
    random_number = random.randint(0, 50)
    

    # Get user name
    user_name = input("please input your name: ")
    user_number = (int(input("Please enter your number: ")))
    print (user_name)
    # the winning number
    winning_number = 30

    # Check if the random number matches the winning number
    if random_number == winning_number :
        print(f"Congratulations {user_number}! Your lucky number is {winning_number}. You are the lucky winner!")
    else:
        print(f"you chose number {user_number}, sorry, the generated number is  {random_number} so is not the winning number. Please try again.")

# Call the lottery_gen() function to run the program
lottery_gen()