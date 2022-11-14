




#tickets -> list

#parkingSpaces -> list

garage = ['tickets', 'parkingSpaces']

#self.currentTicket -> dictionary


class Garage():
    def __init__(self):
        spaces = 2
    
    currentTicket ={
    'tickets':5,
    'parkingSpaces':5,
    'paid':'False'
}
   
    def takeTicket(self):  
        if self.currentTicket['tickets'] >0:
            
            self.currentTicket['tickets'] -= 1
            print (f"There is now {self.currentTicket['tickets']} tickets left.")
        
        elif self.currentTicket['tickets'] <= 0:
            print('No more tickets left. Please exit!')

    def leaveGarage(self):

        self.currentTicket['parkingSpaces'] +=1
        print(f"There is now {self.currentTicket['parkingSpaces']} parking spaces left.")        
            
    def parkingSpaces(self):
        if self.currentTicket['parkingSpaces'] >0:
            self.currentTicket['parkingSpaces'] -=1
            print(f"There is now {self.currentTicket['parkingSpaces']} parking spaces left.")
        
        elif self.currentTicket['parkingSpaces'] <= 0:
            print('No more parking spaces left. Please exit!')
        
        
    def payForParking(self, payment):
        # Display an input that waits for an amount from the user and store it in a variable
        
        payment = int(input('Paid(Enter 1) (or) UnPaid(Enter 2): '))
        if payment == 1:
            print('TICKET HAS BEEN PAID {15 MINS COOLDOWN}')
            self.currentTicket['paid'] = 'True'
            print(self.currentTicket)
        elif payment == 2:
            print('TICKET HAS NOT BEEN PAID {PLEASE MAKE A PAYMENT}')
        else:
            print('INVALID OPTION {PLEASE TRY AGAIN}')
        
        # If the payment variable is not empty then (meaning the ticket has been paid) -> display a message to the user that their ticket has been paid and they have 15mins to leave
        
        # This should update the "self.currentTicket" dictionary key "paid" to True


car = Garage()

def main():
    while True:
        response = input('Would you like to park? (Y/N): ')
            
        if response == 'yes' or response == 'y':
            car.takeTicket()
            car.parkingSpaces()
        
            choice = input('Would you like to leave now?: (y/n)')
            
            if choice == 'yes':
                car.payForParking()
                
                
        elif response.lower() == 'no' or response == 'n':
            car.leaveGarage()
            print("Have a good day!")
            break
    
main()