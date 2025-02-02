from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

quotes = [
    {"author": "Angelita Lim", "quote": "I saw that you were perfect, and so I loved you. Then I saw that you were not perfect and I loved you even more."},
    {"author": "Unknown", "quote": "To the world you may be one person, but to one person you are the world."},
    {"author": "Robert A. Heinlein", "quote": "Love is that condition in which the happiness of another person is essential to your own."},
    {"author": "Audrey Hepburn", "quote": "The best thing to hold onto in life is each other."},
    {"author": "Unknown", "quote": "I need you like a heart needs a beat."},
    {"author": "The Notebook", "quote": "I am who I am because of you. You are every reason, every hope and every dream I've ever had."},
    {"author": "Alfred Tennyson", "quote": "If I had a flower for every time I thought of you...I could walk through my garden forever."},
    {"author": "Elinor Glyn", "quote": "Romance is the glamour which turns the dust of everyday life into a golden haze."},
    {"author": "A. A. Milne", "quote": "If you live to be a hundred, I want to live to be a hundred minus one day so I never have to live without you."},
    {"author": "Goo Goo Dolls", "quote": "You're the closest to heaven that I'll ever be."}
]

def get_random_quote(name, keyword):
    matching_quotes = [quote for quote in quotes if keyword.lower() in quote["quote"].lower()]

    if matching_quotes:
        selected_quote = random.choice(matching_quotes)["quote"]
        if name:
            selected_quote = selected_quote.replace("the", name, 1) # Only replace the first instance of "the"
        return {"author": random.choice(matching_quotes)["author"], "quote": selected_quote}
    elif name:
      selected_quote = random.choice(quotes)["quote"]
      selected_quote = selected_quote.replace("the", name, 1) # Only replace the first instance of "the"
      return {"author": random.choice(quotes)["author"], "quote": selected_quote}    
    else:
        return random.choice(quotes)


@app.route("/", methods=["GET", "POST"])
def index():
    quote = None
    if request.method == "POST":
        name = request.form.get("name")
        keyword = request.form.get("keyword")
        quote = get_random_quote(name, keyword)
    return render_template("index.html", quote=quote)

if __name__ == "__main__":
    app.run(debug=True)