from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Adventure(Base):
    __tablename__ = 'adventure_table'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)

    # Relationship with Avatar table
    avatars = relationship("Avatar", back_populates="adventure")

    # Relationship with Attacker table
    attackers = relationship("Attacker", back_populates="adventure")


class Avatar(Base):
    __tablename__ = 'avatars'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    health_points = Column(Integer)
    damage_points = Column(Integer)
    last_health_points = Column(Integer)  # New column for the last health point
    last_damage_points = Column(Integer)  # New column for the last damage point
    adventure_id = Column(Integer, ForeignKey('adventure_table.id'))

    # Relationship with Adventure table
    adventure = relationship("Adventure", back_populates="avatars")
   


class Attacker(Base):
    __tablename__ = 'attacker_table'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    starting_health = Column(Integer)
    current_health = Column(Integer)
    damage_points = Column(Integer)
    adventure_id = Column(Integer, ForeignKey('adventure_table.id'))

    # Relationship with Adventure table
    adventure = relationship("Adventure", back_populates="attackers")