#encrypting data
#hello ->encrypt()->2713hjasdfg345
import hashlib
password = input("Enter the Password:")
password = password.encode('utf-8')
password = hashlib.sha256(password).hexdigest()
print(password)