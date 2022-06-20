
import matplotlib.pyplot as plt

#fc=float(input("Enter your total fixed cost: ")) # Fixed Cost
fc=4500
#vc=float(input("Enter your total variable cost: ")) # Variable Cost
vc=0
#units=int(input("How many total units do you have: "))
units=20
#sp=float(input("What is your selling price per unit: "))
sp=350
tc=fc+vc
bep= fc/(sp-vc) # break-even point/units
bep_tr= bep*sp# break-even revenue
tr= units*sp
print(f"\nYour Product Total Cost is :{tc} pkr,\n You will break-even if you sell approx {round(bep)} units\n Total Revenue: {tr} ")
# plot lines
Units=list(range(units+1))
profits=[i-tc for i in [i for i in range(0,int(tr+1),round((tr+1)/units))] ]
# Fc=[]
# #a=[fc for i in range(len(Units))]
# Tc=[]
# Tr=[]
#print(bep,[bep for i in range(len(Units))])
print(profits)
#
plt.plot(Units,[fc for i in range(len(Units))], label = "Fixed Cost")
plt.plot(Units,[i for i in range(0,int(tr+1),round((tr+1)/units))], label = "Total Revenue")
plt.plot(Units,[tc for i in range(len(Units))], label = "Total Cost")
plt.plot([bep for i in range(len(Units))],[i for i in range(0,int(tr+1),round((tr+1)/units))], label = "Break Even",linestyle="--")
plt.plot(Units,profits, label = "Profits",marker="o",color="mediumseagreen",markersize=5)

plt.legend()
# plt.plot([tc],[fc])
plt.title('Break-Even Analysis')
plt.xlabel('Units')
plt.ylabel('Pkr')
plt.grid(True)
plt.xticks(Units)  

plt.text(20,tr, "TR", color='orange', fontsize=10)
plt.text(20,fc, "FC", color='green', fontsize=10)
plt.text(bep-1,tr, "BEP", color='red', fontsize=10)
plt.text(20,profits[-1]+200, "Profit", color='mediumseagreen', fontsize=10)

plt.plot(bep, bep_tr, marker="o", markersize=5, markeredgecolor="black", markerfacecolor="red")
plt.show()
