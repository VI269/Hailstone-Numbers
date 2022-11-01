try:
    import matplotlib.pyplot as plt
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
        if input("Q to quit or anything else to show graph: ").lower() == 'q':
            quit()
        plt.show()
except:
    print('Something went wrong')
