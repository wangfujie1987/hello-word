# 此程序可根据照片的拍摄时间来修改照片的文件名
import os
import exifread
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
