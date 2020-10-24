startclang:
	clang -o test.exe main.c
	./test.exe

startgcc:
	gcc -o test main.c
	./test.exe

pg:
	flex main.l
	bison -d main.y
	gcc -o main lex.yy.c main.tab.c
	./main

debug:
	flex main.l
	bison -d --debug main.y
	gcc -o main lex.yy.c main.tab.c

repl-pg:
	./flex main.l
	./bison -d main.y
	clang -o test main.tab.c lex.yy.c

repl-debug:
	./flex main.l
	./bison -d --debug main.y
	clang -o test lex.yy.c main.tab.c