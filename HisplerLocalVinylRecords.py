# Hipster's Local Vinyl Records: Customer's Order Details #

# This program should be able to ask for the customer's name
# Ask for the delivery distance in Kilometers
# Ask for the cost of record purchased 
# Calculate the delivery cost
# Calculate the purchase cost 
# Calculate the Total Cost
# Print purchase summary for customer
# Delivery Cost:
# Purchase Cost:
#Total Cost:

#Important Information#
deliveryRatePerKM = 15
salesTax = 0.14

# Ask the customer to input name
customerName = input("Enter the customer's name: ")

# Delivery distance
deliveryDistance = float(input("Enter the delivery distance: "))

# Cost of record purchased
costofRecordPurchsed = float(input("Enter the cost of record purchased: "))

#Calculations
deliveryCost = deliveryDistance * deliveryRatePerKM
purchaseCost = costofRecordPurchsed * salesTax
totalCost = purchaseCost + deliveryCost


