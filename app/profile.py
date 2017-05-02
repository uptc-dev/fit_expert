class Profile(object):
    """docstring for Profile."""
    def __init__(self):
        self.name = ''
        self.gender = ''
        self.age = ''

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
