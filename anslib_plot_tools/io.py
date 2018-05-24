import os

def skip_comments(lines, nline):
    " Get the next line from a set of commented lines "

    success = 0

    # get the first uncommented line
    for line in lines[nline:]:
        line = line.split('#', 1)[0]
        line = line.rstrip()
        nline = nline + 1
        if line == '':
            continue
        success = 1
        return line, nline

    if (success == 0):
        return None, -1

def append_number_to_name(filename):

    candid = filename.rsplit('.',2)[-2]

    ## candid is not a number
    if( not candid.isdigit() ):
        #print 'bad %s %s' % (candid, candid[-1])
        all_str = filename.rsplit('.',1)
        filename_out = "%s.0.%s" % (all_str[0], all_str[1])
        return append_number_to_name(filename_out)
    
   ## the file already exists     
    if os.path.isfile(filename):
        # print 'bad %s exists' % candid
        all_str = filename.rsplit('.',2)
        filename_out = "%s.%d.%s" % (all_str[0], int(all_str[1])+1, all_str[2])
        return append_number_to_name(filename_out)

    ## everything is fine
    return filename
