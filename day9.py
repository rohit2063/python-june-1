# import random
# attempt = 5
# while True:
#     attempt = attempt - 1
#     data = ["R", "P", "S"]
#     computer_pick = random.choice(data)
#     print(computer_pick)
#     user = input("Enter any R/P/S ").upper()
#     if user not in data:
#         print("Wrong input enter RPS")
#         continue
#     if user == computer_pick:
#         print("Draw")

#     elif (
#         (user == "R" and computer_pick == "S")
#         or (user == "S" and computer_pick == "P")
#         or (user == "P" and computer_pick == "R")
#     ):
#         print("user win")

#     else:
#         print("computer win")

#     if attempt <= 0:
#         result = input("do you want play again y/n").lower()
#         if result=="y":
#             attempt = 5
#             continue
#         else:
#             break
