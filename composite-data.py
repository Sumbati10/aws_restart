import csv
import copy

# Define a dictionary template for vehicles
myVehicle = {
    "vin": "<empty>",
    "make": "<empty>",
    "model": "<empty>",
    "year": 0,
    "range": 0,
    "topSpeed": 0,
    "zeroSixty": 0.0,
    "mileage": 0
}

# Print the default vehicle dictionary
for key, value in myVehicle.items():
    print(f"{key} : {value}")

# Create an empty list to hold inventory data
myInventoryList = []

# Open and read the CSV file
with open('car_fleet.csv') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')
    lineCount = 0

    # Loop through each row in the CSV file
    for row in csvReader:
        # Print column names from the first row
        if lineCount == 0:
            print(f'Column names are: {", ".join(row)}')
            lineCount += 1
        else:
            # Print each row's data for visual verification
            print(f'vin: {row[0]}, make: {row[1]}, model: {row[2]}, year: {row[3]}, '
                  f'range: {row[4]}, topSpeed: {row[5]}, zeroSixty: {row[6]}, mileage: {row[7]}')
            
            # Copy the vehicle template to add new data
            currentVehicle = copy.deepcopy(myVehicle)
            
            # Assign values from the CSV row to the corresponding vehicle properties
            currentVehicle["vin"] = row[0]
            currentVehicle["make"] = row[1]
            currentVehicle["model"] = row[2]
            currentVehicle["year"] = row[3]
            currentVehicle["range"] = row[4]
            currentVehicle["topSpeed"] = row[5]
            currentVehicle["zeroSixty"] = row[6]
            currentVehicle["mileage"] = row[7]
            
            # Add the updated vehicle to the inventory list
            myInventoryList.append(currentVehicle)
            
            # Increment the line count
            lineCount += 1

    # Summary of lines processed
    print(f'Processed {lineCount} lines.')

# Print out each vehicle's properties from the inventory list
for myCarProperties in myInventoryList:
    for key, value in myCarProperties.items():
        print(f"{key} : {value}")
    print("-----")  # Separator between cars
