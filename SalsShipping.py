# Sal's Shipping
# Jonathan Tran
# 02/08/2021

#weight = 8.4
#weight = 1.5
#weight = 4.8
weight = 41.5

# Ground Shipping

if weight <= 2:
  cost_ground = weight * 1.50 + 20.00
elif weight > 2 and weight <= 6:
  cost_ground = weight * 3.00 + 20.00
elif weight > 6 and weight <= 10:
  cost_ground = weight * 4.00 + 20.00
elif weight > 10:
  cost_ground = weight * 4.75 + 20.00

# Ground Premium Shipping

cost_ground_premium = 125.00

# Drone Shipping

if weight <= 2:
  cost_drone = weight * 4.50
elif weight > 2 and weight <= 6:
  cost_drone = weight * 9.00
elif weight > 6 and weight <= 10:
  cost_drone = weight * 12.00
elif weight > 10:
  cost_drone = weight * 14.25

print("Cost Ground: " + str(cost_ground))

print("Cost Ground Premium: " + str(cost_ground_premium))

print("Cost Drone Shipping: " + str(cost_drone))

print("Cheapest method for a 4.8 lb package is Ground Shipping")

print("Cheapest method for a 41.5 lb package is Ground Premium")