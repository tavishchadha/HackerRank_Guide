if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    output_list = []

    for i in range(0,x+1):
        for j in range(0,y+1):
            for k in range(0,z+1):
                if(i+j+k != n):
                    output_list.append([i,j,k])
                else:
                    pass

    print(output_list)
