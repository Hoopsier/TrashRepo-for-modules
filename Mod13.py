from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/alkuluku/<number>")
def get_is_prime(number):
    isPrime = True
    number = int(number)
    if number <= 1:
        isPrime = False

    for i in range(2, number):
        if i % number == 0:
            isPrime = False

    data = {
        "number": number,
        "isPrime": isPrime
    }
    return jsonify(data), 200


if __name__ == "__main__":
    app.run(debug=True)
