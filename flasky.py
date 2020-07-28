from flask import Flask, abort, request, jsonify

app = Flask(__name__)


@app.route('/test', methods=['POST'])

def str_json():
    try:
        string_to_cut = request.get_json["string_to_cut"]
    except:
        print('POST request key not recognized')
        abort(400)
    final_string = string_cut(string_to_cut)
    return jsonify({"return_string": final_string,})


def string_cut(str_cut):
    new_str = ""
    i = 0
    for item in str_cut:
        str_cut = str_cut[i:]
        if i == 2:
            new_str += item
            i = 0
        else:
            i += 1
    return new_str


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=4998, debug=True)
