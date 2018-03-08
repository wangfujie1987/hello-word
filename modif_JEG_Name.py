# 此程序可根据照片的拍摄时间来修改照片的文件名
import os
import exifread
#
#
# def getExif(filename):
#     FIELD = 'EXIF DateTimeOriginal'
#     fd = open(filename, 'rb')
#     tags = exifread.process_file(fd)
#     fd.close()
#     if FIELD in tags:
#         new_name = str(tags[FIELD]).replace(':', '').replace(' ', '_') + os.path.splitext(filename)[1]
#         tot = 1
#         while os.path.exists(new_name):
#             new_name = str(tags[FIELD]).replace(':', '').replace(' ', '_') + '_' + str(tot) + \
#                        os.path.splitext(filename)[1]
#             tot += 1
#         new_name2 = new_name.split(".")[0] + '__' + filename
#         print(new_name2)
#         os.rename(filename, new_name2)
#     else:
#         print('No {} found'.format(FIELD))
#
#
# for filename in os.listdir('F:\modify_JPG_Name'):
#     # if os.path.isfile(filename):
#     #     getExif(filename)
#     print(filename)

#打开文件，并获取对应的拍摄日期
# fd = open('F:\modify_JPG_Name\\551.JPG', 'rb')
# tags = exifread.process_file(fd)
# FIELD = 'EXIF DateTimeOriginal'
# fd.close()
# newname=tags#获取拍摄日期
# print(tags)
# #处理文件名
# print(tags)
# print(newname)
# newname1=str(newname).replace(":",'').replace(" ","_")
# print(newname1)
# test=os.path.splitext('F:\modify_JPG_Name\IMG_9461.JPG')[0]
# print(test)

#完整程序 第一种写法 bug：没考虑重复拍摄日期的问题
# dir1 = 'F:\modify_JPG_Name\\'
# FIELD = 'EXIF DateTimeOriginal'
# for parent, dirnames, filename in os.walk("F:\modify_JPG_Name"):#返回的filename为list类型
#     print(type(filename))  # 修改前
#     for i in filename:
#          try:
#             fd = open(dir1 + i, 'rb')
#             tags = exifread.process_file(fd)
#             fd.close()
#             tagesnew = str(tags[FIELD]).replace(':', '').replace(' ', '_')  # 获取拍摄时间，并处理格式
#             tot = 1
#             os.renames(dir1 + i,dir1+tagesnew+'.JPG')#修改文件名，新的文件名：拍摄时间.jpg
#          except:
#             continue#如果有异常，则继续（非jpg文件会出现异常）
#     print(filename)  # 修改后


# 完整程序 第二种写法 考虑重复拍摄日期
dir1 = 'F:\modify_JPG_Name\\'
FIELD = 'EXIF DateTimeOriginal'
for filename in os.listdir('F:\modify_JPG_Name'):  # 返回的filename为str类型
    try:
        fd = open(dir1 + filename, 'rb')
        tags = exifread.process_file(fd)
        fd.close()
        tagesnew = str(tags[FIELD]).replace(':', '').replace(' ', '_') + os.path.splitext(filename)[
            1]  # 获取拍摄时间，并处理格式,os.path.splitext用来分离文件名和扩展名
        tot = 1
        # print(os.path.exists(dir1 + tagesnew))
        if FIELD in tags:#存在拍摄日期的照片才会修改
         while os.path.exists(dir1 + tagesnew):
            tagesnew = str(tags[FIELD]).replace(':', '').replace(' ', '_') + '_' + str(tot) + \
                       os.path.splitext(filename)[1]  # str(tot)#存在相同的拍摄时间
            tot += 1
         os.renames(dir1 + filename, dir1 + tagesnew)  # 修改文件名，新的文件名：拍摄时间_原文件名
         print('%s 文件名修改成功'%filename)
    except:
        print('error')
        continue  # 如果有异常，则继续（非jpg文件会出现异常）
