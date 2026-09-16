import ollama
from datetime import datetime
from pytz import timezone
from time import sleep
import holidays

#To-Do list:

#1. Make it generate 5 MOTDs, and have it rate which one is funniest

tz = timezone("US/Eastern")  # Better than "EST" (handles daylight saving)

date = f"{datetime.now(tz).day + 1}/{datetime.now(tz).month}/{datetime.now(tz).year}"

us_holidays = holidays.US()

ai_prompt = f"""This is an automated Python script. Below are 10 example Messages Of The Day.
I want you to create your own based on their humor style.
Do not send any other information, only the message of the day.

For reference, todays date is {date} in dd/mm/yyyy format.
The holidays today are: {us_holidays.get(f"{date}")}

Also, this API is accessible to every country that has internet access, so be sure not to make any jokes that could be offensive to any specific Race, Religion, Sex, ect. You are allowed to make fun of Scientology.

Examples:
hi
today is a day
happy christmas guys
i wanna eat waffles for breakfast
dont search up google on google or the nukes will launch
free robux
no more free robux guys, i only give away paid robux now.
guys its ai dont fall for it
subscribe to my video and like the channel pls
This Message-Of-The-Day is brought to you by Nord VPN!"""


def generate_motd():
    response = ollama.generate(
        model="llama3.2",
        prompt=ai_prompt
    )
    return response["response"].strip()


def save_motd(text):
    with open("motd.txt", "w", encoding="utf-8") as f:
        f.write(text)
    with open("motd.history.txt", "a", encoding="utf-8") as f:
        f.write(f"{text}\n")
    print(f"[{datetime.now(tz)}] New MOTD saved: {text}")


# Generate one immediately on start
motd = generate_motd()
save_motd(motd)

print("MOTD generator started...")

while True:
    now = datetime.now(tz)

    # Generate a new one every day at 23:55
    if now.hour == 23 and now.minute == 55 and now.second < 2:
        motd = generate_motd()
        save_motd(motd)
        sleep(2)  # prevent generating multiple times in the same minute

    sleep(1)