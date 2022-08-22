contacts = {
    "number": 5,
    "family":
        [
            {"name": "Jen Garland", "email": "jen.garland@hotmail.com"},
            {"name": "David Moon", "email": "dbm070@gmail.com"},
            {"name": "Jess Moon", "email": "jessicalmoon@gmail.com"},
            {"name": "James Moon", "email": "mrjamesjmoon@gmail.com"},
            {"name": "Jeff Moon", "email": "fenwaysection29@gmail.com"},
        ]
}

for family_member in contacts["family"]:
    print(family_member["email"])
