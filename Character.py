import os.path
import io
import requests
from PIL import Image

class Character:
    def __init__(self, name, gender, species, origin, status, image_url, number_of_episodes):
        self.name = name
        self.gender = gender
        self.species = species
        self.origin = origin
        self.status = status
        self.image_url = image_url
        self.number_of_episodes = number_of_episodes
        self.image_name = self.name.replace(" ", "")+'.png'
        self.image_path = './images/'+self.image_name
        self.download_image()

    def show_character(self):
        print(self.name, self.gender)
    
    def download_image(self):
        if not os.path.exists(self.image_path):
            response = requests.get(self.image_url)
            img_data = response.content

            image = Image.open(io.BytesIO(img_data))
            image = image.resize((200, 200), Image.Resampling.LANCZOS) # Lanczos gives better scaling IMG quality
            image.save(self.image_path)

            print(self.name + "Is downloaded!")

    def get_image(self):
        return Image.open(self.image_path)

