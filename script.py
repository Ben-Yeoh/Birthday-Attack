import sys
import hashlib

def hash_file(file):
    h = hashlib.sha256()
    with open(file, "rb") as f:
        while True:
            chunk = f.read(1024)
            if not chunk:
                break
            h.update(chunk)
    return h.hexdigest()

def hash_string(str):
    h = hashlib.sha256()
    h.update(str)
    return h.hexdigest()

def add_whitespace(text):
    if isinstance(text, file):
        with open(file, "a") as f:
            f.write(" ")
    else:
        return text + " "

def file_to_string(file):
    with open(file, "r") as f:
        return f.read().encode('utf-8')

def generate_hashes(file, amount):
    hashes = []
    s = file_to_string(file)
    for i in range(amount):
        hashes.append(hash_string(s))
    return hashes


def birthday_attack(digits, real, fake):
    digits = int(digits)
    real_hashes = generate_hashes(real)
    fake_hashes = generate_hashes(fake)

    for real_hash in real_hashes:
        for fake_hash in fake_hashes:
            if real_hash[-digits:] == fake_hash[-digits:]:
                print(f"Collision found (last {digits} digits):\n{real_hash}\n{fake_hash}\n")


birthday_attack(sys.argv[1], sys.argv[2], sys.argv[3])