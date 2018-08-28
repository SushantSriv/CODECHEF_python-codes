for i in range(int(input())):
    s=input().upper()
    print(min(s.count("C"),s.count("H"),s.count("E"),s.count("F")))
