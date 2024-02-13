import os

# Define the folder containing the files
folder_path = "C:\\Users\\Charles\\Desktop\\greythorn-repository\\nft-image-generator-modified\\parts\\06Accessories"

# Define the data
data = [
    {"name": "None", "id": 1},
    {"name": "Band-Aid", "id": 2},
    {"name": "Cuban Link Chain", "id": 3},
    {"name": "Ear Studs", "id": 4},
    {"name": "Gold Earrings", "id": 5},
    {"name": "Lightning", "id": 6},
    {"name": "Silver Earrings", "id": 7},
    {"name": "White Beard", "id": 8},
    {"name": "Beard", "id": 9},
    {"name": "Big Mustache", "id": 10},
    {"name": "Face Mask", "id": 11},
    {"name": "Glasses-1", "id": 12},
    {"name": "Glasses-2", "id": 13},
    {"name": "Sticky Note", "id": 14},
    {"name": "Monocle", "id": 15},
    {"name": "Sunglasses", "id": 16},
    {"name": "Nose Hair", "id": 17},
    {"name": "Little Bird", "id": 18},
    {"name": "Crown", "id": 19}
]


# Rename files
for item in data:
    old_name = os.path.join(folder_path, f"{item['name']}.png")
    new_name = os.path.join(folder_path, f"accessories{item['id']}.png")
    try:
        os.rename(old_name, new_name)
        print(f"Renamed {old_name} to {new_name}")
    except FileNotFoundError:
        print(f"File {old_name} not found.")
    except FileExistsError:
        print(f"File {new_name} already exists.")
