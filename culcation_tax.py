import time


def clacluate_total_salary(base_salary,bouns):
      total_salary=base_salary+bouns
      tax_puy=calcluate_tax(total_salary)
      return total_salary - tax_puy



def calcluate_tax(income):
      return income * 0.15


base_salary=float(input("enter your base salary:  "))
bouns=float(input("how much your bouns did you get? "))

time.sleep(3)
final_salary=clacluate_total_salary(base_salary,bouns)
print(" please wait... loading")
time.sleep(3)
print(f"the fainl salary : $ {final_salary}")