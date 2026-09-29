me = {"name" : "Anastasiia", "surname" : "Kuznitsova", "group" : "IT-32", "city" : "Lutsk", "birth_year" : "2009", "hobbies" : ["games", "movies", "dog"]}

for key, value in me.items():
    print(key, ":", value)

print(me.keys())
print(len(me))

print(me["group"])
print(me.get("email", "unknown"))  #бо в нас немає ключа з назвою email

me["email"] = "2024.kuznitsova.anastasiia@ktbp.net.ua"
me["city"] = "Horokhiv"
no_birth_year = me.pop("birth_year")
print(no_birth_year)
for key, value in me.items():
    print(key, ":", value)

print("phone" in me)