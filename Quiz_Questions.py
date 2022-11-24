import random

english = {"We are playing.(if sentaance is correct then write True else False).":"True",
    "There are 3 types of tenses.":"True",
    "Is,am,are are helping verbs.":"True",
    "Is,am,are are adverbs.":"False"
    }

maths = {"We can add two numbers by subrtacting(-) them.":"False",
    "10 + 5 = 14":"False","The sign of multipaction is * .":"True",
    "There are 10 candies if 7 candies are eaten then 3 candies are left.":"True",
    "Multiplication of 0 with any number gives 0.":"True"
    }

science = {"Formula of Water is H2O.":"True",
    "Carbon can form 4 bonds.":"True","Human\'s need carbon dioxide for respiration.":"False",
    "Plants do photosynthesis by taking carbon dioxide.":"True",
    "Methanol is alcohol.":"True","Suffix of alcohol is ol.":"True"
    }

social_studies = {
    "INDIA got independent in 1947.":"True",
    "The treaty of constantinople was signed in 1832.":"True",
    "In Galicia,the aristocracy spoke German language.":"False",
    "The founder of Hoa Hoa movement is Huynh Phu So.":"True",
    "The French indo - China established in 1887.":"True"
    }

general_knowledge = {
    "National song of INDIA is \"Vande Matatam\".":"True",
    "National tree of INDIA is \"Banyan Tree\"":"True",
    "Nationl river of INDIA is \"Yamuna\"":"False",
    "There are 7 continents in world.":"True",
    "The largest planet of our solar system is \"Earth\"":"False"
    }

key1,value1 = random.choice(list(english.items()))
key2,value2 = random.choice(list(maths.items()))
key3,value3 = random.choice(list(science.items()))
key4,value4 = random.choice(list(social_studies.items()))
key5,value5 = random.choice(list(general_knowledge.items()))
Total = 0

name = input("Your name:- ")
print("\n")

print("Quiz Questions(Write answer in proper format True or False)")
print("\n")
print(f"Question-1: {key1}")
ans1 = input("Answer: ")
if ans1==value1:
    print("Congratulations")
    Score_1 = 1
    print(f"Score: {Score_1}")
    print("\n")
else:
    Score_1 = 0
    print(f"Score: {Score_1}")
    print("\n")

print(f"Question-2: {key2}")
ans2 = input("Answer: ")
if ans2==value2:
    print("Congratulations")
    Score_2 = 1
    print(f"Score: {Score_2}")
    print("\n")
else:
    Score_2 = 0
    print(f"Score: {Score_2}")
    print("\n")


print(f"Question-3: {key3}")
ans3 = input("Answer: ")
if ans3 == value3:
    print("Congratulations")
    Score_3 = 1
    print(f"Score: {Score_3}")
    print("\n")
else:
    Score_3=0
    print(f"Score: {Score_3}")
    print("\n")

print(f"Question-4: {key4}")
ans4 = input("Answer: ")
if ans4==value4:
    print("Congratulations")
    Score_4 = 1
    print(f"Score: {Score_4}")
    print("\n")
else:
    Score_4 = 0
    print(f"Score: {Score_4}")
    print("\n")

print(f"Question-5: {key5}")
ans5 = input("Answer: ")
if ans5==value5:
    print("Congratulations")
    Score_5 = 1
    print(f"Score: {Score_5}")
    print("\n")
else:
    Score_5 = 0
    print(f"Score: {Score_5}")
    print("\n")

Total=Score_1+Score_2+Score_3+Score_4+Score_5
print(f"{name} your total score is {Total} out of 5")

