class Account:
    
    def __init__(self, acc_holder, acc_no, balance):
        self.acc_holder = acc_holder
        self.acc_no = acc_no
        self.balance = balance
            
    def getBalance(self):
        return self.balance
        
    def getDetails(self):
        print(f'Acc_Holder : {self.acc_holder} \nAcc_no : {self.acc_no} \nBalance : {self.balance}\n')
        
    def Debit(self, amt):
        self.balance-=amt
        print(f'Debited, new balance : {self.balance}\n')
    
    def Credit(self, amt):
        self.balance+=amt
        print(f'Credited, new balance : {self.balance}\n')
     
person1 = Account('Person1', '01234', 5000)

print(person1.acc_holder)

person1.getBalance()
person1.getDetails()
person1.Credit(300)

person2 = Account('Person2', '09876', 15000)

print(person2.acc_holder)

person2.getBalance()
person2.getDetails()
person2.Debit(300)
