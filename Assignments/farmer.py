# Land distribution
total_land = 80
segments = 5
land_per_crop = total_land / segments  # 16 acres each

# Tomato yield (split)
tomato_land = land_per_crop
tomato_yield_30 = 0.3 * tomato_land * 10  # tonnes
tomato_yield_70 = 0.7 * tomato_land * 12
tomato_total_kg = (tomato_yield_30 + tomato_yield_70) * 1000  # to kg
tomato_price = 7
tomato_sales = tomato_total_kg * tomato_price

# Potato
potato_yield = land_per_crop * 10 * 1000  # to kg
potato_price = 20
potato_sales = potato_yield * potato_price

# Cabbage
cabbage_yield = land_per_crop * 14 * 1000
cabbage_price = 24
cabbage_sales = cabbage_yield * cabbage_price

# Sunflower
sunflower_yield = land_per_crop * 0.7 * 1000
sunflower_price = 200
sunflower_sales = sunflower_yield * sunflower_price

# Sugarcane
sugarcane_yield = land_per_crop * 45
sugarcane_price = 4000
sugarcane_sales = sugarcane_yield * sugarcane_price

# Total sales
total_sales = tomato_sales + potato_sales + cabbage_sales + sunflower_sales + sugarcane_sales

# Chemical-free sales at end of 11 months: tomato, potato, cabbage, sunflower
chemical_free_sales = tomato_sales + potato_sales + cabbage_sales + sunflower_sales

# Print results
print("a. Total Sales from 80 acres: Rs.", format(int(total_sales), ","))
print("b. Sales from Chemical-Free Farming (at end of 11 months): Rs.", format(int(chemical_free_sales), ","))
