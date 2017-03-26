#!/usr/bin/env
# -*- coding: utf-8 -*-
from github_webhook import Webhook
from flask import Flask, session, render_template
from subprocess import call
from ConfigParser import ConfigParser

config = ConfigParser()
config.read('settings.conf')
app_secret = config.get('default', 'app_secret')
endpoint = config.get('default', 'endpoint')
secret = config.get('default', 'secret')
default_receiver = config.get('default', 'default_receiver')

app = Flask(__name__)  # Standard Flask app
app.secret_key = app_secret
app.debug = True
webhook = Webhook(app, endpoint='/'+endpoint, secret=secret) # Defines '/postreceive' endpoint

@app.route("/")        # Standard Flask endpoint
def hello_world():
    return "Hello, World!"

# @app.route("/issue", methods=['GET', 'POST'])        # Standard Flask endpoint
# def hello_issue():
#     return "Hello, issue!"

def send_qq_msg(msg):
    cmd = ["qq", "send", "discuss", default_receiver]
    qq_cmd = cmd.append(msg)
    call(cmd)

def parse_event_data(data):
    msg = []
    commits = data["commits"]
    repo_name = data["repository"]["name"]
    branch_name = data["ref"].split('/')[-1]
    head_author = data["head_commit"]["author"]["name"]
    total_commits = len(commits)

    push_stat = "[{0}:{1}] {2} new commits by {3}".format(repo_name, branch_name, total_commits, head_author)
    cm_list = ["{0}: {1} - {2}".format(commit["id"][:6], commit["message"], commit["committer"]["name"]) for commit in commits ]

    msg.append(push_stat)
    msg.extend(cm_list)
    return msg

@webhook.hook()        # Defines a handler for the 'push' event
def on_push(data):
    message_body = []
    message_body = parse_event_data(data)
    # print("Got push with: {0}".format(data))
    for msg in message_body:
        send_qq_msg(msg)

@webhook.hook(event_type="ping")        # Defines a handler for the 'ping' event
def on_ping(data):
    return_data = data["zen"]
    print("Got ping with: {0}".format(return_data))
    return "Got, ping!"

@webhook.hook(event_type="issue")        # Defines a handler for the 'issue' event
def on_issue(data):
    print("Got issue with: {0}".format(data))
    return render_template('json.html', data_json = data)


if __name__ == "__main__":
  app.run(host="127.0.0.1", port=4567)