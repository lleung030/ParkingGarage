




#tickets -> list

#parkingSpaces -> list

garage = ['tickets', 'parkingSpaces']

#self.currentTicket -> dictionary


class Garage():
    def __init__(self, takeTicket, parkingSpaces, payForParking, leaveGarage):
        self.takeTicket = takeTicket
        self.parkingSpaces = parkingSpaces
        self.payForParking = payForParking
        self.leaveGarage = leaveGarage
        
    currentTicket ={
    'tickets':100,
    'parkingSpaces':100,
    'paid':'False'
}
   
    def takeTicket(self):
        
        if self.currentTicket['tickets']>0:
            self.currentTicket['tickets'] -= 1
                
        
        # This should decrease the amount of tickets available by 1
        
        # This should decrese the amount of parkingSpaces avaialable by 1

    def leaveGarage(self):
        
        if self.currentTicket['parkingSpaces']>0:
            self.currentTicket['parkingSpaces'] +=1
        
        # If the ticket has been paid, display a message of "Thank You, have a nice day"
        # If the ticket has not been paid, display an input prompt for payment
        # Once paid, display message "Thank you, have a nice day!"
        # Update parkingSpaces list to increase by 1 (meaning add to the parkingSpaces list)
        # Update tickets list to increase by 1 (meaning add to the tickets list)
        
            
    def parkingSpaces(self):
        # This should decrase the amount of parkingSpaces available by 1
        
        if self.currentTicket['parkingSpaces']>0:
            self.currentTicket['parkingSpaces'] -=1
        
        
    def payForParking(self):
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


currentTicket = Garage()

def main():
    while True:
        response = input('Would you like to park? (Y/N): ')
            
        if response == 'yes' or response == 'y':
            currentTicket.takeTicket()
            
        # elif response.lower() == 'no' or response == 'n':
        #     print("Have a good day!")
        #     break
    
main()