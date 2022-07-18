from functools import wraps
from quart import current_app, session, redirect

def verify_credentials(
    username: str, 
    password: str
):
    config = current_app.config
    if (
        username == config.get("ADMIN_USERNAME")
        and 
        password == config.get("ADMIN_PASSWORD")
    ):
        return True 
    return False 

def protected(wrapped):
    def decorator(f):
        @wraps(f)
        async def decorated_func(*args, **kwargs):
            if not "authorized" in session:
                return redirect("/auth/login")  
            
            response = await f(*args, **kwargs)
            return response
        return decorated_func
    return decorator(wrapped)