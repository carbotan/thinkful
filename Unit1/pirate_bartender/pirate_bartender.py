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

def askQuestion():
    answers = {}
    for kind, question in questions.items():
        print(question)
        answers[kind] = input().lower() in ["yes", "y"]
    return answers

def makeDrink(answers):
    drinkIngredients = []
    for kind, ingredientList in ingredients.items():
      #  if kind = True in answers then random from ingredientlist
        if answers[kind] == True:
            drinkIngredients.append(random.choice(ingredientList))
    return drinkIngredients

answers = askQuestion()
drink = makeDrink(answers)

print("Your drink consists of " + ", ".join(drink) + ".")
        
















'''
def questFunc():
    answers = {}
    for type, quest in questions.items():
        print(quest)
        answers[type] = input().lower() in ["y", "yes"]
        print("")
    return answers

def drinkFunc():
    drink = []
    for type, ingredient in ingredients.items():
        drink[ingredient] = random.choice(type)
    return drink

hello = questFunc()
print(hello)
print(random.choice(ingredients))
'''