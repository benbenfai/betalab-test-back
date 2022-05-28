from flask_bcrypt import Bcrypt

pw_hash = Bcrypt.generate_password_hash('123', 'a3af94dbd21c266ce08e34750420b67bfef6f7fe9190b4991c8991e495eb600b').decode('utf-8')
print(pw_hash)
Bcrypt.check_password_hash(pw_hash, 'a3af94dbd21c266ce08e34750420b67bfef6f7fe9190b4991c8991e495eb600b')
print(Bcrypt.check_password_hash(pw_hash, 'a3af94dbd21c266ce08e34750420b67bfef6f7fe9190b4991c8991e495eb600b'))