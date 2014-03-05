# parse RTF file and output result to file
from rtf_parser import rtf_parser
import time
import pprint

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print "No input filename"
        sys.exit(1)
    
    fn = sys.argv[1]
    print "Input file =", fn
    
    # read file data
    f = open(fn, "rU")
    data = f.read()
    
    # RTF last byte is \x00, remove it
    if data[-1] == '\x00':
        data = data[:-1]
    
    print "data length = %d" % len(data)
    
    '''
    # Give the lexer some input
    lex.input(data)
    #print data
    
    # Tokenize
    print "token:"
    while 1:
        tok = lex.token()
        if not tok: break      # No more input
        print tok
    '''
        
    #print data
    print "parse..."
    t1 = time.clock()
    res = rtf_parser.parse(data)
    t2 = time.clock()
    print "parse ok"
        
    print "formating result text..."
    res_text = pprint.pformat(res)
    
    #print
    #print res_text
    fo = open("result.txt", "wt")
    print >> fo, res_text
    print "time = %f" % (t2 - t1)
