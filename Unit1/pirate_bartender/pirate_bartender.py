import random

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?",
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}

adjective = ["Funny", "Messy", "Silly"]
noun = ["Walrus", "Monkey", "Turtle"]

def askQuestion():
    answers = {}
    for kind, question in questions.items():
        print(question)
        answers[kind] = input().lower() in ["yes", "y"]
        print("")
    return answers

def makeDrink(answers):
    drinkIngredients = []
    for kind, ingredientList in ingredients.items():
      #  if kind = True in answers then random from ingredientlist
        if answers[kind] == True:
            drinkIngredients.append(random.choice(ingredientList))
    return drinkIngredients

def cocktailName():
    drinkName = []
    drinkName.append(random.choice(adjective))
    drinkName.append(random.choice(noun))
    return drinkName

def main():
    answers = askQuestion()
    drinkContents = makeDrink(answers)
    drinkName = cocktailName()
    print("Your drink consists of: \n a " + " \n a ".join(drinkContents))
    print(" \n It is called the " + " ".join(drinkName) + "! \n")
    print("Would you like to make another drink?")
    anotherDrink = input().lower() in ["yes", "y"]
    if anotherDrink == True:    
        main()
    else: 
        print("Have a nice day!")
        
if __name__ == "__main__":
    main()