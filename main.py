from flask import Flask, send_from_directory

# Serve the project folder itself so relative paths like images/, css/ and js/ resolve.
app = Flask(__name__, static_folder=".", static_url_path="")


@app.route("/")
def index():
    return send_from_directory(".", "index.html")


if __name__ == "__main__":
    # Port 5000 is used by AirPlay Receiver on macOS, so use 5001.
    app.run(host='0.0.0.0', port=5001)
