from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


host = "127.0.0.1"
user = "root"
password = "caifu123"
db = "xd_test"
charset = "utf8mb4"

Base = declarative_base()


class User(Base):
    __tablename__ = "config"
    id = Column(Integer, primary_key=True)
    app = Column(String)
    dict_key = Column(String)
    dict_value = Column(String)


def test_orm():
    # print(password)
    engine = create_engine(
        "mysql+pymysql://{user}:{password}@{host}/{db}".format(
            host=host, db=db, user=user, password=password
        ),
        echo=True,
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    u1 = User(id="6", app="hogwarts", dict_key="yangbai", dict_value="547556017@qq.com")
    # session.add(u1)
    # session.commit()
    u2 = session.query(User).filter_by(app="hogwarts").first()
    print(u2.app)
