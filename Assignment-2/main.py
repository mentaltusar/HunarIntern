from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    happiness = None
    if request.method == "POST":
        n = int(request.form["n"])
        m = int(request.form["m"])
        array = list(map(int, request.form["array"].split()))
        A = set(map(int, request.form["A"].split()))
        B = set(map(int, request.form["B"].split()))

        happiness = 0
        for element in array:
            if element in A:
                happiness += 1
            elif element in B:
                happiness -= 1

    return render_template("index.html", happiness=happiness)


if __name__ == "__main__":
    app.run(debug=True)
