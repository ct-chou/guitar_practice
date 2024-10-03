import random

def select_random_fret():
    string = random.randint(1, 6)
    fret = random.randint(0, 12)  
    return string, fret

if __name__ == "__main__":
    while True:
        input("Press Enter to select a random fret...")
        string, fret = select_random_fret()
        print(f"What note is: String {string}, Fret {fret}?")
