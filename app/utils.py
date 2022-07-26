from functools import wraps

from quart import session, redirect

from app.models import Admin

async def verify_credentials(
    username: str, 
    password: str
):
    admin = await Admin.get_or_none(username=username, password=password) 
    if admin:
        return True 
    else:
        return False 

def protected(wrapped):
    def decorator(f):
        @wraps(f)
        async def decorated_func(*args, **kwargs):
            if not "authorized" in session:
                return redirect("/admin/login")  
            
            response = await f(*args, **kwargs)
            return response
        return decorated_func
    return decorator(wrapped)