import re
from functools import *
#Thomas Kestler


class recDescent:
    # begin section of code provided by the professor of my CS530 class
    # relational (unary) operators (prefix)
    
    relop = ['<', '>', '<=', '>=', '=', '!=', 'not']
    
    #def testfunc(self):
        #print(relop[1])

    # binary operators (infix)
    dashop = ['-', '–']
    logicop = ['and', 'or']

    # tokens for manipulating priority
    priopen = '('
    priclose = ')'

    # constructor to initialize and set class level variables
    def __init__(self, expr = ""):

        # string to be parsed
        self.expr = expr

        # tokens from lexer tokenization of the expression
        self.tokens = []

    # lexer - tokenize the expression into a list of tokens
    # the tokens are stored in an list which can be accessed by self.tokens
    # do not edit any piece of code in this function
    def lex(self):
        self.tokens = re.findall("[-\(\)=]|[!<>]=|[<>]|\w+|[^ +]\W+", self.expr)
        # filter out the possible spaces in the elements
        self.tokens = list(filter((lambda x: len(x)), 
                           list(map((lambda x: x.strip().lower()), self.tokens))))    
						   
						   
	#end code provided by CS530 professor. the rest of the code below is my own.
    
    # parser - determine if the input expression is valid or not
    currToken=0#keeps track of current index of the expression
    terminat = False#this tells the below functions to stop if the index is about to go out of bounds
    

    

    # validate() function will return True if the expression is valid, False otherwise 
    
    def validate(self):
        
        self.lex()
        
        cExp = self.tokens#variable which keeps track of all the tokens
        
        global currToken#this is done in every function so the value of this is retained across the whole program
        global terminat
        
        currToken=0
        terminat=False
        while currToken < len(cExp):
            #start parsing
            if(terminat==True):
                return False
            if self.exp(cExp)==True:#move on to next token if valid expression is found
                currToken+=1  
                
            else:
                return False #return false if the exp was not valid
        return True
        
        
   

        
    def exp(self,x):#exp non terminal procedure. <exp> ::= <term> { and <term> | or <term> }
        #handles expressions of terms/etc
        global currToken
        global terminat
        
        if(terminat==True):#if index out of bound issue found, return invalid
            return False
        
        if self.term(x)==True:
            
            if((self.increment(x))==False):
                #if term returned true, this would mean we have reached the end of the expression, and that is valid
                
                if(currToken<len(x) and (x[currToken]=='and' or x[currToken]=='or' or (x[currToken] in recDescent.relop))):
                    
                    return False#if the last token is a relop or a logicop, expression is invalid.
                 
                return True
           
            if(x[currToken]=='and' or x[currToken]=='or'):#check for logic operators
                    
                if((self.increment(x))==False):
                        
                    return False
                if(self.term(x)==True):#look for next term
                        
                    return True
                else:#there is a strange issue here where this gets reached even though the previous token was not a logic operator. the extra condition here fixes that.
                        
                    if(x[currToken-1]!='and' or x[currToken-1]!='or'):
                            
                        return True
                    return False
            else:#if expression is just a single term, valid. this deals with nested ending parentheses
                    
                return True
            

        else:
            #if first term is invalid
            return False
        
    

    #procedure for term nonterminal: <term> ::= int dashop int | <relop>int | (<exp>)
    def term(self,x):
        #check if integer. if not, check for left parenthesis '('. if not, invalid
        
        global currToken
        global terminat
        
        if(terminat==True):
            return False
        
        
        if x[currToken].isdigit():#checking for integer
            if((self.increment(x))==False):
                return False
            if(x[currToken]=='-'):#see if int is followed by dash
                if((self.increment(x))==False):
                    return False
                if(x[currToken].isdigit()):
                    
                    return True #term can be int-int, so this is valid
            return False #term cannot be single int, so make invalid
        elif (x[currToken] in recDescent.relop):#see if term is relop followed by int
            
            if((self.increment(x))==False):
                return False
            if(x[currToken].isdigit()):
                
                return True #relop int found, valid term
        elif x[currToken] == '(':# if parenthesis found, deal with expression inside
            
            if((self.increment(x))==False):
                return False
            if(self.exp(x)==True):
                if((self.increment(x))==False):
                    return False
                if(x[currToken]==')'):
                    
                    return True
                
            
            return True
       
        if(len(x)-currToken>=2 and x[currToken==')']):#this is the other way ending parentheses are handled
            
            currToken-=1
            return True
        return False#if opening parenthesis or int not found, term is not valid
        
        
    def increment(self,a):#this method will increment currToken if it is still in the range of the length of x
        #a=x, the full expression.
        global currToken
        
        global terminat
        
        if(currToken<len(a)-1):
            currToken+=1
            
            return True
        else:
            
            terminat = True
            return False
            

    # parsing procedures corresponding to the grammar rules - follow Figure 5.17
  


