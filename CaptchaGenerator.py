import random
import string

codes = list(string.ascii_uppercase + string.ascii_lowercase + string.digits)
Captcha = ""
for i in range(0, 5):
    Captcha += random.choice(codes)
print(Captcha)
