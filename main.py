from flask import Flask, redirect, request
import cgi
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding; 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius:
            }}
            textarea{{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form action = '/' method = ['POST']>
            <label for ='input'>Rotate by:</label>
            <input type='text' name = 'rot' value = 0 />
            
            <textarea name = 'textarea'>{0}</textarea>           

            <br>

            <input type ='submit' value='Submit Query' />
        </form>
    </body>
    </html>
"""

@app.route('/')
def index():
    return form.format(" ")

@app.route('/', methods=['POST'])
def encrypt():
    
    rot = int(request.form.get('rot'))
    text = request.form.get('textarea')

    return form.format("<h1>" + rotate_string(text, rot) + "</h1>")


app.run()