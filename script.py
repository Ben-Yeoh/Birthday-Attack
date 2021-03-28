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

def hash_string(string: str) -> str:
    h = hashlib.sha256()
    h.update(string.encode('utf-8'))
    return h.hexdigest()

def add_whitespace(text):
    if isinstance(text, io.TextIOBase):
        with open(file, "a") as f:
            f.write(" ")
    else:
        return text + " "

def file_to_string(filename: str) -> str:
    with open(filename, "r") as f:
        return f.read()

def string_to_file(string: str, filename: str):
    with open(f"output/{filename}", "w") as f:
        f.write(string)

def generate_hashes(file: io.TextIOBase, num_hashes: int) -> list:
    hashes = []
    s = file_to_string(file)

    for i in range(num_hashes):
        hash = hash_string(s)
        hashes.append({ "hash": hash, "plaintext": s })
        s = add_whitespace(s)

    return hashes

def output_hashes(real: str, fake: str, real_hash: object, fake_hash: object):
    string_to_file("Real: {}\nFake: {}\n".format(real_hash["hash"], fake_hash["hash"]), "hashes.txt")
    string_to_file(real_hash["plaintext"], real)
    string_to_file(fake_hash["plaintext"], fake)

def birthday_attack(real: str, fake: str, digits: int = 2, num_hashes: int = 5000):
    real_hashes = generate_hashes(real, num_hashes)
    fake_hashes = generate_hashes(fake, num_hashes)
    collisions = 0

    for real_hash in real_hashes:
        for fake_hash in fake_hashes:
            if real_hash["hash"][-digits:] == fake_hash["hash"][-digits:]:
                if not collisions:
                    output_hashes(real, fake, real_hash, fake_hash)
                print("Collision found (last {} hex values):\n{}\n{}\n".format(digits, real_hash["hash"], fake_hash["hash"]))
                collisions += 1
    print(f"Number of collisions with {2 * num_hashes} hashes: {collisions}")
