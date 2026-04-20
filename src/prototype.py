import copy

# Lighting symbols
LIGHT_SYMBOLS = {
    0: " ",
    50: ".",
    100: "#"
}

# Predefined lighting modes
modes = {
    "atmosphere": {
        "main": 50,
        "bed": 50,
        "bathroom": 0,
        "entrance": 0
    },
    "night": {
        "main": 0,
        "bed": 50,
        "bathroom": 0,
        "entrance": 50
    },
    "work": {
        "main": 100,
        "bed": 50,
        "bathroom": 100,
        "entrance": 100
    }
}

current_mode = "atmosphere"
demo_room = copy.deepcopy(modes[current_mode])


# --- Helpers ---

def insert_label(line, label):
    start = max(0, (len(line) - len(label)) // 2)
    return line[:start] + label + line[start+len(label):]


# --- Drawing ---

def draw_room(room):
    main = LIGHT_SYMBOLS[room["main"]]
    bed = LIGHT_SYMBOLS[room["bed"]]
    bath = LIGHT_SYMBOLS[room["bathroom"]]
    entrance = LIGHT_SYMBOLS[room["entrance"]]

    print("\n=== HOTEL ROOM FLOOR PLAN ===")
    print(f"Current mode: {current_mode}\n")

    print("+---------------------------------+")

    # TOP (Bed area left)
    for i in range(6):
        if i == 0:
            print("|" + "-"*14 + "+" + main*18 + "|")
        elif 1 <= i <= 4:
            left = bed * 14
            right = main * 18
            if i == 2:
                left = insert_label(left, "BED")
            print("|" + left + "|" + right + "|")
        else:
            print("|" + "-"*14 + "+" + main*18 + "|")

    # Divider
    print("|" + bed*15 + main*18 + "|")

    # BOTTOM (Bathroom left)
    print("|" + "-"*18 + "+" + entrance*14 + "|")
    for i in range(6):
        left = bath * 18
        right = entrance * 14

        if i == 2:
            left = insert_label(left, "BATH")

        print("|" + left + "|" + right + "|")

    print("+---------------------------------+")


# --- Mode Editing ---

def edit_mode():
    print("\nAvailable modes:", ", ".join(modes.keys()))
    mode = input("Which mode to edit? ")

    if mode not in modes:
        print("Mode not found")
        return

    print("\nSet lighting (0, 50, 100)\n")

    for key in modes[mode]:
        try:
            val = int(input(f"{key}: "))
            if val in [0, 50, 100]:
                modes[mode][key] = val
        except:
            print("Invalid input")


# --- Apply Mode ---

def apply_mode():
    global demo_room, current_mode

    print("\nAvailable modes:", ", ".join(modes.keys()))
    mode = input("Select mode to apply: ")

    if mode in modes:
        current_mode = mode
        demo_room = copy.deepcopy(modes[mode])
        print(f"\n✔ Applied mode: {mode}")
    else:
        print("Mode not found")


# --- Emergency ---

def emergency():
    global demo_room, current_mode

    for key in demo_room:
        demo_room[key] = 100

    current_mode = "EMERGENCY"
    print("\n⚠ Emergency mode activated! All lights ON")

def change_mode():
    global current_mode, demo_room

    print("\nAvailable modes:", ", ".join(modes.keys()))
    mode = input("Select mode to switch to: ")

    if mode in modes:
        current_mode = mode
        demo_room = copy.deepcopy(modes[mode])
        print(f"\nCurrent mode changed to: {mode}")
    else:
        print("Mode not found")


# --- Main Loop ---

def main():
    while True:
        print("""
RoomLight Demo
--------------
1. View room
2. Edit a lighting mode
3. Apply mode to room
4. Emergency mode
5. Change mode
6. Exit
""")

        choice = input("Select option: ")

        if choice == "1":
            draw_room(demo_room)
        elif choice == "2":
            edit_mode()
        elif choice == "3":
            apply_mode()
        elif choice == "4":
            emergency()
        elif choice == "5":
            change_mode()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()