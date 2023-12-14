from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Adventure, Avatar, Attacker
from Adventure import undegroundcave, temple,Avatar1,Player # Import your adventure modules

# Create the database tables
engine = create_engine('sqlite:///game.db')  # Use an appropriate database URL
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()
#Add Avatar to the Avatartable
# Populate the data for the Forgotten Temple Adventure
temple_player = Avatar(name="Babji", health_points=100, damage_points=20)
temple_instance = temple.ForgottenTempleAdventure()
#session.add(Adventure(name=temple_instance.__class__.__name__))
session.add(temple_player)

# Link Avatar to the Adventure
temple_instance.avatar = temple_player
session.add(temple_instance)

# Populate the data for the Underground Caverns Adventure
caverns_player = Avatar(name="Avatar Roshi", health_points=100, damage_points=50)
caverns_instance = undegroundcave.UndergroundCavernsAdventure(player=caverns_player)
#session.add(Adventure(name=caverns_instance.__class__.__name__))
session.add(caverns_player)

# Link Avatar to the Adventure
caverns_instance.avatar = caverns_player
session.add(caverns_instance)

# Commit the changes to the database
session.commit()
# Add adventures to the Adventure table
adventures = [temple_instance, caverns_instance]

for adventure in adventures:
    adventure_instance = Adventure(name=adventure.name)
    session.add(adventure_instance)

    avatar = session.query(Avatar).filter_by(name=adventure.name).first()
    avatar.adventure = adventure_instance

# Commit the changes to the database
session.commit()
# Display the adventure details
adventures = session.query(Adventure).all()
for adventure in adventures:
    print(f"\nAdventure: {adventure.name}")
  

    # Display the avatar details for each adventure
    avatar = session.query(Avatar).filter_by(adventure_id=adventure.id).first()
    
    print(f"Health Points: {avatar.health_points}")
    print(f"Damage Points: {avatar.damage_points}")
    print(f"Last Health Points: {avatar.last_health_points}")
    print(f"Last Damage Points: {avatar.last_damage_points}")

