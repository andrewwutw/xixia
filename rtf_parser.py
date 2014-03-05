# RTF file grammer declaration file
import ply.lex as lex
import ply.yacc as yacc

tokens = (
    'LEFT_BRACE', 'RIGHT_BRACE',
    'CONTROL_WORD', 'HEX_VALUE_LIST',
    'CONTROL_SYMBOL', 'UNFORMAT_TEXT'
)
t_LEFT_BRACE = "{"
t_RIGHT_BRACE = "}"
t_CONTROL_WORD = r"(\\\*)?\\[a-zA-Z]+[0-9]*\ ?"   # = [\*]\LetterSequence<Delimiter>[one-optinal-space]
t_HEX_VALUE_LIST = r"(\\'[0-9a-f]{2})+"           # = \'xx\'xx...
t_CONTROL_SYMBOL = r"\\[^a-zA-Z]"
t_UNFORMAT_TEXT = r"[^\\\{\}]+"                   # = any vharacter other than \ { }

# Newlines
def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print "Illegal character '%s'" % t.value[0]
    t.lexer.skip(1)

def p_rtf_block(p):
    'rtf_block : LEFT_BRACE CONTROL_WORD rtf_block_data RIGHT_BRACE'
    p[0] = p[1:]
    #print "rtf_block", p[0]

def p_rtf_block_data(p):
    '''rtf_block_data : rtf_block_data rtf_block_elem'''
    #p[0] = p[1] + [p[2]]
    p[0] = p[1]
    p[0] += [p[2]]
    #print "add elem %d" % len(p[1]),

def p_rtf_block_data_empty(p):
    '''rtf_block_data : empty'''
    p[0] = []

def p_empty(p):
    '''empty :'''
    pass
    
def p_rtf_block_elem(p):
    '''rtf_block_elem : UNFORMAT_TEXT
                      | HEX_VALUE_LIST
                      | CONTROL_SYMBOL
                      | CONTROL_WORD
                      | rtf_block'''
    p[0] = p[1]
    #print "line %d pos %d" % (p.lineno(1), p.lexpos(1))
    #print "line %d" % p.lineno(1)
    #print "rtf_block_elem:", p[0]

def p_error(p):
    print "Syntax error at '%s'" % p.value


# Build the lexer
lex.lex()
rtf_parser = yacc.yacc()
