for i in range(int(input())):
    s=input()
    if(s.count("0")<s.count("1")):
        print("WIN")
    else:
        print("LOSE")
