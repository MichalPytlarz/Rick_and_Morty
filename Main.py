import requests
from tkinter import *
from PIL import Image, ImageTk
from Character import Character


url = "https://rickandmortyapi.com/api/character/?page=1"

response = requests.get(url)

json_response = response.json()
json_response_result = json_response["results"]

characters = []

for obj in json_response_result:
    name = obj["name"]
    gender = obj["gender"]
    species = obj["species"]
    origin = obj["origin"]["name"]
    status = obj["status"]
    image_url = obj["image"]
    number_of_episodes = len(obj["episode"])


    character = Character(name, gender, species, origin, status, image_url, number_of_episodes)

    character.show_character()
    characters.append(character)