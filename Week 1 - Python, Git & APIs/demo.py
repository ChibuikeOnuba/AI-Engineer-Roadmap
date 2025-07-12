import requests
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'circuit_diagram.png')

r = requests.get('https://imgs.xkcd.com/comics/circuit_diagram.png')

print(r.content)

with open(file_path, 'wb') as f:
    f.write(r.content)
print("Image downloaded and saved as 'circuit_diagram.png'")