# first we create a class name TodoApp
class TodoApp:
    def __init__(self):
        self.mylist=[]
    

    def add(self,item):
        self.mylist.append(item)
    
    def show(self):
        return self.mylist
    
    def complete(self,index):
        try:
            self.mylist.pop(index-1)
        except:
            return -1

todo= TodoApp()
var= True
while var:
    print('\nWelcome to our Todo App')
    print('1.Enter 1 for adding items')
    print('2.Enter 2 for showing all items')
    print('3.Enter 3 for removing item')
    print('4.Enter 4 for Exit')

    choice= int(input('> '))

    if choice==1:
        item = input('Enter Item name: ')
        todo.add(item)
        print('Item added succesfully')
    
    elif choice==2:
        mylist= todo.show()
        p=1
        if mylist:
            print("Your Todo List: ")
            print('______________________\n')
            for i in mylist:
                print(str(p) + '. '+ i )
                p=p+1
            print('______________________')
        else: 
            print('List is Empty,First add some items')
        
    elif choice==3:
        mylist= todo.show()
        p=1
        if mylist:
            print('Your Todo List: \n')
            print('______________________\n')
            for i in mylist:
                print(str(p) + '. '+i )
                p=p+1
            print('______________________')   
            index = int(input('Enter the number of item you want to delete\n'))
            if todo.complete(index)==-1:
                print('Invalid Input\n')
                
            else:
                print('Item removed Succesfully')
        else: 
            print('List is Empty,First add some items')
    
    else:
        var=False
        print('Thankyou for using Todo')
