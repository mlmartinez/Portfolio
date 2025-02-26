def main():
    #ask and recieve user input
    print('Please type something: ', end='')
    user_input = input()

    #run the conversion function
    print(convert(user_input))

def convert(smiley):
    #replace the happy and sad faces using unicode
    smiley = smiley.replace(':)', '\U0001F642')
    smiley = smiley.replace(':(', '\U0001F641')

    #return the newly converted emojis
    return smiley

main()