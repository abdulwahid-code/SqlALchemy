from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, DateTime

mysql_user = 'root'
mysql_password = 'Shellkode@12345'
mysql_host = 'localhost'
mysql_port = '3306'
mysql_database = 'geekprofile'

# Create database connection string
mysql_conn_str = f'mysql+pymysql://{mysql_user}:{mysql_password}@{mysql_host}:{mysql_port}/{mysql_database}'


# SQLALCHEMY_DATABASE_URL = "mysql+pymysql://:Shellkode@12345@localhost:3306/geekprofile"

engine = create_engine(mysql_conn_str)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


class Data(Base):
    __tablename__ = "data"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    status = Column(String)
    scheduled_time = Column(DateTime)
    repeat = Column(String)


Base.metadata.create_all(bind=engine)
