
class Garage():
    def __init__(self):
        spaces = 2
    
    currentTicket ={
    'tickets':5,
    'parkingSpaces':5,
    'paid':'False'
}
       
    def pay(self):
        
        print('Ticket has been paid. Please exit... {15 MINS COOLDOWN}')
        self.currentTicket['paid'] = 'True'
        print(self.currentTicket['paid'])
        # print the number of spots and tickets left afterward
        
        
        # elif payment == 2:
        #     print('TICKET HAS NOT BEEN PAID {PLEASE MAKE A PAYMENT}')
        # else:
        #     print('INVALID OPTION {PLEASE TRY AGAIN}')

car = Garage()

def main():
    # while True:
    #     response = input('Would you like to park? (Y/N): ')
            
    #     if response == 'yes' or response == 'y':    
    car.pay()
    
    # elif choice == 'no':
        #     print('bye')
