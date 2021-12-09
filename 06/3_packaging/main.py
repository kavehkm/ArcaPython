# internal
from world import iran as IR
from world import united_states
from world import germany, japan


total_population_message = 'Total population of {} is {}'
city_population_message = '___ population of {} is {}'


countries = {
    'Iran': IR,
    'United States': united_states,
    'Germany': germany,
    'Japan': japan
}

for country_name, country in countries.items():
    print('#' * 10, country_name.upper(), '#' * 10)
    print(total_population_message.format(country_name.title(), country.total))
    for city_name, city_population in country.cities.items():
        print(city_population_message.format(city_name.title(), city_population))
