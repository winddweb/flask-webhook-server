# flask-github-webhook

**Author:** Yifeng Huang

## Introduction

This is a simple web-server that handles webhook request from Github.com and send messages to qq chat application.

## Example output

```
github_bot  10:06:37
[swe525-hw1:master] 2 new commits by Yifeng
github_bot  10:06:38
b11b9a: fix: bug fix - Yifeng
github_bot  10:06:39
122786: fix: more bugs it's insane #123 - Yifeng
```

## Just in case

if you don't know qq, please google it. 

You need an account, and probably a cellphone app installed before you can run qqbot.

## Setup

Change the settings.conf before you start the server.

Also don't forget to setup the webhook on Github for your repository.

Change the `settings-example.conf` to `settings.conf`

## Dependencies

- [qqbot](https://github.com/pandolia/qqbot)


- [python-github-webhook](https://github.com/bloomberg/python-github-webhook)


- [flask](https://github.com/pallets/flask)