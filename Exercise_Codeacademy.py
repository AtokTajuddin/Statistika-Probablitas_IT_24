# Page 1
print "Hello World"

#Page 2
print("Hello World") # Pada python 3

#Page 3
print("Hello " + "pwd")

#Page 4
print("How do you make a hot dog stand?")
print("You take away its chair!")

#Page 5
todays_date = "March 31, 2023"
print(todays_date)

#Page 6
product = 133/7
remainder = 1398%11

#Page 7 (Updating Variables)
january_to_june_rainfall = 1.93 + 0.71 + 3.53 + 3.41 + 3.69 + 4.50
annual_rainfall = january_to_june_rainfall

july_rainfall = 1.05
annual_rainfall += july_rainfall

august_rainfall = 4.91
annual_rainfall += august_rainfall

september_rainfall = 5.16
october_rainfall = 7.20
november_rainfall = 5.06
december_rainfall = 4.06

annual_rainfall += september_rainfall
annual_rainfall += october_rainfall
annual_rainfall += november_rainfall
annual_rainfall += december_rainfall

#Page 8 (Command)
city_name = "St. Potatosburg"
#Hello this is command line
city_pop = 340000

#Page 9 (Numbers)

cucumbers = 1
price_per_cucumber = 3.25
total_cost = price_per_cucumber*cucumbers
print(total_cost)
print(isinstance(total_cost,int))
print("Tipe data cucumber","",type(total_cost))

#Page 10 (Two types of division)

cucumbers = 100
num_people = 6
whole_cucumbers_per_person = cucumbers/num_people
a = whole_cucumbers_per_person
print(a)
#float_cucumbers_per_person = float(cucumbers/num_people) dengan inii hasilnya berbeda dimana program menangkap bahwa cucumbers/num_people di integerkan lalu dihitunh
#kemudian baru di ubah ke tipe data float bukan diproses dalam perhitungan float yang dimana seharushnya hasilnya adalah 16.66667 dst....
float_cucumbers_per_person = float(cucumbers)/num_people
b = float_cucumbers_per_person
print(b)

#Page 11 (Multi-line strings)
haiku = """

The old pond,
A frog jumps in:
Plop!
"""

# Page 12 (Booleans)
# Hi! I'm Maria and I live in script.py.
# I'm an expert Python coder.
# I'm 21 years old and I plan to program cool stuff forever.

age_is_12 = 0 #Bisa juga diganti dengan False
name_is_maria = 1 # Bisa juga diganti dengan True

# Page 13 (Value Error)

float_1 = 0.25
float_2 = 40.0
product = float_1*float_2
big_string = "The product was " + str(product) #Bisa diganti dengan f"The product was {product}" -> ini lebih simpel menggunakan metode f-string 
print(float(product))
print(big_string)

#Page 14 (Review)

skill_completed = "Python Syntax"
exercises_completed = 13

#The amount of points for each exercise may change, because points don't exist yet

points_per_exercise = 5
point_total = 100
point_total += (exercises_completed*points_per_exercise)
print("I got "+str(point_total)+" points!")
