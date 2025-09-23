import os
import shutil

def file_copy(source_dir, destination_dir):
    #Check if the source directory and destination directory exist, if they don't raise an Exception Error.
    abs_source_dir = os.path.abspath(source_dir)
    abs_dest_dir = os.path.abspath(destination_dir)
    print(f"Destination Directory: {os.path.basename(abs_dest_dir)}")
    if not os.path.exists(abs_source_dir):
        raise Exception("Source Directory doesn't exist.")
    if os.path.isfile(abs_dest_dir):
        raise Exception("Destination is a file")
    if os.path.exists(abs_dest_dir):
        shutil.rmtree(abs_dest_dir)
        print(f"Deleting directory: {abs_dest_dir}")
    os.mkdir(abs_dest_dir, mode=0o777)
    print(f"Creating Directory: {abs_dest_dir}")
    file_copy_helper(abs_source_dir,abs_dest_dir)
    

def file_copy_helper(abs_source_dir, abs_dest_dir):
    print(f"Collecting contents of {abs_source_dir} to copy to {abs_dest_dir}:")
    source_list = os.listdir(abs_source_dir) #creates a list of the files in the source directory
    for file in source_list:
        abs_file_source = os.path.join(abs_source_dir,file)
        abs_file_dest = os.path.join(abs_dest_dir,file)
        
        if os.path.isfile(abs_file_source):   
            shutil.copy(abs_file_source,abs_file_dest)
            print(f"Copying file from {abs_file_source} to {abs_file_dest}")
        if os.path.isdir(abs_file_source):
            print(f"Creating Sub-Directory: {abs_file_dest}")
            os.mkdir(abs_file_dest, mode=0o777)
            print(f"Recursively calling function on :{abs_file_dest}")
            file_copy_helper(abs_file_source,abs_file_dest)
    #os.path.exsits(path) returns a boolean if the directory exists or not.
    #os.listdir(path='.') returns a unordered list containg the names of the entries in the directory given by the path.
    #os.path.join(path, /., *paths) joins one or more path segments intelligently.  Returns the value of the concatenation of path and all member paths* Ex: os.path.join(C:, foo) returns C:foo
    #os.path.isfile(path) returns a boolean if the path is an existing regular file.
    #os.path.isdir(path) returns a boolean if the path is an existing directory
    #os.mkdir(path, mode=0o777, *, dor_fd=None) creates a directory named (path) with numeric mode (mode)

    #shutil.copy(src, dst, *, follow_symlinks = True) Copies the file (src) to the file or directory (dst).  (src) & (dst) should be path-like objects or strings.
    #shutil.rmtree(path, ignore_errors=False, onerror=None, *, onexc=None, dir_fd=None) Deletes an entire directory tree:(path) must point to a directory.