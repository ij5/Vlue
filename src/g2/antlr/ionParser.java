// Generated from ion.g4 by ANTLR 4.8
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
	static { RuntimeMetaData.checkVersion("4.8", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		DQ=1, SQ=2, COLON=3, NEWLINE=4, TAB=5, COMMA=6, EQUAL=7, IDENTIFIER=8, 
		OTHER=9;
	public static final int
		RULE_root = 0, RULE_elements = 1, RULE_body = 2, RULE_body_value = 3, 
		RULE_head = 4, RULE_attr_equal = 5, RULE_element_value = 6;
	private static String[] makeRuleNames() {
		return new String[] {
			"root", "elements", "body", "body_value", "head", "attr_equal", "element_value"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'\"'", "'''", "':'", "'\n'", "'\t'", "','", "'='"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "DQ", "SQ", "COLON", "NEWLINE", "TAB", "COMMA", "EQUAL", "IDENTIFIER", 
			"OTHER"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
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
		public HeadContext head() {
			return getRuleContext(HeadContext.class,0);
		}
		public TerminalNode NEWLINE() { return getToken(ionParser.NEWLINE, 0); }
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
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ionListener ) ((ionListener)listener).enterRoot(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ionListener ) ((ionListener)listener).exitRoot(this);
		}
	}

	public final RootContext root() throws RecognitionException {
		RootContext _localctx = new RootContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_root);
		try {
			setState(21);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,0,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(14);
				head();
				setState(15);
				match(NEWLINE);
				setState(16);
				body();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(18);
				head();
				setState(19);
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
		public TerminalNode COMMA() { return getToken(ionParser.COMMA, 0); }
		public TerminalNode EQUAL() { return getToken(ionParser.EQUAL, 0); }
		public TerminalNode OTHER() { return getToken(ionParser.OTHER, 0); }
		public ElementsContext elements() {
			return getRuleContext(ElementsContext.class,0);
		}
		public ElementsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_elements; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ionListener ) ((ionListener)listener).enterElements(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ionListener ) ((ionListener)listener).exitElements(this);
		}
	}

	public final ElementsContext elements() throws RecognitionException {
		return elements(0);
	}

	private ElementsContext elements(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ElementsContext _localctx = new ElementsContext(_ctx, _parentState);
		ElementsContext _prevctx = _localctx;
		int _startState = 2;
		enterRecursionRule(_localctx, 2, RULE_elements, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(28);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case IDENTIFIER:
				{
				setState(24);
				match(IDENTIFIER);
				}
				break;
			case COMMA:
				{
				setState(25);
				match(COMMA);
				}
				break;
			case EQUAL:
				{
				setState(26);
				match(EQUAL);
				}
				break;
			case OTHER:
				{
				setState(27);
				match(OTHER);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			_ctx.stop = _input.LT(-1);
			setState(40);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,3,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(38);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,2,_ctx) ) {
					case 1:
						{
						_localctx = new ElementsContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_elements);
						setState(30);
						if (!(precpred(_ctx, 8))) throw new FailedPredicateException(this, "precpred(_ctx, 8)");
						setState(31);
						match(IDENTIFIER);
						}
						break;
					case 2:
						{
						_localctx = new ElementsContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_elements);
						setState(32);
						if (!(precpred(_ctx, 7))) throw new FailedPredicateException(this, "precpred(_ctx, 7)");
						setState(33);
						match(COMMA);
						}
						break;
					case 3:
						{
						_localctx = new ElementsContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_elements);
						setState(34);
						if (!(precpred(_ctx, 6))) throw new FailedPredicateException(this, "precpred(_ctx, 6)");
						setState(35);
						match(EQUAL);
						}
						break;
					case 4:
						{
						_localctx = new ElementsContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_elements);
						setState(36);
						if (!(precpred(_ctx, 5))) throw new FailedPredicateException(this, "precpred(_ctx, 5)");
						setState(37);
						match(OTHER);
						}
						break;
					}
					} 
				}
				setState(42);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,3,_ctx);
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

	public static class BodyContext extends ParserRuleContext {
		public TerminalNode TAB() { return getToken(ionParser.TAB, 0); }
		public RootContext root() {
			return getRuleContext(RootContext.class,0);
		}
		public Body_valueContext body_value() {
			return getRuleContext(Body_valueContext.class,0);
		}
		public BodyContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_body; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ionListener ) ((ionListener)listener).enterBody(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ionListener ) ((ionListener)listener).exitBody(this);
		}
	}

	public final BodyContext body() throws RecognitionException {
		BodyContext _localctx = new BodyContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_body);
		try {
			setState(47);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,4,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(43);
				match(TAB);
				setState(44);
				root();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(45);
				match(TAB);
				setState(46);
				body_value(0);
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

	public static class Body_valueContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(ionParser.IDENTIFIER, 0); }
		public TerminalNode COMMA() { return getToken(ionParser.COMMA, 0); }
		public TerminalNode EQUAL() { return getToken(ionParser.EQUAL, 0); }
		public TerminalNode OTHER() { return getToken(ionParser.OTHER, 0); }
		public Body_valueContext body_value() {
			return getRuleContext(Body_valueContext.class,0);
		}
		public Body_valueContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_body_value; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ionListener ) ((ionListener)listener).enterBody_value(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ionListener ) ((ionListener)listener).exitBody_value(this);
		}
	}

	public final Body_valueContext body_value() throws RecognitionException {
		return body_value(0);
	}

	private Body_valueContext body_value(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		Body_valueContext _localctx = new Body_valueContext(_ctx, _parentState);
		Body_valueContext _prevctx = _localctx;
		int _startState = 6;
		enterRecursionRule(_localctx, 6, RULE_body_value, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(54);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case IDENTIFIER:
				{
				setState(50);
				match(IDENTIFIER);
				}
				break;
			case COMMA:
				{
				setState(51);
				match(COMMA);
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
			setState(66);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,7,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(64);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,6,_ctx) ) {
					case 1:
						{
						_localctx = new Body_valueContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_body_value);
						setState(56);
						if (!(precpred(_ctx, 8))) throw new FailedPredicateException(this, "precpred(_ctx, 8)");
						setState(57);
						match(IDENTIFIER);
						}
						break;
					case 2:
						{
						_localctx = new Body_valueContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_body_value);
						setState(58);
						if (!(precpred(_ctx, 7))) throw new FailedPredicateException(this, "precpred(_ctx, 7)");
						setState(59);
						match(COMMA);
						}
						break;
					case 3:
						{
						_localctx = new Body_valueContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_body_value);
						setState(60);
						if (!(precpred(_ctx, 6))) throw new FailedPredicateException(this, "precpred(_ctx, 6)");
						setState(61);
						match(EQUAL);
						}
						break;
					case 4:
						{
						_localctx = new Body_valueContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_body_value);
						setState(62);
						if (!(precpred(_ctx, 5))) throw new FailedPredicateException(this, "precpred(_ctx, 5)");
						setState(63);
						match(OTHER);
						}
						break;
					}
					} 
				}
				setState(68);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,7,_ctx);
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
		public TerminalNode COLON() { return getToken(ionParser.COLON, 0); }
		public Attr_equalContext attr_equal() {
			return getRuleContext(Attr_equalContext.class,0);
		}
		public HeadContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_head; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ionListener ) ((ionListener)listener).enterHead(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ionListener ) ((ionListener)listener).exitHead(this);
		}
	}

	public final HeadContext head() throws RecognitionException {
		HeadContext _localctx = new HeadContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_head);
		try {
			setState(75);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,8,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(69);
				match(IDENTIFIER);
				setState(70);
				match(COLON);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(71);
				match(IDENTIFIER);
				setState(72);
				attr_equal();
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

	public static class Attr_equalContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(ionParser.IDENTIFIER, 0); }
		public TerminalNode EQUAL() { return getToken(ionParser.EQUAL, 0); }
		public List<TerminalNode> SQ() { return getTokens(ionParser.SQ); }
		public TerminalNode SQ(int i) {
			return getToken(ionParser.SQ, i);
		}
		public Element_valueContext element_value() {
			return getRuleContext(Element_valueContext.class,0);
		}
		public List<TerminalNode> DQ() { return getTokens(ionParser.DQ); }
		public TerminalNode DQ(int i) {
			return getToken(ionParser.DQ, i);
		}
		public Attr_equalContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_attr_equal; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ionListener ) ((ionListener)listener).enterAttr_equal(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ionListener ) ((ionListener)listener).exitAttr_equal(this);
		}
	}

	public final Attr_equalContext attr_equal() throws RecognitionException {
		Attr_equalContext _localctx = new Attr_equalContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_attr_equal);
		try {
			setState(89);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,9,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(77);
				match(IDENTIFIER);
				setState(78);
				match(EQUAL);
				setState(79);
				match(SQ);
				setState(80);
				element_value(0);
				setState(81);
				match(SQ);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(83);
				match(IDENTIFIER);
				setState(84);
				match(EQUAL);
				setState(85);
				match(DQ);
				setState(86);
				element_value(0);
				setState(87);
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

	public static class Element_valueContext extends ParserRuleContext {
		public TerminalNode COLON() { return getToken(ionParser.COLON, 0); }
		public TerminalNode COMMA() { return getToken(ionParser.COMMA, 0); }
		public TerminalNode EQUAL() { return getToken(ionParser.EQUAL, 0); }
		public TerminalNode IDENTIFIER() { return getToken(ionParser.IDENTIFIER, 0); }
		public TerminalNode OTHER() { return getToken(ionParser.OTHER, 0); }
		public Element_valueContext element_value() {
			return getRuleContext(Element_valueContext.class,0);
		}
		public Element_valueContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_element_value; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ionListener ) ((ionListener)listener).enterElement_value(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ionListener ) ((ionListener)listener).exitElement_value(this);
		}
	}

	public final Element_valueContext element_value() throws RecognitionException {
		return element_value(0);
	}

	private Element_valueContext element_value(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		Element_valueContext _localctx = new Element_valueContext(_ctx, _parentState);
		Element_valueContext _prevctx = _localctx;
		int _startState = 12;
		enterRecursionRule(_localctx, 12, RULE_element_value, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(97);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case COLON:
				{
				setState(92);
				match(COLON);
				}
				break;
			case COMMA:
				{
				setState(93);
				match(COMMA);
				}
				break;
			case EQUAL:
				{
				setState(94);
				match(EQUAL);
				}
				break;
			case IDENTIFIER:
				{
				setState(95);
				match(IDENTIFIER);
				}
				break;
			case OTHER:
				{
				setState(96);
				match(OTHER);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			_ctx.stop = _input.LT(-1);
			setState(111);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,12,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(109);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,11,_ctx) ) {
					case 1:
						{
						_localctx = new Element_valueContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_element_value);
						setState(99);
						if (!(precpred(_ctx, 10))) throw new FailedPredicateException(this, "precpred(_ctx, 10)");
						setState(100);
						match(COLON);
						}
						break;
					case 2:
						{
						_localctx = new Element_valueContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_element_value);
						setState(101);
						if (!(precpred(_ctx, 9))) throw new FailedPredicateException(this, "precpred(_ctx, 9)");
						setState(102);
						match(COMMA);
						}
						break;
					case 3:
						{
						_localctx = new Element_valueContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_element_value);
						setState(103);
						if (!(precpred(_ctx, 8))) throw new FailedPredicateException(this, "precpred(_ctx, 8)");
						setState(104);
						match(EQUAL);
						}
						break;
					case 4:
						{
						_localctx = new Element_valueContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_element_value);
						setState(105);
						if (!(precpred(_ctx, 7))) throw new FailedPredicateException(this, "precpred(_ctx, 7)");
						setState(106);
						match(IDENTIFIER);
						}
						break;
					case 5:
						{
						_localctx = new Element_valueContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_element_value);
						setState(107);
						if (!(precpred(_ctx, 6))) throw new FailedPredicateException(this, "precpred(_ctx, 6)");
						setState(108);
						match(OTHER);
						}
						break;
					}
					} 
				}
				setState(113);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,12,_ctx);
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
		case 1:
			return elements_sempred((ElementsContext)_localctx, predIndex);
		case 3:
			return body_value_sempred((Body_valueContext)_localctx, predIndex);
		case 6:
			return element_value_sempred((Element_valueContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean elements_sempred(ElementsContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 8);
		case 1:
			return precpred(_ctx, 7);
		case 2:
			return precpred(_ctx, 6);
		case 3:
			return precpred(_ctx, 5);
		}
		return true;
	}
	private boolean body_value_sempred(Body_valueContext _localctx, int predIndex) {
		switch (predIndex) {
		case 4:
			return precpred(_ctx, 8);
		case 5:
			return precpred(_ctx, 7);
		case 6:
			return precpred(_ctx, 6);
		case 7:
			return precpred(_ctx, 5);
		}
		return true;
	}
	private boolean element_value_sempred(Element_valueContext _localctx, int predIndex) {
		switch (predIndex) {
		case 8:
			return precpred(_ctx, 10);
		case 9:
			return precpred(_ctx, 9);
		case 10:
			return precpred(_ctx, 8);
		case 11:
			return precpred(_ctx, 7);
		case 12:
			return precpred(_ctx, 6);
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\13u\4\2\t\2\4\3\t"+
		"\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\3\2\3\2\3\2\3\2\3\2\3\2\3\2"+
		"\5\2\30\n\2\3\3\3\3\3\3\3\3\3\3\5\3\37\n\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3"+
		"\3\3\7\3)\n\3\f\3\16\3,\13\3\3\4\3\4\3\4\3\4\5\4\62\n\4\3\5\3\5\3\5\3"+
		"\5\3\5\5\59\n\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\7\5C\n\5\f\5\16\5F\13"+
		"\5\3\6\3\6\3\6\3\6\3\6\3\6\5\6N\n\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3"+
		"\7\3\7\3\7\3\7\5\7\\\n\7\3\b\3\b\3\b\3\b\3\b\3\b\5\bd\n\b\3\b\3\b\3\b"+
		"\3\b\3\b\3\b\3\b\3\b\3\b\3\b\7\bp\n\b\f\b\16\bs\13\b\3\b\2\5\4\b\16\t"+
		"\2\4\6\b\n\f\16\2\2\2\u0088\2\27\3\2\2\2\4\36\3\2\2\2\6\61\3\2\2\2\b8"+
		"\3\2\2\2\nM\3\2\2\2\f[\3\2\2\2\16c\3\2\2\2\20\21\5\n\6\2\21\22\7\6\2\2"+
		"\22\23\5\6\4\2\23\30\3\2\2\2\24\25\5\n\6\2\25\26\5\4\3\2\26\30\3\2\2\2"+
		"\27\20\3\2\2\2\27\24\3\2\2\2\30\3\3\2\2\2\31\32\b\3\1\2\32\37\7\n\2\2"+
		"\33\37\7\b\2\2\34\37\7\t\2\2\35\37\7\13\2\2\36\31\3\2\2\2\36\33\3\2\2"+
		"\2\36\34\3\2\2\2\36\35\3\2\2\2\37*\3\2\2\2 !\f\n\2\2!)\7\n\2\2\"#\f\t"+
		"\2\2#)\7\b\2\2$%\f\b\2\2%)\7\t\2\2&\'\f\7\2\2\')\7\13\2\2( \3\2\2\2(\""+
		"\3\2\2\2($\3\2\2\2(&\3\2\2\2),\3\2\2\2*(\3\2\2\2*+\3\2\2\2+\5\3\2\2\2"+
		",*\3\2\2\2-.\7\7\2\2.\62\5\2\2\2/\60\7\7\2\2\60\62\5\b\5\2\61-\3\2\2\2"+
		"\61/\3\2\2\2\62\7\3\2\2\2\63\64\b\5\1\2\649\7\n\2\2\659\7\b\2\2\669\7"+
		"\t\2\2\679\7\13\2\28\63\3\2\2\28\65\3\2\2\28\66\3\2\2\28\67\3\2\2\29D"+
		"\3\2\2\2:;\f\n\2\2;C\7\n\2\2<=\f\t\2\2=C\7\b\2\2>?\f\b\2\2?C\7\t\2\2@"+
		"A\f\7\2\2AC\7\13\2\2B:\3\2\2\2B<\3\2\2\2B>\3\2\2\2B@\3\2\2\2CF\3\2\2\2"+
		"DB\3\2\2\2DE\3\2\2\2E\t\3\2\2\2FD\3\2\2\2GH\7\n\2\2HN\7\5\2\2IJ\7\n\2"+
		"\2JK\5\f\7\2KL\7\5\2\2LN\3\2\2\2MG\3\2\2\2MI\3\2\2\2N\13\3\2\2\2OP\7\n"+
		"\2\2PQ\7\t\2\2QR\7\4\2\2RS\5\16\b\2ST\7\4\2\2T\\\3\2\2\2UV\7\n\2\2VW\7"+
		"\t\2\2WX\7\3\2\2XY\5\16\b\2YZ\7\3\2\2Z\\\3\2\2\2[O\3\2\2\2[U\3\2\2\2\\"+
		"\r\3\2\2\2]^\b\b\1\2^d\7\5\2\2_d\7\b\2\2`d\7\t\2\2ad\7\n\2\2bd\7\13\2"+
		"\2c]\3\2\2\2c_\3\2\2\2c`\3\2\2\2ca\3\2\2\2cb\3\2\2\2dq\3\2\2\2ef\f\f\2"+
		"\2fp\7\5\2\2gh\f\13\2\2hp\7\b\2\2ij\f\n\2\2jp\7\t\2\2kl\f\t\2\2lp\7\n"+
		"\2\2mn\f\b\2\2np\7\13\2\2oe\3\2\2\2og\3\2\2\2oi\3\2\2\2ok\3\2\2\2om\3"+
		"\2\2\2ps\3\2\2\2qo\3\2\2\2qr\3\2\2\2r\17\3\2\2\2sq\3\2\2\2\17\27\36(*"+
		"\618BDM[coq";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}