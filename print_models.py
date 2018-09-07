#!/usr/bin/python
unprint_list = ['Microsoft', 'Macbook', 'Adobe', 'Autodesk']
complete_fnames = []


def print_model(unprint_fn, completed_fnames):
    while unprint_list:
        current_fn = unprint_list.pop()
        print "Printing file is: ", current_fn
        complete_fnames.append(current_fn)


def dis_print(complete_fnames):
    for complete_fn in complete_fnames:
        print complete_fn

print_model(unprint_list,complete_fnames)
print "\n"
dis_print(complete_fnames)