import re

str1 = "your service is Good"
#test_case = str1.lower()
#print(test_case)

pattern = r'good'

match = re.search(pattern,str1, re.IGNORECASE)

if match:
  print ("found", match.group())
else:
  print("not found")

str2= "Price is $1000"
pattern2= r"\d+"

match2 = re.search(pattern2, str2, re.IGNORECASE)

if match2:
  print ("found digit", match2.group())
else:
  print ("not found")


str3 = "Mail at pial.33@gmail.com or info@daraz.com.bd"
pattern3= r"\b[A-Za-z0-9._]+@[a-zA-z]+\.[a-z|A-z]{0,}\b"

match3= re.findall(pattern3, str3, re.IGNORECASE)
if match3:
  print("found", match3)
else:
  print("not found")



          