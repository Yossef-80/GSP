# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 15:34:39 2022

@author: Youssef
"""
import pandas as pd
#import numpy as np
#------------- classes-----------------------
class Items:
    def __init__(self):
        self.items=[]
        self.support_count=0
        
class three_or_more_sequence:
    def __init__(self):
        self.sequence=[]
        self.first=[]
        self.last=[]

     
class Sequence:
    
    def __init__(self,user_id):
        self.user_id=user_id
        
        self.sequence=[]
        
#--!--read file    
df=pd.read_csv('Book1.csv')
#---------------functions--------------------

#-----------join 3 items or more function
def join_3_or_more(items_LIST):
    
    #count the incoming list
    primary_count=len(items_LIST)
    three_or_more_List=[]
    for item_obj in items_LIST:
        
        if (len(item_obj[0])>1 or  len(item_obj[len(item_obj)-1])>1) and len(item_obj)==1:#{(ab)}
            for k in range(0,len(item_obj[0])):
                 item_seq=three_or_more_sequence()#contains the Sequence[] first[] last[]
                 item_seq.sequence=item_obj.copy()
                 item_seq.first.append(item_obj[0][k])
                 item_seq.last.append(item_obj[0][len(item_obj[0])-1-k])
                 three_or_more_List.append(item_seq)
                 
        elif  len(item_obj[0])>1:#{(ab),f}
             item_seq=three_or_more_sequence()
             item_seq.sequence=item_obj
             temp_remove=item_obj.copy()
             temp2=item_obj.copy()
             temp2.pop(0)
             temp_remove.pop(len(item_obj)-1)
             item_seq.last=temp_remove
             for k in range(0,len(item_obj[0])):
                  item_seq=three_or_more_sequence()
                  item_seq.sequence=item_obj.copy()
                  item_seq.first=item_obj[0][k]+temp2
                  item_seq.last=temp_remove
                  three_or_more_List.append(item_seq)
            
             
        elif  len(item_obj[len(item_obj)-1])>1:#{f,(ab)}    
             item_seq=three_or_more_sequence()
             item_seq.sequence=item_obj
             remove_first=item_obj.copy()
             temp2=item_obj.copy()
             temp2.pop(len(item_obj)-1)
             remove_first.pop(0)
             for k in range(0,len(item_obj[len(item_obj)-1])):
                  item_seq=three_or_more_sequence()
                  item_seq.sequence=item_obj.copy()
                  item_seq.first=remove_first
                  item=[]
                  item.append(item_obj[len(item_obj)-1][k])
                  item_seq.last=temp2+item
                  item.clear()
                  three_or_more_List.append(item_seq)
             
        else:
             item_seq=three_or_more_sequence()
             item_seq.sequence=item_obj
             temp1=item_obj.copy()
             temp2=item_obj.copy()
             temp1.pop(0)

             temp2.pop(len(item_obj)-1)
             first_removed=temp1
             last_removed=temp2
           #  print('---->obj:',item_obj,"-----temp1:",temp1,"--------temp2:",temp2)

             item_seq.first=first_removed
             item_seq.last=last_removed
             three_or_more_List.append(item_seq)
    The_List=[]
    temp=[]
    for i in range(0,len(three_or_more_List)):
        if len(three_or_more_List[i].sequence)==1:#['ab']
            for j in range(0,len(three_or_more_List)):
                print("sequence->",three_or_more_List[j].sequence,"first->",three_or_more_List[j].first,"last->",three_or_more_List[j].last)
                
                if three_or_more_List[i].last==three_or_more_List[j].first and three_or_more_List[i].sequence != three_or_more_List[j].sequence:
                    the_item=Items()
                    print("1------>",three_or_more_List[i].sequence," ",three_or_more_List[i].last,"<>",three_or_more_List[j].sequence)
                    print(three_or_more_List[j].last.copy()+three_or_more_List[i].sequence.copy())
                    
                    the_item.items=three_or_more_List[j].last.copy()+three_or_more_List[i].sequence.copy()
                    if the_item.items not in temp:
                        
                        temp.append(three_or_more_List[j].last.copy()+three_or_more_List[i].sequence.copy())
                        The_List.append(the_item)
                    
        elif len(three_or_more_List[i].sequence)==2:#['a','b'] to make three candidate itemset
            for j in range(0,len(three_or_more_List)):
                if three_or_more_List[i].first==three_or_more_List[j].last:
                        the_item=Items()
                        the_item.items=three_or_more_List[i].last+three_or_more_List[i].first+three_or_more_List[j].first
                        The_List.append(the_item)
                elif three_or_more_List[i].last==three_or_more_List[j].first:
                    
                        the_item=Items()
                        the_item.items=three_or_more_List[i].first+three_or_more_List[i].first+three_or_more_List[j].last
                        if the_item.items not in temp:

                            temp.append(three_or_more_List[i].first+three_or_more_List[i].first+three_or_more_List[j].last)
                            The_List.append(the_item)
        else:
            for j in range(0,len(three_or_more_List)):#to generate more than 3 candidate items
                if three_or_more_List[i].first==three_or_more_List[j].last:                        
                    the_item=Items()
                    the_item.items=three_or_more_List[i].last+three_or_more_List[j].first
                    The_List.append(the_item)
                elif three_or_more_List[i].last==three_or_more_List[j].first:
                    the_item=Items()
                    the_item.items=three_or_more_List[i].first+three_or_more_List[j].last
                    if the_item.items not in temp:
    
                        temp.append(three_or_more_List[i].first+three_or_more_List[j].last)
                        The_List.append(the_item)
    secondary_count=len(The_List)
    if secondary_count==primary_count:
         # stop=1 
          return None
    return The_List
                  
#---------------      

#join 2 items
def  join_2(items_LIST):
    sorted(items_LIST)
    
    #join sequence {a,b}
    join_first=[]
    for i in range (len(items_LIST)):
        for j in range(len(items_LIST)):
           ''' join_first.append(items_LIST[i].join(items_LIST[j]))'''
           item=Items()
           item.items.append(items_LIST[i][0])
           item.items.append(items_LIST[j][0])
           join_first.append(item)
          
    join_first2=[]
    for i in range (len(items_LIST)):
        for j in range(i+1,len(items_LIST)):
           ''' join_first.append(items_LIST[i].join(items_LIST[j]))'''    
           s=''
           
           item=Items()
           combine=s+items_LIST[i][0]+items_LIST[j][0]
           item.items.append(combine)
           join_first2.append(item)
      
    listToReturn=join_first+join_first2
    return listToReturn



#count the support    
def count_support(customersLIST,support_count_LIST,minimum_Support):
   
    #support_count_LIST=list(dict.fromkeys(support_count_LIST))
    '''   for i in range(0,len(support_count_LIST)):
        for j in  range(i,len(support_count_LIST)-1):
            if support_count_LIST[i].items is support_count_LIST[j].items:
                support_count_LIST.pop(i)
'''

    for item_seq in support_count_LIST:
        if len(item_seq.items)==1:#item_seq ==1 {ab}
            for itemset in customersLIST:
                for item_in_itemset in itemset.sequence:
                    if item_seq.items[0] in item_in_itemset:
                        item_seq.support_count=item_seq.support_count+1
                        break
        else:#if item_seq >1 {a,b,c}
            for itemset in customersLIST:# {'a','b','ab','c','d'} 
                itemsCount=0 
                index=0
                for i in range(0,len(item_seq.items)):
                    for j in range(index,len(itemset.sequence)):
                        if item_seq.items[i] in itemset.sequence[j]:
                            index=j+1
                            itemsCount=itemsCount+1
                if itemsCount==len(item_seq.items):
                    item_seq.support_count=item_seq.support_count+1
                        
                   
                    

    ''' for i in range(0,len(support_count_LIST)):
        print(support_count_LIST[i].items," supportCount",support_count_LIST[i].support_count," before",i)
        '''   
        
    #pruning the sequence    
    newList=[]
    for i in support_count_LIST:
        if i.support_count>=minimum_Support:
            newList.append(i)
    
    for i in range(0,len(newList)):
        print(newList[i].items," supportCount",newList[i].support_count," after",i)
    itemsList=[]
    for i in range(0,len(newList)):
        itemsList.append(newList[i].items)
    itemsList=sorted(itemsList)
    return itemsList
         
                       
                

#Items_Perchased=df["Items Purchased"].tolist()




the_Minimum_Support=2




#read the customer id in list
Customer_id=df["Customer ID"].tolist()

#get the customer_id & items Purchased Columns
Customers=df.iloc[:,1:3].copy()


#get the number Of Customers by 
num_of_customers=max(Customer_id)

num_of_transactions=len(df.index)
customersLIST=[]

#the id starts from 1
for i  in range(1,num_of_customers+1):
    seq=Sequence(i)
    customersLIST.append(seq)

    
the_list_of_items=(Customers["Items Purchased"].tolist())
#get items
items_LIST=[]
for i in range(len(the_list_of_items)):
    if len(the_list_of_items[i] )>1:
        for j in range(len(the_list_of_items[i])):
            items_LIST.append(the_list_of_items[i][j])
            
        items_LIST.pop(i)
    else:
        items_LIST.append(the_list_of_items[i])
        
#remove redunduncy
items_LIST=list(dict.fromkeys(items_LIST))

#the items_LIST now have all items in data set without redunduncy
support_LIST=[]
#make a List of items which have support count
for i in  items_LIST:
    supp=Items() #->Items()->items[],support_count
    supp.items.append(i)
    support_LIST.append(supp)

#make the customerList -> ['a','b','ab','c','d']
for i in range(num_of_transactions):
    for j in range(num_of_customers):
         if (Customers["Customer ID"].iloc[i] == customersLIST[j].user_id):
            # print("stored in user:",j+1,", item:",Customers["Items Purchased"].iloc[i])
            # print(customersLIST[j].user_id)
             #print(Customers["Customer ID"].iloc[i] ,"==", customersLIST[j].user_id,"transaction number",i,"user number",j,"value ",Customers["Items Purchased"].iloc[i])
             customersLIST[j].sequence.append(Customers["Items Purchased"].iloc[i])

i=0             
#for i in range(len(customersLIST[2].sequence)):
   # print(customersLIST[2].sequence[i]) 


     
itemsList=count_support(customersLIST,support_LIST,the_Minimum_Support)
#print(itemsList[0])
join2list=join_2(itemsList)
joint2SupList=count_support(customersLIST, join2list, the_Minimum_Support)
#count support

#for i in join3_list:
  #  print("items:",i.items)
#join4_list=join_3_or_more(joint3SupList)
#joint4SupList=count_support(customersLIST, join4_list, 2)

stop = 0
joint3SupList=joint2SupList.copy()
while stop==0:
    join3_list=join_3_or_more(joint3SupList)
    if join3_list == None:
        break
    joint3SupList=count_support(customersLIST, join3_list, the_Minimum_Support)





