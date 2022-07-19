from secretbox import SecretBox

secrets = SecretBox(auto_load=True)

class AppConfig:
    """
    Base configuration class. Configuration settings for all all environments.
    """
    
    # Default settings.
    QUART_ENV = "development"
    DEBUG = True
    TESTING = True
    WTF_CSRF_ENABLED = True 

    # Environemntal settings.
    SECRET_KEY = secrets.get("APP_SECRET_KEY")
    POSTGRESQL_CONNECTION_STRING = secrets.get("POSTGRESQL_CONNECTION_STRING")

    # Admin Credentials.
    ADMIN_USERNAME = secrets.get("ADMIN_USERNAME")
    ADMIN_PASSWORD = secrets.get("ADMIN_PASSWORD")