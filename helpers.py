import hashlib, os
import binascii

def hash_password(password):
    # Generate a random salt
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    
    # Create a password hash using SHA-512 and the salt
    pwd_hash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), salt, 100000)
    
    # Convert the hash to a hexadecimal string and concatenate with the salt
    pwd_hash = binascii.hexlify(pwd_hash)
    
    return (salt + pwd_hash).decode('ascii')

def check_password(hashed_password, user_password):
    # Extract the salt and hashed password from the stored value
    salt = hashed_password[:64]
    hashed_password = hashed_password[64:]
    
    # Hash the user-provided password with the same salt and compare with stored hash
    pwd_hash = hashlib.pbkdf2_hmac('sha512', user_password.encode('utf-8'), salt.encode('ascii'), 100000)
    pwd_hash = binascii.hexlify(pwd_hash).decode('ascii')
    
    return pwd_hash == hashed_password
