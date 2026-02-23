class GeneralConfig:
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(GeneralConfig):
    SQLALCHEMY_DATABASE_URI = "sqlite:///app.db"