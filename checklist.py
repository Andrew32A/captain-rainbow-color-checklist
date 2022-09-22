# There are seven colors in the rainbow, and seven items of clothing to color.
# He can never wear the same color on any of his items. If he is wearing a purple shoe, he cannot wear a second purple shoe.
# He must wear every color of the rainbow each day.

checklist = list()

def list_all_items():
    index = 0
    for list_item in checklist:
        print (str(index) + list_item)
        index += 1


# Define Functions
def create(item):
    checklist.append(item)

def read(index):
    print(index)
    print(index)

def update(index, item):
    checklist[index] = item

def destroy(index):
    checklist.pop(index)

def test():
    create("purple socks")
    create("red shirt")

    read(0)
    read(1)

    update(0, "purple socks")

    destroy(1)

    read(0)

    list_all_items()

test()




# random stuff

# colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
# clothes = ["hat", "sunglasses", "shirt", "pants", "underwear", "socks", "shoes"]
# days = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]


# for i in range(len(days)):
#     day = days[i]

#     for i in range(len(colors)):
#         color = colors[i]

#         for i in range(len(clothes)):
#             clothe = clothes[i]

#             print (f"On {day}, Captain Rainbow will wear {color} {clothe}.")