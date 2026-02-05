# We are going to be setting up HTTP requests using Python and the 'requests' library
# if our venv is running, installing packages will only install them in our virtual environment, not gloabally

import requests
import logging

#Logging
# Logging configuration
logging.basicConfig(
    level=logging.INFO, # this is the default and you can change the logging level
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler("pokemon.log"),
        logging.StreamHandler()
    ]
)

logging.debug('Hello, Debug!')
logging.info('Hello, Info!')
logging.warning('Hello, Warning!')
logging.error('Hello, Error!')
logging.critical('Hello, Critical!')

logger = logging.getLogger(__name__)

# query = input(f"Enter a Pokemon name or pokedex # to fetch its data: ")

# We will use the PokeAPI to fetch pokemon data
# #using the .lower functon to make the query lowercase since that is what pokeapi uses
# url = f"https://pokeapi.co/api/v2/pokemon/{query.lower()}" 

# response = requests.get(url)
# # print(response) #this will just print the response code
# # print(response.json()) #print the entire JSON response

# format our JSON repsponse
# name = response.json()['name']
# dex_number = response.json()['id']
# height = response.json()['height']
# weight = response.json()['weight']

# Pokemon types are stored in a list of dictionaries
# types = [t['type']['name'] for t in response.json()['types']]

# now we can print our formatted data
# print(f"Name: {name.capitalize()}")
# print(f"Pokedex Number: {dex_number}")
# print(f"Height: {height / 10} m") #Height is in decimeters
# print(f"Weight: {weight / 10} kg") #weight is in hectograms
# print(f"Types: {','.join(types)}")

# We can simplify this be defining a function
def get_pokemon(pokemon_name):
    
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}" 

    try:
        response = requests.get(url, timeout=5)

        # Handle http errors(ex: 404)
        response.raise_for_status()
        data = response.json()

        # drill into and format our JSON response
        pokemon_info = {
            "name": data['name'].capitalize(),
            "pokedex_number": data['id'],
            "height": data['height'],
            "weight": data['weight'],
            "types": [t['type']['name'] for t in data['types']]
        }

        logger.info(f"Pokemon {pokemon_name} exists and returned some data")
        return pokemon_info
    
    except requests.exceptions.HTTPError:
        print(f"Pokemon '{pokemon_name}' not found.")

        logger.warning(f"Pokemon not found: {pokemon_name}")
        #logger.debug(e, exe_info=True)

    except requests.exceptions.ConnectionError:
        print("Network error occurred. Check your internet connection.")
        logging.error("Network connection error")

    except requests.exceptions.Timeout:
        print("Request timed out.")
        logger.error("Connection timed out")

    except requests.exceptions.RequestException as e:
        print(f"Unexpected error: {e}")
        logger.error("You broke it in a way I did not expect")

pokemon_name = input("Enter a Pokemon name: ")
pokemon = get_pokemon(pokemon_name)
print(f"Name: {pokemon['name']}")
print(f"Pokedex number: {pokemon['pokedex_number']}")
print(f"Height: {pokemon['height']}")
print(f"Weight {pokemon['weight']}")
print(f"Types: {pokemon['types']}")
 