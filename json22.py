# IMPORT JSON MODULES
import json
#  Convert from Python to JSON
some_details ={
    "name": "Vishali",
    "age": 22,
    "city": "Madurai"
  }
result = json.dumps(some_details)
print("Some details :", result)

# Parse JSON - Convert from JSON to Python
some_details =' { "name": "Vishali", "age": 22, "city": "Madurai"}' 
result = json.loads(some_details)
print("City :", result["city"])

# Convert a Python object containing all the legal data types:
data = {
  "name": "vishali",
  "age": 20,
  "studying": True,
  "mrried": False,
  "siblings": ("Tharanya",),
  "pets": None,
  "vehicle": [
    {"model": " RE 350", "mpg": 27.5},
    {"model": "unicon", "mpg": 10}
  ],
  "college":[
     {"clg name" :"Annamalai univercity", }
  ]
}
#  Print full object.
print("Main object data : ",json.dumps(data))
# Print nested object.
print("Nested object vehicle  : ",json.dumps(data["vehicle"]))
# Indend spaces.
print("Indend (space) : ",json.dumps(data, indent= 3))

# Indend spaces separators
print(json.dumps(data, indent=3, separators=(". " , "= ")))

# Sort-keys alphabetically by keys
print(json.dumps(data, indent=3, sort_keys=True))
#  Normal format 
print(json.dumps(data, indent=3, sort_keys=False))










