def divide():
    try:
        print("file open")
        a = int(input("enter a number"))
        b = int(input("enten antother"))
        c = a/b
        print(c)
        print("file closed")
    #when you type b=0
    except ZeroDivisionError as e:
        print(e)
    #when you type any anthing othre than int
    except ValueError as e:
        print(e)
    except Exception as e:
        print(e)
    finally:
        #to avoid resource leak we need to close resources at any cost
        print("file close")
divide()