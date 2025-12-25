#****************************************** 10 ******************************************

# def introduce(name, age, contires):
#     name = print('ur name is Abdullah')
#     age = print('ur age is 22')
#     contires = print('ur lives in saudi arabia')
#     return name


# output = introduce()
#
# print(output)

# introduce()


# def add(n1, n2):
#     return n1 + n2
#
# def sub(n1, n2):
#     return n1 - n2
#
# def dvide(n1, n2):
#     return n1 / n2
#
# def mult(n1, n2):
#     return n1 * n2
#
#
# n1 = int(input('Enter the first number: '))
#
# calcuater_off = False
#
# while not calcuater_off:
#
#     opreations = {
#         '+': add, '-': sub, '%': dvide, '*': mult
#     }
#
#     methods = []
#     for method in opreations:
#         methods += method
#
#     methodolgy = str(
#         input(f'choose one of this method to calculate the number {methods}: '))
#
#     n2 = int(input('Enter the other number: '))
#
#
#
#     first_value = opreations[methodolgy](n1, n2)
#     print(first_value)
#
#     choice = input('type "c" to add another number or "s" to stop calcuete: ').lower()
#     if choice == 'c':
#         final_value = opreations[methodolgy](first_value, n2)
#
#     elif choice == 's':
#         calcuater_off = True
#
#     else:
#         print("Erorr choice.")




#************************************************* day 11 *************************************************

import random

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random_card = random.choice(cards)
    return random_card

user_card = []
computer_card = []

for cards in range(2):
    user_card.append(deal_card())
    computer_card.append(deal_card())

# print(user_card)
# print(computer_card)



def calculate_score(cards):
    """take a list from cards of user and calcute the total cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    elif 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


is_game_over = False

while not is_game_over:
    user_score = calculate_score(user_card)
    computer_score = calculate_score(computer_card)
    print(f'user_score {user_score}')
    print(f'computer_score {computer_score}')

    if user_score == 0 or computer_score == 0 or user_score > 21:
        is_game_over = True
        print('game ends.')

    elif user_score < 19:
        more_card = input('Do u want to add a card? type "y" or "n": ').lower()
        if more_card == "y":
            user_card.append(deal_card())
            user_score = calculate_score(user_card)

        else:
            is_game_over = True

    while computer_score != 0 and computer_card < 17:
        computer_card.append(deal_card())
        computer_score = calculate_score(computer_card)






