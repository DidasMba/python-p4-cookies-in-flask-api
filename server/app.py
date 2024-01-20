from flask import Flask, session, jsonify, make_response, request
import os

app = Flask(__name__)

# Set a secret key for the session (needed for secure session handling)
app.secret_key = os.urandom(24)

@app.route('/sessions/<string:key>', methods=['GET'])
def show_session(key):
    # Set values in the session object
    session["hello"] = session.get("hello") or "World"
    session["goodnight"] = session.get("goodnight") or "Moon"

    # Create a response containing session and cookie information
    response = make_response(jsonify({
        'session': {
            'session_key': key,
            'session_value': session[key],
            'session_accessed': session.accessed,
        },
        'cookies': [{cookie: request.cookies[cookie]}
                     for cookie in request.cookies],
    }), 200)

    # Set a new cookie
    response.set_cookie('mouse', 'Cookie')

    return response

if __name__ == '__main__':
    app.run(debug=True, port=5555)

    