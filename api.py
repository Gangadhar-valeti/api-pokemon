#how to connect to an API using python
import requests
baseurl="https://pokeapi.co/api/v2/"
def getpokemon(name):
    url=f"{baseurl}/pokemon/{name}"
    responce=requests.get(url)
    print(responce)
    if responce.status_code==200:
        pokemondata=responce.json()
        print("the server is good")
        return pokemondata
    else:
        print(" you cannot connect the api server")
        return None
name=input(" the pokemon nmae to know the details=")
pokemoninfo=getpokemon(name)

if pokemoninfo:
    print(f" name={pokemoninfo["name"].capitalize()}")
    print(f"id={pokemoninfo["id"]}")
    print(f"weight={pokemoninfo["weight"]}")
    print(f"height={pokemoninfo["height"]}")
    