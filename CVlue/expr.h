/*
	Parser header generated by unicc from expr.par.
	DO NOT EDIT THIS FILE MANUALLY, IT WILL GO AWAY!
*/

#ifndef EXPR_H
#define EXPR_H

/* Wide character processing enabled? */
#ifndef UNICC_WCHAR
#define UNICC_WCHAR					0
#endif

/* UTF-8 processing enabled? */
#if !UNICC_WCHAR
#ifndef UNICC_UTF8
#	define UNICC_UTF8				1
#endif
#else
#	ifdef UNICC_UTF8
#	undef UNICC_UTF8
#	endif
#	define UNICC_UTF8				0
#endif

/* UNICC_CHAR is used as character type for internal processing */
#ifndef UNICC_CHAR
#if UNICC_UTF8 || UNICC_WCHAR
#	define UNICC_CHAR				wchar_t
#	define UNICC_CHAR_FORMAT		"%S"
#else
#	define UNICC_CHAR				char
#	define UNICC_CHAR_FORMAT		"%s"
#endif
#endif /* UNICC_CHAR */

/* UNICC_SCHAR defines the character type for semantic action procession */
#ifndef UNICC_SCHAR
#if UNICC_WCHAR
#	define UNICC_SCHAR				wchar_t
#	define UNICC_SCHAR_FORMAT		"%S"
#else
#	define UNICC_SCHAR				char
#	define UNICC_SCHAR_FORMAT		"%s"
#endif
#endif /* UNICC_SCHAR */

/* Boolean */
#ifndef UNICC_BOOLEAN
#define UNICC_BOOLEAN			short
#endif

/* Debug level */
#ifndef UNICC_DEBUG
#define UNICC_DEBUG				0
#endif

/* Stack debug switch */
#ifndef UNICC_STACKDEBUG
#define UNICC_STACKDEBUG		0
#endif

/* Parse error macro */
#ifndef UNICC_PARSE_ERROR
#define UNICC_PARSE_ERROR( pcb ) \
	fprintf( stderr, "line %d, column %d: syntax error on symbol %d, token '" \
		UNICC_SCHAR_FORMAT "'\n", \
	( pcb )->line, ( pcb )->column, pcb->sym, _lexem( pcb ) )
#endif

/* Input buffering clean-up */
#ifndef UNICC_CLEARIN
#define UNICC_CLEARIN( pcb )		_clear_input( pcb )
#endif

/*TODO:*/
#ifndef UNICC_NO_INPUT_BUFFER
#define UNICC_NO_INPUT_BUFFER	0
#endif

/* Memory allocation step size for dynamic stack- and buffer allocation */
#ifndef UNICC_MALLOCSTEP
#define UNICC_MALLOCSTEP		128
#endif

/* Call this when running out of memory during memory allocation */
#ifndef UNICC_OUTOFMEM
#define UNICC_OUTOFMEM( pcb )	fprintf( stderr, \
									"Fatal error, ran out of memory\n" ), \
								exit( 1 )
#endif

/* Static switch */
#ifndef UNICC_STATIC
#define UNICC_STATIC			static
#endif

#ifdef UNICC_PARSER
#undef UNICC_PARSER
#endif
#define UNICC_PARSER			"" "debug"

/* Don't change next three defines below! */
#ifndef UNICC_ERROR
#define UNICC_ERROR				0
#endif
#ifndef UNICC_REDUCE
#define UNICC_REDUCE			1
#endif
#ifndef UNICC_SHIFT
#define UNICC_SHIFT				2
#endif
#ifndef UNICC_SUCCESS
#define UNICC_SUCCESS			4
#endif

/* Error delay after recovery */
#ifndef UNICC_ERROR_DELAY
#define UNICC_ERROR_DELAY		3
#endif

/* Enable/Disable terminal selection in semantic actions */
#ifndef UNICC_SEMANTIC_TERM_SEL
#define UNICC_SEMANTIC_TERM_SEL	0
#endif

/* Value Types */
typedef int _vtype;

/* Typedef for symbol information table */
typedef struct
{
	char*			name;
	char*			emit;
	short			type;
	UNICC_BOOLEAN	lexem;
	UNICC_BOOLEAN	whitespace;
	UNICC_BOOLEAN	greedy;
} _syminfo;

/* Typedef for production information table */
typedef struct
{
	char*	definition;
	char*	emit;
	int		length;
	int		lhs;
} _prodinfo;


/* Abstract Syntax Tree */
typedef struct _AST _ast;

struct _AST
{
	char*			emit;
	UNICC_SCHAR*	token;

	_ast*	parent;
	_ast*	child;
	_ast*	prev;
	_ast*	next;
};

/* Stack Token */
typedef struct
{
	_vtype		value;
	_ast*		node;

	_syminfo*	symbol;

	int					state;
	unsigned int		line;
	unsigned int		column;
} _tok;


/* Parser Control Block */
typedef struct
{
	/* Is this PCB allocated by parser? */
	char				is_internal;

	/* Stack */
	_tok*		stack;
	_tok*		tos;

	/* Stack size */
	unsigned int		stacksize;

	/* Values */
	_vtype		ret;
	_vtype		test;

	/* State */
	int					act;
	int					idx;
	int					lhs;

	/* Lookahead */
	int					sym;
	int					old_sym;
	unsigned int		len;

	/* Input buffering */
	UNICC_SCHAR*		lexem;
	UNICC_CHAR*			buf;
	UNICC_CHAR*			bufend;
	UNICC_CHAR*			bufsize;

	/* Lexical analysis */
	UNICC_CHAR			next;
	UNICC_CHAR			eof;
	UNICC_BOOLEAN		is_eof;

	/* Error handling */
	int					error_delay;
	int					error_count;

	unsigned int		line;
	unsigned int		column;

	/* Abstract Syntax Tree */
	_ast*		ast;

	/* User-defined components */
	

} _pcb;

#endif /* EXPR_H */