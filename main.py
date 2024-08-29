# EX1.Create function to sum numbers in array [1,2,3,4,5,6]

def sum_numbers(numbers):
    total = 0  
    for i in range (len(numbers)):
          total += numbers[i]
    return total 
numbers = [1, 2, 3, 4, 5, 6]  
result = sum_numbers(numbers)  
print(result)  



# # EX2.Create function to sum odd number in array [1,2,3,4,5,6]


def max_number(numbers):
    max_num = numbers[0]  
    count=0
    for i in range(len(numbers)):  
        if numbers[i] % 2 == 0 :
            max_num = numbers[i] 
            count+=1 
    return max_num
number = [2, 3, 5, 0, 11, 5, 2]
count = max_number(number)
print(count)


# # EX3.Create function to find Max number in array [2,3,5,0,11,5,2]


def max_number(numbers):
    max_num = numbers[0]  
    for i in range(len(numbers)):  
        if numbers[i] >  max_num:
            max_num = numbers[i]  
    return max_num
number = [2, 3, 5, 0, 11, 5, 2]
result = max_number(number)
print(result)



# # EX4.Create function to find Min number in array [2,3,5,0,11,5,2]

def min_number(numbers):
    min_num = numbers[0]
    for i in range(len(numbers)):  
        if numbers[i] <  min_num :
            min_num = numbers[i]  
    return min_num
number = [2, 3, 5, 0, 11, 5, 2]
result = min_number(number)
print(result)

# # # EX5.Create function to count of number 5 in array [2,3,5,0,11,5,2]

def count_fives(numbers):
    count = 0
    for i in range(len(numbers)):
        if numbers[i] == 5:
            count += 1
    return count
numbers = [2, 3, 5, 0, 11, 5, 2]
result = count_fives(numbers)
print(result)


# # EX6.Create function to count positive number in array [-1,11,2,0,-1,4]

def count_positive(numbers):
    count = 0
    for i in range(len(numbers)):
        if numbers[i] > 0:
            count += 1
    return count
numbers = [-1,11,2,0,-1,4]
result = count_positive(numbers)
print(result)
 

# # EX7.Create function to count negative number in array [-1,11,2,0,-1,4]

def count_positive(numbers):
    count = 0
    for i in range(len(numbers)):
        if numbers[i] < 0:
            count += 1
    return count
numbers = [-1,11,2,0,-1,4]
result = count_positive(numbers)
print(result)

# EX8.Create function to sum total of price 
# products = [
#     {"name": "Apple", "price": 20},
#     {"name": "Orange", "price": 24},
# ]
def sum_total_price(products):
    total = 0
    for product in products:
        total += product["price"]
    return total
products = [
    {"name": "Apple", "price": 20},
    {"name": "Orange", "price": 24},
]
total = sum_total_price(products)
print("Sum total of price:", total)


# EX9.Create function to find average of price
# products = [
#     {"name": "Apple", "price": 20},
#     {"name": "Orange", "price": 24},
# ]
def sum_total_price(products):
    total = 0
    for product in products:
        total += product["price"]
    return total
def average_price(products):
    total_price = sum_total_price(products)
    number_of_products = len(products)
    if number_of_products == 0:
        return 0  
    return total_price / number_of_products
products = [
    {"name": "Apple", "price": 20},
    {"name": "Orange", "price": 24},
]
total = sum_total_price(products)
print("Sum total of price:", total)
average = average_price(products)
print("Average price:", average)

# # EX10.Show product name that has maximum price

# products = [
#     {"name": "Apple", "price": 20},
#     {"name": "Orange", "price": 24},
# ]
def sum_total_price(products):
    total = 0
    for product in products:
        total += product["price"]
    return total

def product_with_max_price(products):
    if not products:
        return None 
    max_product = products[0]
    for product in products:
        if product["price"] > max_product["price"]:
            max_product = product
    return max_product
products = [
    {"name": "Apple", "price": 20},
    {"name": "Orange", "price": 24},
]
total = sum_total_price(products)
print("Sum total of price:", total)
max_product = product_with_max_price(products)
if max_product:
    print("Product with maximum price:", max_product["name"], "with price", max_product["price"])
else:
    print("No products available.")





