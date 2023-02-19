class bank:
    def __init__(self,name,accn,accty):
        self.accn=accn
        self.name=name
        self.accty=accty
        self.balance=0
    def showact(self):
        print("Account holder name : ",self.name)
        print("Account number : ", self.accn)
        print("Account type : ", self.accty)
        print("Account balance : ", self.balance)
    def dep(self,d1):
        self.balance= self.balance+d1
        return self.balance

    def withd(self, w1):
        self.balance = self.balance-w1
        return self.balance
n=input("Enter your name : ")
a=int(input("Enter your account number : "))
t=input("Enter your account type :")
o=bank(n,a,t)

while(True):
    print("MENU \n 1.DEPOSIT \n2.WITHDRAWAL\n3.EXIT")
    choice=int(input("Enter your choice : "))
    if(choice==1):
        amt=int(input("Enter the amount to be deposited :"))
        o.dep(amt)
        o.showact()
    elif(choice==2):
        amt=int(input("Enter the amount to be withdrawed :"))
        if(amt>o.balance):
            print("Insufficient balance")
        else:
            o.withd(amt)
            o.showact()
    elif(choice==3):
        exit(0)
    else:
        print("Enter a valid choice")
