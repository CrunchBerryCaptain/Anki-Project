"""Modules needed to grab data from API as json, format and save to text file
dotenv to keep token a secret"""

import os
import json
import requests as reqz
from dotenv import load_dotenv

load_dotenv()


def get_trainee_data() -> dict:
    """Get data for Trainee from Airtable API"""

    token = os.getenv("token")
    headers = {"Authorization": f"Bearer {token}"}
    base_id = "app4sBqDntLhMJNIC"
    table_id = "tbl3u8i1YF2Bhvw3s"

    response = reqz.get(
        f"https://api.airtable.com/v0/{base_id}/{table_id}", headers=headers, timeout=10)

    data = response.json()

    return data


def save_json_to_file(data: list[dict]) -> None:
    """Save quiz data to local json file"""
    with open('trainee_data/quiz_data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f)


def load_from_json() -> list[dict]:
    """Load quiz data from local json file"""
    with open("quiz_data.json", encoding='utf-8') as file:
        return json.load(file)


def get_wrong_answers(data: list[dict]) -> list[dict]:
    """Get list of dicts containing just questions answered wrong, and their correct answers"""

    wrong_answers = []

    records = data.get("records")
    for record in records:
        fields = record.get("fields")
        if fields.get("Self-Assessed") == "Wrong":
            question = fields.get("Question")
            answer = fields.get("Question Answer")
            wrong_answers.append({
                "Question": question,
                "Answer": answer
            })

    return wrong_answers


def wrong_answers_to_txt(path: str, wrong_answers: list[dict]) -> None:
    """Save questions answered wrong, and their correct answers to a correctly formatted text file
    for Anki to read properly."""

    with open(path, 'w', encoding='utf-8') as f:

        for data in wrong_answers:
            line = ""
            # Format question by replacing all new lines with <br> tags. Remove last <br> tag from the end.
            # Use pipe | for separator to separate question from answer (only one that seems to work).
            # Format answer same as question, but add new line at end to separate different cards in txt file.
            question = data.get("Question").replace(
                "\n", "<br>").rstrip("<br>")
            separator = "|"
            answer = data.get("Answer").replace(
                "\n", "<br>").rstrip("<br>") + "\n"
            line = question + separator + answer

            f.write(line)


if __name__ == "__main__":
    # create folder for users
    LOCAL_PATH = "trainee_data/"
    if not os.path.exists(LOCAL_PATH):
        os.makedirs(LOCAL_PATH)

    trainee_data = get_trainee_data()
    wrong_answers_list = get_wrong_answers(trainee_data)
    save_json_to_file(wrong_answers_list)

    FILENAME = "anki_cards.txt"
    wrong_answers_to_txt(f'{LOCAL_PATH}{FILENAME}', wrong_answers_list)
