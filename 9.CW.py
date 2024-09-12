# DICTIONARIES #2:

#Classwork:
#1 & 2
zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries","Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air": ["Gemini", "Libra", "Aquarius"]}
print(zodiac_elements.get('earth'))
print(zodiac_elements.get('fire'))

#3 & 4
user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
if "teraCoder" not in user_ids:
    user_ids["teraCoder"] = 100000
    tc_id = user_ids.get("teraCoder", 100000)
    print(tc_id)

elif "superStackSmash" not in user_ids:
    user_ids["superStackSmash"] = 100000
    stack_id = user_ids.get("superStackSmash", 100000)
    print(stack_id)

#5 & 6
available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20, "strength sandwich": 25, "stamina grains": 15, "power stew": 30}
(available_items.pop("power stew"))
(available_items.pop("stamina grains"))
print(available_items)

#7
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}
lessons = []
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}
for key in num_exercises.keys():
    lessons.append(key)
print(lessons)

#8
total = []
for key,value in num_exercises.items():
    print(key,value)
    total.append(value)
print(total)

#9
women_in_occupation = {"CEO": 28, "Engineering Manager": 9, "Pharmacist": 58, "Physician": 40, "Lawyer": 37, "Aerospace Engineer": 9}
for key, value in women_in_occupation.items():
    print("Women make up", value, "percent of", key + "s")