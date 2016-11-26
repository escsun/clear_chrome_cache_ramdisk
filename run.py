import os
import time
import psutil
import schedule

local_drive = "E:\\"
path_to_chrome_cache = "E:\\Chrome\\Default\\Cache\\"
percent_size = 65
size_in_kb = 768
check_schedule_in_minutes = 10
# counters
total_deleted_files_size = 0
total_deleted_files_count = 0


def job():
    """
    Delete chrome cache from ram disk, when percent equal or higher than percent_size
    """
    global total_deleted_files_count, total_deleted_files_size
    disk = psutil.disk_usage(local_drive)  # path to disk
    if disk.percent >= percent_size:  # do remove files when percent usage equal 90 or higher
        path = path_to_chrome_cache  # full path to google cache
        files = [x for x in os.listdir(path)]  # generate files list
        size_to_delete = size_in_kb * 1024  # convert KBytes to Bytes
        files_to_ignore = ['index', 'data_0', 'data_1', 'data_2', 'data_3']  # Files to ignore

        for file in files:
            if os.path.getsize(path + file) > size_to_delete and file not in files_to_ignore:
                print("File: {file} size: {sz} was deleted!".format(file=file, sz=os.path.getsize(path + file)))
                total_deleted_files_count += 1
                total_deleted_files_size += os.path.getsize(path + file) / 1024 / 1024
                os.remove(path + file)
        print("Files deleted: %d" % total_deleted_files_count)
        print("Total size of deleted files: %.2f mb" % total_deleted_files_size)
    else:
        print("Disk usage {percent}".format(percent=disk.percent))

schedule.every(check_schedule_in_minutes).minutes.do(job)

while True:
    schedule.run_pending()
    time_to_update = int(schedule.idle_seconds())
    if time_to_update % 60 == 0:
        print("Time to update in minutes: %d" % (time_to_update / 60))
    time.sleep(1)
