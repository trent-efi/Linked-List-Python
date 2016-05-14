import pdb

class Node:
    def __init__(self, Data): 
        self.nxt = None
	self.Data = Data
    #end init

#end class

class L_List:
    def __init__(self):
	self.head = None
        self.curr = None
	self.Count = 0
    #end

    def Insert(self, Data):
        n = Node(Data)
	if self.curr == None:
	    self.curr = n
	    self.head = n
	else:
	    self.curr.nxt = n
	    self.curr = n
	    self.Count += 1
    #end

    def Print_LL(self):
        curr = self.head
	while curr != None:
            print curr.Data
	    curr = curr.nxt
	#end
    #end

    def Reverse_LL(self):


        if self.Count > 1:
            curr = self.head
	    prev = None
	    nxt = None
            while curr != None:
                nxt = curr.nxt
		curr.nxt = prev
		prev = curr
		curr = nxt
	    #end
	    self.head = prev
	#end
    #end
#end L_List


l = L_List()
l.Insert(14)
l.Insert("Trent")
l.Insert("Russell")
l.Insert(23)
print "\nPrinting\n"
l.Print_LL()
print "\nReverseing\n"
l.Reverse_LL()
l.Print_LL()

