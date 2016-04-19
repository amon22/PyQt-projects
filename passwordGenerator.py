import random
import string


class PasswordGenerator(object):
    @staticmethod
    def generate(chars, length=8):
        password = ""
        for i in range(0, length):
            password += random.choice(chars)
        return password

print PasswordGenerator.generate(string.ascii_letters, 8)


