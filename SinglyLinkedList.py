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
    
    def swap_nodes(self, j, k):
        if j == k:
            return print("Same nodes")
        if j == 0:
            curr1 = self.head
            curr2 = self.head
            for i in range(1,k+1):
                curr2 = curr2.next
            self.head = curr2
            curr1.next = curr2.next
            curr2.next = curr1
            return 
        if k == 0:
            curr1 = self.head
            curr2 = self.head
            for i in range(1,j+1):
                curr2 = curr2.next
            self.head = curr2
            curr1.next = curr2.next
            curr2.next = curr1
            return
        curr1 = self.head
        for i in range(1, j+1):
            curr1 = curr1.next
        curr2 = self.head
        for i in range(1, k+1):
            curr2 = curr2.next
        temp = curr1.next
        curr1.next = curr2.next
        curr2.next = temp
        return
    def reverse(self):
        prev = None
        curr = self.head
        while curr:
            new = curr.next
            curr.next = prev
            prev = curr
            curr = new
        #self.head.next = None
        self.head = prev
    def merge_sorted(self, L):
        P = self.head
        Q = L.head
        S = None
        if not Q:
            return P
        if not P:
            return Q
        
        if P and Q:
            if P.data <= Q.data:
                S = P
                P = S.next
            else:
                S = Q
                Q = S.next
            new_head = S
        while P and Q:
            if P.data <= Q.data:
                S.next = P
                S = P
                P = S.next
            else:
                S.next = Q
                S = Q
                Q = S.next
        if not Q:
            S.next = P
        if not P:
            S.next = Q
            
        return new_head
             
            
llist = LinkedList()
llist.append(1)
llist.append(3)
llist.append(5)
#llist.print_list()
#llist.insert_at("C",1)
#llist.print_list()
llist.append(6)
llist.print_list()
print("---------------")
# =============================================================================
# llist.swap_nodes(1,2)
# llist.print_list()
# print("---------------")
# llist.reverse()
# llist.print_list()
# =============================================================================
llist2 = LinkedList()
llist2.append(2)
llist2.append(4)
llist2.append(7)
llist2.print_list()
print("---------------")

llist.merge_sorted(llist2)
llist.print_list()
