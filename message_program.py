# print a message
while True:
    input_message = input('''\nPlease select what the weather is like today: 
    A. Sunny
    B. Rainy
    C. Clear
    D. [Exit program]
    \nselection: ''').upper()

    if input_message == "A":
        print("\nIt is sunny outside!")
    elif input_message == "B":
        print("\nIt is rainy outside.")
    elif input_message == "C":
        print("\nThe sky is clear today.")
    elif input_message == "D":
        print("\n...Program exited.")
        exit()
    else:
        print("\nPlease select a valid menu option from A-D.")





