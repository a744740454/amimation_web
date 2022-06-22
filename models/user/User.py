from models.base.base import Base,BaseModel
from sqlalchemy import Column, String,Integer


class UserInfo(Base,BaseModel):
    __tablename__ = 'user_info'

    username = Column(String(20))
    email = Column(String(20))
    telephone = Column(String(20))
    password = Column(String(30))

    def from_json(self, data, add_exclude_columns=None):
        exclude_columns = []
        if add_exclude_columns:
            exclude_columns.extend(add_exclude_columns)
        for column in self.__table__.columns:
            if column.name in exclude_columns:
                continue

            setattr(self, column.name, data.get(column.name, getattr(self, column.name)))
        return self