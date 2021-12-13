id = 0

def create_menus(): 
    global id
    create_menus.counter += 1
    id = create_menus.counter + 3

create_menus.counter = 0

for i in range(100):
    create_menus()

print(create_menus.counter)
print(id)