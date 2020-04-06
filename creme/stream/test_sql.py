from sql import iter_sql # type: ignore
from sqlalchemy import create_engine, MetaData 

db_uri = 'sqlite:///db.sqlite'
engine = create_engine(db_uri)

metadata = MetaData()
metadata.reflect(bind=engine)

query = 'SELECT * FROM census'

with engine.connect() as con:
    for row in iter_sql(query, con):
        print(row)
