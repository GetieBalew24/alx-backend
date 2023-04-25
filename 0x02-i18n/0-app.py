#!/usr/bin/env python3
""" setup a basic Flask app in 0-app.py
"""


from flask import Flask, render_template
app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET'], strict_slashes=False)
def helloWorld() -> str:
    """
    Returns:
        str:  return Welcome to Holberton
    """
    return render_template('0-index.html')
if __name__ == '__main__':
    app.run()