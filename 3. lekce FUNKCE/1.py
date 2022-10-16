rain = True
watering_truck = True
if rain == True or watering_truck == True:
    wet_street = True
else:
    wet_street = False
print(wet_street)

# Část == True můžete vynechat, následující kód provede to samé.

rain = True
watering_truck = True
if rain or watering_truck:
    wet_street = True
else:
    wet_street = False
print(wet_street)

