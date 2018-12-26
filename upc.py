#THIS WILL RETURN UPC CHECK VALUE

upc = '04210000526'

def main(upc):
    for i  in upc:
        result = 0
        for i in range(0,11,2):
            result += int(upc[i])
    result *= 3 
    for i in upc:
        for i in range(1,11,2):
            result += int(upc[i])
    result %= 10
    if result != 0:
        return 10 - result
    else:
        return 0
    
print(main(upc))
