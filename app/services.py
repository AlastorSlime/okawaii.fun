from .models import Url 
from datetime import datetime

class NotFound(Exception):
    pass 

class AlreadyExists(Exception):
    pass 

class UrlService():
    @staticmethod
    async def get_by_id(id: str):
        url = await Url.get_or_none(id=id)
        
        if not url:
            raise NotFound()
        return url

    @staticmethod
    async def get_all():
        urls = await Url.all()
        return urls 

    @staticmethod
    async def create(
        id: str,
        redirect: str
    ):  
        if await Url.get_or_none(id=id):
            raise AlreadyExists()

        new_url = await Url.create(
            id=id,
            redirect=redirect,
            created_on=datetime.now()
        )
        return new_url
    
    @staticmethod
    async def delete_by_id(id: str):
        url = await Url.get_or_none(id=id)
        if not url:
            raise NotFound()

        await Url.delete(url)