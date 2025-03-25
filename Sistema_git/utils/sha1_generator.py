from hashlib import sha1

def generate_sha1_checksum(filename):
    with open(filename, "rb") as f:
        file_data = f.read()
    return sha1(file_data).hexdigest()