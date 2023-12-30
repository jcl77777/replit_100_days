'''
🌟Contact Card🌟

Input your name > David Morgan

Input your date of birth > 01/01/1900

Input your telephone number > 01234 567890

Input your email > david@replit.com

Input your address > The Cupboard Under The Stairs, Replit Towers, NY.

Hi David Morgan. Our dictionary says that you were born on 01/01/1900, we can call you on 01234 567890, email david@replit.com, or write to The Cupboard Under The Stairs, Replit Towers, NY.
'''
info_dict = {}

print("🌟Contact Card🌟")

name = input("Input your name > ").strip().capitalize()
#append into list
#way1: info_dict["name"] = name
info_dict.update({"name": name})

dob = input("Input your date of birth > ").strip()
info_dict.update({"date_of_birthday": dob})

tel = input("Input your telephone number > ").strip()
info_dict.update({"tel": tel})

email = input("Input your email > ").strip()
info_dict.update({"email": email})

address = input("Input your address > ").strip()
info_dict.update({"address": address})

print("Information stored successfully:")
print(f"Hi {name}, Our dictionary says that you were born on {dob}, we can call you on {tel}, email {email}, or write to {address}.")