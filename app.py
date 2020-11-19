from flask import Flask, redirect, request, url_for, render_template
app = Flask(__name__)


@app.route("/")
def home():
    message = request.args.get("message")
    return render_template("index.html", message=message)


@app.route("/test")
def test():
    return url_for("static", filename="sqsq")


@app.route("/id/<user>")
def sample(user):
    return render_template("index.html", message=user)


@app.route('/upload', methods=['POST'])
def upload_file():
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        uploaded_file.save("static/upload/" + uploaded_file.filename)
    return render_template("view.html", path=uploaded_file.filename)


# app.run(debug=True)
if __name__ == '__main__':
    app.run(debug=True)
