import os.path
class Account:
    def __init__(self, name):
        self.name = name
        self.newfile = self.name + '.txt'
        self.filename = self.name + 'File'
        self.wrong = []
        self.info = []
        self.incorrect = False

    def createAccount(self,Password):
        self.Password = Password

        if len(self.info) == 0:
            with open(self.newfile, 'a') as self.filename:
                self.filename.writelines(self.Password + '\n')
                self.filename.writelines('0' + '\n')
                    

            with open(self.newfile, 'r') as self.filename:
                for i in self.filename.readlines():
                    self.wrong.append(i)

                for j in self.wrong:
                    correct = j.replace('\n', '')
                    self.info.append(correct)
            

    def withdraw(self, amountToTake, Username):
        self.Username = Username
        self.amountToTake = amountToTake
        self.money = int(self.info[-1])
        self.moneyleft = self.money - self.amountToTake

        if self.amountToTake > self.money:
            print('Card declined!')

        else:
            print(f'${self.amountToTake} withdrawl successful! Your new balance is: ${self.moneyleft}')
            with open(f"C:\\Users\\krist\\.vscode\\Python_Files\\{self.Username}.txt", 'a') as withdraw:
                withdraw.writelines(str(self.moneyleft) + '\n')


    def deposit(self, amountToGive, Username):
        self.empty3 = []
        self.empty4 = []
        self.Username = Username
        self.amountToGive = amountToGive

        with open(f"C:\\Users\\krist\\.vscode\\Python_Files\\{self.Username}.txt", 'a') as firstmoner:
            firstmoner.writelines(self.amountToGive + '\n')

        with open(f"C:\\Users\\krist\\.vscode\\Python_Files\\{self.Username}.txt", 'r') as depositmoney:
            for i in depositmoney.readlines():
                self.empty3.append(i)
        
        for j in self.empty3:
            better = j.replace('\n', '')
            self.empty4.append(better)

        recent = int(self.empty4[-1])
        prior = int(self.empty4[-2])
        self.newbalance = recent + prior

        with open(f"C:\\Users\\krist\\.vscode\\Python_Files\\{self.Username}.txt", 'a') as deposit2:
            deposit2.writelines(str(self.newbalance) + '\n')

        print(f'${self.amountToGive} deposit successful!\n Your new balance is: ${self.newbalance}')

    def checkbalance(self, Username):
        self.Username = Username
        print(f'Your available balance is: ${self.info[-1]}')

    def checkBoth(self,checkpassword, checkUser):
        self.empty = []
        self.empty2 = []
        if os.path.exists(f"C:\\Users\\krist\\.vscode\\Python_Files\\{checkUser}.txt") == True:
            with open(f"C:\\Users\\krist\\.vscode\\Python_Files\\{checkUser}.txt") as self.filename:
                for i in self.filename:
                    self.empty.append(i)
                
                for j in self.empty:
                    better = j.replace('\n', '')
                    self.empty2.append(better)
                    self.info.append(better)

            self.checkpassword = checkpassword
            self.check = self.empty2[0]
            if self.check != self.checkpassword:
                self.incorrect = True