import tkinter


class Skill:
    def __init__(self, skill_name, image_path, level):
        self.skill = skill_name
        self.image = image_path
        self.level = level
        self.plus = "plus_sign.png"
        self.minus = "minus_sign.png"
        self.image = tkinter.PhotoImage(file=rf"{self.image}")
        self.plus = tkinter.PhotoImage(file=rf"{self.plus}")
        self.minus = tkinter.PhotoImage(file=rf"{self.minus}")

    def level_up(self):
        self.level += 1
        return self.level


    def level_down(self):
        self.level -= 1
        return self.level




