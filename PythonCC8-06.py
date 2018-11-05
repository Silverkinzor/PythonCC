# 8-6. City Names: Write a function called city_country() that takes in the name
# of a city and its country. The function should return a string formatted like this:
# "Santiago, Chile"
# Call your function with at least three city-country pairs, and print the value
# that’s returned.

def city_country(city, country):
    cityStr = (city + ', ' + country)
    return cityStr.title()

func_test = city_country('toronto', 'canada')
print(func_test)

func_test = city_country('santiago', 'chile')
print(func_test)

func_test = city_country(country='united states', city='san jose')
print(func_test)