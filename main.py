import random
password_characters = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
password_length = int(input("Введите длину пароля: "))
generated_password = ""
for _ in range(password_length):
    generated_password += random.choice(password_characters)
print("Сгенерированный пароль:", generated_password)
