#E=mc2
def main():
    #ask and recieve user input
    print('Please enter mass (in kilograms): ', end='')
    mass_input = input()
    
    #run the calculation
    print('E = ' + calculation(mass_input) + ' Joules')

def calculation(mass):
    #convert mass to an integer
    mass = int(mass)

    #approximate speed of light and speed of light squared
    c = 300000000
    c_squared = c*c

    #Final equation
    energy = mass*c_squared

    #convert back into a string and return the answer
    #can convert in main if you want to keep as an integer
    return str(energy)

main()