# Web Identity

This script can generate identity (alls properties of an human on internet like : name, gender, username, password, bankings informations, etc...), and store them into a sqlite database. Then it will be able to crearte an email address based on this informations using a
[MailCow](https://mailcow.github.io/mailcow-dockerized-docs) SMTP server.

In this way, the script can use the created email address to create accounts on social networks.

``run.bat`` and ``run.sh`` files are used to facilitate the use ofe the tool, but in reality there are 3 main scripts. ``identitygen.py``, which is used to create identities and register them in the database. ``identityactions.py``, which is used to perform actions on identities stored in the database. And ``identitylive.py``, which is used to perform automatic actions on identities such as spending time on social networks.

- [Requirements](#requirements)
- [Installation]()
- [Configuration](#configuration)
- [Usage](#usage)

***
## Requirements

**Python 3**

- **Your own [MailCow](https://mailcow.github.io/mailcow-dockerized-docs/) SMTP Server** configured and working
- Install [Google Chrome](https://www.google.com/intl/en_us/chrome)
- Install [Chrome Driver](https://chromedriver.chromium.org/downloads) and add it to the **PATH**
- Install the required python packages using the command bellow :
```
pip install -r requirements.txt
```

***
## Installation

### Windows
[download repository](https://github.com/danglock/)


### Linux
```
git clone https://github.com/danglock/
```


***
## Configuration
First you need to configure MailCow credentials. Go to the ``config.py`` file, then set values to following variables :

| Variable         | Description                            | Exemple value
|------------------|----------------------------------------|--------------
| mailcow_url      | The url leading to your mailcow portal | mailcow_url="https://mail.demoniak.ch"
| mailcow_username | The mailcow administrator username, used to create new addresses | mailcow_username="admin"
| mailcow_password | The passord used to connect to the administrator account | mailcow_password="s3cRet123!"


***
## Usage
### Arguments


### identitygen
| Argument       | Description |
|----------------|-------------|
| -b --banking   | Generate valid banking informations  |
| -m --mailcow   | Create an email address, make sure you have correctly followed the [configuration](#configuration) step.
| -fb --facebook | Create a facebook account
| -p --proxy     |

### identityactions
| Argument       | Description |
|----------------|-------------|
| -l --list      | List all identities stored in the database |
| -m --modify    | Modify an identity
| -i --instagram | Perform instagram operations with one ore more identities that have a registered instagram account.

exemple : 
```
identityactions.py -s
```


### identitylive
| Argument       | Description | Exemple |
|----------------|-------------|---------|
| -s<br>--select    | Live a selected identity | ``identitylive.py -s <username>`` |
| -a<br>--aleatory  | Modify an identity       |
| -fb<br>--facebook||
| -i --instagram | Perform instagram operations with one ore more identities that have a registered instagram account.