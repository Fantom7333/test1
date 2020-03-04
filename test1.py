from flask import Flask, render_template, request, redirect, url_for, session
import requests
app = Flask(__name__, template_folder="templates")



@app.route('/', methods=['GET', 'POST'])
def home():
    requests.post("http://127.0.0.1:5000/", data={id:"TEST1", text:"Page for test"})
