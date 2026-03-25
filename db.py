from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData

DATABASE_URL = "sqlite:///database.db"

engine = create_engine(DATABASE_URL, echo=False)
metadata = MetaData()

users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String),
    Column("email", String),
)

metadata.create_all(engine)

# Insert sample data (only once)
with engine.connect() as conn:
    result = conn.execute(users.select())
    if result.first() is None:
        conn.execute(
            users.insert(),
            [
                {"name": "Alice", "email": "alice@gmail.com"},
                {"name": "Bob", "email": "bob@gmail.com"},
            ],
        )
