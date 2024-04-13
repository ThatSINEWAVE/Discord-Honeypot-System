import json
import random
import os


def load_wordlist(filename):
    tools_dir = os.path.dirname(__file__)
    filepath = os.path.join(tools_dir, '..', 'Database', filename)
    with open(filepath, 'r') as file:
        wordlist = [line.strip() for line in file]
    return wordlist


def generate_nickname(wordlist):
    # Choose one or two random words from the wordlist
    num_words = random.randint(1, 2)
    words = [random.choice(wordlist).capitalize() for _ in range(num_words)]
    # Combine words into a nickname
    nickname = ''.join(words)
    return nickname


def generate_nicknames(wordlist, num_nicknames):
    nicknames = []
    for _ in range(num_nicknames):
        nicknames.append(generate_nickname(wordlist))
    return nicknames


def save_nicknames_to_json(nicknames, filename):
    tools_dir = os.path.dirname(__file__)
    filepath = os.path.join(tools_dir, '..', 'Database', filename)
    with open(filepath, 'w') as file:
        json.dump(nicknames, file, indent=4)


if __name__ == "__main__":
    wordlist = load_wordlist("wordlist.txt")  # Provide the path to your wordlist file
    num_nicknames = 10000
    nicknames = generate_nicknames(wordlist, num_nicknames)
    save_nicknames_to_json(nicknames, "nicknames.json")
