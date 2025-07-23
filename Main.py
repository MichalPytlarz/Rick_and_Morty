import requests
from tkinter import *
from PIL import ImageTk
from Character import Character
from Scrollable import ScrollableFrame

def load_data():
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

        # character.show_character()
        characters.append(character)

    return characters

characters = load_data()



root = Tk()
root.title("Rick and Morty Characters")
root.geometry("535x560")
root.update()
root.resizable(0, 0)
scrollable = ScrollableFrame(root)

for char in characters:

    # Frame for each character
    list_item_frame = Frame(scrollable.scrollable_frame, borderwidth=4, relief=GROOVE)

    # left frame for image
    left_frame = Frame(list_item_frame)
    # loading the img
    photo = ImageTk.PhotoImage(char.get_image())
    image_label = Label(left_frame, image = photo)
    image_label.image = photo
    image_label.pack(fill = BOTH, expand = True)
    left_frame.grid(row = 0, column = 0, padx = 7.5, pady = 15)

    # right frame for description 

    right_frame = Frame(list_item_frame)

    Properties = ["name", "species", "gender", "origin", "status"]

    for i in range(len(Properties)):
        prop = Properties[i]
        Label(right_frame, text =f"{prop.capitalize()}: {getattr(char, prop)}" , font=("Calibri", 12), padx = 7.5).pack(anchor= W, expand= True)

    Label(right_frame, text = str(char.number_of_episodes) + " Episodes", font=("Calibri", 12), padx = 7.5).pack(anchor= W, expand= True)



    right_frame.grid(row = 0, column = 1, sticky = 'we')


    list_item_frame.pack(fill = X, padx = 7.5)


scrollable.pack(fill=BOTH, expand=True) 


root.mainloop()

