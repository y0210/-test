import time
import subprocess

bat_file_install = "C:/Users/xu_peng/Desktop/yunzhijia/安装.bat"
bat_file_start = "C:/Users/xu_peng/Desktop/yunzhijia/打卡.bat"


def install_apk():
    output = subprocess.check_output(bat_file_install, shell=True)

def clock_in():
    output = subprocess.check_output(bat_file_start, shell=True)

def up():
    year, mounth, day = input('输入年，月，日，“/”符号隔开:').split('/')
    starttime = year + '-' + mounth + '-' + day + " " + '09:10:00'
    return time.strptime(starttime,"%Y-%m-%d %H:%M:%S")

def down():
    year, mounth, day = input('输入年，月，日，“/”符号隔开:').split('/')
    starttime = year + '-' + mounth + '-' + day + " " + '18:30:00'
    return time.strptime(starttime,"%Y-%m-%d %H:%M:%S")

current_time = time.localtime()

if __name__  == '__main__':
    choice = input('请选择上班（0）或者下班（1）:')
    if choice == '1' :
        start_time = down()
        time_difference = time.mktime(start_time) - time.mktime(current_time)
        wait_time = time_difference/60/60
        if time_difference > 0:
            print('等待' + '%.2f'%wait_time + '小时后执行')
            time.sleep(time_difference)
            # install_apk()
            clock_in()
    else :
        start_time = up()
        time_difference = time.mktime(start_time) - time.mktime(current_time)

        wait_time = time_difference/60/60
        if time_difference > 0:
            print('等待' + '%.2f'%wait_time + '小时后执行')
            time.sleep(time_difference)
            # install_apk()
            clock_in()