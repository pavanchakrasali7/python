# # ele=[1,2,3,4,5,6]
# # it=iter(ele)
# # for i in it:
# #     print(i)
# from itertools import count
# itertor=count(1)
# for i in range(5):
#     print(next(itertor))

# class topten:
#     def __init__(self):
#         self.num=1
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.num<=10:
#             val=self.num
#             self.num+=1
#             return val
#         else:
#             raise StopIteration
# values=topten()
# for i in values:
#     print(i)


# class ten:
#     def __init__(self):
#         self.num=1
#     def __iter__(self):
#         return self
#     def __next__(self):

#         if self.num<=10:
#             val=self.num
#             self.num+=1
#             return val
#         else:
#             raise StopIteration
        
# values=ten()
# for i in values:
#     print(i)

# class MyNumbers:
#   def __iter__(self):
#     self.a = 1
#     return self

#   def __next__(self):
#     if self.a<=100:
#         x = self.a
#         self.a += 1
#         return x
#     else:
#         raise StopIteration
# values=MyNumbers ()
# for i in values:
    
# 	print
# name="python"
# if name in["java"or"html"or"css"]:
#     print("sucsees")
# else:
#     print("failed")
