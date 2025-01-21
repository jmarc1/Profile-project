from flask import Flask, session

app = Flask(__name__)
app.secret_key="there are a lot of secrets"

