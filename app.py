import flask
import slackclient
import os
from flask import request

slacktoken = os.getenv("slacktoken")
slackchannel = os.getenv('slackchannel')

app = flask.Flask('LemmeIn')
slack = slackclient.SlackClient(token=slacktoken)


@app.route('/')
def index():
    return flask.send_from_directory('.', 'index.html')


@app.route('/submit', methods=['POST', 'GET'])
def submit():
    name = request.values.get('name')
    door = request.values.get('door')
    composed_string = "{} needs to be let in at the {} door".format(name, door)
    call = slack.api_call(
        "chat.postMessage",
        channel=slackchannel,
        text=composed_string
    )
    print(call)
    print(composed_string)
    return flask.send_from_directory('.', 'submitted.html')
