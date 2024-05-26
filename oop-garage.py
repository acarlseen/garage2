import random

class Garage():
    def __init__(self, num_spots: int = 20) -> None:
        self.parking_spaces = self.generate_lot(num_spots)
        self.tickets = self.generate_tickets_list(num_spots)
        self.current_tickets = {}
    
    def generate_lot(self, num_spaces):
        exp = len(str(num_spaces))
        start = pow(10, exp)
        result = [x + start for x in range(num_spaces)]
        return result
        
    
    def generate_tickets_list(self, num_tickets) -> list:
        result = []
        for x in range(num_tickets):
            ticket = random.randint(1000,9999)
            while ticket in result:
                ticket = random.randint(1000,9999)
            result.append(ticket)
        return result
    
    def retreive_ticket(self) -> int:
        valid = False
        while valid == False:
            ticket_number = input('Welcome back! Enter your ticket number (or "quit"): ')
            if ticket_number.lower() == 'quit':
                return
            elif ticket_number.isdigit() and int(ticket_number) in self.current_tickets.keys():
                valid = True
                ticket_number = int(ticket_number)
        return ticket_number
    
    def take_ticket(self):
        if len(self.tickets) == 0:
            print('Sorry, there are no tickets/spots available.')
            return
        ticket_number = self.tickets.pop(random.randint(0,len(self.tickets) - 1))
        
        spot = self.parking_spaces.pop(random.randint(0,len(self.parking_spaces)-1))
        
        self.current_tickets[ticket_number] = {'parking_space': spot, 'amount_due': 10, 'paid' : False}
        print(f'Your ticket number is {ticket_number}, please hold on to your ticket. Enjoy your parking spot.')
    
    def pay_for_parking(self, ticket_number: int = 0):
        if ticket_number == 0:
            ticket_number = self.retreive_ticket();
        
        space, amount_due, paid = self.current_tickets[ticket_number].values()
        payment = ''
        while payment.isdigit() == False:
            payment = input(f'Thank you. \n Please pay ${amount_due} before leaving the lot. Enter payment, bills only (or "quit")')
            if payment.lower() == 'quit':
                return
        balance = amount_due - int(payment)
        if balance <= 0:
            if balance < 0:
                print(f'Your change is: {balance*-1}')
            self.current_tickets[ticket_number]['amount_due'] = 0
            self.current_tickets[ticket_number]['paid'] = True

            print('Thank you for parking with ParkAnywhere, please exit the lot within 15 minutes.')
        else:
            self.current_tickets[ticket_number] = {'parking_space': space, 'amount_due': balance, 'paid' : paid}
            print(f'Please pay the remaining balance of ${balance} before exiting the lot')
    
    def leave_garage(self):
        ticket_number = self.retreive_ticket();
        space, amount_due, paid = self.current_tickets[ticket_number].values()
        
        if paid == False:
            self.pay_for_parking(ticket_number)
        
        if paid == True:        
            self.parking_spaces.append(space)
            self.tickets.append(ticket_number)
            print('Thank you for parking with ParkAnywhere. Please leave.')
        else:
            return

if __name__ == '__main__':
    lot = Garage(100)
    run_app = True
    function_dict = {'park' : lot.take_ticket, 'pay': lot.pay_for_parking, 'leave':lot.leave_garage}
    while run_app == True:
        user_input: str = input('Hello, this is a $10 flat-rate parking garage. \n What would you like to do? [Park, Pay, Leave, Quit] ')
        if user_input.lower() == 'quit':
            run_app = False
        if user_input.isalpha() and user_input.lower() in function_dict.keys():
            function_dict[user_input.lower()]();