import os

SECRET_KEY = 'e1c6fe5819c4bc8857e2cbce963a7be5904692eba862d1a809f195710aff5cdc'
SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://std_1679_exam:1q2w3e4r@std-mysql.ist.mospolytech.ru/std_1679_exam'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True
ADMIN_ROLE_ID = 1
MODER_ROLE_ID = 2
USER_ROLE_ID = 3
UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'media', 'images')