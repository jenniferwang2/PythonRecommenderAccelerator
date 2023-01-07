from flask import Flask, render_template, request, url_for, jsonify
from Recommender import do_Predict

app = Flask(__name__)
#a simple get request that will display the result in your browser. You can extend this with a POST request where user and item is provided as input.
@app.route("/predictions", methods=['GET'], strict_slashes=False, endpoint='func1')
def predictions():
    return jsonify(do_Predict())



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(use_reloader=False)

