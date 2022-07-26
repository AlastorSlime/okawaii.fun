from secretbox import SecretBox

secrets = SecretBox(auto_load=True)

class AppConfig:
    """
    Base configuration class. Configuration settings for all all environments.
    """
    
    # Default settings.
    QUART_ENV = "production"
    DEBUG = False
    TESTING = False
    WTF_CSRF_ENABLED = True 

    # Environemntal settings.
    SECRET_KEY = secrets.get("APP_SECRET_KEY")
    POSTGRESQL_CONNECTION_STRING = secrets.get("POSTGRESQL_CONNECTION_STRING")