class Profile(object):
    """docstring for Profile."""
    def __init__(self):
        self.name = ''
        self.gender = ''
        self.age = ''
        self.mood = ''
        self.time = ''

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_gender(self, gender):
        self.gender = gender

    def get_gender(self):
        return self.gender

    def set_age(self, age):
        self.age = age

    def get_age(self):
        return self.age

    def set_mood(self, mood):
        self.mood = mood

    def get_mood(self):
        return self.mood

    def set_time(self, time):
        self.time = time

    def get_time(self):
        return self.time
