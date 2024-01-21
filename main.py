import random
while True:
    lang = input('Choose your language: russian english spanish french turkish chinese ')
    selected_languages = lang.split()
    for lang in selected_languages:
        if lang == 'russian':
            print('Добро пожаловать на генератор паролей!')
            password_characters = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
            password_length = int(input("Введите длину пароля: "))
            generated_password = ""
            for t in range(password_length):
                generated_password += random.choice(password_characters)
            print("Сгенерированный пароль:", generated_password)
        elif lang == 'english':
            print('Welcome to password generator!')
            password_characters = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
            password_length = int(input("Enter your password length: "))
            generated_password = ""
            for t in range(password_length):
                generated_password += random.choice(password_characters)
            print("Generated password:", generated_password)
        elif lang == 'spanish':
            print('Bienvenido al generador de contraseñas!')
            password_characters = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
            password_length = int(input("Introduzca la longitud de la contraseña: "))
            generated_password = ""
            for t in range(password_length):
                generated_password += random.choice(password_characters)
            print("Contraseña generada:", generated_password)
        elif lang == 'french':
            print('Bienvenue sur le générateur de mots!')
            password_characters = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
            password_length = int(input("Entrez la longueur de votre mot de passe: "))
            generated_password = ""
            for t in range(password_length):
                generated_password += random.choice(password_characters)
            print("Mot de passe généré:", generated_password)
        elif lang == 'turkish':
            print('Şifre oluşturucuya hoş geldiniz!')
            password_characters = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
            password_length = int(input("Şifre uzunluğunu girin: "))
            generated_password = ""
            for t in range(password_length):
                generated_password += random.choice(password_characters)
            print("Oluşturulan şifre:", generated_password)
        elif lang == 'chinese':
            print('歡迎使用密碼產生器')
            password_characters = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
            password_length = int(input("輸入您的密碼長度: "))
            generated_password = ""
            for t in range(password_length):
                generated_password += random.choice(password_characters)
            print("產生的密碼:", generated_password)
        else:
            print('Write number 1-7 to choose your language or your language aint defined)')
