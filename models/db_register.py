from sqlalchemy import create_engine
from sqlalchemy.engine import URL, make_url
from sqlalchemy.orm import sessionmaker,scoped_session
from config import CONF


def create_db_url():
    username = CONF.get("mysql").get("user")
    password = CONF.get("mysql").get("password", "")
    db = CONF.get("mysql").get("db")
    host = CONF.get("mysql").get("host")
    port = CONF.get("mysql").get("port")
    url = make_url('mysql+pymysql://{}:{}@{}:{}/{}'.format(username, password, host, port, db))
    db_url = url.update_query_dict({
        "charset": "utf8",
        "autocommit": "true"
    })
    print(db_url)
    return db_url


def create_session():
    db_url = create_db_url()
    # 初始化数据库连接:
    engine = create_engine(db_url, pool_size=5, max_overflow=5, pool_pre_ping=True)

    # 创建DBSession类型:
    session = sessionmaker(bind=engine)
    session = scoped_session(session)
    return session
