import argparse
import math
import sys

parser = argparse.ArgumentParser(description="Loan Calculator")
parser.add_argument("--type", type=str, choices=["annuity", "diff", ], help="Select what what you want to calculate")
parser.add_argument("--principal", type=float, help="Enter the principal amount")
parser.add_argument("--periods", type=float, help="Enter the time in months")
parser.add_argument("--interest", type=float, help="Enter the interest rate")
parser.add_argument("--payment", type=float, help="Enter the monthly payment amount")
args = parser.parse_args()

num_of_none_vars = sum([var is None for var in [args.interest, args.payment, args.periods, args.principal]])
if num_of_none_vars >= 2:
    print("Incorrect parameters.")
    sys.exit()


def differentiate(principal, period, nominal_interest):
    overpayment = 0
    for x in range(1, int(period) + 1):
        differ = math.ceil((principal / period) + nominal_interest * (
                principal - ((principal * (x - 1)) / period)))
        overpayment += differ
        print(f"Month {x}: payment is {differ}")
    print(f"\nOverpayment = {int(overpayment - principal)}")


def annuity(monthly_pay, period, loan, nominal_interest):
    # calculate principal we have pay months and interest
    if args.principal is None:
        principal = math.floor(monthly_pay / (
                (nominal_interest * (1 + nominal_interest) ** period) / ((1 + nominal_interest) ** period - 1)))
        print(f"Your loan principal = {principal}!")
        # calculate overpayment
        print(f"Overpayment = {int(monthly_pay * period - principal)}")

    # calculate annuity payment we have time principal and interest
    elif args.payment is None:
        annuity_pay = math.ceil(
            loan * ((nominal_interest * (1 + nominal_interest) ** period) / ((1 + nominal_interest) ** period - 1)))
        print(f"Your annuity payment = {annuity_pay}!")
        print(f"Overpayment = {int(annuity_pay * period - loan)}")

    # calculate time principal(loan), monthly pay and interest
    elif args.periods is None:
        num_of_months = math.ceil(math.log(monthly_pay / (monthly_pay - nominal_interest * loan), 1 + nominal_interest))
        years, months = divmod(num_of_months, 12)
        print(f"It will take {years} years to repay this loan!")
        # print overpayment
        print(f"Overpayment = {int(monthly_pay * num_of_months - loan)}")


def starter(interest):
    if args.type == "diff":
        if args.interest is None:
            print("Incorrect parameters.")
        else:
            nominal_interest = (interest / 1200)
            differentiate(args.principal, args.periods, nominal_interest)
    elif args.type == "annuity":
        nominal_interest = (interest / 1200)
        annuity(args.payment, args.periods, args.principal, nominal_interest)


starter(args.interest)
