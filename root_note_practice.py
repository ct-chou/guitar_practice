import random

def get_random_note():
    notes = ['A', 'A#', 'Bb', 'B', 'C', 'C#', 'Db', 'D', 
             'D#', 'Eb', 'E', 'F', 'F#', 'Gb', 'G', 'G#', 'Ab']
    string = [5, 6]
    return [random.choice(string), random.choice(notes)]

if __name__ == "__main__":
    print("Press Enter to get a random musical note. Type 'exit' and press Enter to quit.")
    while True:
        user_input = input()
        if user_input.lower() == 'exit':
            break
        string, note = get_random_note()
        print(f"String: {string}, Note: {note}")