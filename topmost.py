import wordfreq
import sys
import urllib.request

def main():

    if sys.argv[2].startswith("http"): 
        # if statement for checking if sys.argv[2] is a url or static
        response = urllib.request.urlopen(sys.argv[2])
        lines = response.read().decode("utf8").splitlines()
        inp_file = lines
    else:
        with open(sys.argv[2], encoding='utf-8') as f:
            inp_file = f.readlines()

    list_inp_file = [] 
    for line in inp_file:
        striped_inp_lines = line.strip('\n')
        list_inp_file.append(striped_inp_lines)
        # strips each line and appends each line to a list


    eng_stop = open(sys.argv[1], encoding = 'utf-8')
    # takes the second argument in sys

    list_stop_file = []
    for line in eng_stop:
        striped_stop_lines = line.strip()
        list_stop_file.append(striped_stop_lines)
        # strips each line and appends each line to a list

    eng_stop.close()

    t = wordfreq.tokenize(list_inp_file) # calls the function tokenize, we store it as t to add it to countWords
    c = wordfreq.countWords(t,list_stop_file)# calls the function countWords, we store it as c to add it to printTopMost
    wordfreq.printTopMost(c,int(sys.argv[3]))# calls the function printTopMost



if __name__ == '__main__':
    main()
