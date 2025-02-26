def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    #remove the leading $
    dollar = d.replace('$', '')

    #convert new string to float
    dollar = float(dollar)
    return dollar


def percent_to_float(p):
    #remove the trailing %
    percents = p.replace('%', '')

    #convert new string to float
    percents = float(percents) / 100
    return percents


main()