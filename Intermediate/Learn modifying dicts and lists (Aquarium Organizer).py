import json

aquarium_dict = {
    "Community Tank": {
        "fish": ["Neon Tetra", "Guppy", "Molly", "Platy"],
        "invertebrates": ["Cherry Shrimp"],
        "water_type": "Freshwater",
        "notes": "Peaceful and colorful mix, suitable for beginners."
    },
    
    "Planted Shrimp Tank": {
        "fish": ["Endler's Livebearer", "Chili Rasbora"],
        "invertebrates": ["Cherry Shrimp", "Snails"],
        "water_type": "Freshwater",
        "notes": "Shrimp thrive in heavily planted tanks. Avoid large or aggressive fish."
    }
}

# TODO: Use dict.update() to add more fish
# - Add "Mystery Snail", "Corydoras Catfish" and "Cherry Barb" to "Community Tank"
# - Add "Otocinclus" and "Amano Shrimp" to "Planted Shrimp Tank"


# += Adds elements (plural!) from an iterable to a list.	Modifies a list in place, adding multiple elements from another iterable.
aquarium_dict["Community Tank"]["fish"] += ["Corydoras Catfish", "Cherry Barb"]

# append() Adds a single(!) element to the end of a list.	Modifies a list in place, adding one element.
aquarium_dict["Community Tank"]["invertebrates"].append("Mystery Snail")

# dict.update()	Updates the dictionary with key-value pairs (adds new or updates existing keys).	Modifies a dictionary by updating existing keys or adding new ones.
aquarium_dict["Planted Shrimp Tank"].update({
    "fish": aquarium_dict["Planted Shrimp Tank"]["fish"] + ["Otocinclus"],
    "invertebrates": aquarium_dict["Planted Shrimp Tank"]["invertebrates"] + ["Amano Shrimp"]
})

#direct assignment
aquarium_dict["Community Tank"]["liter"] = 150

#setdefault() will add the key "liter" only if it doesn't already exist. It won't update the value if "liter" is already present.
aquarium_dict["Planted Shrimp Tank"].setdefault("liter", 50)

# dict.update()
# aquarium_dict["Planted Shrimp Tank"].update({
#     "liter": 50
# })

print("aquarium_dict =")
print(json.dumps(aquarium_dict, indent=4))
