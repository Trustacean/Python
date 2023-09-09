class BankAccount():
    def __init__(self,accountNumber,name,balance):
        self.__accountNumber = accountNumber
        self.name = name
        self.balance = balance
    def Deposit(self,amount):
        self.balance += amount
    def Withdraw(self,amount):
        self.balance -= amount
    def bankFees(self):
        self.balance -= self.balance/20
    def display(self):
        print ("Account Number %s" % self.__accountNumber)
        print ("Name %s" % self.name)
        print ("Balance %s" % self.balance)

Me = BankAccount(221,"Edward",0)
Me.Deposit(1000)
Me.display()
Me.Withdraw(100)
Me.display()
Me.bankFees()
Me.display()
print (Me.__accountNumber)
