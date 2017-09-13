# Microservice for Search Index of Phone Numbers

This script normalize phone numbers for format like `9291112233`.\
Script running as daemon in background.\
If connect with database will be lost - script trying connecting to db again every 2 min(can be changed). \
Script request new phone numbers for edit every 5 min(can be changed).

# How to install

1. Recomended use venv or virtualenv for better isolation.\
   Venv setup example: \
   `python3 -m venv myenv`\
   `source myenv/bin/activate`
2. Install requirements: \
   `pip3 install -r requirements.txt` (alternatively try add `sudo` before command)
3. Open `env_conf` and correct values: 
    - for connection timeout (if some troubles with connect to database) `CONNECT_TIMEOUT`. Must be in seconds! 
    - for request new phone numbers `REQUEST_TIMEOUT`. Must be in seconds! 
    - URL for your database `DB_URI`. Example pattern:\
     `<engine>://<username>:<password>@<host>:<port>/<database>`
4. Add new environment parameters to Your system: `source env_conf`
    
# How to use
Firstly, create new column(named `edited_contact_phone`) for edited phone numbers:\
`alembic upgrade head` \
Second step - run script: \
`python3 daemonize_phones.py`
# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
