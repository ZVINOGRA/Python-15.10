import re
string = "Michael, how are you? - Cool, how is John Williamns and Michael Jordan? I don't know but Michael Johnson is fine. Michael do you still score points with LeBron James, Michael Green AKA Star and Michael Wood?"
pattern = re.compile("(Michael)\s[A-z.]+")

result = re.findall(pattern, string)
print(result)
