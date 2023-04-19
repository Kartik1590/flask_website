from sqlalchemy import create_engine,text
import os
connection_string=os.environ['connection_string']
engine=create_engine(connection_string)


def load_db():
  with engine.connect() as connection:
    result=connection.execute(text('select * from jobs'))
    result_dicts=[]
    for row in result:
      result_dicts.append(dict(row))
  return result_dicts

