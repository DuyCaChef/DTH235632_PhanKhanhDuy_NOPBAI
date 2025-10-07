s = "  Python is Fun!  "

print(s.lower())       # "  python is fun!  "
print(s.strip())       # "Python is Fun!"
print(s.replace("Fun", "Cool"))  # "  Python is Cool!  "
print(s.split())       # ['Python', 'is', 'Fun!']
print("-".join(["a","b","c"]))   # "a-b-c"
print(s.find("is"))    # 9