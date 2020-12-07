import sys
import collections
import csv

def main (csv_file):
    # Open file and list values
    with open (csv_file, 'r') as _file:
        _list = [r for r in csv.DictReader(_file)]
        
        ## OUTPUT:: Total fruits
        print ("\nTotal number of fruit: %d\n" % (len(_list)))

        # Get fruit names for collection and sort (desc)
        fruit_names = [ x['fruit'] for x in _list ]
        fruit_types = collections.Counter(fruit_names)
        
        ## OUTPUT:: Types of fruit
        print ("Types of fruit: %d\n" % (len(fruit_types)))
        # Sort fruit collection (desc) 
        fruit_sorted = sorted(fruit_types.items(),key=lambda x: x[1],reverse=True)
        ## OUTPUT:: Types of fruit & total of each
        print ("The number of each fruit by type:")
        for f in fruit_sorted:
            print ("%s : %d" % (f[0],f[1]))

        print ("\nFruit characteristics:")
        index = 0
        # Loop groups by type
        while index < len(fruit_types.keys()):
            char_list = []
            # Get & filter fruit characteristics
            # note: You may not want to use list() --not the proper way
            for i in _list:
                if list(fruit_types.keys())[index] in list(i.values()):
                    char_list.extend([i['characteristic1'].strip(),i['characteristic2'].strip()])

            ## OUTPUT: fruit count, fruit name, and characteristics (no dups)
            fruit_char = ', '.join(collections.Counter(char_list).keys())
            print ("%d %s : %s" % (list(fruit_types.values())[index], list(fruit_types.keys())[index], fruit_char))
            index +=1
        
        threshold_days = 3
        fruit_overThreshold = []
        print ("\nFruits over %d days old:" % (threshold_days))
        # Get & filter fruits over 3 days old 
        for n in _list:
            if int(n['days']) > threshold_days:
                fruit_overThreshold.append(n['fruit'])
        overThreshold_List = collections.Counter(fruit_overThreshold)
    
        ## OUTPUT: One sentence summary of total fruits above threshold
        total_overThreshold_head =  ', '.join(['{0} {1}'.format(v, k) for k,v in overThreshold_List.items()][:-1])
        total_overThreshold_tail = str(['{0} {1}'.format(v, k) for k,v in overThreshold_List.items()][-1])
        print ("%s and %s are over %d days old \n" % (total_overThreshold_head, total_overThreshold_tail, threshold_days))

# Inline param error handling
try:
    if len(sys.argv) < 2:
        print ("ERROR: Missing CSV file parameter.\n")
    elif len(sys.argv) > 2:
        print ("ERROR: Please make sure to use a single CSV file as a parameter.\n")
    elif sys.argv[1][-4:] != ".csv":
        print ("ERROR: Unable to process file. Make sure to use CSV files only.\n")
    else:
        main(sys.argv[1])
except Exception as e:
    print (e)
