# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 15:38:30 2021

@author: wajee
"""

from bid_logo import logo

def Place_Bids(name,amount,Name_Dictionary,Bidders_dictionary):
    
    Name_Dictionary[name]=amount
    Bidders_dictionary['Bids Placed']=Name_Dictionary
    greatest=0
    highest_bidder=''
    
    for key1,value1 in Bidders_dictionary.items():
        for key2,value2 in value1.items():
            
            if(value2>greatest):
                greatest=value2
                highest_bidder=key2
    
    return(highest_bidder,greatest)
                
    
def main():
    
    print(logo)
    print("Welcome to the Bidding Program:")
    Name_Dictionary=dict()
    Bidders_dictionary=dict()

    choice='Y'
    
    while choice=='Y' or choice=='y':
        
        name=input("Please Enter your Name:")
        amount=int(input("Please Enter your Bid amount:"))
        high_bidders_name,amount_bid=Place_Bids(name,amount,Name_Dictionary,Bidders_dictionary)
        print("Does anyone else wish to add another bid")
        choice=input("Please Enter Y for Yes N for No:")
    
    print(f"The Highest Bidder Name is : {high_bidders_name} And the Amount is : {amount_bid}")
    print("Congratulations")
    

if __name__ == '__main__':
    main()