def getProductData() :
	#SERIAL NUMBER

	serialNumber = 'NO SERIAL'
	with open('/sys/class/dmi/id/product_serial') as f:
		serialNumber = f.read().strip()

	#PRODUCT NAME
	productName = 'NO PRODUCT NAME'
	with open('/sys/class/dmi/id/product_name') as f:
		productName = f.read().strip()

	return  "SN:\t\t" + str(serialNumber) + '\n' \
			"Product:\t\t" + str(productName) + '\n'
