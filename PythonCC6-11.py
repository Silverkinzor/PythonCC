# 6-11. Cities: Make a dictionary called cities. Use the names of three cities as
# keys in your dictionary. Create a dictionary of information about each city and
# include the country that the city is in, its approximate population, and one fact
# about that city. The keys for each city’s dictionary should be something like
# country, population, and fact. Print the name of each city and all of the information
# you have stored about it.

cities = {
    'toronto': {
        'country': 'Canada',
        'population': '~3000000',
        'fact': 'I live in Toronto.',
        },

    'san jose': {
        'country': 'United States',
        'population': '~1000000',
        'fact': 'My cousins live in San Jose.'
        },

    'tallinn': {
        'country': 'Estonia',
        'population': '~410000',
        'fact': "Alot of my grandma's side of the family lives in Tallinn."
        },

    }

for city, information in cities.items():

    print(city.title() + ':')

    for info_type, info in information.items():
        print('\t' + info_type.title() + ': ' + info)

    print('')