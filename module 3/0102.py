# # # #1
# # # is_next = None
# # # num = int(input("Enter the number of points: "))
# # # if num >= 83:
# # #     is_next = True
# # # else:
# # #     is_next = False
    
# # # #2
# # # is_active = input("Is the user active? ")
# # # is_admin = input("Is the user administrator? ")
# # # is_permission = input("Does the user have access? ")

# # # is_admin = bool(is_admin)
# # # is_active = bool(is_active)
# # # is_permission = bool(is_permission)

# # # access = True if is_admin or is_active and is_permission else False

# # # #3

# # # work_experience = int(input("Enter your full work experience in years: "))


# # # if 1 < work_experience <= 5:
# # #     developer_type = "Middle"
# # # elif work_experience <= 1:
# # #     developer_type = "Junior"
# # # else: 
# # #     developer_type = "Senior"

# # # #4
    
# # # num = int(input("Enter a number: "))

# # # if num > 0:
# # #     if num % 2 == 1:
# # #         result = "Positive odd number"
# # #     else: 
# # #         result = "Positive even number"
# # # elif num < 0:
# # #     result = "Negative number"
# # # else:
# # #     result = "It is zero"

# # #5

# # import math

# # a = int(input("Enter coefficient a: "))
# # b = int(input("Enter coefficient b: "))
# # c = int(input("Enter coefficient c: "))

# # D = b ** 2 - 4 * a * c

# # if D > 0:
# #     x1 = (-b + math.sqrt(D)) / (2 * a)
# #     x2 = (-b - math.sqrt(D)) / (2 * a)
# # elif D == 0:
# #     D = b2 - 4 * a * c
# # else:
# #      print("Рівняння не має дійсних коренів")
    
# # #7
     
# # num = int(input("Enter the integer (0 to 100): "))
# # sum = 0

# # while num > 0:
# #     sum += num
# #     num -= 1
    
# # print(sum)

# # #8

# # message = "Never argue with stupid people, they will drag you down to their level and then beat you with experience."
# # search = "r"
# # result = 0
# # for char in message:
# #     if char == search:
# #         result += 1
    
        


#12
pool = 1000
quantity = int(input("Enter the number of mailings: "))
try:
    chunk = pool // quantity
    print("succesful")
except:
    print('Divide by zero completed!')
        

# message = "Never argue with stupid people, they will drag you down to their level and then beat you with experience."
# # search = "r"
# # result = 0
# # for char in message:
# #     if char == "r":
# #        result +1
    

# # #9
    
# sum = 0
# while True:
#     num = int(input("Enter integer (0 for output): "))
#     if num >100:
#         break
#     for i in range(num + 1):
#         sum = sum + i
#         print(sum)


# #10
        

# sum = 0
# while True:
#     num = int(input("Enter integer (0 for output): "))
#     if num == 0:
#         break
#     for i in range(num + 1):
#         if i % 2 == 0:
#             sum = sum + i

# #11
            
# message = input("Enter a message: ")
# offset = int(input("Enter the offset: "))
# encoded_message = ""

# for char in message:
#     if char.isalpha():
#         base = 'a' if char.islower() else 'A'
#         pos = ord(char) - ord(base)
#         new_pos = (pos + offset) % 26
#         new_char = chr(new_pos + ord(base))
# #         encoded_message += new_char
# #     else:
# #         encoded_message += char


# message = input("Enter your message >>> ")
# offset = int(input("Enter offset >>> "))
# encoded_message = ""
# for ch in message:
#     pos = ord(ch) - ord('a')
#     pos = (pos + offset) % 26
#     new_char = chr(pos + ord("a"))
#     encoded_message += new_char
# print(encoded_message)
        
# # for ch in message:
# #     if 'a' <= ch <= 'z':
# #         pos = ord(ch) - ord('a')
# #         pos = (pos + offset) % 26
# #         new_char = chr(pos + ord("a"))
#         encoded_message += new_char
        
    
        