from argon2 import PasswordHasher


def generate_hash(pw_raw):
    ph = PasswordHasher()
    return ph.hash(pw_raw)