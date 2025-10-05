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

#----Input--Name
customerName = input("Enter the customer's name: ")

#---Input--Delivery distance
deliveryDistance = float(input("Enter the delivery distance: "))

#--Input-- record purchased
costofRecordPurchsed = float(input("Enter the cost of record purchased: "))

#-----Calculations----
deliveryCost = deliveryDistance * deliveryRatePerKM
taxPerRecordPurchase = costofRecordPurchsed * salesTax
purchaseCost = costofRecordPurchsed + taxPerRecordPurchase
totalCost = purchaseCost + deliveryCost

#-----Output-----
print("Hispler Local Vinyl Records - Customer Order Detail")
print(f"\n\nPurchase summary for {customerName}")
print("\tDelivery cost:\t${0:.2f}".format(deliveryCost))
print("\tPurchase cost:\t${0:.2f}".format(purchaseCost))
print("\tTotal cost:\t${0:.2f}".format(totalCost))





