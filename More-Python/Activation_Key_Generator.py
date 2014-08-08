"""
Activation key -> generated from combination
email and random salt SHA1 hash

"""

import hashlib
import random


salt = hashlib.sha1(str(random.random())).hexdigest()[:10]
email = "dogancankilment@gmail.com"

if isinstance(email, unicode):
    email = email.encode('utf-8')
activation_key = hashlib.sha1(salt+email).hexdigest()

print "hashlib-salt: \n", salt
print "email: \n", email
print "activation_key: \n", activation_key
