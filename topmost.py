import wordfreq
import sys
import urllib.request

response = urllib.request.urlopen(sys.argv[2])
lines = response.read().decode("utf8").splitlines()

def main():

    if sys.argv[2].startswith("http"):
        inp_file = lines
    else:
        inp_file = open(sys.argv[2], encoding='utf-8')
        inp_file.close()

    list_inp_file = [] 
    for line in inp_file:
        striped_inp_lines = line.strip('\n')
        list_inp_file.append(striped_inp_lines)


    eng_stop = open(sys.argv[1], encoding = 'utf-8')

    list_stop_file = []
    for line in eng_stop:
        striped_stop_lines = line.strip()
        list_stop_file.append(striped_stop_lines)

    eng_stop.close()

    t = wordfreq.tokenize(list_inp_file)
    c = wordfreq.countWords(t,list_stop_file)
    wordfreq.printTopMost(c,int(sys.argv[3]))



if __name__ == '__main__':
    main()
