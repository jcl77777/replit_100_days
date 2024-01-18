'''
🌟Jobs Jobs Jobs!🌟

Job type: Lawyer
Salary: $ Squillions
Hours worked: 60

Job type: Teacher
Salary: $ Nowhere near enough
Hours worked: All of them
Subject: Computer Science
Position: Classroom Teacher

Job type: Doctor
Salary: $ Doing very nicely thank you
Hours worked: 50
Speciality: Pediatric Consultant
Years of Experience: 7
'''

#Object oriented Programming
class job:
  job_type = None
  salary = None
  hours_worked = None

  #set the basic info for class job
  def __init__(self, job_type, salary, hours_worked): 
    self.job_type = job_type
    self.salary = salary
    self.hours_worked = hours_worked

  #print the info
  def print(self):
    print(f"Job type: {self.job_type}, Salary: {self.salary}, Hours worked: {self.hours_worked}")
    print()

class teacher(job): # set a subset class teacher using class job

  subject = None
  position = None
  
  def __init__(self,salary, hours_worked,subject,position): # give 2 more infos for class teacher on top of class job
    self.job_type = "Teacher"
    self.salary = salary
    self.hours_worked = hours_worked
    self.subject = subject
    self.position = position

  def print(self):
    print(f"Job type: {self.job_type}, Salary: {self.salary}, Hours worked: {self.hours_worked}")
    print(f"Subject: {self.subject}, Where to find: {self.position}")
    print()

class doctor(job): # set a subset class doctor using class job

  speciality = None
  yr_experience = None

  def __init__(self,salary, hours_worked, speciality,yr_experience): # give 2 more infos for class doctor on top of class job
    self.job_type = "Docter"
    self.salary = salary
    self.hours_worked = hours_worked
    self.speciality = speciality
    self.yr_experience = yr_experience

  def print(self):
    print(f"Job type: {self.job_type}, Salary: {self.salary}, Hours worked: {self.hours_worked}")
    print(f"Speciality: {self.speciality}, Year of Experience: {self.yr_experience}")
    print()
    

print("🌟Jobs Jobs Jobs!🌟")
print()

lawyer = job("Lawyer", "$ Squillions", "60")
lawyer.print()

teacher = teacher("$ Nowhere near enough","All of them","Computer Science","Classroom Teacher") 
teacher.print()

doctor = doctor("$ Doing very nicely thank you","50","Pediatric Consultant", "7")
doctor.print()