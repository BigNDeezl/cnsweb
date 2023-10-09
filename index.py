from flask import Flask
cnsweb = Flask(__name__)

@cnsweb.route("/")
def run():
    return "Hello Updated Git World"

if __name__ == "__main__":
    cnsweb.run(host="0.0.0.0", port=int("3000"), debug=True)