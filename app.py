from flask import Flask, render_template

app = Flask(__name__)

@app.get("/")
def index():
    return render_template("index.html", title="AI@UNC")

@app.get("/projects")
def projects():
    return render_template("projects.html", title="Projects | AI@UNC")

@app.get("/programs")
def programs():
    return render_template("programs.html", title="Programs | AI@UNC")

@app.get("/events")
def events():
    return render_template("404new.html", title="Events | AI@UNC")

@app.get("/contact")
def contact():
    return render_template("404new.html", title="Contact | AI@UNC")

@app.get("/join")
def join():
    return render_template("join.html", title="Join | AI@UNC")

@app.errorhandler(404)
def not_found(e):
    return render_template("404.html", title="404 | AI@UNC"), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
