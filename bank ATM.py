#nestedwhile
print("Welcome to State Bank Of India ATM")
restart=('Y')
chances=3
balance=67.14
while chances>=0:
    pin: int=int(input('please enter your 4 digit pin:'))
    if pin=='1234':
        print('you entered your pin correctly\n')
        while restart not in ('n','NO','no','N'):
            print('Please press 1 for your balance')
            print('Please press 2 to make a withdraw\n')
            print('Please press 3 to pay in\n')
            print('Please press 4 to return card\n')
            option:int = int(input('What would you like to choose?'))
            if option==1:
                print('Your balance is XYZ',balance,'\n')
                restart=input('Would you like to go back?')
            if restart in('n','NO','no','N'):
                    print('Thankyou!')
                    break
            elif option==2:
                 option2='y'
                 withdrawl : float = float(input('how much would you like to withdraw\n10$/20$/30$/40$/50$'))
                 if withdrawl in [10,20,30,40,50]:
                            balance=balance-withdrawl
                            print('Your balance is now $',balance)
                            restart=input('Would you like to go back')
                            if restart in('n','NO','no','N'):
                              print('Thankyou!')
                            break
                 elif withdrawl!=[10,20,30,40,50]:
                    print('Invalid Amount,Please retry\n')
                    restart='y'
                 elif withdrawl==1:
                  withdrawl=float(input('Please enter desired amount:'))
            elif option == 3:
                  pay_in = float(input('how much woud you like to pay in?\n'))
                  balance = balance + pay_in
                  print('\n Your balance is now $', balance)
                  restart = input('Would you like to go back?')
                  if restart in ('n', 'NO', 'no', 'N'):
                      print('Thankyou!')
                      break
            elif option==4:
              print('Please wait while your card is returned...\n')
            print('Thankyou for your service')
            break
        else:
            print('Please enter a correct number\n')
            restart='y'
    elif pin != '1234':
       print('Incorrect Password')
       chances = chances - 1
    if chances==0:
           print('\nNo more tries')
           break