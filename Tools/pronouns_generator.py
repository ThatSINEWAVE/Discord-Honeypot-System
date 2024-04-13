import random
import json
import os


def generate_pronouns(num_pronouns):
    pronouns = []
    for _ in range(num_pronouns):
        subject_pronouns = ["I", "you", "he", "she", "it", "we", "you", "they", "Batman", "Kermit the Frog", "Gandalf",
                            "Santa Claus", "The Tooth Fairy", "Dumbledore", "Yoda", "The Hulk", "Iron Man", "Einstein"]
        object_pronouns = ["me", "you", "him", "her", "it", "us", "you", "them", "myself", "yourself", "himself",
                           "herself", "itself", "ourselves", "yourselves", "themselves", "Homer Simpson", "Shrek",
                           "Waldo", "A Ghost", "The Loch Ness Monster", "A Unicorn", "A Zombie", "The Easter Bunny"]

        pronoun = f"{random.choice(subject_pronouns)}/{random.choice(object_pronouns)}"
        pronouns.append(pronoun)
    return pronouns


def save_pronouns_to_json(pronouns, filename):
    database_dir = os.path.join(os.path.dirname(__file__), '..', 'Database')
    filepath = os.path.join(database_dir, filename)
    with open(filepath, 'w') as file:
        json.dump(pronouns, file, indent=4)


if __name__ == "__main__":
    num_pronouns = 1000
    fake_pronouns = generate_pronouns(num_pronouns)
    save_pronouns_to_json(fake_pronouns, "pronouns.json")
