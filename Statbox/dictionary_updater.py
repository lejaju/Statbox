import pickle
"""This file works as a dictionary updater for data.pkl file. 
Modify the dictionary below and run the script once in order to add your
own skills for main.py where you can assign them into a Skill class."""

skilla_list = {
    "python": 1,
    "cpp": 1,
    "ctf": 1,
    "game_dev": 1,
    "game_hacking": 1,
    "yoga": 1,
    "meditation": 11,
    "prayer": 1,
    "running": 1,
    "cooking": 1,
    "discipline": 1,
    "chess": 1,
    "producing": 1,
    "writing": 1,
    "freestyling": 1,
    "reading": 1,
    "audiobooks": 1,
    "speedcubing": 1,
}
a_file = open("data.pkl", "wb")
pickle.dump(skilla_list, a_file)
a_file.close()
