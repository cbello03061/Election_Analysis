print ("Hello Wordl")
#counties=["Arapahoe","Denver","Jefferson"
#if counties[1]=="Denver":
 #   print(counties[1])

county=0
counties=["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El paso is in the list of counties")
else:
    print("El Paso is not the list of countes")

#if "Arapahoe" in counties "El paso" in counties:
    #rint("Arapahoe and El Paso ara in the list of counties")
#else:
    print("Arapahoe or El Paso is not in the list of counties")

for county in counties:
    print(county)

#for num in range(5)
   # print(num)

counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])

for i in range(len(counties)):
    print(counties[i])

counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")

