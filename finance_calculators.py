import math

print("Choose either investment or bond from the menu below to proceed")

type_calc1="investement             -to calculate the amount of interest you'll earn on interest"
print(type_calc1)
type_calc2 = "bond                    -to calculate the amount you'll have to pay on home loan"
print(type_calc2)

select_type_of_calc = input("enter the type of calculation between investment and bond: " )

#if investment is selected do the following steps
if select_type_of_calc == 'investment' or select_type_of_calc == 'INVESTMENT' or select_type_of_calc == 'Investment':
    #declaring variable amount_of money and asking for an input either investement and bond
    amount_of_money_deposited = float((input("Enter the amount of money: ")))
    #declaring variable interest_rate and asking for an input
    interest_rate = float(input("enter the interest rate :"))
    #declaring variable num_of_yrs and asking for an input from the user
    period = float(input("input the number of years :"))
    #declaring variable type_of_method and asking for an input from user
    type_of_method = input("choose where you want simple or compound: ")
    #if the user chose simple from the previous variable type_of_method
    if type_of_method == "simple":
        #declaring variable method 1 if the condition on the previous line is met
        method1 = float(amount_of_money_deposited*(1+(interest_rate/100)*period))
        #printing variable method2
        print(method1)

    #if the above condition is not met test the following condition     
    elif type_of_method == "compound":
        #declaring variable amount2 if the condition on the previouse line is met
        amount2 = float(amount_of_money_deposited*math.pow(1+(interest_rate/100),period))
        #printing variable in amount2
        print(amount2)

#as bond is selected do the following steps
elif select_type_of_calc == "bond" or select_type_of_calc == "BOND" or select_type_of_calc == "Bond":
    #declaring variable present_value and asking for an input
    present_value = float(input("enter the present value of the house: "))
    #declaring variable interest_rates2 and asking for an input
    interest_rate2=float(input("Enter the interest rate: "))
    #declaring variable period2 and asking for an input
    period2=float(input("enter the number of months you plan to take to replay the bond: "))
    #calculating the repayment by months using the previouse variables
    Calc_repay_month=float((interest_rate2*present_value)/(1 - (1+(interest_rate2/100)**(-period2))))
    print(Calc_repay_month)

else:
    print("Please enter a valid option")


    



