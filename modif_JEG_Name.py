# 此程序可根据照片的拍摄时间来修改照片的文件名
import os
import exifread
import time
import datetime

def get_FileCreateTime(filename):  # 返回文件创建日期和修改日期两者最小值，filename包括为包括绝对名录的文件名
    try:
        timestamp = os.path.getctime(filename)  # timestamp
        date_time = datetime.datetime.fromtimestamp(timestamp)  # 格式化
        timestamp1=os.path.getmtime(filename)#修改时间
        date_time1=datetime.datetime.fromtimestamp(timestamp1)
        if date_time>date_time1:
          return date_time1
        else:
            return date_time
    except:
        name=datetime.datetime.utcnow()#系统日期
        return name

# 完整程序 第二种写法 考虑重复拍摄日期
dir = 'H:\pic'
dir1 = dir + '\\'
FIELD = 'EXIF DateTimeOriginal'
for filename in os.listdir(dir):  # 返回的filename为str类型
    try:
        if os.path.splitext(filename)[1] == '.jpg' or os.path.splitext(filename)[1] == '.JPG':#如果是jpg文件则根据拍摄时间或者创建时间修改
            fd = open(dir1 + filename, 'rb')
            tags = exifread.process_file(fd)
            fd.close()
            if (FIELD in tags) and (str(tags[FIELD])!=""):  # 有拍摄日期的照片修改为拍摄日期
                # print(tags)
                print(tags[FIELD])
                tagesnew = str(tags[FIELD]).replace(':', '').replace(' ', '_') + os.path.splitext(filename)[
                    1]  # 获取拍摄时间，并处理格式,os.path.splitext用来分离文件名和扩展名
                tot = 1
                while os.path.exists(dir1 + tagesnew):
                    tagesnew = str(tags[FIELD]).replace(':', '').replace(' ', '_') + '_' + str(tot) + \
                               os.path.splitext(filename)[1]  # str(tot)#存在相同的拍摄时间
                    tot += 1
                os.renames(dir1 + filename, dir1 + tagesnew)  # 修改文件名，新的文件名：拍摄时间_原文件名
            else:  # 如果无拍摄日期，则修改为文件的创建时间
                newname1 = get_FileCreateTime(dir + '\\' + filename)  # 获取文件的创建时间
                newname = str(newname1).replace(':', '').replace(' ', '_').replace('-','') + os.path.splitext(filename)[
                    1]
                tot = 1
                while os.path.exists(dir1 + newname):
                    newname = str(newname1).replace(':', '').replace(' ', '_') + '_' + str(tot) + \
                              os.path.splitext(filename)[1]  # str(tot)#存在相同的拍摄时间
                    tot += 1
                os.renames(dir1 + filename, dir1 + newname)  # 修改文件名，新的文件名：拍摄时间
        else:#其它文件则根据文件创建时间修改
            newname1 = get_FileCreateTime(dir + '\\' + filename)  # 获取文件的创建时间
            newname = str(newname1).replace(':', '').replace(' ', '_').replace('-','') + os.path.splitext(filename)[
                1]
            tot = 1
            while os.path.exists(dir1 + newname):
                newname = str(newname1).replace(':', '').replace(' ', '_') + '_' + str(tot) + \
                          os.path.splitext(filename)[1]  # str(tot)#存在相同的拍摄时间
                tot += 1
            # print(newname1)
            # print(newname)
            os.renames(dir1 + filename, dir1 + newname)  # 修改文件名，新的文件名：创建时间_原文件名
        print('%s 文件名修改成功' % filename)
    except:
         print('error')
         continue  # 如果有异常，则继续下一张
