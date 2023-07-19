# finding temprature using this function , intial max min takes Zero
# iterates the tempature value which takes as input from user 
# comparing each value min and max return  max and min after comparing the all element in the list 

def find_Temp(temperatures):
    maxTemp = minTemp = temperatures[0]  # intial the value is zero 
 
#  iterates the list to find max and min value in the list 

    for temp in temperatures:
        if temp > maxTemp:
            maxTemp = temp
        if temp < minTemp:
            minTemp = temp

    return maxTemp, minTemp


inputTempValue = []
n = 5  # here we're taking just 5 temprature value 

for i in range(n):
        temp = float(input(f"Enter temperature {i + 1}: "))  #taking float value 
        inputTempValue.append(temp) # here append fuction add value in list which takes from the user 

maxTemperature, minTemperature = find_Temp(inputTempValue)

# Printing  max and min temprature 
print(f"Maximum temperature: {maxTemperature}")
print(f"Minimum temperature: {minTemperature}")



# note: i used google for  concept like .append () in list to be


