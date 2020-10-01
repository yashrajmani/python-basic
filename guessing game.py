answer1 = 3
print("please guessssssss:::::: ")
guess=int(input())

#####################THIS IS A SHORT CODE FOR THE SAME ################################
if guess == answer1:
    print("SAHI JAWAB $$$$$$$$$$$$$$$$")
else :
    if guess < answer1:
        print("guess higher : ")
    else:
        print("plz guess lower : ")
    guess = int(input())
    if guess==answer1:
        print("CORRECT $$$$$")
    else:
        print("INCORRECT ------ ")

###########################################################################################

# ###############THIS IS THE LONG CODE FOR THE SAME ########################################
# if guess < answer1:
#     print("toooo lowwwww ::::::!!!!! guess a high  ")
#     guess2 = int(input())
#     if guess2 == answer1:
#          print("YOU GUESSED IT CORRECTLY  $$$$$$")
#     else:
#          print("wrong ")
#
# elif guess > answer1:
#     print("tooooo high :::::::!!!!!!!  guess a low")
#     guess2 =int(input())
#     if guess2 == answer1:
#         print("YOU GUESSED IT CORRECTLY  $$$$$$")
#     else:
#         print("wrong ")
# else :
#     print("YOU WON @@@@@@@@@@@@@@@@")
# #########################################################################################