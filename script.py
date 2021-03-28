import io
import sys
import hashlib

def hash_file(file: io.TextIOBase) -> str:
    h = hashlib.sha256()
    with open(file, "rb") as f:
        while True:
            chunk = f.read(1024)
            if not chunk:
                break
            h.update(chunk)
    return h.hexdigest()

def hash_string(str: str) -> str:
    h = hashlib.sha256()
    h.update(str.encode('utf-8'))
    return h.hexdigest()

def add_whitespace(text):
    if isinstance(text, io.TextIOBase):
        with open(file, "a") as f:
            f.write(" ")
    else:
        return text + " "

def file_to_string(filename: str) -> str:
    with open(file, "r") as f:
        return f.read()

def generate_hashes(file: io.TextIOBase, num_hashes: int) -> list:
    hashes = []
    s = file_to_string(file)
    for i in range(num_hashes):
        hashes.append(hash_string(s))
        s = add_whitespace(s)
    return hashes

def birthday_attack(real: str, fake: str, digits = 2: int, num_hashes = 5000: int):
    real_hashes = generate_hashes(real, num_hashes)
    fake_hashes = generate_hashes(fake, num_hashes)
    collisions = 0

    for real_hash in real_hashes:
        for fake_hash in fake_hashes:
            if real_hash[-digits:] == fake_hash[-digits:]:
                print(f"Collision found (last {digits} hex values):\n{real_hash}\n{fake_hash}\n")
                collisions += 1
    print(f"Number of collisions with {2 * num_hashes} hashes: {collisions}")
