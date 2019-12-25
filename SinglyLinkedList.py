# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 22:28:46 2019

@author: ritap
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
        
class LinkedList:
    def __init__(self):
        self.head = None
    
    def print_list(self):
        curr_node = self.head
        
        while curr_node:
            print(curr_node.data)
            curr_node = curr_node.next
    
    def append(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return 
        
        last_node = self.head
        
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
    
    def prepend(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return
        
        new_node.next = self.head
        self.head = new_node
        
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
        
        
llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("D")
#llist.print_list()
llist.insert_at("C",1)
#llist.print_list()
llist.delete_at(2)
llist.print_list()


    