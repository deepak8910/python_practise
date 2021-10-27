import subprocess
import json
import argparse
import os
def parse_cli_arguments():
    """
    Parses CLI arguments
    """
    parser = argparse.ArgumentParser(description='Converts directory files list to json file')
    parser.add_argument('-p', '--path', default= '.', 
                        help='path for the directory (default is present directory)')
    parser.add_argument('-t', '--target-file', default= 'target.json', 
                        help='name of the target json file (default is target.json)')
    
    args = parser.parse_args()
    return args

def write_to_json(args):
    """
    Takes the arguments and writes output to json file
    """
    if not os.path.exists(args.path):
        print("Path: %r does not exists" % args.path)
        return None
    output = subprocess.check_output(['ls', '-l', args.path], encoding='utf-8')
    output = output.split("\n")
    output.remove(output[0])
    output.pop()
    dictionary = {}
    for line in output:
        line = line.split()
        filename = line[-1]
        dictionary[filename] = {}
        dictionary[filename]["permissions"] = line[0]
        dictionary[filename]["links"]       = line[1]
        dictionary[filename]["user"]        = line[2]
        dictionary[filename]["group"]       = line[3]
        dictionary[filename]["size"]        = line[4]
        dictionary[filename]["date"]        = line[5] + " " + line[6] + " " + line[7]

    with open(args.target_file,"w") as fp:
        json.dump(dictionary,fp)

args = parse_cli_arguments()
write_to_json(args)
