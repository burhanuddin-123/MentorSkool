from loader import Loader

l = Loader("products.csv")
l.load("localhost","root","","Mentorskool","Product")


# import pandas
# #
# data = pandas.read_csv("products.csv")
# #
# list_data = list(data.columns)
# list_datatypes = list(data.dtypes)
# proper_datatype = []
# for value in list_datatypes:
#     if value == "object":
#         proper_datatype.append("VARCHAR")
#     elif value == "int64":
#         proper_datatype.append("INT")
#     else:
#         proper_datatype.append("NUMBER")
# print(proper_datatype)
# # for value in list_datatypes:
# #     if
# # print(list_data)
# # print(list_datatypes)
# # i = 0
# # for i in range(len(list_data)):
# #     if i==0:
# #         print(list_data[i])
# #         print(list_datatypes[i])
# #         i = i+1
