# Created by Moontasir Abtahee at 2/26/2022

# Feature: #Enter feature name here
# Enter feature description here

# Scenario: # Enter scenario name here
# Enter steps here



class FinalQ:
    def print(self,array,idx):
        if(idx<len(array)):
            profit = self.calcProfit(array[idx]) #TO DO
            print(f"{idx+1}. Investment: {array[idx]}; Profit: {self.calcProfit(array[idx])}")
            self.print(array,idx+1)

    def calcProfit(self,investment):
        if investment<= 25000:
            return 0.0
        elif investment>25000 and investment<=100000:
            return 45+ self.calcProfit(investment-1000)
        elif investment>100000:
            return 80 +self.calcProfit(investment-1000)
        else:
            return 0



    # Tester
array = [25000, 100000, 250000, 350000]
f = FinalQ()
f.print(array, 0)