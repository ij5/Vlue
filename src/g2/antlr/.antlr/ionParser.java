// Generated from d:\D\jaehee\Project\pl\src\g2\antlr\ion.g4 by ANTLR 4.7.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class ionParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.7.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		DQ=1, SQ=2, COLON=3, NEWLINE=4, TAB=5, COMMA=6, EQUAL=7, IDENTIFIER=8, 
		OTHER=9;
	public static final int
		RULE_root = 0, RULE_body = 1, RULE_elements = 2, RULE_head = 3, RULE_empty = 4, 
		RULE_attr = 5, RULE_attr_equal = 6, RULE_other = 7;
	public static final String[] ruleNames = {
		"root", "body", "elements", "head", "empty", "attr", "attr_equal", "other"
	};

	private static final String[] _LITERAL_NAMES = {
		null, "'\"'", "'''", "':'", "'\n'", "'\t'", "','", "'='"
	};
	private static final String[] _SYMBOLIC_NAMES = {
		null, "DQ", "SQ", "COLON", "NEWLINE", "TAB", "COMMA", "EQUAL", "IDENTIFIER", 
		"OTHER"
	};
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "ion.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public ionParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}
	public static class RootContext extends ParserRuleContext {
		public List<TerminalNode> NEWLINE() { return getTokens(ionParser.NEWLINE); }
		public TerminalNode NEWLINE(int i) {
			return getToken(ionParser.NEWLINE, i);
		}
		public RootContext root() {
			return getRuleContext(RootContext.class,0);
		}
		public HeadContext head() {
			return getRuleContext(HeadContext.class,0);
		}
		public BodyContext body() {
			return getRuleContext(BodyContext.class,0);
		}
		public ElementsContext elements() {
			return getRuleContext(ElementsContext.class,0);
		}
		public RootContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_root; }
	}

	public final RootContext root() throws RecognitionException {
		RootContext _localctx = new RootContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_root);
		try {
			setState(42);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,0,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(16);
				match(NEWLINE);
				setState(17);
				root();
				setState(18);
				match(NEWLINE);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(20);
				head();
				setState(21);
				match(NEWLINE);
				setState(22);
				body();
				setState(23);
				match(NEWLINE);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(25);
				head();
				setState(26);
				elements(0);
				setState(27);
				match(NEWLINE);
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(29);
				head();
				setState(30);
				match(NEWLINE);
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(32);
				match(NEWLINE);
				setState(33);
				root();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(34);
				head();
				setState(35);
				match(NEWLINE);
				setState(36);
				body();
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(38);
				head();
				setState(39);
				elements(0);
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(41);
				head();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class BodyContext extends ParserRuleContext {
		public TerminalNode TAB() { return getToken(ionParser.TAB, 0); }
		public RootContext root() {
			return getRuleContext(RootContext.class,0);
		}
		public ElementsContext elements() {
			return getRuleContext(ElementsContext.class,0);
		}
		public BodyContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_body; }
	}

	public final BodyContext body() throws RecognitionException {
		BodyContext _localctx = new BodyContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_body);
		try {
			setState(48);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(44);
				match(TAB);
				setState(45);
				root();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(46);
				match(TAB);
				setState(47);
				elements(0);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ElementsContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(ionParser.IDENTIFIER, 0); }
		public TerminalNode EQUAL() { return getToken(ionParser.EQUAL, 0); }
		public TerminalNode OTHER() { return getToken(ionParser.OTHER, 0); }
		public ElementsContext elements() {
			return getRuleContext(ElementsContext.class,0);
		}
		public ElementsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_elements; }
	}

	public final ElementsContext elements() throws RecognitionException {
		return elements(0);
	}

	private ElementsContext elements(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ElementsContext _localctx = new ElementsContext(_ctx, _parentState);
		ElementsContext _prevctx = _localctx;
		int _startState = 4;
		enterRecursionRule(_localctx, 4, RULE_elements, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(54);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case IDENTIFIER:
				{
				setState(51);
				match(IDENTIFIER);
				}
				break;
			case EQUAL:
				{
				setState(52);
				match(EQUAL);
				}
				break;
			case OTHER:
				{
				setState(53);
				match(OTHER);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			_ctx.stop = _input.LT(-1);
			setState(64);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,4,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(62);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,3,_ctx) ) {
					case 1:
						{
						_localctx = new ElementsContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_elements);
						setState(56);
						if (!(precpred(_ctx, 6))) throw new FailedPredicateException(this, "precpred(_ctx, 6)");
						setState(57);
						match(IDENTIFIER);
						}
						break;
					case 2:
						{
						_localctx = new ElementsContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_elements);
						setState(58);
						if (!(precpred(_ctx, 5))) throw new FailedPredicateException(this, "precpred(_ctx, 5)");
						setState(59);
						match(EQUAL);
						}
						break;
					case 3:
						{
						_localctx = new ElementsContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_elements);
						setState(60);
						if (!(precpred(_ctx, 4))) throw new FailedPredicateException(this, "precpred(_ctx, 4)");
						setState(61);
						match(OTHER);
						}
						break;
					}
					} 
				}
				setState(66);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,4,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class HeadContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(ionParser.IDENTIFIER, 0); }
		public AttrContext attr() {
			return getRuleContext(AttrContext.class,0);
		}
		public TerminalNode COLON() { return getToken(ionParser.COLON, 0); }
		public EmptyContext empty() {
			return getRuleContext(EmptyContext.class,0);
		}
		public HeadContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_head; }
	}

	public final HeadContext head() throws RecognitionException {
		HeadContext _localctx = new HeadContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_head);
		try {
			setState(75);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,5,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(67);
				match(IDENTIFIER);
				setState(68);
				attr();
				setState(69);
				match(COLON);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(71);
				match(IDENTIFIER);
				setState(72);
				empty();
				setState(73);
				match(COLON);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class EmptyContext extends ParserRuleContext {
		public EmptyContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_empty; }
	}

	public final EmptyContext empty() throws RecognitionException {
		EmptyContext _localctx = new EmptyContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_empty);
		try {
			enterOuterAlt(_localctx, 1);
			{
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class AttrContext extends ParserRuleContext {
		public Attr_equalContext attr_equal() {
			return getRuleContext(Attr_equalContext.class,0);
		}
		public AttrContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_attr; }
	}

	public final AttrContext attr() throws RecognitionException {
		AttrContext _localctx = new AttrContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_attr);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(79);
			attr_equal();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Attr_equalContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(ionParser.IDENTIFIER, 0); }
		public TerminalNode EQUAL() { return getToken(ionParser.EQUAL, 0); }
		public List<TerminalNode> SQ() { return getTokens(ionParser.SQ); }
		public TerminalNode SQ(int i) {
			return getToken(ionParser.SQ, i);
		}
		public OtherContext other() {
			return getRuleContext(OtherContext.class,0);
		}
		public List<TerminalNode> DQ() { return getTokens(ionParser.DQ); }
		public TerminalNode DQ(int i) {
			return getToken(ionParser.DQ, i);
		}
		public Attr_equalContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_attr_equal; }
	}

	public final Attr_equalContext attr_equal() throws RecognitionException {
		Attr_equalContext _localctx = new Attr_equalContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_attr_equal);
		try {
			setState(93);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,6,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(81);
				match(IDENTIFIER);
				setState(82);
				match(EQUAL);
				setState(83);
				match(SQ);
				setState(84);
				other(0);
				setState(85);
				match(SQ);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(87);
				match(IDENTIFIER);
				setState(88);
				match(EQUAL);
				setState(89);
				match(DQ);
				setState(90);
				other(0);
				setState(91);
				match(DQ);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class OtherContext extends ParserRuleContext {
		public TerminalNode EQUAL() { return getToken(ionParser.EQUAL, 0); }
		public TerminalNode COMMA() { return getToken(ionParser.COMMA, 0); }
		public TerminalNode COLON() { return getToken(ionParser.COLON, 0); }
		public TerminalNode IDENTIFIER() { return getToken(ionParser.IDENTIFIER, 0); }
		public TerminalNode OTHER() { return getToken(ionParser.OTHER, 0); }
		public OtherContext other() {
			return getRuleContext(OtherContext.class,0);
		}
		public OtherContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_other; }
	}

	public final OtherContext other() throws RecognitionException {
		return other(0);
	}

	private OtherContext other(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		OtherContext _localctx = new OtherContext(_ctx, _parentState);
		OtherContext _prevctx = _localctx;
		int _startState = 14;
		enterRecursionRule(_localctx, 14, RULE_other, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(101);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case EQUAL:
				{
				setState(96);
				match(EQUAL);
				}
				break;
			case COMMA:
				{
				setState(97);
				match(COMMA);
				}
				break;
			case COLON:
				{
				setState(98);
				match(COLON);
				}
				break;
			case IDENTIFIER:
				{
				setState(99);
				match(IDENTIFIER);
				}
				break;
			case OTHER:
				{
				setState(100);
				match(OTHER);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			_ctx.stop = _input.LT(-1);
			setState(115);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,9,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(113);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,8,_ctx) ) {
					case 1:
						{
						_localctx = new OtherContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_other);
						setState(103);
						if (!(precpred(_ctx, 10))) throw new FailedPredicateException(this, "precpred(_ctx, 10)");
						setState(104);
						match(EQUAL);
						}
						break;
					case 2:
						{
						_localctx = new OtherContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_other);
						setState(105);
						if (!(precpred(_ctx, 9))) throw new FailedPredicateException(this, "precpred(_ctx, 9)");
						setState(106);
						match(COMMA);
						}
						break;
					case 3:
						{
						_localctx = new OtherContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_other);
						setState(107);
						if (!(precpred(_ctx, 8))) throw new FailedPredicateException(this, "precpred(_ctx, 8)");
						setState(108);
						match(COLON);
						}
						break;
					case 4:
						{
						_localctx = new OtherContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_other);
						setState(109);
						if (!(precpred(_ctx, 7))) throw new FailedPredicateException(this, "precpred(_ctx, 7)");
						setState(110);
						match(IDENTIFIER);
						}
						break;
					case 5:
						{
						_localctx = new OtherContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_other);
						setState(111);
						if (!(precpred(_ctx, 6))) throw new FailedPredicateException(this, "precpred(_ctx, 6)");
						setState(112);
						match(OTHER);
						}
						break;
					}
					} 
				}
				setState(117);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,9,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 2:
			return elements_sempred((ElementsContext)_localctx, predIndex);
		case 7:
			return other_sempred((OtherContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean elements_sempred(ElementsContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 6);
		case 1:
			return precpred(_ctx, 5);
		case 2:
			return precpred(_ctx, 4);
		}
		return true;
	}
	private boolean other_sempred(OtherContext _localctx, int predIndex) {
		switch (predIndex) {
		case 3:
			return precpred(_ctx, 10);
		case 4:
			return precpred(_ctx, 9);
		case 5:
			return precpred(_ctx, 8);
		case 6:
			return precpred(_ctx, 7);
		case 7:
			return precpred(_ctx, 6);
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\13y\4\2\t\2\4\3\t"+
		"\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\3\2\3\2\3\2\3\2\3\2"+
		"\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3"+
		"\2\3\2\3\2\3\2\5\2-\n\2\3\3\3\3\3\3\3\3\5\3\63\n\3\3\4\3\4\3\4\3\4\5\4"+
		"9\n\4\3\4\3\4\3\4\3\4\3\4\3\4\7\4A\n\4\f\4\16\4D\13\4\3\5\3\5\3\5\3\5"+
		"\3\5\3\5\3\5\3\5\5\5N\n\5\3\6\3\6\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b"+
		"\3\b\3\b\3\b\3\b\3\b\5\b`\n\b\3\t\3\t\3\t\3\t\3\t\3\t\5\th\n\t\3\t\3\t"+
		"\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\7\tt\n\t\f\t\16\tw\13\t\3\t\2\4\6\20"+
		"\n\2\4\6\b\n\f\16\20\2\2\2\u0088\2,\3\2\2\2\4\62\3\2\2\2\68\3\2\2\2\b"+
		"M\3\2\2\2\nO\3\2\2\2\fQ\3\2\2\2\16_\3\2\2\2\20g\3\2\2\2\22\23\7\6\2\2"+
		"\23\24\5\2\2\2\24\25\7\6\2\2\25-\3\2\2\2\26\27\5\b\5\2\27\30\7\6\2\2\30"+
		"\31\5\4\3\2\31\32\7\6\2\2\32-\3\2\2\2\33\34\5\b\5\2\34\35\5\6\4\2\35\36"+
		"\7\6\2\2\36-\3\2\2\2\37 \5\b\5\2 !\7\6\2\2!-\3\2\2\2\"#\7\6\2\2#-\5\2"+
		"\2\2$%\5\b\5\2%&\7\6\2\2&\'\5\4\3\2\'-\3\2\2\2()\5\b\5\2)*\5\6\4\2*-\3"+
		"\2\2\2+-\5\b\5\2,\22\3\2\2\2,\26\3\2\2\2,\33\3\2\2\2,\37\3\2\2\2,\"\3"+
		"\2\2\2,$\3\2\2\2,(\3\2\2\2,+\3\2\2\2-\3\3\2\2\2./\7\7\2\2/\63\5\2\2\2"+
		"\60\61\7\7\2\2\61\63\5\6\4\2\62.\3\2\2\2\62\60\3\2\2\2\63\5\3\2\2\2\64"+
		"\65\b\4\1\2\659\7\n\2\2\669\7\t\2\2\679\7\13\2\28\64\3\2\2\28\66\3\2\2"+
		"\28\67\3\2\2\29B\3\2\2\2:;\f\b\2\2;A\7\n\2\2<=\f\7\2\2=A\7\t\2\2>?\f\6"+
		"\2\2?A\7\13\2\2@:\3\2\2\2@<\3\2\2\2@>\3\2\2\2AD\3\2\2\2B@\3\2\2\2BC\3"+
		"\2\2\2C\7\3\2\2\2DB\3\2\2\2EF\7\n\2\2FG\5\f\7\2GH\7\5\2\2HN\3\2\2\2IJ"+
		"\7\n\2\2JK\5\n\6\2KL\7\5\2\2LN\3\2\2\2ME\3\2\2\2MI\3\2\2\2N\t\3\2\2\2"+
		"OP\3\2\2\2P\13\3\2\2\2QR\5\16\b\2R\r\3\2\2\2ST\7\n\2\2TU\7\t\2\2UV\7\4"+
		"\2\2VW\5\20\t\2WX\7\4\2\2X`\3\2\2\2YZ\7\n\2\2Z[\7\t\2\2[\\\7\3\2\2\\]"+
		"\5\20\t\2]^\7\3\2\2^`\3\2\2\2_S\3\2\2\2_Y\3\2\2\2`\17\3\2\2\2ab\b\t\1"+
		"\2bh\7\t\2\2ch\7\b\2\2dh\7\5\2\2eh\7\n\2\2fh\7\13\2\2ga\3\2\2\2gc\3\2"+
		"\2\2gd\3\2\2\2ge\3\2\2\2gf\3\2\2\2hu\3\2\2\2ij\f\f\2\2jt\7\t\2\2kl\f\13"+
		"\2\2lt\7\b\2\2mn\f\n\2\2nt\7\5\2\2op\f\t\2\2pt\7\n\2\2qr\f\b\2\2rt\7\13"+
		"\2\2si\3\2\2\2sk\3\2\2\2sm\3\2\2\2so\3\2\2\2sq\3\2\2\2tw\3\2\2\2us\3\2"+
		"\2\2uv\3\2\2\2v\21\3\2\2\2wu\3\2\2\2\f,\628@BM_gsu";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}