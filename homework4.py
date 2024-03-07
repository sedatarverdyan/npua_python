
arr = input('Enter numbers separated by space')
numbers = map(int,arr.split(' '))

def sum_of_elements(number, **kwargs):
    sum =0
    check = input('Do you want to exclude negative numbers? (yes/no): ')
    if check=="yes":
        kwargs['exclude_negative'] = True
    for number in numbers:
        if  kwargs['exclude_negative']:
            if number>=0:
                sum = sum + number 
        else:
            sum =sum +number
    return sum
print(sum_of_elements(numbers, exclude_negative=False))

