import uuid
from models.base.base import Base, BaseModel
from sqlalchemy import Column, String, Integer, Text, UniqueConstraint


class UserRelImage(Base, BaseModel):
    """用户收藏的图片"""
    __tablename__ = 'user_rel_image'

    user_id = Column(Integer, nullable=True, doc="用户id")
    image_id = Column(Integer, nullable=True, doc="图片id")
