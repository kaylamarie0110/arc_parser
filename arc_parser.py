import os

uri_counters = {}

def arc_parse(file_name):
    is_meta_data = 1
    num_char_to_ignore = 0
    curr_char_count = 0

    with open(file_name, 'r') as f:
        for line in f:
            if is_meta_data:
                is_meta_data = 0
                meta_data = line.split(" ")
                uri = meta_data[0]
                print uri
                print "======================="
                num_char_to_ignore = int(meta_data[-1])
                try:
                    uri_counters[uri] = uri_counters[uri] + 1
                except:
                    uri_counters[uri] = 1
            else:
                curr_char_count = curr_char_count + len(line)
                if curr_char_count == num_char_to_ignore + 1:
                    curr_char_count = 0
                    is_meta_data = 1

path = 'C:/_Kayla/phd_research/data/unzipped'
for dir_entry in os.listdir(path):
    file_name = path + '/' + dir_entry
    if dir_entry[-4:] == '.arc':
        arc_parse(file_name)
    else:
        print "Not an arc file"

print uri_counters
