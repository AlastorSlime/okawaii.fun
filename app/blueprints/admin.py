from app.services import AlreadyExists, UrlService, NotFound
from app.utils import protected

from quart import Blueprint, render_template, request, abort, redirect, flash

admin_blueprint = Blueprint(
    "admin",
    __name__,
    url_prefix="/admin"
)

@admin_blueprint.route("/")
@protected
async def panel():
    urls = await UrlService.get_all()
    return await render_template(
        "dashboard.html",
        urls=urls,
        total_urls=len(urls),
    )

@admin_blueprint.route("/get/<id>")
async def get(id):
    try:
        data = await UrlService.get_by_id(id=id)
        return {
            "id": data.id,
            "redirect": data.redirect,
            "created_on": str(data.created_on),
        }
    except NotFound:
        abort(404)

@admin_blueprint.route("/delete/<id>")
@protected
async def delete(id):
    try:
        await UrlService.delete_by_id(id)
        await flash(f"Url /{id} has been deleted.", category="success")
        return redirect("/admin")
    except NotFound:
        await flash(f"Couldn't find /{id} url in the database.", category="error")
        return redirect("/admin")

@admin_blueprint.route("/create", methods=["POST"])
@protected
async def create():
    form = await request.form
    form_id = form.get("id").replace("/", "")
    form_redirect = form.get("redirect")

    if not form_id and not form_redirect:
        return abort(400)
    try:
        await UrlService.create(
            id=form_id,
            redirect=form_redirect
        )
        await flash(f"Url /{form_id} has been created.", category="success")
        return redirect("/admin")
    except AlreadyExists:
        await flash(f"Url /{form_id} already exists.", category="error")
        return redirect("/admin")