import pandas as pd

data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}

frame = pd.DataFrame(data)

print(frame)


frame_1 = pd.DataFrame(data, columns=['year', 'state', 'pop', 'debt'], index=['one', 'two', 'three', 'four', 'five'])
# frame_1 = pd.DataFrame(data, columns=['year', 'state', 'pop', 'debt'])
print(frame_1)

# Phương Án 1
# import pandas as pd
# data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
#         'year': [2000, 2001, 2002, 2001, 2002],
#         'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
# df = pd.DataFrame(data)
# df['debt'] = ['one', 'two', 'three', 'four', 'five']
# print(df)

# Phương Án 2
# import pandas as pd
# data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
#         'year': [2000, 2001, 2002, 2001, 2002],
#         'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
# debt = ['one', 'two', 'three', 'four', 'five']

# df = pd.DataFrame(data, columns=['year', 'state', 'pop', 'debt'])
# df['debt'] = debt
# print(df)


# Chọn một cột trong DataFrame
print(frame_1['year'])
# Chọn nhiều cột cùng lúc
print(frame_1[['year', 'pop']])
# Chọn một hàng trong DataFrame
frame_1.loc["three"]
# Chọn nhiều hàng trong DataFrame
frame_1.loc[["three", "two"]]

# #Gắn 1 giá trị cho tất cả
# frame['year'] = 1996
# print(frame)
# #Bằng một list có độ dài bằng số dòng
# frame['year'] = [1996, 1997, 1998, 1999, 2000]
# print(frame)
# #Bằng một series
# frame['year'] = pd.Series([1996, 1998, 2001], index=[0, 1, 3])
# print(frame)

# #change index
# frame_1.index = ['a', 'b', 'c', 'd', 'e']
# print(frame_1)



