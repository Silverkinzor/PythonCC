# For PythonCC11-01

# def city_country(city, country):
#     """Combines a city and country name into a single string"""
#     combinedCCstr = city + ', ' + country
#     return combinedCCstr.title()

# For PythonCC11-02, pt. 1

# def city_country(city, country, population):
#     """Combines a city and country name into a single string"""
#     combinedCCstr = city.title() + ', ' + country.title() + ' – population ' + population
#     return combinedCCstr

# For PythonCC11-02, pt. 2

def city_country(city, country, population=''):
    """Combines a city and country name into a single string"""
    if population:
        combinedCCstr = city.title() + ', ' + country.title() + ' – population ' + str(population)
    else:
        combinedCCstr = city.title() + ', ' + country.title()
    return combinedCCstr