ion: ion.y ion.l
	bison -d ion.y
	flex ion.l
	gcc -o ion ion.tab.c lex.yy.c -lm