from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

df = pd.read_csv("dictionary.csv")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/api/v1/<word>")
def definition(word):
    definition = df.loc[df["word"] == word]["definition"].squeeze()
    result_dict = {"Definition": definition, "Word": word}
    return result_dict

app.run(debug=True, port=5001)
