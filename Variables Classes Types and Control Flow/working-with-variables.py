message = "Global Message"

def main():

    global message

    message = "Local Message"
    print(message)
    
    myStr = "test"
    myNum = 55

    # print(myStr + myNum) # Error
    print(myStr + str(myNum))

if __name__ == "__main__":
    main()
    print(message)