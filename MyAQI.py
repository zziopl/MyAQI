print("Hello and welcome to MyAQI!")
print("Anyone who does not know what an air quality index is, is a  is used for reporting daily air quality. It tells you how clean or polluted your air is, and what associated health effects might be a concern for you.")
aqi = input("Enter the air quality index of your country: ")
result = int(aqi)
if result >= 0 and result <= 50:
    print("Air quality is satisfactory, and air pollution poses little or no risk.")
elif result >= 51 and result <= 100:
    print("	Air quality is acceptable. However, there may be a risk for some people, particularly those who are unusually sensitive to air pollution")
elif result >= 101 and result <= 150:
    print("Members of sensitive groups may experience health effects. The general public is less likely to be affected.")
elif result >= 151 and result <= 200:
    print("Some members of the general public may experience health effects; members of sensitive groups may experience more serious health effects.")
elif result >= 201 and result <= 300:
    print("Health alert: The risk of health effects is increased for everyone.")
elif result >= 301:
    print("Health warning of emergency conditions: everyone is more likely to be affected.")

 
