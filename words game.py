import random

categories = {cities: towns.txt, imena: names.txt}
words_list = []
game_word = ""
letter_list = game_word
first_letter = list(game_word)[0]
end_letter = list(len(game_word))
#отношение не всегда к game_word, но и к input
##index = int##

while first_letter == end_letter:
    
    input("Выберите категорию(cities/imena)")
    #if input = "cities":
    if categ = input():
        f = open(categories[categ], "r")
        towns = open("towns.txt", "r")
        for line in towns:
            words_list.append(line)
        index = random.randint(0, len(words_list)-1)
        game_word = words_list[index]
        words_list.clean(index)
    
    #elif input = "imena":
    if categ = input():
        f = open(categories[categ], "r")
        towns = open("names.txt", "r")
        for line in names:
            words_list.append(line)
        index = random.randint(0, len(words_list)-1)
        game_word = words_list[index]
        words_list.clean(index)

    else:
        print("Ты написал несуществующую категорию!")

    print(game_word)
    input("")
    if first_letter == end_letter:
        print(game_word)

    else:
        print("Первая и последняя буквы не совпадают!")
        input("")
        continue

