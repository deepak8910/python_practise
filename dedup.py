import os
import subprocess

def get_files_cksum(dir_path):
    """
    input: directory name
    returns : dictionary of file names with their checksum
    """
    file_cksum_map = {}
    if not os.path.exists(dir_path):
        print("Directory:%r does not exist" % dir_path)
        return None
    for (root,dirs,files) in os.walk(dir_path, topdown=True):
        for file in files:
            filename = root + "/" + file
            cksum = subprocess.check_output(['cksum', filename], encoding='utf-8')
            cksum = cksum.split()
            file_cksum_map[filename] = cksum[0]
    return file_cksum_map


def delete_duplicate(file_cksum_map):

    """
    input : dictionary of file name and its checksum

    """
    cksum_dict = {}
    link_file_list = []
    bytes_saved = 0
    for filename, cksum in file_cksum_map.items():
        if cksum not in cksum_dict.keys():
            cksum_dict[cksum] = filename
        else:
            os.system("rm " + filename)
            print("file : %r got deleted" %filename)
            cmd = "ln -s " + cksum_dict[cksum] + " " + filename
            #print(cmd)
            
            os.system(cmd)
            
            link_file_list.append(filename)
            size = subprocess.check_output(['cksum', cksum_dict[cksum]], encoding='utf-8')
            size = size.split()
            bytes_saved += int(size[1])
    return link_file_list, bytes_saved

from pprint import pprint
file_cksum_map = get_files_cksum("/Users/deepakpulgurle/Documents/test")
pprint(file_cksum_map)
print(delete_duplicate(file_cksum_map))

