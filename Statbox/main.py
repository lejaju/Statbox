import tkinter
from skills import Skill
import pickle
from typing import Dict



"""Saving the modified dictionary into a .pkl file. """
def save_to_file(skilli):
    a_file = open("data.pkl", "wb")
    pickle.dump(skilli, a_file)
    a_file.close()


"""Level ups a skill inside a Skill object and saves it into a .pkl file"""
def func_up_level(skill: Skill, skill_list: Dict):
    skill_list[skill.skill] = skill.level_up()
    skill_list = save_to_file(skill_list)
    skill.msg.configure(text=f"{skill.level}/99")


def func_down_level(skill: Skill, skill_list: Dict):
    skill_list[skill.skill] = skill.level_down()
    skill_list = save_to_file(skill_list)
    skill.msg.configure(text=f"{skill.level}/99")


def create_message(skill: Skill):
    return tkinter.Label(win, font=FONT, justify="left",
                         borderwidth=0, border=0, anchor="w", text=f"{skill.level}/99", background="#c8c8c8")

def create_label(image_object):
    return tkinter.Label(win, image=image_object, width=110, height=78)


def create_plus(skill: Skill):
    return tkinter.Button(image=skill.plus, command=lambda: func_up_level(skill, skill_list),
                          borderwidth=0,background="#c8c8c8",
                          bd=0, activebackground="#c8c8c8", width=9, height=9)


def create_minus(skill: Skill):
    return tkinter.Button(image=skill.minus, command=lambda: func_down_level(skill, skill_list),background="#c8c8c8",
                          bd=0, activebackground="#c8c8c8", width=9, height=9)


# Program starts by loading the data and creating a dictionary called skill_list
data_file = open("data.pkl", "rb")
skill_list = pickle.load(data_file)
data_file.close()

# Assigning a font const and other GUI data
FONT = ("MV Boli", 10, "bold")
win = tkinter.Tk()
win.geometry('338x484')
win.resizable(False, False)
win.title("Statbox")
win.wm_attributes("-transparentcolor", 'grey')
# Creating the skill objects and resources and placing them into the GUI

# Python
python = Skill("python", "python_logo.png", skill_list["python"])
python_label = create_label(python.image)
python_label.place(x=0, y=2)
python.msg = create_message(python)
python.msg.place(x=55, y=32)
python_plus = create_plus(python)
python_plus.place(x=78, y=52)
python_minus = create_minus(python)
python_minus.place(x=58, y=52)

# C++
cpp = Skill("cpp", "cpp_logo.png", skill_list["cpp"])
cpp_label = create_label(cpp.image)
cpp_label.place(x=112, y=2)
cpp.msg = create_message(cpp)
cpp.msg.place(x=165, y=32)
cpp_plus = create_plus(cpp)
cpp_plus.place(x=192, y=52)
cpp_minus = create_minus(cpp)
cpp_minus.place(x=170, y=52)

# CTF
ctf = Skill("ctf", "ctf_logo.png", skill_list["ctf"])
ctf_label = create_label(ctf.image)
ctf_label.place(x=224, y=2)
ctf.msg = create_message(ctf)
ctf.msg.place(x=281, y=32)
ctf_plus = create_plus(ctf)
ctf_plus.place(x=311, y=52)
ctf_minus = create_minus(ctf)
ctf_minus.place(x=291, y=52)

# Game-dev
game_dev = Skill("game_dev", "gamedev_logo.png", skill_list["game_dev"])
game_dev_label = create_label(game_dev.image)
game_dev_label.place(x=0, y=82)
game_dev.msg = create_message(game_dev)
game_dev.msg.place(x=60, y=119)
game_dev_plus = create_plus(game_dev)
game_dev_plus.place(x=88, y=139)
game_dev_minus = create_minus(game_dev)
game_dev_minus.place(x=68, y=139)

# Game-hacking
game_hacking = Skill("game_hacking", "gamehacking_logo.png", skill_list["game_hacking"])
game_hacking_label = create_label(game_hacking.image)
game_hacking_label.place(x=112, y=82)
game_hacking.msg = create_message(game_hacking)
game_hacking.msg.place(x=165, y=119)
game_hacking_plus = create_plus(game_hacking)
game_hacking_plus.place(x=192, y=139)
game_hacking_minus = create_minus(game_hacking)
game_hacking_minus.place(x=172, y=139)

# Discipline
discipline = Skill("discipline", "discipline_logo.png", skill_list["discipline"])
discipline_label = create_label(discipline.image)
discipline_label.place(x=224, y=82)
discipline.msg = create_message(discipline)
discipline.msg.place(x=281, y=119)
discipline_plus = create_plus(discipline)
discipline_plus.place(x=311, y=139)
discipline_minus = create_minus(discipline)
discipline_minus.place(x=291, y=139)

# Yoga
yoga = Skill("yoga", "yoga_logo.png", skill_list["yoga"])
yoga_label = create_label(yoga.image)
yoga_label.place(x=0, y=162)
yoga.msg = create_message(yoga)
yoga.msg.place(x=55, y=199)
yoga_plus = create_plus(yoga)
yoga_plus.place(x=83, y=218)
yoga_minus = create_minus(yoga)
yoga_minus.place(x=63, y=218)

# Meditation
meditation = Skill("meditation", "meditation_logo.png", skill_list["meditation"])
meditation_label = create_label(meditation.image)
meditation_label.place(x=112, y=162)
meditation.msg = create_message(meditation)
meditation.msg.place(x=165, y=199)
meditation_plus = create_plus(meditation)
meditation_plus.place(x=192, y=218)
meditation_minus = create_minus(meditation)
meditation_minus.place(x=172, y=218)

# Prayer
prayer = Skill("prayer", "prayer_logo.png", skill_list["prayer"])
prayer_label = create_label(prayer.image)
prayer_label.place(x=224, y=162)
prayer.msg = create_message(prayer)
prayer.msg.place(x=281, y=199)
prayer_plus = create_plus(prayer)
prayer_plus.place(x=311, y=219)
prayer_minus = create_minus(prayer)
prayer_minus.place(x=291, y=219)

# Running
running = Skill("running", "running_logo.png", skill_list["running"])
running_label = create_label(running.image)
running_label.place(x=0, y=242)
running.msg = create_message(running)
running.msg.place(x=55, y=279)
running_plus = create_plus(running)
running_plus.place(x=78, y=298)
running_minus = create_minus(running)
running_minus.place(x=58, y=298)

# Cooking
cooking = Skill("cooking", "cooking_logo.png", skill_list["cooking"])
cooking_label = create_label(cooking.image)
cooking_label.place(x=112, y=242)
cooking.msg = create_message(cooking)
cooking.msg.place(x=168, y=279)
cooking_plus = create_plus(cooking)
cooking_plus.place(x=192, y=298)
cooking_minus = create_minus(cooking)
cooking_minus.place(x=172, y=298)

# Chess
chess = Skill("chess", "chess_logo.png", skill_list["chess"])
chess_label = create_label(chess.image)
chess_label.place(x=224, y=242)
chess.msg = create_message(chess)
chess.msg.place(x=275, y=279)
chess_plus = create_plus(chess)
chess_plus.place(x=300, y=298)
chess_minus = create_minus(chess)
chess_minus.place(x=280, y=298)

# Producing
producing = Skill("producing", "producing_logo.png", skill_list["producing"])
producing_label = create_label(producing.image)
producing_label.place(x=0, y=322)
producing.msg = create_message(producing)
producing.msg.place(x=62, y=361)
producing_plus = create_plus(producing)
producing_plus.place(x=87, y=380)
producing_minus = create_minus(producing)
producing_minus.place(x=67, y=380)

# Writing
writing = Skill("writing", "writing_logo.png", skill_list["writing"])
writing_label = create_label(writing.image)
writing_label.place(x=112, y=322)
writing.msg = create_message(writing)
writing.msg.place(x=168, y=361)
writing_plus = create_plus(writing)
writing_plus.place(x=192, y=380)
writing_minus = create_minus(writing)
writing_minus.place(x=172, y=380)

# Freestyling
freestyling = Skill("freestyling", "freestyle_logo.png", skill_list["freestyling"])
freestyling_label = create_label(freestyling.image)
freestyling_label.place(x=224, y=322)
freestyling.msg = create_message(freestyling)
freestyling.msg.place(x=275, y=361)
freestyling_plus = create_plus(freestyling)
freestyling_plus.place(x=300, y=380)
freestyling_minus = create_minus(freestyling)
freestyling_minus.place(x=280, y=380)

# Reading
reading = Skill("reading", "reading_logo.png", skill_list["reading"])
reading_label = create_label(reading.image)
reading_label.place(x=0, y=402)
reading.msg = create_message(reading)
reading.msg.place(x=55, y=439)
reading_plus = create_plus(reading)
reading_plus.place(x=84, y=460)
reading_minus = create_minus(reading)
reading_minus.place(x=64, y=460)

# Audiobooks
audiobooks = Skill("audiobooks", "audiobooks_logo.png", skill_list["audiobooks"])
audiobooks_label = create_label(audiobooks.image)
audiobooks_label.place(x=112, y=402)
audiobooks.msg = create_message(audiobooks)
audiobooks.msg.place(x=168, y=439)
audiobooks_plus = create_plus(audiobooks)
audiobooks_plus.place(x=192, y=460)
audiobooks_minus = create_minus(audiobooks)
audiobooks_minus.place(x=172, y=460)

# Speedcubing
speedcubing = Skill("speedcubing", "speedcubing_logo.png", skill_list["speedcubing"])
speedcubing_label = create_label(speedcubing.image)
speedcubing_label.place(x=224, y=402)
speedcubing.msg = create_message(speedcubing)
speedcubing.msg.place(x=275, y=439)
speedcubing_plus = create_plus(speedcubing)
speedcubing_plus.place(x=300, y=460)
speedcubing_minus = create_minus(speedcubing)
speedcubing_minus.place(x=280, y=460)

win.mainloop()
