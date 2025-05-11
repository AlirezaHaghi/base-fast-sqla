import sqlalchemy as sa
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from .settings import settings

engine = create_async_engine(
    settings.async_database_url,
    echo=True,
)

sessionmaker = async_sessionmaker(engine)


async def init_db():
    from src.models import Base
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    await create_first_admin()


async def create_first_admin():
    from .models import User
    from .authentication import get_password_hash
    async with sessionmaker.begin() as session:
        stmt = sa.select(User).where(User.username == "alireza")
        result = await session.execute(stmt)
        first_admin = result.scalar_one_or_none()
        if not first_admin:
            first_admin = User(
                username="alireza",
                hashed_password=get_password_hash("alireza"),
                is_admin=True,
            )

