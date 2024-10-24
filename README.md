# What is the SCC?
Simple C compiler implemented by Python.


# What is compiler?
Compiler is a program that translate a language to another, in this case, convert source code written in C to Assembly.


<b>Follow from source code to executable file:</b>

Source code (text) -[Pre-processor]-> Pre-processed source code -[Compiler]-> Assembly code -[Assembler]-> Object file (binary) -[Linker]-> Executable (binary)

# Design
## Compiler passes
Source Code goes through 4 passes to be converted into assembly file, shown as follow:

program.c -[Lexer]-> list of tokens -[Parser]-> abstract syntax tree (AST) -[Assembly Generation]-> Assembly -[Code Emission]-> program.s (assembly file).

**Description**:
- Lexer pass: breaks up the source code into a list of tokens.
- Parser pass: converts a list of tokens in to AST -> easy to traverse and analyze.
- Assembly Generation pass: converts AST into assembly and organize in a structure required by the compiler.
- Code Emission pass: writes those assembly strucutre to file.


## Compiler driver interface:
Currently support the following flags.

--lex
--parse
--codegen





