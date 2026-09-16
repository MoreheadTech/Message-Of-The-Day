# Message-Of-The-Day
This is the code for the Message Of The Day (motd) api made by MoreheadTech.

Distributed under the GNU General Public License 3.0

# Guide

Step 1: Install required Dependencies.

Install APT packages if not installed
```
sudo apt install python3-full screen git
```

Install NodeJS from https://nodejs.org/en/download/

Install Ollama from https://ollama.com/

Then, initialize a Python Virtual Environment
```
python3 -m venv motd
```

Install the required Python libraries
```
motd/bin/pip install ollama pytz holidays
```
Now, install the LLM the script uses
```
ollama pull llama3.2
```

Step 2: Downloading the code

Download the code
```
git clone https://github.com/MoreheadTech/Message-Of-The-Day
```

Then bring it into your home folder (or whatever folder you are in)
```
mv Message-Of-The-Day/* .
```

Step 3: Running the code

Initialize the first screen session
```
screen -S motd-main
```

Then run the code in that screen session
```
motd/bin/python3 motd.py
```

Initialize the second screen session
```
screen -S motd-api
```

And run the NodeJS API in there
```
node api.js
```

then press CTRL-A + D to exit the second screen session, then again to get back to the main terminal.

Congratulations! You now have your own MOTD bot.
