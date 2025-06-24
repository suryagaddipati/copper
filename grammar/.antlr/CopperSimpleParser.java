// Generated from /home/surya/code/copper/grammar/CopperSimple.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class CopperSimpleParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.9.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		MODEL=1, VIEW=2, DIMENSION=3, MEASURE=4, JOIN=5, FROM=6, EXTENDS=7, TYPE=8, 
		EXPRESSION=9, PRIMARY_KEY=10, VALUE_FORMAT=11, LABEL=12, DESCRIPTION=13, 
		HIDDEN_PARAM=14, TIERS=15, SQL_LATITUDE=16, SQL_LONGITUDE=17, UNITS=18, 
		RELATIONSHIP=19, STRING_TYPE=20, NUMBER_TYPE=21, DATE_TYPE=22, DATE_TIME_TYPE=23, 
		YESNO_TYPE=24, TIER_TYPE=25, BIN_TYPE=26, LOCATION_TYPE=27, ZIPCODE_TYPE=28, 
		DISTANCE_TYPE=29, DURATION_TYPE=30, TIME_TYPE=31, UNQUOTED_TYPE=32, COUNT_TYPE=33, 
		SUM_TYPE=34, AVERAGE_TYPE=35, MIN_TYPE=36, MAX_TYPE=37, COUNT_DISTINCT_TYPE=38, 
		MEDIAN_TYPE=39, PERCENTILE_TYPE=40, ONE_TO_ONE=41, ONE_TO_MANY=42, MANY_TO_ONE=43, 
		MANY_TO_MANY=44, YES=45, NO=46, USD=47, PERCENT=48, PERCENT_1=49, PERCENT_2=50, 
		COLON=51, SEMICOLON=52, LBRACE=53, RBRACE=54, LBRACKET=55, RBRACKET=56, 
		COMMA=57, IDENTIFIER=58, INTEGER=59, STRING_LITERAL=60, DAX_EXPRESSION=61, 
		COMMENT=62, NEWLINE=63, WS=64;
	public static final int
		RULE_program = 0, RULE_statement = 1, RULE_comment = 2, RULE_modelStatement = 3, 
		RULE_modelBody = 4, RULE_dimensionStatement = 5, RULE_measureStatement = 6, 
		RULE_dimensionParameter = 7, RULE_measureParameter = 8, RULE_viewStatement = 9, 
		RULE_viewBody = 10, RULE_joinStatement = 11, RULE_joinParameter = 12, 
		RULE_typeParameter = 13, RULE_expressionParameter = 14, RULE_labelParameter = 15, 
		RULE_descriptionParameter = 16, RULE_primaryKeyParameter = 17, RULE_hiddenParameter = 18, 
		RULE_valueFormatParameter = 19, RULE_tiersParameter = 20, RULE_sqlLatitudeParameter = 21, 
		RULE_sqlLongitudeParameter = 22, RULE_unitsParameter = 23, RULE_fromParameter = 24, 
		RULE_extendsParameter = 25, RULE_relationshipParameter = 26, RULE_typeValue = 27, 
		RULE_relationshipValue = 28, RULE_booleanValue = 29, RULE_stringValue = 30, 
		RULE_formatValue = 31, RULE_arrayValue = 32, RULE_daxExpression = 33, 
		RULE_identifier = 34;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "statement", "comment", "modelStatement", "modelBody", "dimensionStatement", 
			"measureStatement", "dimensionParameter", "measureParameter", "viewStatement", 
			"viewBody", "joinStatement", "joinParameter", "typeParameter", "expressionParameter", 
			"labelParameter", "descriptionParameter", "primaryKeyParameter", "hiddenParameter", 
			"valueFormatParameter", "tiersParameter", "sqlLatitudeParameter", "sqlLongitudeParameter", 
			"unitsParameter", "fromParameter", "extendsParameter", "relationshipParameter", 
			"typeValue", "relationshipValue", "booleanValue", "stringValue", "formatValue", 
			"arrayValue", "daxExpression", "identifier"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'model'", "'view'", "'dimension'", "'measure'", "'join'", "'from'", 
			"'extends'", "'type'", "'expression'", "'primary_key'", "'value_format'", 
			"'label'", "'description'", "'hidden'", "'tiers'", "'sql_latitude'", 
			"'sql_longitude'", "'units'", "'relationship'", "'string'", "'number'", 
			"'date'", "'date_time'", "'yesno'", "'tier'", "'bin'", "'location'", 
			"'zipcode'", "'distance'", "'duration'", "'time'", "'unquoted'", "'count'", 
			"'sum'", "'average'", "'min'", "'max'", "'count_distinct'", "'median'", 
			"'percentile'", "'one_to_one'", "'one_to_many'", "'many_to_one'", "'many_to_many'", 
			"'yes'", "'no'", "'usd'", "'percent'", "'percent_1'", "'percent_2'", 
			"':'", "';'", "'{'", "'}'", "'['", "']'", "','"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "MODEL", "VIEW", "DIMENSION", "MEASURE", "JOIN", "FROM", "EXTENDS", 
			"TYPE", "EXPRESSION", "PRIMARY_KEY", "VALUE_FORMAT", "LABEL", "DESCRIPTION", 
			"HIDDEN_PARAM", "TIERS", "SQL_LATITUDE", "SQL_LONGITUDE", "UNITS", "RELATIONSHIP", 
			"STRING_TYPE", "NUMBER_TYPE", "DATE_TYPE", "DATE_TIME_TYPE", "YESNO_TYPE", 
			"TIER_TYPE", "BIN_TYPE", "LOCATION_TYPE", "ZIPCODE_TYPE", "DISTANCE_TYPE", 
			"DURATION_TYPE", "TIME_TYPE", "UNQUOTED_TYPE", "COUNT_TYPE", "SUM_TYPE", 
			"AVERAGE_TYPE", "MIN_TYPE", "MAX_TYPE", "COUNT_DISTINCT_TYPE", "MEDIAN_TYPE", 
			"PERCENTILE_TYPE", "ONE_TO_ONE", "ONE_TO_MANY", "MANY_TO_ONE", "MANY_TO_MANY", 
			"YES", "NO", "USD", "PERCENT", "PERCENT_1", "PERCENT_2", "COLON", "SEMICOLON", 
			"LBRACE", "RBRACE", "LBRACKET", "RBRACKET", "COMMA", "IDENTIFIER", "INTEGER", 
			"STRING_LITERAL", "DAX_EXPRESSION", "COMMENT", "NEWLINE", "WS"
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
	public String getGrammarFileName() { return "CopperSimple.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public CopperSimpleParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class ProgramContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(CopperSimpleParser.EOF, 0); }
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(73);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << MODEL) | (1L << VIEW) | (1L << COMMENT) | (1L << NEWLINE))) != 0)) {
				{
				{
				setState(70);
				statement();
				}
				}
				setState(75);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(76);
			match(EOF);
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

	public static class StatementContext extends ParserRuleContext {
		public ModelStatementContext modelStatement() {
			return getRuleContext(ModelStatementContext.class,0);
		}
		public ViewStatementContext viewStatement() {
			return getRuleContext(ViewStatementContext.class,0);
		}
		public CommentContext comment() {
			return getRuleContext(CommentContext.class,0);
		}
		public TerminalNode NEWLINE() { return getToken(CopperSimpleParser.NEWLINE, 0); }
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_statement);
		try {
			setState(82);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case MODEL:
				enterOuterAlt(_localctx, 1);
				{
				setState(78);
				modelStatement();
				}
				break;
			case VIEW:
				enterOuterAlt(_localctx, 2);
				{
				setState(79);
				viewStatement();
				}
				break;
			case COMMENT:
				enterOuterAlt(_localctx, 3);
				{
				setState(80);
				comment();
				}
				break;
			case NEWLINE:
				enterOuterAlt(_localctx, 4);
				{
				setState(81);
				match(NEWLINE);
				}
				break;
			default:
				throw new NoViableAltException(this);
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

	public static class CommentContext extends ParserRuleContext {
		public TerminalNode COMMENT() { return getToken(CopperSimpleParser.COMMENT, 0); }
		public CommentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_comment; }
	}

	public final CommentContext comment() throws RecognitionException {
		CommentContext _localctx = new CommentContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_comment);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(84);
			match(COMMENT);
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

	public static class ModelStatementContext extends ParserRuleContext {
		public TerminalNode MODEL() { return getToken(CopperSimpleParser.MODEL, 0); }
		public TerminalNode COLON() { return getToken(CopperSimpleParser.COLON, 0); }
		public IdentifierContext identifier() {
			return getRuleContext(IdentifierContext.class,0);
		}
		public TerminalNode LBRACE() { return getToken(CopperSimpleParser.LBRACE, 0); }
		public TerminalNode RBRACE() { return getToken(CopperSimpleParser.RBRACE, 0); }
		public List<ModelBodyContext> modelBody() {
			return getRuleContexts(ModelBodyContext.class);
		}
		public ModelBodyContext modelBody(int i) {
			return getRuleContext(ModelBodyContext.class,i);
		}
		public ModelStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_modelStatement; }
	}

	public final ModelStatementContext modelStatement() throws RecognitionException {
		ModelStatementContext _localctx = new ModelStatementContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_modelStatement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(86);
			match(MODEL);
			setState(87);
			match(COLON);
			setState(88);
			identifier();
			setState(89);
			match(LBRACE);
			setState(93);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << DIMENSION) | (1L << MEASURE) | (1L << COMMENT) | (1L << NEWLINE))) != 0)) {
				{
				{
				setState(90);
				modelBody();
				}
				}
				setState(95);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(96);
			match(RBRACE);
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

	public static class ModelBodyContext extends ParserRuleContext {
		public DimensionStatementContext dimensionStatement() {
			return getRuleContext(DimensionStatementContext.class,0);
		}
		public MeasureStatementContext measureStatement() {
			return getRuleContext(MeasureStatementContext.class,0);
		}
		public CommentContext comment() {
			return getRuleContext(CommentContext.class,0);
		}
		public TerminalNode NEWLINE() { return getToken(CopperSimpleParser.NEWLINE, 0); }
		public ModelBodyContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_modelBody; }
	}

	public final ModelBodyContext modelBody() throws RecognitionException {
		ModelBodyContext _localctx = new ModelBodyContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_modelBody);
		try {
			setState(102);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case DIMENSION:
				enterOuterAlt(_localctx, 1);
				{
				setState(98);
				dimensionStatement();
				}
				break;
			case MEASURE:
				enterOuterAlt(_localctx, 2);
				{
				setState(99);
				measureStatement();
				}
				break;
			case COMMENT:
				enterOuterAlt(_localctx, 3);
				{
				setState(100);
				comment();
				}
				break;
			case NEWLINE:
				enterOuterAlt(_localctx, 4);
				{
				setState(101);
				match(NEWLINE);
				}
				break;
			default:
				throw new NoViableAltException(this);
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

	public static class DimensionStatementContext extends ParserRuleContext {
		public TerminalNode DIMENSION() { return getToken(CopperSimpleParser.DIMENSION, 0); }
		public TerminalNode COLON() { return getToken(CopperSimpleParser.COLON, 0); }
		public IdentifierContext identifier() {
			return getRuleContext(IdentifierContext.class,0);
		}
		public TerminalNode LBRACE() { return getToken(CopperSimpleParser.LBRACE, 0); }
		public TerminalNode RBRACE() { return getToken(CopperSimpleParser.RBRACE, 0); }
		public List<DimensionParameterContext> dimensionParameter() {
			return getRuleContexts(DimensionParameterContext.class);
		}
		public DimensionParameterContext dimensionParameter(int i) {
			return getRuleContext(DimensionParameterContext.class,i);
		}
		public DimensionStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_dimensionStatement; }
	}

	public final DimensionStatementContext dimensionStatement() throws RecognitionException {
		DimensionStatementContext _localctx = new DimensionStatementContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_dimensionStatement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(104);
			match(DIMENSION);
			setState(105);
			match(COLON);
			setState(106);
			identifier();
			setState(107);
			match(LBRACE);
			setState(111);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << TYPE) | (1L << EXPRESSION) | (1L << PRIMARY_KEY) | (1L << VALUE_FORMAT) | (1L << LABEL) | (1L << DESCRIPTION) | (1L << HIDDEN_PARAM) | (1L << TIERS) | (1L << SQL_LATITUDE) | (1L << SQL_LONGITUDE) | (1L << UNITS) | (1L << COMMENT) | (1L << NEWLINE))) != 0)) {
				{
				{
				setState(108);
				dimensionParameter();
				}
				}
				setState(113);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(114);
			match(RBRACE);
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

	public static class MeasureStatementContext extends ParserRuleContext {
		public TerminalNode MEASURE() { return getToken(CopperSimpleParser.MEASURE, 0); }
		public TerminalNode COLON() { return getToken(CopperSimpleParser.COLON, 0); }
		public IdentifierContext identifier() {
			return getRuleContext(IdentifierContext.class,0);
		}
		public TerminalNode LBRACE() { return getToken(CopperSimpleParser.LBRACE, 0); }
		public TerminalNode RBRACE() { return getToken(CopperSimpleParser.RBRACE, 0); }
		public List<MeasureParameterContext> measureParameter() {
			return getRuleContexts(MeasureParameterContext.class);
		}
		public MeasureParameterContext measureParameter(int i) {
			return getRuleContext(MeasureParameterContext.class,i);
		}
		public MeasureStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_measureStatement; }
	}

	public final MeasureStatementContext measureStatement() throws RecognitionException {
		MeasureStatementContext _localctx = new MeasureStatementContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_measureStatement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(116);
			match(MEASURE);
			setState(117);
			match(COLON);
			setState(118);
			identifier();
			setState(119);
			match(LBRACE);
			setState(123);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << TYPE) | (1L << EXPRESSION) | (1L << VALUE_FORMAT) | (1L << LABEL) | (1L << DESCRIPTION) | (1L << HIDDEN_PARAM) | (1L << UNITS) | (1L << COMMENT) | (1L << NEWLINE))) != 0)) {
				{
				{
				setState(120);
				measureParameter();
				}
				}
				setState(125);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(126);
			match(RBRACE);
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

	public static class DimensionParameterContext extends ParserRuleContext {
		public TypeParameterContext typeParameter() {
			return getRuleContext(TypeParameterContext.class,0);
		}
		public ExpressionParameterContext expressionParameter() {
			return getRuleContext(ExpressionParameterContext.class,0);
		}
		public LabelParameterContext labelParameter() {
			return getRuleContext(LabelParameterContext.class,0);
		}
		public DescriptionParameterContext descriptionParameter() {
			return getRuleContext(DescriptionParameterContext.class,0);
		}
		public PrimaryKeyParameterContext primaryKeyParameter() {
			return getRuleContext(PrimaryKeyParameterContext.class,0);
		}
		public HiddenParameterContext hiddenParameter() {
			return getRuleContext(HiddenParameterContext.class,0);
		}
		public ValueFormatParameterContext valueFormatParameter() {
			return getRuleContext(ValueFormatParameterContext.class,0);
		}
		public TiersParameterContext tiersParameter() {
			return getRuleContext(TiersParameterContext.class,0);
		}
		public SqlLatitudeParameterContext sqlLatitudeParameter() {
			return getRuleContext(SqlLatitudeParameterContext.class,0);
		}
		public SqlLongitudeParameterContext sqlLongitudeParameter() {
			return getRuleContext(SqlLongitudeParameterContext.class,0);
		}
		public UnitsParameterContext unitsParameter() {
			return getRuleContext(UnitsParameterContext.class,0);
		}
		public CommentContext comment() {
			return getRuleContext(CommentContext.class,0);
		}
		public TerminalNode NEWLINE() { return getToken(CopperSimpleParser.NEWLINE, 0); }
		public DimensionParameterContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_dimensionParameter; }
	}

	public final DimensionParameterContext dimensionParameter() throws RecognitionException {
		DimensionParameterContext _localctx = new DimensionParameterContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_dimensionParameter);
		try {
			setState(141);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case TYPE:
				enterOuterAlt(_localctx, 1);
				{
				setState(128);
				typeParameter();
				}
				break;
			case EXPRESSION:
				enterOuterAlt(_localctx, 2);
				{
				setState(129);
				expressionParameter();
				}
				break;
			case LABEL:
				enterOuterAlt(_localctx, 3);
				{
				setState(130);
				labelParameter();
				}
				break;
			case DESCRIPTION:
				enterOuterAlt(_localctx, 4);
				{
				setState(131);
				descriptionParameter();
				}
				break;
			case PRIMARY_KEY:
				enterOuterAlt(_localctx, 5);
				{
				setState(132);
				primaryKeyParameter();
				}
				break;
			case HIDDEN_PARAM:
				enterOuterAlt(_localctx, 6);
				{
				setState(133);
				hiddenParameter();
				}
				break;
			case VALUE_FORMAT:
				enterOuterAlt(_localctx, 7);
				{
				setState(134);
				valueFormatParameter();
				}
				break;
			case TIERS:
				enterOuterAlt(_localctx, 8);
				{
				setState(135);
				tiersParameter();
				}
				break;
			case SQL_LATITUDE:
				enterOuterAlt(_localctx, 9);
				{
				setState(136);
				sqlLatitudeParameter();
				}
				break;
			case SQL_LONGITUDE:
				enterOuterAlt(_localctx, 10);
				{
				setState(137);
				sqlLongitudeParameter();
				}
				break;
			case UNITS:
				enterOuterAlt(_localctx, 11);
				{
				setState(138);
				unitsParameter();
				}
				break;
			case COMMENT:
				enterOuterAlt(_localctx, 12);
				{
				setState(139);
				comment();
				}
				break;
			case NEWLINE:
				enterOuterAlt(_localctx, 13);
				{
				setState(140);
				match(NEWLINE);
				}
				break;
			default:
				throw new NoViableAltException(this);
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

	public static class MeasureParameterContext extends ParserRuleContext {
		public TypeParameterContext typeParameter() {
			return getRuleContext(TypeParameterContext.class,0);
		}
		public ExpressionParameterContext expressionParameter() {
			return getRuleContext(ExpressionParameterContext.class,0);
		}
		public LabelParameterContext labelParameter() {
			return getRuleContext(LabelParameterContext.class,0);
		}
		public DescriptionParameterContext descriptionParameter() {
			return getRuleContext(DescriptionParameterContext.class,0);
		}
		public HiddenParameterContext hiddenParameter() {
			return getRuleContext(HiddenParameterContext.class,0);
		}
		public ValueFormatParameterContext valueFormatParameter() {
			return getRuleContext(ValueFormatParameterContext.class,0);
		}
		public UnitsParameterContext unitsParameter() {
			return getRuleContext(UnitsParameterContext.class,0);
		}
		public CommentContext comment() {
			return getRuleContext(CommentContext.class,0);
		}
		public TerminalNode NEWLINE() { return getToken(CopperSimpleParser.NEWLINE, 0); }
		public MeasureParameterContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_measureParameter; }
	}

	public final MeasureParameterContext measureParameter() throws RecognitionException {
		MeasureParameterContext _localctx = new MeasureParameterContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_measureParameter);
		try {
			setState(152);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case TYPE:
				enterOuterAlt(_localctx, 1);
				{
				setState(143);
				typeParameter();
				}
				break;
			case EXPRESSION:
				enterOuterAlt(_localctx, 2);
				{
				setState(144);
				expressionParameter();
				}
				break;
			case LABEL:
				enterOuterAlt(_localctx, 3);
				{
				setState(145);
				labelParameter();
				}
				break;
			case DESCRIPTION:
				enterOuterAlt(_localctx, 4);
				{
				setState(146);
				descriptionParameter();
				}
				break;
			case HIDDEN_PARAM:
				enterOuterAlt(_localctx, 5);
				{
				setState(147);
				hiddenParameter();
				}
				break;
			case VALUE_FORMAT:
				enterOuterAlt(_localctx, 6);
				{
				setState(148);
				valueFormatParameter();
				}
				break;
			case UNITS:
				enterOuterAlt(_localctx, 7);
				{
				setState(149);
				unitsParameter();
				}
				break;
			case COMMENT:
				enterOuterAlt(_localctx, 8);
				{
				setState(150);
				comment();
				}
				break;
			case NEWLINE:
				enterOuterAlt(_localctx, 9);
				{
				setState(151);
				match(NEWLINE);
				}
				break;
			default:
				throw new NoViableAltException(this);
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

	public static class ViewStatementContext extends ParserRuleContext {
		public TerminalNode VIEW() { return getToken(CopperSimpleParser.VIEW, 0); }
		public TerminalNode COLON() { return getToken(CopperSimpleParser.COLON, 0); }
		public IdentifierContext identifier() {
			return getRuleContext(IdentifierContext.class,0);
		}
		public TerminalNode LBRACE() { return getToken(CopperSimpleParser.LBRACE, 0); }
		public TerminalNode RBRACE() { return getToken(CopperSimpleParser.RBRACE, 0); }
		public List<ViewBodyContext> viewBody() {
			return getRuleContexts(ViewBodyContext.class);
		}
		public ViewBodyContext viewBody(int i) {
			return getRuleContext(ViewBodyContext.class,i);
		}
		public ViewStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_viewStatement; }
	}

	public final ViewStatementContext viewStatement() throws RecognitionException {
		ViewStatementContext _localctx = new ViewStatementContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_viewStatement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(154);
			match(VIEW);
			setState(155);
			match(COLON);
			setState(156);
			identifier();
			setState(157);
			match(LBRACE);
			setState(161);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << DIMENSION) | (1L << MEASURE) | (1L << JOIN) | (1L << FROM) | (1L << EXTENDS) | (1L << COMMENT) | (1L << NEWLINE))) != 0)) {
				{
				{
				setState(158);
				viewBody();
				}
				}
				setState(163);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(164);
			match(RBRACE);
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

	public static class ViewBodyContext extends ParserRuleContext {
		public FromParameterContext fromParameter() {
			return getRuleContext(FromParameterContext.class,0);
		}
		public ExtendsParameterContext extendsParameter() {
			return getRuleContext(ExtendsParameterContext.class,0);
		}
		public JoinStatementContext joinStatement() {
			return getRuleContext(JoinStatementContext.class,0);
		}
		public DimensionStatementContext dimensionStatement() {
			return getRuleContext(DimensionStatementContext.class,0);
		}
		public MeasureStatementContext measureStatement() {
			return getRuleContext(MeasureStatementContext.class,0);
		}
		public CommentContext comment() {
			return getRuleContext(CommentContext.class,0);
		}
		public TerminalNode NEWLINE() { return getToken(CopperSimpleParser.NEWLINE, 0); }
		public ViewBodyContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_viewBody; }
	}

	public final ViewBodyContext viewBody() throws RecognitionException {
		ViewBodyContext _localctx = new ViewBodyContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_viewBody);
		try {
			setState(173);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case FROM:
				enterOuterAlt(_localctx, 1);
				{
				setState(166);
				fromParameter();
				}
				break;
			case EXTENDS:
				enterOuterAlt(_localctx, 2);
				{
				setState(167);
				extendsParameter();
				}
				break;
			case JOIN:
				enterOuterAlt(_localctx, 3);
				{
				setState(168);
				joinStatement();
				}
				break;
			case DIMENSION:
				enterOuterAlt(_localctx, 4);
				{
				setState(169);
				dimensionStatement();
				}
				break;
			case MEASURE:
				enterOuterAlt(_localctx, 5);
				{
				setState(170);
				measureStatement();
				}
				break;
			case COMMENT:
				enterOuterAlt(_localctx, 6);
				{
				setState(171);
				comment();
				}
				break;
			case NEWLINE:
				enterOuterAlt(_localctx, 7);
				{
				setState(172);
				match(NEWLINE);
				}
				break;
			default:
				throw new NoViableAltException(this);
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

	public static class JoinStatementContext extends ParserRuleContext {
		public TerminalNode JOIN() { return getToken(CopperSimpleParser.JOIN, 0); }
		public TerminalNode COLON() { return getToken(CopperSimpleParser.COLON, 0); }
		public IdentifierContext identifier() {
			return getRuleContext(IdentifierContext.class,0);
		}
		public TerminalNode LBRACE() { return getToken(CopperSimpleParser.LBRACE, 0); }
		public TerminalNode RBRACE() { return getToken(CopperSimpleParser.RBRACE, 0); }
		public List<JoinParameterContext> joinParameter() {
			return getRuleContexts(JoinParameterContext.class);
		}
		public JoinParameterContext joinParameter(int i) {
			return getRuleContext(JoinParameterContext.class,i);
		}
		public JoinStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_joinStatement; }
	}

	public final JoinStatementContext joinStatement() throws RecognitionException {
		JoinStatementContext _localctx = new JoinStatementContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_joinStatement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(175);
			match(JOIN);
			setState(176);
			match(COLON);
			setState(177);
			identifier();
			setState(178);
			match(LBRACE);
			setState(182);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << TYPE) | (1L << EXPRESSION) | (1L << RELATIONSHIP) | (1L << COMMENT) | (1L << NEWLINE))) != 0)) {
				{
				{
				setState(179);
				joinParameter();
				}
				}
				setState(184);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(185);
			match(RBRACE);
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

	public static class JoinParameterContext extends ParserRuleContext {
		public TypeParameterContext typeParameter() {
			return getRuleContext(TypeParameterContext.class,0);
		}
		public RelationshipParameterContext relationshipParameter() {
			return getRuleContext(RelationshipParameterContext.class,0);
		}
		public ExpressionParameterContext expressionParameter() {
			return getRuleContext(ExpressionParameterContext.class,0);
		}
		public CommentContext comment() {
			return getRuleContext(CommentContext.class,0);
		}
		public TerminalNode NEWLINE() { return getToken(CopperSimpleParser.NEWLINE, 0); }
		public JoinParameterContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_joinParameter; }
	}

	public final JoinParameterContext joinParameter() throws RecognitionException {
		JoinParameterContext _localctx = new JoinParameterContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_joinParameter);
		try {
			setState(192);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case TYPE:
				enterOuterAlt(_localctx, 1);
				{
				setState(187);
				typeParameter();
				}
				break;
			case RELATIONSHIP:
				enterOuterAlt(_localctx, 2);
				{
				setState(188);
				relationshipParameter();
				}
				break;
			case EXPRESSION:
				enterOuterAlt(_localctx, 3);
				{
				setState(189);
				expressionParameter();
				}
				break;
			case COMMENT:
				enterOuterAlt(_localctx, 4);
				{
				setState(190);
				comment();
				}
				break;
			case NEWLINE:
				enterOuterAlt(_localctx, 5);
				{
				setState(191);
				match(NEWLINE);
				}
				break;
			default:
				throw new NoViableAltException(this);
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

	public static class TypeParameterContext extends ParserRuleContext {
		public TerminalNode TYPE() { return getToken(CopperSimpleParser.TYPE, 0); }
		public TerminalNode COLON() { return getToken(CopperSimpleParser.COLON, 0); }
		public TypeValueContext typeValue() {
			return getRuleContext(TypeValueContext.class,0);
		}
		public List<TerminalNode> SEMICOLON() { return getTokens(CopperSimpleParser.SEMICOLON); }
		public TerminalNode SEMICOLON(int i) {
			return getToken(CopperSimpleParser.SEMICOLON, i);
		}
		public TypeParameterContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_typeParameter; }
	}

	public final TypeParameterContext typeParameter() throws RecognitionException {
		TypeParameterContext _localctx = new TypeParameterContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_typeParameter);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(194);
			match(TYPE);
			setState(195);
			match(COLON);
			setState(196);
			typeValue();
			setState(197);
			match(SEMICOLON);
			setState(199);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==SEMICOLON) {
				{
				setState(198);
				match(SEMICOLON);
				}
			}

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

	public static class ExpressionParameterContext extends ParserRuleContext {
		public TerminalNode EXPRESSION() { return getToken(CopperSimpleParser.EXPRESSION, 0); }
		public TerminalNode COLON() { return getToken(CopperSimpleParser.COLON, 0); }
		public DaxExpressionContext daxExpression() {
			return getRuleContext(DaxExpressionContext.class,0);
		}
		public List<TerminalNode> SEMICOLON() { return getTokens(CopperSimpleParser.SEMICOLON); }
		public TerminalNode SEMICOLON(int i) {
			return getToken(CopperSimpleParser.SEMICOLON, i);
		}
		public ExpressionParameterContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expressionParameter; }
	}

	public final ExpressionParameterContext expressionParameter() throws RecognitionException {
		ExpressionParameterContext _localctx = new ExpressionParameterContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_expressionParameter);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(201);
			match(EXPRESSION);
			setState(202);
			match(COLON);
			setState(203);
			daxExpression();
			setState(204);
			match(SEMICOLON);
			setState(205);
			match(SEMICOLON);
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

	public static class LabelParameterContext extends ParserRuleContext {
		public TerminalNode LABEL() { return getToken(CopperSimpleParser.LABEL, 0); }
		public TerminalNode COLON() { return getToken(CopperSimpleParser.COLON, 0); }
		public StringValueContext stringValue() {
			return getRuleContext(StringValueContext.class,0);
		}
		public List<TerminalNode> SEMICOLON() { return getTokens(CopperSimpleParser.SEMICOLON); }
		public TerminalNode SEMICOLON(int i) {
			return getToken(CopperSimpleParser.SEMICOLON, i);
		}
		public LabelParameterContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_labelParameter; }
	}

	public final LabelParameterContext labelParameter() throws RecognitionException {
		LabelParameterContext _localctx = new LabelParameterContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_labelParameter);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(207);
			match(LABEL);
			setState(208);
			match(COLON);
			setState(209);
			stringValue();
			setState(210);
			match(SEMICOLON);
			setState(212);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==SEMICOLON) {
				{
				setState(211);
				match(SEMICOLON);
				}
			}

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

	public static class DescriptionParameterContext extends ParserRuleContext {
		public TerminalNode DESCRIPTION() { return getToken(CopperSimpleParser.DESCRIPTION, 0); }
		public TerminalNode COLON() { return getToken(CopperSimpleParser.COLON, 0); }
		public StringValueContext stringValue() {
			return getRuleContext(StringValueContext.class,0);
		}
		public List<TerminalNode> SEMICOLON() { return getTokens(CopperSimpleParser.SEMICOLON); }
		public TerminalNode SEMICOLON(int i) {
			return getToken(CopperSimpleParser.SEMICOLON, i);
		}
		public DescriptionParameterContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_descriptionParameter; }
	}

	public final DescriptionParameterContext descriptionParameter() throws RecognitionException {
		DescriptionParameterContext _localctx = new DescriptionParameterContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_descriptionParameter);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(214);
			match(DESCRIPTION);
			setState(215);
			match(COLON);
			setState(216);
			stringValue();
			setState(217);
			match(SEMICOLON);
			setState(219);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==SEMICOLON) {
				{
				setState(218);
				match(SEMICOLON);
				}
			}

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

	public static class PrimaryKeyParameterContext extends ParserRuleContext {
		public TerminalNode PRIMARY_KEY() { return getToken(CopperSimpleParser.PRIMARY_KEY, 0); }
		public TerminalNode COLON() { return getToken(CopperSimpleParser.COLON, 0); }
		public BooleanValueContext booleanValue() {
			return getRuleContext(BooleanValueContext.class,0);
		}
		public List<TerminalNode> SEMICOLON() { return getTokens(CopperSimpleParser.SEMICOLON); }
		public TerminalNode SEMICOLON(int i) {
			return getToken(CopperSimpleParser.SEMICOLON, i);
		}
		public PrimaryKeyParameterContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_primaryKeyParameter; }
	}

	public final PrimaryKeyParameterContext primaryKeyParameter() throws RecognitionException {
		PrimaryKeyParameterContext _localctx = new PrimaryKeyParameterContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_primaryKeyParameter);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(221);
			match(PRIMARY_KEY);
			setState(222);
			match(COLON);
			setState(223);
			booleanValue();
			setState(224);
			match(SEMICOLON);
			setState(226);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==SEMICOLON) {
				{
				setState(225);
				match(SEMICOLON);
				}
			}

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

	public static class HiddenParameterContext extends ParserRuleContext {
		public TerminalNode HIDDEN_PARAM() { return getToken(CopperSimpleParser.HIDDEN_PARAM, 0); }
		public TerminalNode COLON() { return getToken(CopperSimpleParser.COLON, 0); }
		public BooleanValueContext booleanValue() {
			return getRuleContext(BooleanValueContext.class,0);
		}
		public List<TerminalNode> SEMICOLON() { return getTokens(CopperSimpleParser.SEMICOLON); }
		public TerminalNode SEMICOLON(int i) {
			return getToken(CopperSimpleParser.SEMICOLON, i);
		}
		public HiddenParameterContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_hiddenParameter; }
	}

	public final HiddenParameterContext hiddenParameter() throws RecognitionException {
		HiddenParameterContext _localctx = new HiddenParameterContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_hiddenParameter);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(228);
			match(HIDDEN_PARAM);
			setState(229);
			match(COLON);
			setState(230);
			booleanValue();
			setState(231);
			match(SEMICOLON);
			setState(233);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==SEMICOLON) {
				{
				setState(232);
				match(SEMICOLON);
				}
			}

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

	public static class ValueFormatParameterContext extends ParserRuleContext {
		public TerminalNode VALUE_FORMAT() { return getToken(CopperSimpleParser.VALUE_FORMAT, 0); }
		public TerminalNode COLON() { return getToken(CopperSimpleParser.COLON, 0); }
		public FormatValueContext formatValue() {
			return getRuleContext(FormatValueContext.class,0);
		}
		public List<TerminalNode> SEMICOLON() { return getTokens(CopperSimpleParser.SEMICOLON); }
		public TerminalNode SEMICOLON(int i) {
			return getToken(CopperSimpleParser.SEMICOLON, i);
		}
		public ValueFormatParameterContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_valueFormatParameter; }
	}

	public final ValueFormatParameterContext valueFormatParameter() throws RecognitionException {
		ValueFormatParameterContext _localctx = new ValueFormatParameterContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_valueFormatParameter);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(235);
			match(VALUE_FORMAT);
			setState(236);
			match(COLON);
			setState(237);
			formatValue();
			setState(238);
			match(SEMICOLON);
			setState(240);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==SEMICOLON) {
				{
				setState(239);
				match(SEMICOLON);
				}
			}

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

	public static class TiersParameterContext extends ParserRuleContext {
		public TerminalNode TIERS() { return getToken(CopperSimpleParser.TIERS, 0); }
		public TerminalNode COLON() { return getToken(CopperSimpleParser.COLON, 0); }
		public ArrayValueContext arrayValue() {
			return getRuleContext(ArrayValueContext.class,0);
		}
		public List<TerminalNode> SEMICOLON() { return getTokens(CopperSimpleParser.SEMICOLON); }
		public TerminalNode SEMICOLON(int i) {
			return getToken(CopperSimpleParser.SEMICOLON, i);
		}
		public TiersParameterContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_tiersParameter; }
	}

	public final TiersParameterContext tiersParameter() throws RecognitionException {
		TiersParameterContext _localctx = new TiersParameterContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_tiersParameter);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(242);
			match(TIERS);
			setState(243);
			match(COLON);
			setState(244);
			arrayValue();
			setState(245);
			match(SEMICOLON);
			setState(246);
			match(SEMICOLON);
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

	public static class SqlLatitudeParameterContext extends ParserRuleContext {
		public TerminalNode SQL_LATITUDE() { return getToken(CopperSimpleParser.SQL_LATITUDE, 0); }
		public TerminalNode COLON() { return getToken(CopperSimpleParser.COLON, 0); }
		public DaxExpressionContext daxExpression() {
			return getRuleContext(DaxExpressionContext.class,0);
		}
		public List<TerminalNode> SEMICOLON() { return getTokens(CopperSimpleParser.SEMICOLON); }
		public TerminalNode SEMICOLON(int i) {
			return getToken(CopperSimpleParser.SEMICOLON, i);
		}
		public SqlLatitudeParameterContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_sqlLatitudeParameter; }
	}

	public final SqlLatitudeParameterContext sqlLatitudeParameter() throws RecognitionException {
		SqlLatitudeParameterContext _localctx = new SqlLatitudeParameterContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_sqlLatitudeParameter);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(248);
			match(SQL_LATITUDE);
			setState(249);
			match(COLON);
			setState(250);
			daxExpression();
			setState(251);
			match(SEMICOLON);
			setState(252);
			match(SEMICOLON);
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

	public static class SqlLongitudeParameterContext extends ParserRuleContext {
		public TerminalNode SQL_LONGITUDE() { return getToken(CopperSimpleParser.SQL_LONGITUDE, 0); }
		public TerminalNode COLON() { return getToken(CopperSimpleParser.COLON, 0); }
		public DaxExpressionContext daxExpression() {
			return getRuleContext(DaxExpressionContext.class,0);
		}
		public List<TerminalNode> SEMICOLON() { return getTokens(CopperSimpleParser.SEMICOLON); }
		public TerminalNode SEMICOLON(int i) {
			return getToken(CopperSimpleParser.SEMICOLON, i);
		}
		public SqlLongitudeParameterContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_sqlLongitudeParameter; }
	}

	public final SqlLongitudeParameterContext sqlLongitudeParameter() throws RecognitionException {
		SqlLongitudeParameterContext _localctx = new SqlLongitudeParameterContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_sqlLongitudeParameter);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(254);
			match(SQL_LONGITUDE);
			setState(255);
			match(COLON);
			setState(256);
			daxExpression();
			setState(257);
			match(SEMICOLON);
			setState(258);
			match(SEMICOLON);
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

	public static class UnitsParameterContext extends ParserRuleContext {
		public TerminalNode UNITS() { return getToken(CopperSimpleParser.UNITS, 0); }
		public TerminalNode COLON() { return getToken(CopperSimpleParser.COLON, 0); }
		public StringValueContext stringValue() {
			return getRuleContext(StringValueContext.class,0);
		}
		public List<TerminalNode> SEMICOLON() { return getTokens(CopperSimpleParser.SEMICOLON); }
		public TerminalNode SEMICOLON(int i) {
			return getToken(CopperSimpleParser.SEMICOLON, i);
		}
		public UnitsParameterContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_unitsParameter; }
	}

	public final UnitsParameterContext unitsParameter() throws RecognitionException {
		UnitsParameterContext _localctx = new UnitsParameterContext(_ctx, getState());
		enterRule(_localctx, 46, RULE_unitsParameter);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(260);
			match(UNITS);
			setState(261);
			match(COLON);
			setState(262);
			stringValue();
			setState(263);
			match(SEMICOLON);
			setState(265);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==SEMICOLON) {
				{
				setState(264);
				match(SEMICOLON);
				}
			}

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

	public static class FromParameterContext extends ParserRuleContext {
		public TerminalNode FROM() { return getToken(CopperSimpleParser.FROM, 0); }
		public TerminalNode COLON() { return getToken(CopperSimpleParser.COLON, 0); }
		public IdentifierContext identifier() {
			return getRuleContext(IdentifierContext.class,0);
		}
		public List<TerminalNode> SEMICOLON() { return getTokens(CopperSimpleParser.SEMICOLON); }
		public TerminalNode SEMICOLON(int i) {
			return getToken(CopperSimpleParser.SEMICOLON, i);
		}
		public FromParameterContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_fromParameter; }
	}

	public final FromParameterContext fromParameter() throws RecognitionException {
		FromParameterContext _localctx = new FromParameterContext(_ctx, getState());
		enterRule(_localctx, 48, RULE_fromParameter);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(267);
			match(FROM);
			setState(268);
			match(COLON);
			setState(269);
			identifier();
			setState(270);
			match(SEMICOLON);
			setState(272);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==SEMICOLON) {
				{
				setState(271);
				match(SEMICOLON);
				}
			}

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

	public static class ExtendsParameterContext extends ParserRuleContext {
		public TerminalNode EXTENDS() { return getToken(CopperSimpleParser.EXTENDS, 0); }
		public TerminalNode COLON() { return getToken(CopperSimpleParser.COLON, 0); }
		public IdentifierContext identifier() {
			return getRuleContext(IdentifierContext.class,0);
		}
		public List<TerminalNode> SEMICOLON() { return getTokens(CopperSimpleParser.SEMICOLON); }
		public TerminalNode SEMICOLON(int i) {
			return getToken(CopperSimpleParser.SEMICOLON, i);
		}
		public ExtendsParameterContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_extendsParameter; }
	}

	public final ExtendsParameterContext extendsParameter() throws RecognitionException {
		ExtendsParameterContext _localctx = new ExtendsParameterContext(_ctx, getState());
		enterRule(_localctx, 50, RULE_extendsParameter);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(274);
			match(EXTENDS);
			setState(275);
			match(COLON);
			setState(276);
			identifier();
			setState(277);
			match(SEMICOLON);
			setState(279);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==SEMICOLON) {
				{
				setState(278);
				match(SEMICOLON);
				}
			}

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

	public static class RelationshipParameterContext extends ParserRuleContext {
		public TerminalNode RELATIONSHIP() { return getToken(CopperSimpleParser.RELATIONSHIP, 0); }
		public TerminalNode COLON() { return getToken(CopperSimpleParser.COLON, 0); }
		public RelationshipValueContext relationshipValue() {
			return getRuleContext(RelationshipValueContext.class,0);
		}
		public List<TerminalNode> SEMICOLON() { return getTokens(CopperSimpleParser.SEMICOLON); }
		public TerminalNode SEMICOLON(int i) {
			return getToken(CopperSimpleParser.SEMICOLON, i);
		}
		public RelationshipParameterContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_relationshipParameter; }
	}

	public final RelationshipParameterContext relationshipParameter() throws RecognitionException {
		RelationshipParameterContext _localctx = new RelationshipParameterContext(_ctx, getState());
		enterRule(_localctx, 52, RULE_relationshipParameter);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(281);
			match(RELATIONSHIP);
			setState(282);
			match(COLON);
			setState(283);
			relationshipValue();
			setState(284);
			match(SEMICOLON);
			setState(286);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==SEMICOLON) {
				{
				setState(285);
				match(SEMICOLON);
				}
			}

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

	public static class TypeValueContext extends ParserRuleContext {
		public TerminalNode STRING_TYPE() { return getToken(CopperSimpleParser.STRING_TYPE, 0); }
		public TerminalNode NUMBER_TYPE() { return getToken(CopperSimpleParser.NUMBER_TYPE, 0); }
		public TerminalNode DATE_TYPE() { return getToken(CopperSimpleParser.DATE_TYPE, 0); }
		public TerminalNode DATE_TIME_TYPE() { return getToken(CopperSimpleParser.DATE_TIME_TYPE, 0); }
		public TerminalNode YESNO_TYPE() { return getToken(CopperSimpleParser.YESNO_TYPE, 0); }
		public TerminalNode TIER_TYPE() { return getToken(CopperSimpleParser.TIER_TYPE, 0); }
		public TerminalNode BIN_TYPE() { return getToken(CopperSimpleParser.BIN_TYPE, 0); }
		public TerminalNode LOCATION_TYPE() { return getToken(CopperSimpleParser.LOCATION_TYPE, 0); }
		public TerminalNode ZIPCODE_TYPE() { return getToken(CopperSimpleParser.ZIPCODE_TYPE, 0); }
		public TerminalNode DISTANCE_TYPE() { return getToken(CopperSimpleParser.DISTANCE_TYPE, 0); }
		public TerminalNode DURATION_TYPE() { return getToken(CopperSimpleParser.DURATION_TYPE, 0); }
		public TerminalNode TIME_TYPE() { return getToken(CopperSimpleParser.TIME_TYPE, 0); }
		public TerminalNode UNQUOTED_TYPE() { return getToken(CopperSimpleParser.UNQUOTED_TYPE, 0); }
		public TerminalNode COUNT_TYPE() { return getToken(CopperSimpleParser.COUNT_TYPE, 0); }
		public TerminalNode SUM_TYPE() { return getToken(CopperSimpleParser.SUM_TYPE, 0); }
		public TerminalNode AVERAGE_TYPE() { return getToken(CopperSimpleParser.AVERAGE_TYPE, 0); }
		public TerminalNode MIN_TYPE() { return getToken(CopperSimpleParser.MIN_TYPE, 0); }
		public TerminalNode MAX_TYPE() { return getToken(CopperSimpleParser.MAX_TYPE, 0); }
		public TerminalNode COUNT_DISTINCT_TYPE() { return getToken(CopperSimpleParser.COUNT_DISTINCT_TYPE, 0); }
		public TerminalNode MEDIAN_TYPE() { return getToken(CopperSimpleParser.MEDIAN_TYPE, 0); }
		public TerminalNode PERCENTILE_TYPE() { return getToken(CopperSimpleParser.PERCENTILE_TYPE, 0); }
		public TypeValueContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_typeValue; }
	}

	public final TypeValueContext typeValue() throws RecognitionException {
		TypeValueContext _localctx = new TypeValueContext(_ctx, getState());
		enterRule(_localctx, 54, RULE_typeValue);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(288);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << STRING_TYPE) | (1L << NUMBER_TYPE) | (1L << DATE_TYPE) | (1L << DATE_TIME_TYPE) | (1L << YESNO_TYPE) | (1L << TIER_TYPE) | (1L << BIN_TYPE) | (1L << LOCATION_TYPE) | (1L << ZIPCODE_TYPE) | (1L << DISTANCE_TYPE) | (1L << DURATION_TYPE) | (1L << TIME_TYPE) | (1L << UNQUOTED_TYPE) | (1L << COUNT_TYPE) | (1L << SUM_TYPE) | (1L << AVERAGE_TYPE) | (1L << MIN_TYPE) | (1L << MAX_TYPE) | (1L << COUNT_DISTINCT_TYPE) | (1L << MEDIAN_TYPE) | (1L << PERCENTILE_TYPE))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
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

	public static class RelationshipValueContext extends ParserRuleContext {
		public TerminalNode ONE_TO_ONE() { return getToken(CopperSimpleParser.ONE_TO_ONE, 0); }
		public TerminalNode ONE_TO_MANY() { return getToken(CopperSimpleParser.ONE_TO_MANY, 0); }
		public TerminalNode MANY_TO_ONE() { return getToken(CopperSimpleParser.MANY_TO_ONE, 0); }
		public TerminalNode MANY_TO_MANY() { return getToken(CopperSimpleParser.MANY_TO_MANY, 0); }
		public RelationshipValueContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_relationshipValue; }
	}

	public final RelationshipValueContext relationshipValue() throws RecognitionException {
		RelationshipValueContext _localctx = new RelationshipValueContext(_ctx, getState());
		enterRule(_localctx, 56, RULE_relationshipValue);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(290);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << ONE_TO_ONE) | (1L << ONE_TO_MANY) | (1L << MANY_TO_ONE) | (1L << MANY_TO_MANY))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
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

	public static class BooleanValueContext extends ParserRuleContext {
		public TerminalNode YES() { return getToken(CopperSimpleParser.YES, 0); }
		public TerminalNode NO() { return getToken(CopperSimpleParser.NO, 0); }
		public BooleanValueContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_booleanValue; }
	}

	public final BooleanValueContext booleanValue() throws RecognitionException {
		BooleanValueContext _localctx = new BooleanValueContext(_ctx, getState());
		enterRule(_localctx, 58, RULE_booleanValue);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(292);
			_la = _input.LA(1);
			if ( !(_la==YES || _la==NO) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
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

	public static class StringValueContext extends ParserRuleContext {
		public TerminalNode STRING_LITERAL() { return getToken(CopperSimpleParser.STRING_LITERAL, 0); }
		public IdentifierContext identifier() {
			return getRuleContext(IdentifierContext.class,0);
		}
		public StringValueContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_stringValue; }
	}

	public final StringValueContext stringValue() throws RecognitionException {
		StringValueContext _localctx = new StringValueContext(_ctx, getState());
		enterRule(_localctx, 60, RULE_stringValue);
		try {
			setState(296);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case STRING_LITERAL:
				enterOuterAlt(_localctx, 1);
				{
				setState(294);
				match(STRING_LITERAL);
				}
				break;
			case IDENTIFIER:
				enterOuterAlt(_localctx, 2);
				{
				setState(295);
				identifier();
				}
				break;
			default:
				throw new NoViableAltException(this);
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

	public static class FormatValueContext extends ParserRuleContext {
		public TerminalNode USD() { return getToken(CopperSimpleParser.USD, 0); }
		public TerminalNode PERCENT() { return getToken(CopperSimpleParser.PERCENT, 0); }
		public TerminalNode PERCENT_1() { return getToken(CopperSimpleParser.PERCENT_1, 0); }
		public TerminalNode PERCENT_2() { return getToken(CopperSimpleParser.PERCENT_2, 0); }
		public TerminalNode STRING_LITERAL() { return getToken(CopperSimpleParser.STRING_LITERAL, 0); }
		public FormatValueContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_formatValue; }
	}

	public final FormatValueContext formatValue() throws RecognitionException {
		FormatValueContext _localctx = new FormatValueContext(_ctx, getState());
		enterRule(_localctx, 62, RULE_formatValue);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(298);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << USD) | (1L << PERCENT) | (1L << PERCENT_1) | (1L << PERCENT_2) | (1L << STRING_LITERAL))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
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

	public static class ArrayValueContext extends ParserRuleContext {
		public TerminalNode LBRACKET() { return getToken(CopperSimpleParser.LBRACKET, 0); }
		public TerminalNode RBRACKET() { return getToken(CopperSimpleParser.RBRACKET, 0); }
		public List<TerminalNode> STRING_LITERAL() { return getTokens(CopperSimpleParser.STRING_LITERAL); }
		public TerminalNode STRING_LITERAL(int i) {
			return getToken(CopperSimpleParser.STRING_LITERAL, i);
		}
		public List<TerminalNode> COMMA() { return getTokens(CopperSimpleParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(CopperSimpleParser.COMMA, i);
		}
		public ArrayValueContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_arrayValue; }
	}

	public final ArrayValueContext arrayValue() throws RecognitionException {
		ArrayValueContext _localctx = new ArrayValueContext(_ctx, getState());
		enterRule(_localctx, 64, RULE_arrayValue);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(300);
			match(LBRACKET);
			setState(309);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==STRING_LITERAL) {
				{
				setState(301);
				match(STRING_LITERAL);
				setState(306);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==COMMA) {
					{
					{
					setState(302);
					match(COMMA);
					setState(303);
					match(STRING_LITERAL);
					}
					}
					setState(308);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			setState(311);
			match(RBRACKET);
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

	public static class DaxExpressionContext extends ParserRuleContext {
		public TerminalNode DAX_EXPRESSION() { return getToken(CopperSimpleParser.DAX_EXPRESSION, 0); }
		public DaxExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_daxExpression; }
	}

	public final DaxExpressionContext daxExpression() throws RecognitionException {
		DaxExpressionContext _localctx = new DaxExpressionContext(_ctx, getState());
		enterRule(_localctx, 66, RULE_daxExpression);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(313);
			match(DAX_EXPRESSION);
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

	public static class IdentifierContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(CopperSimpleParser.IDENTIFIER, 0); }
		public IdentifierContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_identifier; }
	}

	public final IdentifierContext identifier() throws RecognitionException {
		IdentifierContext _localctx = new IdentifierContext(_ctx, getState());
		enterRule(_localctx, 68, RULE_identifier);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(315);
			match(IDENTIFIER);
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

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3B\u0140\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\3\2\7\2J\n\2\f\2\16\2M\13\2\3\2\3\2\3\3\3\3\3"+
		"\3\3\3\5\3U\n\3\3\4\3\4\3\5\3\5\3\5\3\5\3\5\7\5^\n\5\f\5\16\5a\13\5\3"+
		"\5\3\5\3\6\3\6\3\6\3\6\5\6i\n\6\3\7\3\7\3\7\3\7\3\7\7\7p\n\7\f\7\16\7"+
		"s\13\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\7\b|\n\b\f\b\16\b\177\13\b\3\b\3\b"+
		"\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\5\t\u0090\n\t\3\n"+
		"\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\5\n\u009b\n\n\3\13\3\13\3\13\3\13\3\13"+
		"\7\13\u00a2\n\13\f\13\16\13\u00a5\13\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f"+
		"\3\f\3\f\5\f\u00b0\n\f\3\r\3\r\3\r\3\r\3\r\7\r\u00b7\n\r\f\r\16\r\u00ba"+
		"\13\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\5\16\u00c3\n\16\3\17\3\17\3\17"+
		"\3\17\3\17\5\17\u00ca\n\17\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21"+
		"\3\21\3\21\5\21\u00d7\n\21\3\22\3\22\3\22\3\22\3\22\5\22\u00de\n\22\3"+
		"\23\3\23\3\23\3\23\3\23\5\23\u00e5\n\23\3\24\3\24\3\24\3\24\3\24\5\24"+
		"\u00ec\n\24\3\25\3\25\3\25\3\25\3\25\5\25\u00f3\n\25\3\26\3\26\3\26\3"+
		"\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3"+
		"\30\3\31\3\31\3\31\3\31\3\31\5\31\u010c\n\31\3\32\3\32\3\32\3\32\3\32"+
		"\5\32\u0113\n\32\3\33\3\33\3\33\3\33\3\33\5\33\u011a\n\33\3\34\3\34\3"+
		"\34\3\34\3\34\5\34\u0121\n\34\3\35\3\35\3\36\3\36\3\37\3\37\3 \3 \5 \u012b"+
		"\n \3!\3!\3\"\3\"\3\"\3\"\7\"\u0133\n\"\f\"\16\"\u0136\13\"\5\"\u0138"+
		"\n\"\3\"\3\"\3#\3#\3$\3$\3$\2\2%\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36"+
		" \"$&(*,.\60\62\64\668:<>@BDF\2\6\3\2\26*\3\2+.\3\2/\60\4\2\61\64>>\2"+
		"\u0153\2K\3\2\2\2\4T\3\2\2\2\6V\3\2\2\2\bX\3\2\2\2\nh\3\2\2\2\fj\3\2\2"+
		"\2\16v\3\2\2\2\20\u008f\3\2\2\2\22\u009a\3\2\2\2\24\u009c\3\2\2\2\26\u00af"+
		"\3\2\2\2\30\u00b1\3\2\2\2\32\u00c2\3\2\2\2\34\u00c4\3\2\2\2\36\u00cb\3"+
		"\2\2\2 \u00d1\3\2\2\2\"\u00d8\3\2\2\2$\u00df\3\2\2\2&\u00e6\3\2\2\2(\u00ed"+
		"\3\2\2\2*\u00f4\3\2\2\2,\u00fa\3\2\2\2.\u0100\3\2\2\2\60\u0106\3\2\2\2"+
		"\62\u010d\3\2\2\2\64\u0114\3\2\2\2\66\u011b\3\2\2\28\u0122\3\2\2\2:\u0124"+
		"\3\2\2\2<\u0126\3\2\2\2>\u012a\3\2\2\2@\u012c\3\2\2\2B\u012e\3\2\2\2D"+
		"\u013b\3\2\2\2F\u013d\3\2\2\2HJ\5\4\3\2IH\3\2\2\2JM\3\2\2\2KI\3\2\2\2"+
		"KL\3\2\2\2LN\3\2\2\2MK\3\2\2\2NO\7\2\2\3O\3\3\2\2\2PU\5\b\5\2QU\5\24\13"+
		"\2RU\5\6\4\2SU\7A\2\2TP\3\2\2\2TQ\3\2\2\2TR\3\2\2\2TS\3\2\2\2U\5\3\2\2"+
		"\2VW\7@\2\2W\7\3\2\2\2XY\7\3\2\2YZ\7\65\2\2Z[\5F$\2[_\7\67\2\2\\^\5\n"+
		"\6\2]\\\3\2\2\2^a\3\2\2\2_]\3\2\2\2_`\3\2\2\2`b\3\2\2\2a_\3\2\2\2bc\7"+
		"8\2\2c\t\3\2\2\2di\5\f\7\2ei\5\16\b\2fi\5\6\4\2gi\7A\2\2hd\3\2\2\2he\3"+
		"\2\2\2hf\3\2\2\2hg\3\2\2\2i\13\3\2\2\2jk\7\5\2\2kl\7\65\2\2lm\5F$\2mq"+
		"\7\67\2\2np\5\20\t\2on\3\2\2\2ps\3\2\2\2qo\3\2\2\2qr\3\2\2\2rt\3\2\2\2"+
		"sq\3\2\2\2tu\78\2\2u\r\3\2\2\2vw\7\6\2\2wx\7\65\2\2xy\5F$\2y}\7\67\2\2"+
		"z|\5\22\n\2{z\3\2\2\2|\177\3\2\2\2}{\3\2\2\2}~\3\2\2\2~\u0080\3\2\2\2"+
		"\177}\3\2\2\2\u0080\u0081\78\2\2\u0081\17\3\2\2\2\u0082\u0090\5\34\17"+
		"\2\u0083\u0090\5\36\20\2\u0084\u0090\5 \21\2\u0085\u0090\5\"\22\2\u0086"+
		"\u0090\5$\23\2\u0087\u0090\5&\24\2\u0088\u0090\5(\25\2\u0089\u0090\5*"+
		"\26\2\u008a\u0090\5,\27\2\u008b\u0090\5.\30\2\u008c\u0090\5\60\31\2\u008d"+
		"\u0090\5\6\4\2\u008e\u0090\7A\2\2\u008f\u0082\3\2\2\2\u008f\u0083\3\2"+
		"\2\2\u008f\u0084\3\2\2\2\u008f\u0085\3\2\2\2\u008f\u0086\3\2\2\2\u008f"+
		"\u0087\3\2\2\2\u008f\u0088\3\2\2\2\u008f\u0089\3\2\2\2\u008f\u008a\3\2"+
		"\2\2\u008f\u008b\3\2\2\2\u008f\u008c\3\2\2\2\u008f\u008d\3\2\2\2\u008f"+
		"\u008e\3\2\2\2\u0090\21\3\2\2\2\u0091\u009b\5\34\17\2\u0092\u009b\5\36"+
		"\20\2\u0093\u009b\5 \21\2\u0094\u009b\5\"\22\2\u0095\u009b\5&\24\2\u0096"+
		"\u009b\5(\25\2\u0097\u009b\5\60\31\2\u0098\u009b\5\6\4\2\u0099\u009b\7"+
		"A\2\2\u009a\u0091\3\2\2\2\u009a\u0092\3\2\2\2\u009a\u0093\3\2\2\2\u009a"+
		"\u0094\3\2\2\2\u009a\u0095\3\2\2\2\u009a\u0096\3\2\2\2\u009a\u0097\3\2"+
		"\2\2\u009a\u0098\3\2\2\2\u009a\u0099\3\2\2\2\u009b\23\3\2\2\2\u009c\u009d"+
		"\7\4\2\2\u009d\u009e\7\65\2\2\u009e\u009f\5F$\2\u009f\u00a3\7\67\2\2\u00a0"+
		"\u00a2\5\26\f\2\u00a1\u00a0\3\2\2\2\u00a2\u00a5\3\2\2\2\u00a3\u00a1\3"+
		"\2\2\2\u00a3\u00a4\3\2\2\2\u00a4\u00a6\3\2\2\2\u00a5\u00a3\3\2\2\2\u00a6"+
		"\u00a7\78\2\2\u00a7\25\3\2\2\2\u00a8\u00b0\5\62\32\2\u00a9\u00b0\5\64"+
		"\33\2\u00aa\u00b0\5\30\r\2\u00ab\u00b0\5\f\7\2\u00ac\u00b0\5\16\b\2\u00ad"+
		"\u00b0\5\6\4\2\u00ae\u00b0\7A\2\2\u00af\u00a8\3\2\2\2\u00af\u00a9\3\2"+
		"\2\2\u00af\u00aa\3\2\2\2\u00af\u00ab\3\2\2\2\u00af\u00ac\3\2\2\2\u00af"+
		"\u00ad\3\2\2\2\u00af\u00ae\3\2\2\2\u00b0\27\3\2\2\2\u00b1\u00b2\7\7\2"+
		"\2\u00b2\u00b3\7\65\2\2\u00b3\u00b4\5F$\2\u00b4\u00b8\7\67\2\2\u00b5\u00b7"+
		"\5\32\16\2\u00b6\u00b5\3\2\2\2\u00b7\u00ba\3\2\2\2\u00b8\u00b6\3\2\2\2"+
		"\u00b8\u00b9\3\2\2\2\u00b9\u00bb\3\2\2\2\u00ba\u00b8\3\2\2\2\u00bb\u00bc"+
		"\78\2\2\u00bc\31\3\2\2\2\u00bd\u00c3\5\34\17\2\u00be\u00c3\5\66\34\2\u00bf"+
		"\u00c3\5\36\20\2\u00c0\u00c3\5\6\4\2\u00c1\u00c3\7A\2\2\u00c2\u00bd\3"+
		"\2\2\2\u00c2\u00be\3\2\2\2\u00c2\u00bf\3\2\2\2\u00c2\u00c0\3\2\2\2\u00c2"+
		"\u00c1\3\2\2\2\u00c3\33\3\2\2\2\u00c4\u00c5\7\n\2\2\u00c5\u00c6\7\65\2"+
		"\2\u00c6\u00c7\58\35\2\u00c7\u00c9\7\66\2\2\u00c8\u00ca\7\66\2\2\u00c9"+
		"\u00c8\3\2\2\2\u00c9\u00ca\3\2\2\2\u00ca\35\3\2\2\2\u00cb\u00cc\7\13\2"+
		"\2\u00cc\u00cd\7\65\2\2\u00cd\u00ce\5D#\2\u00ce\u00cf\7\66\2\2\u00cf\u00d0"+
		"\7\66\2\2\u00d0\37\3\2\2\2\u00d1\u00d2\7\16\2\2\u00d2\u00d3\7\65\2\2\u00d3"+
		"\u00d4\5> \2\u00d4\u00d6\7\66\2\2\u00d5\u00d7\7\66\2\2\u00d6\u00d5\3\2"+
		"\2\2\u00d6\u00d7\3\2\2\2\u00d7!\3\2\2\2\u00d8\u00d9\7\17\2\2\u00d9\u00da"+
		"\7\65\2\2\u00da\u00db\5> \2\u00db\u00dd\7\66\2\2\u00dc\u00de\7\66\2\2"+
		"\u00dd\u00dc\3\2\2\2\u00dd\u00de\3\2\2\2\u00de#\3\2\2\2\u00df\u00e0\7"+
		"\f\2\2\u00e0\u00e1\7\65\2\2\u00e1\u00e2\5<\37\2\u00e2\u00e4\7\66\2\2\u00e3"+
		"\u00e5\7\66\2\2\u00e4\u00e3\3\2\2\2\u00e4\u00e5\3\2\2\2\u00e5%\3\2\2\2"+
		"\u00e6\u00e7\7\20\2\2\u00e7\u00e8\7\65\2\2\u00e8\u00e9\5<\37\2\u00e9\u00eb"+
		"\7\66\2\2\u00ea\u00ec\7\66\2\2\u00eb\u00ea\3\2\2\2\u00eb\u00ec\3\2\2\2"+
		"\u00ec\'\3\2\2\2\u00ed\u00ee\7\r\2\2\u00ee\u00ef\7\65\2\2\u00ef\u00f0"+
		"\5@!\2\u00f0\u00f2\7\66\2\2\u00f1\u00f3\7\66\2\2\u00f2\u00f1\3\2\2\2\u00f2"+
		"\u00f3\3\2\2\2\u00f3)\3\2\2\2\u00f4\u00f5\7\21\2\2\u00f5\u00f6\7\65\2"+
		"\2\u00f6\u00f7\5B\"\2\u00f7\u00f8\7\66\2\2\u00f8\u00f9\7\66\2\2\u00f9"+
		"+\3\2\2\2\u00fa\u00fb\7\22\2\2\u00fb\u00fc\7\65\2\2\u00fc\u00fd\5D#\2"+
		"\u00fd\u00fe\7\66\2\2\u00fe\u00ff\7\66\2\2\u00ff-\3\2\2\2\u0100\u0101"+
		"\7\23\2\2\u0101\u0102\7\65\2\2\u0102\u0103\5D#\2\u0103\u0104\7\66\2\2"+
		"\u0104\u0105\7\66\2\2\u0105/\3\2\2\2\u0106\u0107\7\24\2\2\u0107\u0108"+
		"\7\65\2\2\u0108\u0109\5> \2\u0109\u010b\7\66\2\2\u010a\u010c\7\66\2\2"+
		"\u010b\u010a\3\2\2\2\u010b\u010c\3\2\2\2\u010c\61\3\2\2\2\u010d\u010e"+
		"\7\b\2\2\u010e\u010f\7\65\2\2\u010f\u0110\5F$\2\u0110\u0112\7\66\2\2\u0111"+
		"\u0113\7\66\2\2\u0112\u0111\3\2\2\2\u0112\u0113\3\2\2\2\u0113\63\3\2\2"+
		"\2\u0114\u0115\7\t\2\2\u0115\u0116\7\65\2\2\u0116\u0117\5F$\2\u0117\u0119"+
		"\7\66\2\2\u0118\u011a\7\66\2\2\u0119\u0118\3\2\2\2\u0119\u011a\3\2\2\2"+
		"\u011a\65\3\2\2\2\u011b\u011c\7\25\2\2\u011c\u011d\7\65\2\2\u011d\u011e"+
		"\5:\36\2\u011e\u0120\7\66\2\2\u011f\u0121\7\66\2\2\u0120\u011f\3\2\2\2"+
		"\u0120\u0121\3\2\2\2\u0121\67\3\2\2\2\u0122\u0123\t\2\2\2\u01239\3\2\2"+
		"\2\u0124\u0125\t\3\2\2\u0125;\3\2\2\2\u0126\u0127\t\4\2\2\u0127=\3\2\2"+
		"\2\u0128\u012b\7>\2\2\u0129\u012b\5F$\2\u012a\u0128\3\2\2\2\u012a\u0129"+
		"\3\2\2\2\u012b?\3\2\2\2\u012c\u012d\t\5\2\2\u012dA\3\2\2\2\u012e\u0137"+
		"\79\2\2\u012f\u0134\7>\2\2\u0130\u0131\7;\2\2\u0131\u0133\7>\2\2\u0132"+
		"\u0130\3\2\2\2\u0133\u0136\3\2\2\2\u0134\u0132\3\2\2\2\u0134\u0135\3\2"+
		"\2\2\u0135\u0138\3\2\2\2\u0136\u0134\3\2\2\2\u0137\u012f\3\2\2\2\u0137"+
		"\u0138\3\2\2\2\u0138\u0139\3\2\2\2\u0139\u013a\7:\2\2\u013aC\3\2\2\2\u013b"+
		"\u013c\7?\2\2\u013cE\3\2\2\2\u013d\u013e\7<\2\2\u013eG\3\2\2\2\33KT_h"+
		"q}\u008f\u009a\u00a3\u00af\u00b8\u00c2\u00c9\u00d6\u00dd\u00e4\u00eb\u00f2"+
		"\u010b\u0112\u0119\u0120\u012a\u0134\u0137";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}