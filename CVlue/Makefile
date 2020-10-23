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