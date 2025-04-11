#Takes names from the called function 
#Here, I'm comparing "Michael" and "no one"
def calculate_love_score(name_1, name_2):
    #Lower cases the inputs 
    name_1 = name_1.lower()
    name_2 = name_2.lower()
    #List out the letters being checked 
    List_True = ["T", "R", "U", "E"]
    List_Love = ["L", "O", "V", "E"]
    #empty list for correct letters
    #to be added to.
    L_in_True = []
    L_in_Love = []
    #Checks name_1 for letters in True 
    for letters in name_1:
        if letters.upper() in List_True:
            L_in_True.append(letters.lower())
    #Checks name_2 for letters in True
    for letters in name_2:
        if letters.upper() in List_True:
            L_in_True.append(letters.lower())
    #Checks name_1 for letters in Love
    for letters in name_1:
        if letters.upper() in List_Love:
            L_in_Love.append(letters.lower())
    #Checks name_2 for letters in Love 
    for letters in name_2:
        if letters.upper() in List_Love:
            L_in_Love.append(letters.lower())
    #Checks the correct letters added to the empty lists
    #and gives the length of those lists in a number. 
    score_1 = (len(L_in_True))
    score_2 = (len(L_in_Love))
    #The lengths of each list next 
    #to each other will be the total score. 
    print(f"{score_1}{score_2}")
#The names being checked by the function
#are entered here. 
calculate_love_score("Michael", "No one")
