from getpass import getpass
import hashlib
import hmac

# Assumptions: no memory-reading attacks, like kernel code injection
# or cold-boot.
#
# TODO: write a C module that tries to at least pin the secret to
# memory.
class credentials:
    def __init__(self, key, secret):
        if key:
            self._key = key
        else:
            self._key = getpass('API Key: ')
        if secret:
            self._secret = secret
        else:
            # This should really be "API Secret: ", but "Password: "
            # is recognized by Emacs and handled accordingly.
            self._secret = getpass('Password: ')

    def key(self):
        return self._key

    def hmac(self, text):
        secret = str.encode(self._secret)
        text = text
        return hmac.new(secret, text, hashlib.sha256).hexdigest()

def ask_user(emacs_friendly=False):
    key = getpass('API Key: ')
    if emacs_friendly:
        secret = getpass('Password: ')
    else:
        secret = getpass('API Secret: ')
    return credentials(key, secret)
