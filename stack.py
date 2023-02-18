def push(a,val):
    a.append(val)
def pop(a):
    item=a.pop()
    print("popped Item",item)
def peek(a):
    last=len(a)-1
    print("peek Element=",a[last])
def display(a):
    for i in range(len(a)-1,-1,-1):
        print(a[i])

a = []
while True:
    choice= int(input("1->push\n2->pop\n3->peak\n4->Display\n5->Exit\nEnetr your choice"))
    if choice==1:
        val=int(input("Enter Number to Insert :"))
        push(a,val)
        print("Element Pushed Successfully...")
    elif choice==2:
        if len(a)==0:
            print("Stack Underflow")
        else:
            pop(a)
    elif choice==3:
        if len(a)==0:
            print("Stack Underflow...")
        else:
            peek(a)
    elif choice==4:
        if len(a)==0:
            print("Stack Underflow")
        else:
            display(a)

    else:
        break;

    
