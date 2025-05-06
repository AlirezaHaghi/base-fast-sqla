from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from settings import settings
from models import Base

engine = create_async_engine(settings.async_database_url, echo=True)

sessionmaker = async_sessionmaker(engine)


async def init_db():
    async with engine.begin() as conn:
        pass
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
        
    await create_first_admin()



async def create_first_admin():
    from models import User
    from authentication import get_password_hash
    async with sessionmaker.begin() as session:
        user = User(
            username="alireza",
            hashed_password=get_password_hash("alireza"),
            is_admin=True,
        )
        session.add(user)
