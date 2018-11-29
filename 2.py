""" PISIT W:5 """
def main():
    """ II """
    num = int(input())
    count = 0
    for j in range(num, 0, -1):
        print(j, end=' ')
        count += 1
        if count == 7:
            print(' ')
            count = 0

main()
