# RecDescentParser
A simple recursive descent parser for validating regular expressions in python. Code for the lexer was provided, and I coded the parsing part.

The functions and procedures for this parser follow the below non-terminal grammar rules which are in Extended Backus-Naur Form.
<relop> ::= < | > | <= | >= | = | != | not          
<exp> ::= <term> { and <term> | or <term> }
<term> ::= int dashop int | <relop>int | (<exp>)

This program takes a single-line expression as input. The lexer tokenizes this expression and the parser
parses the tokens to determine if the input expression is valid or not, according to the grammar rules specified above.
The parser includes a function for each non-terminal symbol above except for relop, which did not require its own procedure.
The functions, 'term' and 'expression', increment through the expression one token at a time. They use recursive descent 
to determine if the input follows the patterns of the non-terminal symbols specified by the grammar rules.
