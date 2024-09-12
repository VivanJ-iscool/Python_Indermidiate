#Homework: Dictionaries #2
#1 & 2
zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries","Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air": ["Gemini", "Libra", "Aquarius"]}
print(zodiac_elements.get('water'))
print(zodiac_elements.get('air'))

#3 & 4
user_ids = {"superCoder": 103419, "pythonGuy": 182921,"samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
if "superCoder" not in user_ids:
    user_ids["superCoder"] = 100000
    tc_id = user_ids.get("superCoder", 100000)
    print(tc_id)

elif "fakeUser" not in user_ids:
    user_ids["fakeUser"] = 100000
    stack_id = user_ids.get("fakeUser", 100000)
    print(stack_id)

#5 & 6
fruits = {"apples": 10, "banana": 5, "berries": 20, "grapes": 25, "melon": 15, "pear": 30}
(fruits.pop("berries"))
(fruits.pop("melon"))
print(fruits)

#7 NEED HELP WITH VARIABLE PART
lessons = []
coding_languages = {"scratch": 10, "python": 13, "HTML": 15, "CSS": 22, "Java": 19, "C": 18, "Javascript": 18}
for key in coding_languages.keys():
    lessons.append(key)
print(lessons)
#8
total = []
for key,value in coding_languages.items():
    print(key,value)
    total.append(value)
print(total)
#9
men_in_occupation = {"CEO": 28, "Engineering Manager": 10, "Pharmacist": 48, "Physician": 45, "Lawyer": 35, "Aerospace Engineer": 19}
for key, value in men_in_occupation.items():
    print("Men make up", value, "percent of", key + "s")

#Suhani's Dictionary
result = {}
start = input("Do you want to start a dictionary?")
while start == "yes":
    keyz = input("Enter your key(Type exit or quit to exit): ")
    if keyz.lower() == "exit" or keyz.lower() == "quit":
        break
    valuee = input("Enter your value: ")
    result[keyz] = valuee

for key,value in result.items():
    print(key,':',value)

while True:
    popper = input("Do you wish to remove a word from your dictionary?")
    if popper == "yes":
        popeyes = input("What word/variable/number do you wish to pop?")
        result.pop(popeyes)
    else:
        for key,value in result.items():
            print(key,':',value)
        break