gross_income=int(input("enter exact gross income: "))
a=int(input("enter no of dependents "))
b=10000
taxable_income=gross_income-(b)-(a*3000)
tax=taxable_income*0.2
print("Income tax is: "+str(tax))
