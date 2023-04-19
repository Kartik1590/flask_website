from sqlalchemy import create_engine,text
import os

connection_string=os.environ['connection']
print(connection_string)

engine = create_engine(connection_string)
def load_db():
  with engine.connect() as connection:
    result=connection.execute(text('select * from jobs'))
    result_dicts=[]
    for row in result.all():
      result_dicts.append(list(row))
    return result_dicts

load_db()