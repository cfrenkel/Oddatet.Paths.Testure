import logging

good_line = 0
bad_line = 0
with open("data/sample.csv") as f, open("data/sample1.csv", "w") as w:
    # w.write("frameNum,x,y,objectNum,size,sequenceNum,TBD,TBD,TBD,filename,start,path time,delta time,TBD\n")
    for line in f:
        l = line.replace(', ', ',').split(',')
        new = (','.join(l))
        if (len(l) == 14):
            w.write(new)
            good_line += 1
        else:
            bad_line += 1
            logging.info("bad line")

print(good_line)
print(bad_line)
