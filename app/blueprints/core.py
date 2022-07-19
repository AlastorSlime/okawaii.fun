from app.services import NotFound, UrlService

from quart import Blueprint, render_template, redirect, abort

core_blueprint = Blueprint(
    "core",
    __name__,
)

@core_blueprint.route("/")
async def root():
    return await render_template("index.html")

@core_blueprint.route("/<id>")
async def redirect_url(id):
    try:
        data = await UrlService.get_by_id(id)
        return redirect(data.redirect)
    except NotFound:
        return abort(404)