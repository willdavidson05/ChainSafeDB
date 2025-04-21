import hashlib

def hash_record(record: str) -> str:
    return hashlib.sha256(record.encode()).hexdigest()
