import hashlib
import random
import base64
import uuid
import datetime


def activation_key_generator():
    """
    Activation key -> generated from combination
    email and random salt SHA1 hash

    """

    salt_made = str(random.random())
    salt = hashlib.sha1(salt_made).hexdigest()[:10]
    email = "dogancankilment@gmail.com"

    expire_date = datetime.datetime.today() + datetime.timedelta(3)
    expire_date_encode = base64.b64encode(
        str(expire_date))

    if isinstance(email, unicode):
        email = email.encode('utf-8')

    activation_key = expire_date_encode.split('=')[0] + hashlib.sha1(
        salt + email).hexdigest()[:10]

    # -- variable control place --
    print len(activation_key)
    print len(expire_date_encode)

    print "random salt_made number",\
        salt_made
    print "hashlib-salt: \n",\
        salt
    print "email: \n",\
        email
    print "activation_key: \n",\
        activation_key
    print "expire_date_encode:",\
        expire_date_encode


def new_generator():
    """
    Trying encode and decode process

    """

    expire_date = datetime.datetime.today() + datetime.timedelta(3)
    email = "dogancankilment@gmail.com"

    activation_key = base64.b64encode(
        str(expire_date)) + base64.b64encode(
        str(email)).split('=')[0]

    print "email control: ",\
        base64.b64decode(
            activation_key.split('=')[1] + '==')
    print "expire date control: ",\
        base64.b64decode(
            activation_key.split('=')[0] + '=')
    print activation_key


def activation_key_generator_reversible():
    """
    another version for try uuid.uuid4()
    random number generator

    """

    salt = uuid.uuid4().hex

    print "salt:",\
        salt
    print "uuid.uuid4():",\
        uuid.uuid4()
    print "uuid.uuid4().hex::",\
        uuid.uuid4().hex

    example_number = "12345678"
    hashed_number = hashlib.sha256(
        salt.encode() + example_number.encode()).hexdigest() + ':' + salt

    print "hashed number: ",\
        hashed_number


if __name__ == '__main__':
    # activation_key_generator()
    # activation_key_generator_reversible()
    new_generator()