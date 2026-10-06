import re


def generate_notes(text):
    # Remove extra spaces
    text = re.sub(r"\s+", " ", text).strip()

    # Split the text into sentences
    sentences = re.split(r"(?<=[.!?])\s+", text)

    # Keep the first 6 sentences
    important_sentences = sentences[:6]

    # Create the notes list
    notes = []

    for sentence in important_sentences:
        if sentence.strip():
            notes.append(sentence.strip())

    return notes