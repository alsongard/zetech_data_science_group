temperature_level = input("enter the temperature you would like to convert : ")
temp = input("enter the format of temp using : [celcius or farheneit]")

if temp == "farheneit":
    celcius = (int(temperature_level) -32) * 5/9
    value = round(celcius, 2)
    print(value)
elif temp == "celcius":
    farheneit = (int(temperature_level) * 9/5) + 32
    value = round(farheneit, 2)
    print(value)