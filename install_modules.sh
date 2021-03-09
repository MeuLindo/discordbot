#!/bin/bash

python3 -m venv venv
source venv/bin/activate

python3 -m pip install requests
python3 -m pip install html2text
python3 -m pip install discord.py
python3 -m pip install python-dotenv
