import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = "moj_tajni_kljuc"
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASE_DIR, "livecard.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False