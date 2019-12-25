# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 22:28:46 2019

@author: ritap
"""
#Creation of a node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
#Creating a linked list     
class LinkedList:
    def __init__(self):
        self.head = None
    
    #printing the list
    def print_list(self):
        curr_node = self.head
        
        while curr_node:
            print(curr_node.data)
            curr_node = curr_node.next
    
    #adding node it the end
    def insert_last(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return 
        
        last_node = self.head
        
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
    
    #adding node at the begining 
    def insert_first(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return
        
        new_node.next = self.head
        self.head = new_node
     
    #adding node at any position
    def insert_at(self, data, index):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        curr_node = self.head
        for i in range(index-1):
            if curr_node.next == None:
                print("Invalid Index")
                return 
            curr_node = curr_node.next
            
        new_node.next = curr_node.next
        curr_node.next = new_node
    
    #deleting node at any position
    def delete_at(self, index):
        if self.head is None:
            print("Empty List")
            return
        if index == 0:
            self.head = self.head.next
            return
        curr_node = self.head
        for i in range(index-1):
            if curr_node.next == None:
                print("Invalid Index")
                return
            curr_node = curr_node.next
        curr_node.next = curr_node.next.next
        
        
arr = LinkedList()
arr.insert_last("A")
arr.insert_last("B")
arr.insert_last("D")
#llist.print_list()
arr.insert_at("C",1)
#llist.print_list()
arr.delete_at(2)
arr.print_list()


    
