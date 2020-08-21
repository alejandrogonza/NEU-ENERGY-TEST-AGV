## Author: Alejandro González Vásquez
#NEU ENERGY Test

import pandas as pd

raw_countries = pd.read_csv('countries.csv')
raw_states = pd.read_csv('states.csv')
raw_cities = pd.read_csv('cities.csv')

Data_Base=pd.merge(raw_countries,raw_states,on="ID_COUNTRY")
Data_Base=pd.merge(Data_Base,raw_cities,on="ID_STATE")
Data_Base=Data_Base.rename(columns={'NAME':'CITY','NAME_y':'STATE','NAME_x':'COUNTRY'})

print("This program will show you what is the population of cities inside countries, states or single cities. For example: If you search a country, this will show you every state, city and its population")

search=input("What would you like to search? (Countries, States, or Cities): ")

while search not in ("Countries" , "States" , "Cities"):
    print("There was a mistake in your input. Verify capital letters.")
    search=input("Again, what would you like to search? (Countries, States, or Cities): ")
    
if search=="Countries":
    country_to_search=input("Which country would you like to search?: ")
    i_country_DB=Data_Base.set_index("COUNTRY", drop = False)
    country=i_country_DB.loc[country_to_search]
    print(country[["STATE","CITY","POPULATION"]])
    
elif search=="States":
    state_to_search=input("Which state would you like to search?: ")
    i_state_DB=Data_Base.set_index("STATE", drop = False)
    state=i_state_DB.loc[state_to_search,:]
    print(state[["CITY","POPULATION"]])
    
elif search=="Cities":
    city_to_search=input("Which city would you like to search?: ")
    i_city_DB=Data_Base.set_index("CITY", drop = False)
    population=i_city_DB.loc[city_to_search,"POPULATION"]
    print("City: %s. Population:%d" % (city_to_search,population))

        