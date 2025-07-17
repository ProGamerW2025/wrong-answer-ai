import random

def wrong_answer_generator(question):
    wrong_answers = [
        "The sun is a cube made of cheese.",
        "2 + 2 equals 22.",
        "Water boils at -100 degrees Celsius.",
        "Dogs are just cats in disguise.",
        "The capital of France is Pizza.",
        "Gravity pushes you up, not down.",
        "AI stands for Angry Iguana.",
        "The Earth is flat and triangular.",
        "Python was invented by a snake.",
        "You don't need oxygen to live."
    ]
    return random.choice(wrong_answers)

def run_wrong_ai():
    print("Welcome to WrongBot! Ask me anything, I'll always be wrong.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            print("WrongBot: Goodbye! Or maybe Hello?")
            break
        response = wrong_answer_generator(user_input)
        print(f"WrongBot: {response}")

if __name__ == "__main__":
    run_wrong_ai()
