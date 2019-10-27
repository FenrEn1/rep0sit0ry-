def get_favorite(country_dict):
    fav_count = -1
    fav_name = ""
    for key in country_dict.keys():
        if len(country_dict[key]) > fav_count:
            fav_name = key
            fav_count = len(country_dict[key])
    return fav_name

country_dict = {}
while True:
    cur_command = input("Введите команду")
    commands = cur_command.split(" ")

    if commands[0] == "favorite":
        favorite = get_favorite(country_dict)
        if favorite == "":
            print("Стран нет!")
        else:
            print("Любимая страна -", favorite)
        continue
    elif len(commands) < 2:
        print("Нужно ввести город и страну!")
        continue
    else:
        cities = country_dict.get(commands[0])
        if cities is None:
            country_dict[commands[0]] = [commands[1]]
        else:
            try:
                index = country_dict[commands[0]].index(commands[1])
            except ValueError:
                index = -1
            if index == -1:
                country_dict[commands[0]].append(commands[1])
            else:
                print("Город страна уже есть")
                continue
