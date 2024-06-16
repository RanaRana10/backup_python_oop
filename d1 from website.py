
'''
This i got from the https://kinsta.com/blog/python-object-oriented-programming/
'''


# small = 2
# regular = 5
# big = 6
 
# user_budget = input('What is your budget? ')
 
# try:
#    user_budget = int(user_budget)
# except:
#    print('Please enter a number')
#    exit()
 
# if user_budget > 0:
#    if user_budget >= big:
#        print('You can afford the big coffee')
#        if user_budget == big:
#            print('It\'s complete')
#        else:
#            print('Your change is', user_budget - big)
#    elif user_budget == regular:
#        print('You can afford the regular coffee')
#        print('It\'s complete')
#    elif user_budget >= small:
#        print('You can buy the small coffee')
#        if user_budget == small:
#            print('It\'s complete')
#        else:
#            print('Your change is', user_budget - small)





class Coffee:
    def __init__(self, name, price):
        self.name = name
        self.price = float(price)

    def check_budget(self, budget):
        # Check if the budget is valid
        if not isinstance(budget, (int, float)):
            print('Enter float or int')
            exit()
        if budget < 0: 
            print('Sorry you don\'t have money') 
            exit() 

    def get_change(self, budget):
        round_num = budget - self.price
        round_num = round(round_num, 2)
        return round_num
        
    
    def sell(self, budget):
        self.check_budget(budget)
        if budget >= self.price:
            print(f'You can buy the {self.name} coffee')
            if budget == self.price:
                print('It\'s complete')
            else:
                print(f'Here is your change {self.get_change(budget)}$')

            exit('Thanks for your transaction')


small = Coffee('Small', 2)
regular = Coffee('Regular', 5)
big = Coffee('Big', 6)
 
try:
#    user_budget = float(input('What is your budget? '))
   user_budget = 6.999
except ValueError:
   exit('Please enter a number')
  
for coffee in [big, regular, small]:
   coffee.sell(user_budget)



















