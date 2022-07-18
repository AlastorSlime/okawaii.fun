from quart import Blueprint

core = Blueprint(
    "core",
    __name__,
    template_folder="templates"
)

from . import views 