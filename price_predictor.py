time = int(input("Enter your number of weeks "))
fc=float(input("Enter your total fixed cost per week: "))*time # Fixed Cost
#fc=4500
vc=float(input("Enter your total variable cost: ")) # Variable Cost
#vc=0
units=int(input("How many total units do you have per week: "))
units*=time
profit= float(input("How much profit do you wish to make ?: "))
tc=fc+vc
sp=(profit+tc)/units
#tr= units*sp

print(f"For a profit of {profit}, you need to sell {units} units at {sp} pkr in {time} weeks ")

