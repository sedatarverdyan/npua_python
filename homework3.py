arr = input('Enter numbers separated by space')
lists = map(int,arr.split(' '))


def classify_numbers(list):
    even =[]
    odd = []
    for list in lists:
        if list % 2==0:
            even.append(list)
        else:
            odd.append(list)
    return even, odd


        
even, odd = classify_numbers(list)
print('Even numbers', even)
print('Odd numbers', odd)