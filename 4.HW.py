#HOMEWORK
#1,2 and 3
# countries = []
# country = input("What country do you want added? Say 'done' to stop adding contries: ")
# while country != "done":
#     countries.append(country.title())
#     country = input("What country do you want added? Say 'done' to stop adding contries: ")
# countries.sort()
# print("Your countries are", countries)

#4 and 5
# colours = []
# while len(colours) == 0:
#     additionals = input("What colours do you want to add (say done to stop): ")
#     if additionals == "done":
#         break
#     colours.append(additionals)
#     print(colours)
#     colours.pop(0)
#     print(colours)
    
#6
# cities = ["Portland", "San Francisco", "Houston", "Boston"]
# states = ["Oregon", "California", "Texas", "Massachusetts" ]
# city_state = []
# for i in range(len(cities)):
#     temp=cities[i]+', '+states[i]
#     city_state.append(temp)
# print(city_state)


#7
# days = ["Monday", "Wednesday", "Thursday"]
# days.insert(1, "Tuesday")
# days.append("Friday")
# days.extend(["Saturday", "Sunday"])
# print(days)


#Shreya's Torture
capitals = ["Ottawa","New Delhi"]
countries = ["Canada","India"]
while True:
    geo_quiz = input("What country or capitol you want to discover(capatilize it): ")
    if geo_quiz in countries:
        i = countries.index(geo_quiz)
        print("The "+ geo_quiz + "'s capital is",capitals[i])
    
    elif geo_quiz in capitals:
        i = capitals.indez(geo_quiz)
        print(geo_quiz + "is the capital of ", countries[i])
    
    elif geo_quiz not in capitals or geo_quiz not in countries:
        print("I apologize but we do not have that country/capitol at our desposal. Give us some countries and captials we could use for next time:")
        new_countries = input("Enter the name of a new country(say done to stop)")
        new_capitols = input("Enter the name of the capitol of the country(say done to stop)") 
        countries.append(new_countries)
        capitals.append(new_capitols)
        print(new_countries)
        print(new_capitols)
    continue1 = input("Do you want to continue adding countries and capitals(say 'no' to stop)")
    if continue1 == "no":
        break
print(capitals)
print(countries)