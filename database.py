from sqlalchemy import create_engine,text
connection_string = "mysql+mysqlconnector://agizzvupuo3gwjuw1v6w:pscale_pw_DJEZE0MmLoqQETINXGpEsrlKvT8c9t5vRxNaai2CaL9@aws.connect.psdb.cloud:3306/careers"
engine=create_engine(connection_string) 
with engine.connect() as connection:
  result=connection.execute(text('select * from jobs'))
  