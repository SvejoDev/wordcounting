import wordfreq
import sys
import urllib.request

def main():

    inp_file = open(sys.argv[2], encoding='utf-8')

    for line in inp_file:
        striped_inp_lines = line.strip('\n')

    inp_file.close()

    eng_stop = open(sys.argv[1], encoding = 'utf-8')

    for line in eng_stop:
        striped_stop_lines = line.strip('\n')

    eng_stop.close()

    t = wordfreq.tokenize(striped_inp_lines)
    c = wordfreq.countWords(t,striped_stop_lines)
    wordfreq.printTopMost(c,int(sys.argv[3]))



if __name__ == '__main__':
    main()
