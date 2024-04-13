from faker import Faker
import json
import os

def generate_about_me():
    fake = Faker()
    about_me = {
        "sentences": [fake.sentence() for _ in range(2500)],
        "questions": [sentence[:-1] + '?' for sentence in [fake.sentence() for _ in range(2500)]],
        "quotes": [fake.sentence() for _ in range(2500)],
        "funny_phrases": [fake.sentence() for _ in range(2500)]
    }
    return about_me

def save_about_me_to_json(about_me, filename):
    database_dir = os.path.join(os.path.dirname(__file__), '..', 'Database')
    filepath = os.path.join(database_dir, filename)
    with open(filepath, 'w') as file:
        json.dump(about_me, file, indent=4)

if __name__ == "__main__":
    about_me = generate_about_me()
    save_about_me_to_json(about_me, "about_me.json")
