from time import sleep

def main():
    altura = int(input("Altura: "))
    piramide(altura)
    
def piramide(n):
    for i in range(n):
        i += 1
        sleep(0.5)
        print('#' * i)
    
if __name__ == "__main__":
    main()
    