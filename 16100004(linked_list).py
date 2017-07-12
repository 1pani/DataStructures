# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 12:43:19 2017

@author: hp
"""

class Node(object):
    def __init__(self , data = None , agla_node = None):
        self.data = data
        self.agla_node = agla_node
        
    def get_data(self):
        return self.data

    def get_next_node(self):
        return self.agla_node
    
    def set_agla_node(self , new_next):
        self.next_node = new_next
        
class LinkedList(object):               #head of linkedlist
    def __init__(self , mukhiya = None):
        self.mukhiya = mukhiya

    def insert(self , data):                #inserting at head
        naya_node = Node(data)
        naya_node.set_agla_node(self.mukhiya)
        self.mukhiya = naya_node
        
    def size(self):
        current = self.mukhiya
        cnt = 0
        while current:
            cnt+=1
            current = current.get_next_node()
        return cnt

    def search(self,data):
        
        current = self.mukhiya
        found = False
        
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next_node()
        if current is None:
            print("data not in list")
        return current

    def delete(self,data):
        
        current = self.mukhiya
        prev = None
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                prev = current
                current = current.get_next_node()
        if current == None:
            print("data not in list")
            
        if prev == None:
            self.mukhiya = current.get_next_node()
        else:
            prev.set_agla_node(current.get_next_node) 


        
            