from quart import Quart

def create_app() -> Quart:
    """
    Application factory.
    """
    app = Quart(
        __name__,
        static_folder="static",
        template_folder="templates",
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
    from app.blueprints.admin import admin_blueprint
    from app.blueprints.auth import auth_blueprint
    from app.blueprints.core import core_blueprint

    app.register_blueprint(admin_blueprint)
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(core_blueprint)


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