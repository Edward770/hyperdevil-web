from flask import Flask, render_template, request, redirect, flash

app = Flask(__name__)
app.secret_key = "hyper-devil-demo"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        flash("Session Started (Simulated) ✅", "success")
    return render_template("index.html")

@app.route("/stop", methods=["POST"])
def stop():
    flash("Session Stopped (Simulated) ⛔", "error")
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
