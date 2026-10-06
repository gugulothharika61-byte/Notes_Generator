from flask import Flask, render_template, request
from notes_generator import generate_notes

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    notes = []
    original_text = ""

    if request.method == "POST":
        original_text = request.form.get("text", "")

        if original_text.strip():
            notes = generate_notes(original_text)

    return render_template(
        "index.html",
        notes=notes,
        original_text=original_text
    )


if __name__ == "__main__":
    app.run(debug=True)