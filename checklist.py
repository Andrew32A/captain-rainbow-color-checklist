# There are seven colors in the rainbow, and seven items of clothing to color.
# He can never wear the same color on any of his items. If he is wearing a purple shoe, he cannot wear a second purple shoe.
# He must wear every color of the rainbow each day.

# create list
checklist = list()
# could also do checklist = []

# colors
OKBLUE = '\033[94m'
OKCYAN = '\033[96m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
ENDC = '\033[0m'

# welcone message
print(f"{OKCYAN}---- Welcome to Captain Rainbow's Color Checklist! ----\n-- Press h for help --\n{ENDC}")

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

# adds checkmark to item
def mark_completed(index):
    checklist[index] = ("{} {}".format("√", checklist[index]))

# takes user input   
def user_input(prompt):
    user_input = input(prompt).lower()
    return user_input

# selection based on user input
def select(function_code):
    if function_code == "c":
        input_item = user_input(f"{OKGREEN}Input item: {ENDC}")
        create(input_item)

    elif function_code == "r":
        item_index = user_input(f"{OKGREEN}Index Number?: {ENDC}")
        # remember that item_index must actually exist or our program will crash
        # had to add int due to "TypeError: list indices must be integers or slices, not str" - same goes for the following functions that require an index number
        read(int(item_index))

    elif function_code == "p":
        list_all_items()

    elif function_code == "u":
        update_item = user_input(f"{OKGREEN}Index number?: {ENDC}")
        replace_item_with = user_input(f"{OKGREEN}Enter in new item: {ENDC}")
        update(int(update_item), replace_item_with)

    elif function_code == "d":
        destroy_item = user_input(f"{OKGREEN}Index Number?: {ENDC}")
        destroy(int(destroy_item))

    elif function_code == "z":
        check_item = user_input(f"{OKGREEN}Index number?: {ENDC}")
        mark_completed(int(check_item))

    elif function_code == "h":
        print(f"{OKCYAN}\n---- Enter one of the following ----\nC to add to list\nU to replace item from list\nD to delete item from list\nZ to mark complete\nR to Read from list\nP to display list\nQ to quit\n{ENDC}")

    elif function_code == "q":
        print(f"{OKCYAN}\n\n---- Thanks for using Captain Rainbow's Color Checklist! ----\n\n{ENDC}")
        return False

    else:
        print(f"{WARNING}Unknown Option{ENDC}")

    # keeps loop running
    return True

# main loop
running = True
while running:
    selection = user_input(f"\n{OKBLUE}Enter here: {ENDC}")
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