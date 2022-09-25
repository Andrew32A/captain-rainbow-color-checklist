# There are seven colors in the rainbow, and seven items of clothing to color.
# He can never wear the same color on any of his items. If he is wearing a purple shoe, he cannot wear a second purple shoe.
# He must wear every color of the rainbow each day.

# create list
checklist = list()
# could also do checklist = []

# define functions
# lists all items
def list_all_items():
    index = 0
    for list_item in checklist:
        print("{} {}".format(index, list_item))
        index += 1

# creates item in list
def create(item):
    checklist.append(item)

# reads item in list
def read(index):
    # added print line to display indexed item to user
    print(checklist[index])
    return checklist[index]

# updates item in list
def update(index, item):
    checklist[index] = item

# deletes item from list
def destroy(index):
    checklist.pop(index)

# stretch challenge for later
# def mark_completed(index):

# takes user input   
def user_input(prompt):
    user_input = input(prompt).lower()
    return user_input

# selection based on user input
def select(function_code):
    if function_code == "c":
        input_item = user_input("Input item: ")
        create(input_item)

    elif function_code == "r":
        item_index = user_input("Index Number?: ")
        # remember that item_index must actually exist or our program will crash
        # had to add int due to "TypeError: list indices must be integers or slices, not str"
        read(int(item_index))

    elif function_code == "p":
        list_all_items()

    elif function_code == "q":
        return False

    else:
        print("Unknown Option")

    # keeps loop running
    return True

# main loop
running = True
while running:
    selection = user_input("Press C to add to list, R to Read from list, P to display list, and Q to quit: ")
    running = select(selection)







# testing area
# def test():
#     create("purple socks")
#     create("red shirt")

#     read(0)
#     read(1)

#     update(0, "purple socks")

#     destroy(1)

#     read(0)

#     list_all_items()

# test()


# random stuff i wanted to try
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