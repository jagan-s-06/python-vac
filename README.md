<p align="center"><img src="https://via.placeholder.com/250x250.png?text=Your+Logo+Here"></p>

<p align="center">
    <a href="https://twitter.com/yourusername">
      <img src="https://img.shields.io/badge/-TWITTER-black?logo=twitter&style=for-the-badge">
    </a>
    &nbsp;
    <a href="https://yourwebsite.com/">
      <img src="https://img.shields.io/badge/-WEBSITE-black?logo=web&style=for-the-badge">
    </a>
    &nbsp;
    <a href="https://github.com/yourusername">
      <img src="https://img.shields.io/badge/-GITHUB-black?logo=github&style=for-the-badge">
    </a>
</p>

<p align="center">
  <br>
  <b>Powered By</b>
  <br>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white">
  <img src="https://img.shields.io/badge/SMTP-005571?style=for-the-badge&logo=minutemailer&logoColor=white">
</p>

<p>
  <a style="margin-right: 10px;" href="#installation">
    <img src="https://dabuttonfactory.com/button.png?t=INSTALL&f=Open+Sans&ts=15&tc=000&hp=25&vp=10&c=5&bgt=unicolored&bgc=00e2ff">
  </a>
  <a style="margin-right: 10px;" href="#usage">
    <img src="https://dabuttonfactory.com/button.png?t=USAGE&f=Open+Sans&ts=15&tc=000&hp=25&vp=10&c=5&bgt=unicolored&bgc=00e2ff">
  </a>
  <a href="#demo">
    <img src="https://dabuttonfactory.com/button.png?t=DEMO&f=Open+Sans&ts=15&tc=000&hp=25&vp=10&c=5&bgt=unicolored&bgc=00e2ff">
  </a>
</p>

Concept behind this project is simple, provide a seamless web interface using Flask to handle incoming user data, and standard SMTP to route that data as email notifications. Read more on <a href="https://yourwebsite.com"> Your Blog </a>. This Hosts a web server which processes web forms and if the target submits it, we can get:

* Form Fields
* Browser Name and Version
* Public IP Address
* Time of Submission

Along with form data we also get **Automated Email Delivery** without complex APIs:

* Lightweight Web Server
* Automated SMTP Delivery via Python's native `smtplib`
* Dynamic HTML Templates using Jinja2
* Environment Variable Protection via `.env` files

**This tool is a Proof of Concept and is for Educational Purposes Only. It shows how data flows from a web interface to an inbox.**

## Architecture & Algorithm Logic

Here is a visual representation of how the data flows from the client to the inbox:

```text
[ Web Client ] 
      │
      ▼ (HTTP POST)
┌──────────────────────────────────────────┐
│              FLASK SERVER                │
│  1. Route Intercepts Request             │
│  2. Validates Form Data                  │
│  3. Renders Jinja2 Email Template        │
└────────────────────┬─────────────────────┘
                     │
                     ▼ (SMTP Auth / STARTTLS)
            [ SMTP Mail Server ]
                     │
                     ▼
           [ Recipient's Inbox ]
```

## Tested On :

* Kali Linux
* BlackArch Linux
* Ubuntu
* Fedora
* Windows 10/11
* OSX - Monterey v.12.0.1

## Installation

### Standard Setup

```bash
git clone [https://github.com/yourusername/your-repo-name.git](https://github.com/yourusername/your-repo-name.git)
cd your-repo-name/
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Docker

```bash
docker pull yourusername/flask-smtp
```

## Usage

Create a `.env` file in the root directory and add your email settings:

```bash
FLASK_APP=app.py
FLASK_ENV=development
FLASK_PORT=5000

# SMTP Settings
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SMTP_EMAIL=your-email@example.com
SMTP_PASSWORD=your-app-password
```

```bash
python3 app.py -h

usage: app.py [-h] [-p PORT] [-d]

options:
  -h, --help                            show this help message and exit
  -p PORT, --port PORT                  Web server port [ Default : 5000 ]
  -d, --debug                           Enable Flask debug mode 

##################
# Usage Examples #
##################

# Step 1 : In first terminal
$ python3 app.py

# Step 2 : In second terminal start a tunnel service such as ngrok
$ ./ngrok http 5000
```

## Local Tunnels
Use
```
ssh -R 80:localhost:5000 nokey@localhost.run
```
as an alterntive to ngrok

## Demo

**YouTube**

<a href="https://youtube.com/your-video-link">
  <img src="https://via.placeholder.com/800x450.png?text=Click+to+Watch+Demo+Video">
</a>
