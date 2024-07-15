dict1 = {"key1": 2, "key2": None, "key3": 5, "key4": "abc"}
dictrem = {}
for keys, values in dict1.items():
   if values is not None:
      dictrem[keys] = values
print(dictrem)