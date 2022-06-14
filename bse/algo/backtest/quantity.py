
scrip = [{"name": "JINDALSTEL", "fund": 7500, "price": 556.75},
         {"name": "ADANIPORTS", "fund": 7500, "price": 832.15},
         {"name": "BIOCON", "fund": 7500, "price": 342.75},
         {"name": "UPL", "fund": 7500, "price": 815.9},
         ]


leverage = 5

result = []

for item in scrip:
    temp = item['price']/leverage
    result.append({item['name']: round(item['fund']/temp)})

print(result)
