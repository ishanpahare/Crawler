import os

##creating directories for each separate site we crawl
def create_project_dir(directory):
    if not os.path.exists(directory):
        print("Creating Directory: "+directory)
        os.makedirs(directory)

##create_project_dir('test_dir')        

##creating queued and crawled files

def create_data_files(project_name,base_url):
    queue=project_name+'/queue.txt'
    crawled=project_name+'/crawled.txt'
    if not os.path.isfile(queue):
        write_file(queue,base_url)
    if not os.path.isfile(crawled):
        write_file(crawled,'') 

def write_file(path,data):
    f=open(path,'w')
    f.write(data)
    f.close()        

##add data to an existing file
def append_to_file(path,data):
    with open(path,'a') as file:
        file.write(data+ '\n')

##deleting file contents
def delete_file_contents(path):
    with open(path,'w'):
        pass

##read a file and convert each line to set items
def file_to_set(file_name):
    results=set()
    with open(file_name,'rt') as f:
        for line in f:
            results.add(line.replace('\n',''))
    return results

##iterate through the set and each item will be a new line in the file
def set_to_file(links,file):
    delete_file_contents(file)
    for link in sorted(links):
        append_to_file(file,link)
