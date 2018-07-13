from sys import argv

script, usrname = argv
prompt ='>'
print(f"Hi {usrname}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {usrname}?")
likes = input(prompt)

print(f"""
So you said {likes} about liking me.
""")
