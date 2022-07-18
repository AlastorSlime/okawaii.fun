from quart import Quart

def create_app() -> Quart:
    """
    Application factory.
    """
    app = Quart(
        __name__,
        static_folder="static"
    )

    CONFIG_OBJ = "config.AppConfig"
    app.config.from_object(CONFIG_OBJ)

    # Register blueprints.
    register_blueprints(app)

    # Connect to database.
    # Generate schemas if haven't already.
    initialize_database(app)

    return app 


def register_blueprints(app: Quart):
    from . import admin 
    from . import auth
    from . import core 
    
    app.register_blueprint(admin.admin)
    app.register_blueprint(auth)
    app.register_blueprint(core)


def initialize_database(app: Quart):
    from tortoise.contrib.quart import register_tortoise

    register_tortoise(
        app,
        db_url=app.config["POSTGRESQL_CONNECTION_STRING"],
        modules={
            "models": [
                "app.models"
            ],
        },
        generate_schemas=True,
    )