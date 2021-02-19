import pickle
import os
import pathlib
class Account :
    accNo = 0
    name = ''
    deposit=0
    type = ''
    
    def createAccount(self):
        self.accNo= int(input("\t\t\tEnter the account no : "))
        self.name = input("\t\t\tEnter the account holder name : ")
        self.type = input("\t\t\tEnter the type of account [C/S] : ")
        self.deposit = int(input("\t\t\tEnter The Initial amount:"))
        print("\n\n\n\t\t\tAccount Created")
    
    def showAccount(self):
        print("\t\t\tAccount Number : ",self.accNo)
        print("\t\t\tAccount Holder Name : ", self.name)
        print("\t\t\tType of Account",self.type)
        print("\t\t\tBalance : ",self.deposit)
    
    def modifyAccount(self):
        print("\t\t\tAccount Number : ",self.accNo)
        self.name = input("\t\t\tModify Account Holder Name :")
        self.type = input("\t\t\tModify type of Account :")
        self.deposit = int(input("\t\t\tModify Balance :"))
        
    def depositAmount(self,amount):
        self.deposit += amount
    
    def withdrawAmount(self,amount):
        self.deposit -= amount
    
    def report(self):
        print(self.accNo, " ",self.name ," ",self.type," ", self.deposit)
    
    def getAccountNo(self):
        return self.accNo
    def getAcccountHolderName(self):
        return self.name
    def getAccountType(self):
        return self.type
    def getDeposit(self):
        return self.deposit
    

def intro():
    print("\t\t\t\t**********************")
    print("\t\t\t\tBANK MANAGEMENT SYSTEM")
    print("\t\t\t\t**********************")
    print("")

    input("\t\t\tPress Enter To continue")



def writeAccount():
    account = Account()
    account.createAccount()
    writeAccountsFile(account)

def displayAll():
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        mylist = pickle.load(infile)
        for item in mylist :
            print("\t\t\t", item.accNo," ", item.name, " ",item.type, " ",item.deposit )
        infile.close()

    else :
        print("\t\t\tNo records to display")
        

def displaySp(num): 
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        mylist = pickle.load(infile)
        infile.close()
        found = False
        for item in mylist :
            if item.accNo == num :
                print("\t\t\tYour account Balance is = ",item.deposit)
                found = True
    else :
        print("\t\t\tNo records to Search")
    if not found :
        print("\t\t\tNo existing record with this number")

def depositAndWithdraw(num1,num2): 
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        mylist = pickle.load(infile)
        infile.close()
        os.remove('accounts.data')
        for item in mylist :
            if item.accNo == num1 :
                if num2 == 1 :
                    amount = int(input("\t\t\tEnter the amount to deposit : "))
                    item.deposit += amount
                    print("\t\t\tYour account is updated")
                elif num2 == 2 :
                    amount = int(input("\t\t\tEnter the amount to withdraw : "))
                    if amount <= item.deposit :
                        item.deposit -=amount
                    else :
                        print("\t\t\tYou cannot withdraw larger amount")
                
    else :
        print("\t\t\tNo records to Search")
    outfile = open('newaccounts.data','wb')
    pickle.dump(mylist, outfile)
    outfile.close()
    os.rename('newaccounts.data', 'accounts.data')

    
def deleteAccount(num):
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        oldlist = pickle.load(infile)
        infile.close()
        newlist = []
        for item in oldlist :
            if item.accNo != num :
                newlist.append(item)
        os.remove('accounts.data')
        outfile = open('newaccounts.data','wb')
        pickle.dump(newlist, outfile)
        outfile.close()
        os.rename('newaccounts.data', 'accounts.data')
     
def modifyAccount(num):
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        oldlist = pickle.load(infile)
        infile.close()
        os.remove('accounts.data')
        for item in oldlist :
            if item.accNo == num :
                item.name = input("\t\t\tEnter the account holder name : ")
                item.type = input("\t\t\tEnter the account Type : ")
                item.deposit = int(input("\t\t\tEnter the Amount : "))
        
        outfile = open('newaccounts.data','wb')
        pickle.dump(oldlist, outfile)
        outfile.close()
        os.rename('newaccounts.data', 'accounts.data')
   

def writeAccountsFile(account) : 
    
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        oldlist = pickle.load(infile)
        oldlist.append(account)
        infile.close()
        os.remove('accounts.data')
    else :
        oldlist = [account]
    outfile = open('newaccounts.data','wb')
    pickle.dump(oldlist, outfile)
    outfile.close()
    os.rename('newaccounts.data', 'accounts.data')
    


    
# start of the program
ch=''
num=0
intro()

while ch != 8:
    #system("cls");
    print("")
    print("\t\t\t\tMAIN MENU")
    print("\t\t\t1. NEW ACCOUNT")
    print("\t\t\t2. DEPOSIT AMOUNT")
    print("\t\t\t3. WITHDRAW AMOUNT")
    print("\t\t\t4. BALANCE ENQUIRY")
    print("\t\t\t5. ALL ACCOUNT HOLDER LIST")
    print("\t\t\t6. CLOSE AN ACCOUNT")
    print("\t\t\t7. MODIFY AN ACCOUNT")
    print("\t\t\t8. EXIT")
    print("")
    print("\t\t\tSelect Your Option (1-8) ")
    ch = input("\t\t\tEnter your Choice:")
    print("")
    #system("cls");
    
    if ch == '1':
        writeAccount()
    elif ch =='2':
        num = int(input("\t\t\tEnter The account No. : "))
        depositAndWithdraw(num, 1)
    elif ch == '3':
        num = int(input("\t\t\tEnter The account No. : "))
        depositAndWithdraw(num, 2)
    elif ch == '4':
        num = int(input("\t\t\tEnter The account No. : "))
        displaySp(num)
    elif ch == '5':
        displayAll();
    elif ch == '6':
        num =int(input("\t\t\tEnter The account No. : "))
        deleteAccount(num)
    elif ch == '7':
        num = int(input("\t\t\tEnter The account No. : "))
        modifyAccount(num)
    elif ch == '8':
        print("\t\t\tThanks for using bank managemnt system")
        input("\t\t\tPress Enter to Exit")
        break
    else :
        print("\t\t\tInvalid choice")
    
    ch = input("\t\t\tPress Enter to Continue")
    


    
    
    
    
    
    
    
    
    
    

