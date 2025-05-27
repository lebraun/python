from sqlalchemy import Column, Integer, String, Text, ForeignKey, Table
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

# Association table for many-to-many relationship between Video and Tag
videos_tags = Table(
    'videos_tags',
    Base.metadata,
    Column('video_id', Integer, ForeignKey('video.id'), primary_key=True),
    Column('tag_id', Integer, ForeignKey('tag.id'), primary_key=True)
)

class Video(Base):
    __tablename__ = 'video'

    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    description = Column(Text)
    url = Column(String(255), nullable=False)

    tags = relationship('Tag', secondary=videos_tags, back_populates='videos')
