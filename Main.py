
import tkinter as T
from itertools import combinations 

class WORD:
        def __init__(self):
                self.word=""
                self.pron=""
                self.mean=""
                self.word_type=""
        def starter(self,a_word,a_type,a_pron,a_mean):
                self.word=a_word
                self.pron=a_pron
                self.mean=a_mean
                self.word_type=a_type
        def write_to_file(self):
                self.pad_self()
                file=open("File","a+")
                file.write(self.word.capitalize())
                file.write(self.word_type.capitalize())
                file.write(self.pron.capitalize())
                file.write(self.mean.capitalize())
                file.close()
        
        def pad_self(self):
              
                if len(self.word)<51:
                        self.word=self.word+'%'*(50-len(self.word))
                if len(self.mean)<201:
                        self.mean=self.mean+'%'*(200-len(self.mean))
                if len(self.pron)<61:
                        self.pron=self.pron+'%'*(60-len(self.pron))
                if len(self.word_type)<4:
                        self.word_type=self.word_type+'%'*(4-len(self.word_type))

        def read_a_word_from_file(self,ref):
                f= open("File","r")
                f.seek(ref)

                
                self.word=f.read(50)
                self.word_type=f.read(4)
                self.pron=f.read(60)
                self.mean=f.read(200)
                
                f.close()
                
                if self.word.find('%')>0:
                        self.word=self.word[0:self.word.find('%')]
                if self.word_type.find('%')>0:
                        self.word_type=self.word_type[0:self.word_type.find('%')]
                if self.mean.find('%')>0:
                        self.mean=self.mean[0:self.mean.find('%')]
                if self.pron.find('%')>0:
                        self.pron=self.pron[0:self.pron.find('%')]



        def print_word(self):
                print("Word : " , self.word)
                print("Word type : " , self.word_type)
                print("Pronounciation : " , self.pron)
                print("Meanning : " , self.mean)
        
class Atomic_node:
    def __init__(self):
        self.word=""
        self.ref=-1
    
class simpleNode:
    def __init__(self,an_atomic_node:Atomic_node):
        self.simple_node=an_atomic_node
        self.next:simpleNode= None

class Data:
    def __init__(self,new_homeNode:simpleNode):
        self.head=new_homeNode 
        self.tail=new_homeNode
    
    def add(self,new_homeNode:simpleNode):
        self.tail.next=new_homeNode
        self.tail=new_homeNode
    
    def find_prev(self,ref:int):
        current=self.head
        prev:simpleNode=None
        while current!= None:
            if current.simple_node.ref !=ref:
                prev=current
                current=current.next
            else:
                return prev

    def remove(self,a_node:simpleNode):
        current=self.find_prev(a_node)
        current.next=a_node.next
        print("Removed fie from node")
        # del current


    def find_a_word(self,ref):
        current=self.head
        while current!= None:
            if current.simple_node.ref !=ref:
                current=current.next
            else:
                return current

    def update_ref(self,ref,new_ref):
        current=self.head
        while current!= None:
            if current.simple_node.ref !=ref:
                current=current.next
            else:
                current.simple_node.ref=new_ref

class Node:

    def __init__(self,data_node:Data, head_word:str):
                self.data:Data=data_node
                self.right :Node=None
                self.left :Node=None
                self.Height=0
                # self.balance=self.balance_factor()
                self.head_word:str=head_word
        
    def balance_factor(self):
                if self==None:
                        return 0
                else :
                        L=self.left
                        R=self.right
                        left_factor=Height(L)
                        right_factor= Height(R)
                        factor = left_factor-right_factor
                return factor      

class Tree:
    def __init__(self):
       self.root:Node = None
       self.no_of_Data_=0
       self.Load_Tree()
       print_tree(self.root)
   
    def Load_Tree(self):
                f =open("File","a")
                last:int=f.tell()
                f.close()
                f=open("File","r")
                ref=0
                while ref!=last:
                        temp=f.read(314)
                        temp=temp[0:50]
                        if temp.find('%') > 0:
                              temp=temp[0:temp.find('%')]
                
                        self.insert_a_raw_word(temp,ref)
                        ref =f.tell()

    def height_of_a_tree(self):
       return  Height(self.root)-1

    def balance_tree(self, node:Node): #balances the tree at a given node
        current =node
        while current != None:
            factor = current.balance_factor()
            if factor > 1:
                    if current.left.left !=None:
                        current=self.right_rotate(current)
                    else:
                        current=self.left_right_rotation(current)
            elif factor<-1:
                    if current.right.right !=None:
                        current=self.left_rotate(current)
                    else:
                        current=self.right_left_rotation(current)
            else:
                current=self.get_the_parent(current)
            
    def left_rotate(self, to_leave_root:Node): 
            parent =self.get_the_parent(to_leave_root)
            to_be_root:Node= to_leave_root.right 
            to_leave_root.right = to_be_root.left
            to_be_root.left = to_leave_root

            if parent==None:
                self.root = to_be_root
            else :
                if parent.right== to_leave_root:
                    parent.right=to_be_root
                else:
                    parent.left=to_be_root
            return to_be_root
               
    def right_rotate(self, to_leave_root:Node): 
            parent =self.get_the_parent(to_leave_root)
            to_be_root= to_leave_root.left
            
            to_leave_root.left = to_be_root.right 
    
            to_be_root.right = to_leave_root
            if parent==None:
                self.root = to_be_root
            else :
                if parent.left== to_leave_root:
                    parent.left=to_be_root
                else:
                    parent.right=to_be_root
            return to_be_root

    def right_left_rotation(self,to_leave_root:Node):
        #swapping
        temp = to_leave_root.right
        to_leave_root.right=to_leave_root.right.left
        to_leave_root.right.right=temp
        return self.right_rotate(to_leave_root)
           
    def left_right_rotation(self,to_leave_root:Node):
        #swapping
        temp = to_leave_root.left
        to_leave_root.left=to_leave_root.left.right
        to_leave_root.left.left=temp
        return self.left_rotate(to_leave_root)

    def search_a_word(self,a_word:str):
                if self.root==None:
                        return None
                current=self.root
                while 1:
                        if  current.head_word< a_word:
                                current=current.right
                                if current == None:
                            
                                      return None
                        elif current.head_word >a_word:
                                current=current.left
                                if current == None:
                                
                                        return None
                        else:
                               
                                return current

    def insert_A_NODE(self,node:Node): #assuming the item in the node is unique
                self.no_of_Data_=self.no_of_Data_+1
                its_word=node.head_word
                if self.root ==None:
                        self.root=node
                else:
                        current = self.root
                        while 1:
                                if current.head_word<its_word:
                                        if current.right == None :
                                                current.right = node
                                                break
                                        else:
                                                current=current.right
                                                continue
                                else :
                                        if current.left == None :
                                                current.left = node
                                                break
                                        else:
                                                current=current.left
                                                continue
                self.balance_tree(node)
                      
    def insert_a_raw_word(self,raw_word:str, ref:int):
                atomic_temp=Atomic_node()
                atomic_temp.ref=ref
                atomic_temp.word=raw_word


                simple_temp=simpleNode(atomic_temp)
                simple_temp.simple_node=atomic_temp
                simple_temp.next=None
                              
                existance=self.search_a_word(raw_word)
                if existance != None:
                        existance.data.add(simple_temp)
                else:
                       data_temp=Node(Data(simple_temp),raw_word) #critical inserts in a tree
                       self.insert_A_NODE(data_temp)
    
    def remove_root(self):
        print("removing root")
        current=self.get_min_from_right(self.root)
        parent=self.get_the_parent(current)

        #hand over old job
        if parent.right == current:
            parent.right=current.right
        else:
            parent.left=current.right
        
        #take over new 
        current.left=self.root.left
        current.right=self.root.right
        self.root=current
        self.balance_tree(self.root)

        return None

    def remove_a_node(self,a_node:Node):
        print("Node removal started ")
        if a_node==self.root:
            self.remove_root()
        else:
            parent=self.get_the_parent(a_node)
            if a_node.right == None and a_node.left==None:
                if parent.right==a_node:
                    parent.right=None
                else:
                    parent.left=None

            elif a_node.right==None:
                if parent.right==a_node:
                    parent.right=a_node.left
                else:
                    parent.left=a_node.left

            elif a_node.left==None:
                if parent.right==a_node:
                    parent.right=a_node.right
                else:
                    parent.left=a_node.right
            
            else:
                here=self.get_min_from_right(a_node)
    
                #don't forget to handover old job
                parent_of_here=self.get_the_parent(here)
                if parent_of_here.right==here:
                    parent_of_here.right=here.right 
                else:
                    parent_of_here.left=here.right
                    
                #take over new job
                here.right=a_node.right
                here.left=a_node.left

                #serve parent of original
                if parent.right == a_node:
                    parent.right=here
                else:
                    parent.left=here
                  
            del a_node
            self.balance_tree(parent)
        print("Node removal ended here succesfully ")

    def get_max_from_left(self,a_node:Node):
        current=self.root.left
        while current != None:
            current=current.right
        return current
    def get_min_from_right(self,a_node:Node):
        current=self.root.right
        while current != None:
            current=current.left
        return current
    
    def remove_a_word(self,a_word,its_type:str):
        existance=self.search_a_word(a_word)
        if existance!=None:
            if existance.data.head == existance.data.tail:
                print("No duplicate word exists")
                self.remove_a_ref_from_file(existance.data.head.simple_node.ref)
                self.remove_a_node(existance)
            else:#if duplicate word exists
                print("duplicate word exists")
                current =existance.data.head
                temp_word=WORD()
                while current!=None:#finding the specific word from linked list using the word type to identify
                    temp_word.read_a_word_from_file(current.simple_node.ref)
                    if temp_word.word_type!=its_type:
                        current=current.next
                    else:
                        self.remove_a_ref_from_file(current.simple_node.ref)
                        existance.data.remove(current)
                        break
        
    def remove_a_ref_from_file(self,ref:int):
        #save the last elements details
        
        file=open("File","a+")
        ref_of_last=file.tell()-314
        the_last=WORD()
        the_last.read_a_word_from_file(ref_of_last)
        file.close()

        if ref_of_last==ref:
            file=open("File","tr+")
            file.seek(ref_of_last)
            file.truncate()
            file.close()
        else:
            #updating reference on a tree
            mother_node=self.search_a_word(the_last.word)
            mother_node.data.update_ref(ref_of_last,ref)
            #remove last elements from original
            file=open("File","tr+")
            file.truncate(ref_of_last)
            file.close()


            #write from ref + 314 to middle
            file=open("File","r")
            middle=open("user_temp", "w")
            file.seek(ref+314)
            middle.write(file.read())
            file.close()
            middle.close()

        
            # remove from ref to all
            # temp_file=open("user_temp","tr+")
            # temp_file.truncate(ref)
            # temp_file.close()

            #start insering files back staring from the last
            the_last.write_to_file()

            #insert the middle
            file=open("File","tr+")
            temp_file=open("user_temp","r")
            file.seek(0,0)
            file.truncate(ref)
            file.write(temp_file.read())
            file.close()
            temp_file.close()
            print("removed from file already")
            
    def get_the_parent(self,child_node:Node):
        existance=self.search_a_word(child_node.head_word)
        if (existance==None)or(self.root == child_node):
            return None 
        else:                      
            its_word=child_node.head_word
            parent=self.root
            current = self.root
            
            while 1 : 
                if current.head_word<its_word:
                    parent=current
                    current=current.right  
                elif current.head_word>its_word :
                    parent=current
                    current=current.left
                else:
                    return parent
   
    
def print_tree(a_node:Node):   #inorder print of word and  meaning
        if a_node != None:     
            print_tree(a_node.left) 
            # then print the data of node 
            temp=WORD()
            current= a_node.data.head
            while current != None:
                temp.read_a_word_from_file(current.simple_node.ref)
                print(temp.word,"\t:\t",temp.mean)
                current=current.next
            print_tree(a_node.right) 
            
def Height(node:Node):
    if node is None: 
        return 0 
  
    else : 
        lDepth = Height(node.left) 
        rDepth = Height(node.right) 
  
        if (lDepth > rDepth): 
            return lDepth+1
        else: 
            return rDepth+1




















class Board(T.Tk):
    def __init__(self):
        T.Tk.__init__(self)
        self.minsize(300,400)
        self._frame:T.Frame = None
        self.switch_frame(Welcome_frame(self))
        self.title("Dictionary")

    def switch_frame(self, frame_class:T.Frame):
        if self._frame is not None:
            self._frame.destroy()
        self._frame:T.Frame = frame_class
        self._frame.pack()

def Welcome_frame(master):
        temp=T.Frame(master)
        T.Label(temp,height=1, width=1).pack() #visual space
        T.Label(temp,text="A Dictionary", width=30).pack()
        T.Label(temp,height=1, width=1).pack() #visual space
        T.Button(temp, text="Search a Word", command=lambda:master.switch_frame(Search_window_frame(master)),width =13).pack()
        T.Label(temp,height=1, width=1).pack() #visual space
        T.Button(temp, text="Insert a Word", command=lambda:master.switch_frame(Insert_record_frame(master)),width =13).pack()
        T.Label(temp,height=1, width=1).pack() #visual space
        T.Button(temp, text="Remove a Word", command=lambda:master.switch_frame(remove_word_frame(master)),width =13).pack()
        T.Label(temp,height=1, width=1).pack() #visual space        
        T.Button(temp, text="Update a Word", command=lambda:master.switch_frame(update_word_frame(master)),width =13).pack()
        T.Label(temp,height=1, width=1).pack() #visual space              
        T.Button(temp, text="Print all words", command=lambda:master.switch_frame(print_words_frame(master)),width =13).pack()
        return temp
def print_words_frame(master):
        temp=T.Frame(master)
        print("")
        print_tree(TREE.root)

        T.Label(temp, text="words are printed \n on terminal !", width = 25,height=15).pack()
        T.Label(temp,height=1, width=1).pack() #visual space
        T.Button(temp, text = "Back", command=lambda:master.switch_frame(Welcome_frame(master)) ,width = 25).pack()
        return temp

def Search_window_frame(master):
        temp=T.Frame(master)
        search_Entry=T.StringVar()
        T.Label(temp,height=1, width=1).pack() #visual space
        T.Entry(temp,textvariable=search_Entry, width=20, justify=T.CENTER).pack()
        T.Label(temp,height=1, width=1).pack()#visual space
        T.Button(temp, text="Search a Word", command=lambda:master.switch_frame(Search_result_frame(master,search_Entry.get().capitalize())),width =10).pack()
        return temp

def Search_result_frame(master,search_word):
        temp=T.Frame(master)
        existance:Node=TREE.search_a_word(search_word)
        T.Label(temp,height=1, width=1).pack() #csd
        if existance == None:
            result="The word is not found !"
            T.Label(temp,text=result).pack()

        else:
            current=existance.data.head
            temp_WORD=WORD()
            while current!=None:
                temp_WORD.read_a_word_from_file(current.simple_node.ref)
                T.Label(temp,text="Word :"+temp_WORD.word).pack()
                T.Label(temp,height=1, width=1).pack() #visual space
                T.Label(temp,text="Word Type :"+temp_WORD.word_type).pack()
                
                T.Label(temp,height=1, width=1).pack() #visual space
                T.Label(temp,text="Pronounciation :"+temp_WORD.pron).pack()

                 
                T.Label(temp,height=1, width=1).pack() #visual space
                T.Label(temp,text="Meaning :"+temp_WORD.mean).pack()
                T.Label(temp,height=1, width=1).pack() #visual space

                current=current.next
       
        T.Label(temp,height=1, width=1).pack() #visual space
        T.Button(temp, text = "Back", command=lambda:master.switch_frame(Welcome_frame(master)) ,width = 20).pack()
        return temp

def Insert_record_frame(master):
        temp=T.Frame(master)
        word=T.StringVar()
        pron=T.StringVar()
        mean=T.StringVar()
        word_type=T.StringVar()

        T.Label(temp,text="Word :").pack()
        T.Entry(temp,textvariable=word, width=20, justify=T.RIGHT).pack()
        T.Label(temp,height=1, width=1).pack() #visual space


        T.Label(temp,text="Word type : ").pack()
        T.Entry(temp,textvariable=word_type, width=20, justify=T.RIGHT).pack()
        T.Label(temp,height=1, width=1).pack() #visual space

        T.Label(temp, text="Pronounciation : ").pack()
        T.Entry(temp,textvariable=pron, width=20, justify=T.RIGHT).pack()
        T.Label(temp,height=1, width=1).pack() #visual space

        T.Label(temp, text="Meaning : ").pack()
        T.Entry(temp,textvariable=mean, width=20, justify=T.RIGHT).pack()
        T.Label(temp,height=1, width=1).pack() #visual space

        T.Label(temp,height=1, width=1).pack()#visual space
        T.Button(temp, text="Insert the Word", command=lambda:master.switch_frame(Insert_result_frame(master,word.get(),word_type.get(),pron.get(),mean.get())),width =10).pack()
    
        T.Label(temp,height=1, width=1).pack()#visual space  
        T.Button(temp, text = "Back", command=lambda:master.switch_frame(Welcome_frame(master))).pack()
        
        temp.pack()
        return temp

def Insert_result_frame(master,word,word_type,pron,mean):
    temp=T.Frame(master)
    if is_input_good(word,word_type,pron,mean):
        temp_WORD=WORD()

        temp_WORD.word=word
        temp_WORD.word_type=word_type
        temp_WORD.pron=pron
        temp_WORD.mean=mean
        f=open("File","a+")
        TREE.insert_a_raw_word(word,f.tell()) #inserting in a tree is included , f.tell is new ref
        f.close()
        temp_WORD.write_to_file() #writting to a file

        T.Label(temp, text="Inserted !", width = 10,height=10).pack()
        T.Label(temp,height=1, width=1).pack() #visual space
        T.Button(temp, text = "Back", command=lambda:master.switch_frame(Welcome_frame(master)) ,width = 20).pack()
    else:
        T.Label(temp, text="Bad Insertion !", width = 20,height=10).pack()
        T.Label(temp,height=1, width=1).pack() #visual space
        T.Button(temp, text = "Back", command=lambda:master.switch_frame(Welcome_frame(master)) ,width = 20).pack()

    return temp

def is_input_good(word,word_type,pron,mean):
    if len(word)<51 and len(word_type)<5 and  len(pron) and len(mean):
        return True
    else:
        return False

def remove_result_frame(master,the_word:str, the_word_type:str):
    temp=T.Frame(master)
    TREE.remove_a_word(the_word,the_word_type)#actual removing
    T.Label(temp, text="Removed !", width = 20,height=10).pack()
    T.Label(temp,height=1, width=1).pack() #visual space
    T.Button(temp, text = "Back", command=lambda:master.switch_frame(Welcome_frame(master)) ,width = 20).pack()
    return temp
def remove_word_frame(master):
        temp=T.Frame(master)
        word_var=T.StringVar()
        T.Label(temp,height=1, width=1).pack() #visual space
        T.Label(temp,text="The Word").pack()
        T.Entry(temp,textvariable=word_var, width=20, justify=T.RIGHT).pack()
        
        T.Label(temp,height=1, width=1).pack() #visual space

        word_type=T.StringVar()
        T.Label(temp,text="Word type : ").pack()
        T.Entry(temp,textvariable=word_type, width=20, justify=T.RIGHT).pack()
        T.Label(temp,height=1, width=1).pack() #visual space
        
  
        T.Button(temp, text="Remove word", command=lambda:master.switch_frame(remove_result_frame(master,word_var.get().capitalize(),word_type.get().capitalize())),width =16).pack()
        T.Label(temp,height=1, width=1).pack() #visual space        
        T.Button(temp, text = "Back", command=lambda:master.switch_frame(Welcome_frame(master)) ,width = 16).pack()
        
        return temp

def update_word_frame(master):
        temp=T.Frame(master)
        search_Entry=T.StringVar()
     
        T.Label(temp,text="Word :").pack()
        T.Entry(temp,textvariable=search_Entry, width=20, justify=T.RIGHT).pack()
        T.Label(temp,height=1, width=1).pack() #visual space

        
        word_type=T.StringVar()
        T.Label(temp,text="Word type :").pack()
        T.Entry(temp,textvariable=word_type, width=20, justify=T.RIGHT).pack()
        T.Label(temp,height=1, width=1).pack() #visual space
        

        T.Button(temp, text="Update Word", command=lambda:master.switch_frame(update_frame_result(master,search_Entry.get(),word_type.get())),width =15).pack()
        T.Button(temp, text = "Back", command=lambda:master.switch_frame(Welcome_frame(master)) ,width = 15).pack()

        return temp

def update_frame_result(master,a_word:str, the_word_type:str):
    temp=T.Frame(master)
    TREE.remove_a_word(a_word,the_word_type) 

    temp=T.Frame(master)
    word=T.StringVar()
    pron=T.StringVar()
    mean=T.StringVar()
    word_type=T.StringVar()

    T.Label(temp,text="Word :").pack()
    T.Entry(temp,textvariable=word, width=20, justify=T.RIGHT).pack()
    T.Label(temp,height=1, width=1).pack() #visual space

    T.Label(temp,text="Word type : ").pack()
    T.Entry(temp,textvariable=word_type, width=20, justify=T.RIGHT).pack()
    T.Label(temp,height=1, width=1).pack() #visual space

    T.Label(temp, text="Pronounciation : ").pack()
    T.Entry(temp,textvariable=pron, width=20, justify=T.RIGHT).pack()
    T.Label(temp,height=1, width=1).pack() #visual space

    T.Label(temp, text="Meaning : ").pack()
    T.Entry(temp,textvariable=mean, width=20, justify=T.RIGHT).pack()
    T.Label(temp,height=1, width=1).pack() #visual space

    T.Label(temp,height=1, width=1).pack()#visual space
    T.Button(temp, text="Update the Word", command=lambda:master.switch_frame(Insert_result_frame(master,word.get(),word_type.get(),pron.get(),mean.get())),width =10).pack()

    T.Label(temp,height=1, width=1).pack()#visual space  
    T.Button(temp, text = "Back", command=lambda:master.switch_frame(Welcome_frame(master))).pack()
    
    temp.pack()
    return temp

if __name__ == "__main__":
    
    B=Board()
    TREE = Tree()
    B.mainloop()