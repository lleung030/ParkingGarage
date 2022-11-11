




#tickets -> list

#parkingSpaces -> list

garage = ['tickets', 'parkingSpaces']

#currentTicket -> dictionary





class Garage():
    def __init__(self, takeTicket, parkingSpaces, payForParking, leaveGarage):
        self.takeTicket = takeTicket
        self.parkingSpaces = parkingSpaces
        self.payForParking = payForParking
        self.leaveGarage = leaveGarage
        
    currentTicket ={
    'tickets':100,
    'parkingSpaces':100
} 
    def takeTicket(self, tickets):
        
        if currentTicket[tickets]>0:
            currentTicket[tickets] -= 1
                
        
        # This should decrease the amount of tickets available by 1
        
        # This should decrese the amount of parkingSpaces avaialable by 1

    def leaveGarage(self):
        
        if currentTicket[parkingSpaces]>0:
            currentTicket[parkingSpaces] +=1
        
        # If the ticket has been paid, display a message of "Thank You, have a nice day"
        # If the ticket has not been paid, display an input prompt for payment
        # Once paid, display message "Thank you, have a nice day!"
        # Update parkingSpaces list to increase by 1 (meaning add to the parkingSpaces list)
        # Update tickets list to increase by 1 (meaning add to the tickets list)
        
            
    def parkingSpaces(self):
        # This should decrase the amount of parkingSpaces available by 1
        
        if currentTicket[parkingSpaces]>0:
            currentTicket[parkingSpaces] -=1
        
        
    def payForParking(self):
        # Display an input that waits for an amount from the user and store it in a variable
        
        # If the payment variable is not empty then (meaning the ticket has been paid) -> display a message to the user that their ticket has been paid and they have 15mins to leave
        
        # This should update the "currentTicket" dictionary key "paid" to True
