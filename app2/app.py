from flask import Flask, render_template_string

app = Flask(__name__)
LOG_FILE = "/shared/errors.log"

@app.route("/")
def index():
    try:
        with open(LOG_FILE, "r") as f:
            logs = f.read()
    except FileNotFoundError:
        logs = "No logs yet."

    html = """
    <h1>System Errors</h1>
    <pre>{{ logs }}</pre>
    """
    return render_template_string(html, logs=logs)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)