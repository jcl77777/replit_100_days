#create character class with three preset attributes
class character:
  name = None
  health = None
  magic = None

  def __init__(self, name, health, magic):
    self.name = name
    self.health = health
    self.magic = magic
    
  def print(self):
    print(f"Name: {self.name}\nHealth: {self.health}\nMagic Points: {self.magic}")

#create player class based on character class and add a new attribute
class player(character):
  lives = None
  def __init__(self, name, health, magic, lives):
    self.name = name
    self.health = health
    self.magic = magic
    self.lives = lives

  def print(self):
    print(f"Name: {self.name}\nHealth: {self.health}\nMagic Points: {self.magic}")
    print(f"Lives: {self.lives}")
    print()

#create enemy class based on character class and add two new attributes
class enemy(character):
  type = None
  strength = None
  def __init__(self, name, health, magic, type, strength):
    self.name = name
    self.health = health
    self.magic = magic
    self.type = type
    self.strength = strength

  def print(self):
    print(f"Name: {self.name}\nHealth: {self.health}\nMagic Points: {self.magic}")
    print(f"Type: {self.type}\nStrength: {self.strength}")
    print()

#create orc class based on enemy class and add a new attribute
class orc(enemy):
  speed = None
  def __init__(self, name, health, magic, type, strength, speed):
    self.name = name
    self.health = health
    self.magic = magic
    self.type = type
    self.strength = strength
    self.speed = speed

  def print(self):
    print(f"Name: {self.name}\nHealth: {self.health}\nMagic Points: {self.magic}")
    print(f"Type: {self.type}\nStrength: {self.strength}")
    print(f"Speed: {self.speed}")
    print()

#create vampire class based on enemy class and add a new attribute
class vampire(enemy):
  day = None
  def __init__(self, name, health, magic, type, strength, day):
    self.name = name
    self.health = health
    self.magic = magic
    self.type = type
    self.strength = strength
    self.day = day

  def print(self):
    print(f"Name: {self.name}\nHealth: {self.health}\nMagic Points: {self.magic}")
    print(f"Type: {self.type}\nStrength: {self.strength}")
    print(f"Day/Night: {self.day}")
    print()
  
print("🌟Generic RPG🌟")
print()

David = player("David", 100, 50, 3)
David.print()

Boris = vampire("Boris", 45, 70, "Vampire", 3, "Night")
Boris.print()

Rishi = vampire("Rishi", 70, 10, "Vampire", 75, "Day")
Rishi.print()

Bill = orc("Bill", 60, 5, "Orc", 75, 90)
Bill.print()

Ted = orc("Ted", 75, 40, "Orc", 80, 45)
Ted.print()

Station = orc("Station", 35, 40, "Orc", 49, 50)
Station.print()