try:
    import matplotlib.pyplot as plt
except:
    print("Matplotlib not found. Run this command: pip install matplotlib / pip3 install matplotlib")
    print("If none work: python -m pip install matplotlib")
try:
    def hailstone_numbers(number):
        curnum, lst = number, []
        while True:
            lst.append(int(curnum))
            if curnum % 2 == 0:  
                curnum /= 2
            else: 
                curnum = (3*curnum)+1
            if curnum == 1: 
                return lst
    while True:
        num = int(input("Number: "))
        x, y = [i for i in range(1, len(hailstone_numbers(num)))], [hailstone_numbers(num)[i-1] for i in range(1, len(hailstone_numbers(num)))]
        plt.plot(x, y)
        print("Steps: "+str(len(hailstone_numbers(num))))
        inp = input("Q to quit, S to not show the graph, R to stack with the previous graph or anything else to show graph: ").lower()
        if  inp == 'q':
            quit()
        elif inp == 's':
            plt.close()
            continue
        elif inp == 'r':
            continue
        plt.show()
except:
    print('Something went wrong')