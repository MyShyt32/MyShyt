

def loop(i):
    if i is not None:
        print(i)
        if i < 3:
            i = i + 1
            loop(i)
    else:
        i = 0
        loop(i)

def main():
    i = None
    loop(i)

if __name__ == '__main__':
    main()