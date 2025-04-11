def calculate_love_score(name_1, name_2):
    name_1 = name_1.lower()
    name_2 = name_2.lower()
    List_True = ["T", "R", "U", "E"]
    List_Love = ["L", "O", "V", "E"]
    L_in_True = []
    L_in_Love = []

    for letters in name_1:
        if letters.upper() in List_True:
            L_in_True.append(letters.lower())

    for letters in name_2:
        if letters.upper() in List_True:
            L_in_True.append(letters.lower())

    for letters in name_1:
        if letters.upper() in List_Love:
            L_in_Love.append(letters.lower())

    for letters in name_2:
        if letters.upper() in List_Love:
            L_in_Love.append(letters.lower())

    score_1 = (len(L_in_True))
    score_2 = (len(L_in_Love))

    print(f"{score_1}{score_2}")

calculate_love_score("Michael", "No one")
