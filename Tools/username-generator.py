import json
import random
import os


def load_wordlist(filename):
    tools_dir = os.path.dirname(__file__)
    filepath = os.path.join(tools_dir, '..', 'Database', filename)
    with open(filepath, 'r') as file:
        wordlist = [line.strip() for line in file]
    return wordlist


def generate_username(wordlist):
    # Choose a random word from the wordlist
    word = random.choice(wordlist)
    # Generate a random number
    number = random.randint(100, 999)  # Generate a 3-digit number
    # Combine word and number
    username = f"{word}{number}"
    return username


def generate_usernames(wordlist, num_usernames):
    usernames = []
    for _ in range(num_usernames):
        usernames.append(generate_username(wordlist))
    return usernames


def save_usernames_to_json(usernames, filename):
    tools_dir = os.path.dirname(__file__)
    filepath = os.path.join(tools_dir, '..', 'Database', filename)
    with open(filepath, 'w') as file:
        json.dump(usernames, file, indent=4)


if __name__ == "__main__":
    wordlist = load_wordlist("wordlist.txt")  # Provide the path to your wordlist file
    num_usernames = 10000
    usernames = generate_usernames(wordlist, num_usernames)
    save_usernames_to_json(usernames, "usernames.json")
