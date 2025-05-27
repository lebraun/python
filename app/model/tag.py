from sqlalchemy import Column, Integer, String, Text, ForeignKey, Table
from sqlalchemy.orm import relationship, declarative_base
from model.video import videos_tags

Base = declarative_base()

class Tag(Base):
    __tablename__ = 'tag'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)

    videos = relationship('Video', secondary=videos_tags, back_populates='tags')