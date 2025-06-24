// Generated from /home/surya/code/copper/grammar/CopperSimple.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class CopperSimpleLexer extends Lexer {
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
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"MODEL", "VIEW", "DIMENSION", "MEASURE", "JOIN", "FROM", "EXTENDS", "TYPE", 
			"EXPRESSION", "PRIMARY_KEY", "VALUE_FORMAT", "LABEL", "DESCRIPTION", 
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


	public CopperSimpleLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "CopperSimple.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2B\u025c\b\1\4\2\t"+
		"\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4"+
		",\t,\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t"+
		"\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t;\4<\t<\4=\t="+
		"\4>\t>\4?\t?\4@\t@\4A\tA\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3"+
		"\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5"+
		"\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3"+
		"\b\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13"+
		"\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3"+
		"\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3"+
		"\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3"+
		"\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3"+
		"\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3"+
		"\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3"+
		"\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3"+
		"\25\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3"+
		"\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3"+
		"\30\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3"+
		"\33\3\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3"+
		"\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3"+
		"\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3 \3!\3!\3!\3"+
		"!\3!\3!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3$\3$\3$\3$\3$\3"+
		"$\3$\3$\3%\3%\3%\3%\3&\3&\3&\3&\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3"+
		"\'\3\'\3\'\3\'\3\'\3\'\3(\3(\3(\3(\3(\3(\3(\3)\3)\3)\3)\3)\3)\3)\3)\3"+
		")\3)\3)\3*\3*\3*\3*\3*\3*\3*\3*\3*\3*\3*\3+\3+\3+\3+\3+\3+\3+\3+\3+\3"+
		"+\3+\3+\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3-\3-\3-\3-\3-\3-\3-\3-\3"+
		"-\3-\3-\3-\3-\3.\3.\3.\3.\3/\3/\3/\3\60\3\60\3\60\3\60\3\61\3\61\3\61"+
		"\3\61\3\61\3\61\3\61\3\61\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62"+
		"\3\62\3\63\3\63\3\63\3\63\3\63\3\63\3\63\3\63\3\63\3\63\3\64\3\64\3\65"+
		"\3\65\3\66\3\66\3\67\3\67\38\38\39\39\3:\3:\3;\3;\7;\u0228\n;\f;\16;\u022b"+
		"\13;\3<\6<\u022e\n<\r<\16<\u022f\3=\3=\3=\3=\7=\u0236\n=\f=\16=\u0239"+
		"\13=\3=\3=\3>\3>\7>\u023f\n>\f>\16>\u0242\13>\3>\3>\3>\3?\3?\7?\u0249"+
		"\n?\f?\16?\u024c\13?\3@\5@\u024f\n@\3@\6@\u0252\n@\r@\16@\u0253\3A\6A"+
		"\u0257\nA\rA\16A\u0258\3A\3A\3\u0240\2B\3\3\5\4\7\5\t\6\13\7\r\b\17\t"+
		"\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27"+
		"-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W"+
		"-Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m8o9q:s;u<w=y>{?}@\177A\u0081B\3"+
		"\2\b\5\2C\\aac|\6\2\62;C\\aac|\3\2\62;\6\2\f\f\17\17$$^^\4\2\f\f\17\17"+
		"\4\2\13\13\"\"\2\u0264\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2"+
		"\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25"+
		"\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2"+
		"\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2"+
		"\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3"+
		"\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2"+
		"\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2"+
		"Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3"+
		"\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2"+
		"\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2"+
		"w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2"+
		"\2\3\u0083\3\2\2\2\5\u0089\3\2\2\2\7\u008e\3\2\2\2\t\u0098\3\2\2\2\13"+
		"\u00a0\3\2\2\2\r\u00a5\3\2\2\2\17\u00aa\3\2\2\2\21\u00b2\3\2\2\2\23\u00b7"+
		"\3\2\2\2\25\u00c2\3\2\2\2\27\u00ce\3\2\2\2\31\u00db\3\2\2\2\33\u00e1\3"+
		"\2\2\2\35\u00ed\3\2\2\2\37\u00f4\3\2\2\2!\u00fa\3\2\2\2#\u0107\3\2\2\2"+
		"%\u0115\3\2\2\2\'\u011b\3\2\2\2)\u0128\3\2\2\2+\u012f\3\2\2\2-\u0136\3"+
		"\2\2\2/\u013b\3\2\2\2\61\u0145\3\2\2\2\63\u014b\3\2\2\2\65\u0150\3\2\2"+
		"\2\67\u0154\3\2\2\29\u015d\3\2\2\2;\u0165\3\2\2\2=\u016e\3\2\2\2?\u0177"+
		"\3\2\2\2A\u017c\3\2\2\2C\u0185\3\2\2\2E\u018b\3\2\2\2G\u018f\3\2\2\2I"+
		"\u0197\3\2\2\2K\u019b\3\2\2\2M\u019f\3\2\2\2O\u01ae\3\2\2\2Q\u01b5\3\2"+
		"\2\2S\u01c0\3\2\2\2U\u01cb\3\2\2\2W\u01d7\3\2\2\2Y\u01e3\3\2\2\2[\u01f0"+
		"\3\2\2\2]\u01f4\3\2\2\2_\u01f7\3\2\2\2a\u01fb\3\2\2\2c\u0203\3\2\2\2e"+
		"\u020d\3\2\2\2g\u0217\3\2\2\2i\u0219\3\2\2\2k\u021b\3\2\2\2m\u021d\3\2"+
		"\2\2o\u021f\3\2\2\2q\u0221\3\2\2\2s\u0223\3\2\2\2u\u0225\3\2\2\2w\u022d"+
		"\3\2\2\2y\u0231\3\2\2\2{\u023c\3\2\2\2}\u0246\3\2\2\2\177\u024e\3\2\2"+
		"\2\u0081\u0256\3\2\2\2\u0083\u0084\7o\2\2\u0084\u0085\7q\2\2\u0085\u0086"+
		"\7f\2\2\u0086\u0087\7g\2\2\u0087\u0088\7n\2\2\u0088\4\3\2\2\2\u0089\u008a"+
		"\7x\2\2\u008a\u008b\7k\2\2\u008b\u008c\7g\2\2\u008c\u008d\7y\2\2\u008d"+
		"\6\3\2\2\2\u008e\u008f\7f\2\2\u008f\u0090\7k\2\2\u0090\u0091\7o\2\2\u0091"+
		"\u0092\7g\2\2\u0092\u0093\7p\2\2\u0093\u0094\7u\2\2\u0094\u0095\7k\2\2"+
		"\u0095\u0096\7q\2\2\u0096\u0097\7p\2\2\u0097\b\3\2\2\2\u0098\u0099\7o"+
		"\2\2\u0099\u009a\7g\2\2\u009a\u009b\7c\2\2\u009b\u009c\7u\2\2\u009c\u009d"+
		"\7w\2\2\u009d\u009e\7t\2\2\u009e\u009f\7g\2\2\u009f\n\3\2\2\2\u00a0\u00a1"+
		"\7l\2\2\u00a1\u00a2\7q\2\2\u00a2\u00a3\7k\2\2\u00a3\u00a4\7p\2\2\u00a4"+
		"\f\3\2\2\2\u00a5\u00a6\7h\2\2\u00a6\u00a7\7t\2\2\u00a7\u00a8\7q\2\2\u00a8"+
		"\u00a9\7o\2\2\u00a9\16\3\2\2\2\u00aa\u00ab\7g\2\2\u00ab\u00ac\7z\2\2\u00ac"+
		"\u00ad\7v\2\2\u00ad\u00ae\7g\2\2\u00ae\u00af\7p\2\2\u00af\u00b0\7f\2\2"+
		"\u00b0\u00b1\7u\2\2\u00b1\20\3\2\2\2\u00b2\u00b3\7v\2\2\u00b3\u00b4\7"+
		"{\2\2\u00b4\u00b5\7r\2\2\u00b5\u00b6\7g\2\2\u00b6\22\3\2\2\2\u00b7\u00b8"+
		"\7g\2\2\u00b8\u00b9\7z\2\2\u00b9\u00ba\7r\2\2\u00ba\u00bb\7t\2\2\u00bb"+
		"\u00bc\7g\2\2\u00bc\u00bd\7u\2\2\u00bd\u00be\7u\2\2\u00be\u00bf\7k\2\2"+
		"\u00bf\u00c0\7q\2\2\u00c0\u00c1\7p\2\2\u00c1\24\3\2\2\2\u00c2\u00c3\7"+
		"r\2\2\u00c3\u00c4\7t\2\2\u00c4\u00c5\7k\2\2\u00c5\u00c6\7o\2\2\u00c6\u00c7"+
		"\7c\2\2\u00c7\u00c8\7t\2\2\u00c8\u00c9\7{\2\2\u00c9\u00ca\7a\2\2\u00ca"+
		"\u00cb\7m\2\2\u00cb\u00cc\7g\2\2\u00cc\u00cd\7{\2\2\u00cd\26\3\2\2\2\u00ce"+
		"\u00cf\7x\2\2\u00cf\u00d0\7c\2\2\u00d0\u00d1\7n\2\2\u00d1\u00d2\7w\2\2"+
		"\u00d2\u00d3\7g\2\2\u00d3\u00d4\7a\2\2\u00d4\u00d5\7h\2\2\u00d5\u00d6"+
		"\7q\2\2\u00d6\u00d7\7t\2\2\u00d7\u00d8\7o\2\2\u00d8\u00d9\7c\2\2\u00d9"+
		"\u00da\7v\2\2\u00da\30\3\2\2\2\u00db\u00dc\7n\2\2\u00dc\u00dd\7c\2\2\u00dd"+
		"\u00de\7d\2\2\u00de\u00df\7g\2\2\u00df\u00e0\7n\2\2\u00e0\32\3\2\2\2\u00e1"+
		"\u00e2\7f\2\2\u00e2\u00e3\7g\2\2\u00e3\u00e4\7u\2\2\u00e4\u00e5\7e\2\2"+
		"\u00e5\u00e6\7t\2\2\u00e6\u00e7\7k\2\2\u00e7\u00e8\7r\2\2\u00e8\u00e9"+
		"\7v\2\2\u00e9\u00ea\7k\2\2\u00ea\u00eb\7q\2\2\u00eb\u00ec\7p\2\2\u00ec"+
		"\34\3\2\2\2\u00ed\u00ee\7j\2\2\u00ee\u00ef\7k\2\2\u00ef\u00f0\7f\2\2\u00f0"+
		"\u00f1\7f\2\2\u00f1\u00f2\7g\2\2\u00f2\u00f3\7p\2\2\u00f3\36\3\2\2\2\u00f4"+
		"\u00f5\7v\2\2\u00f5\u00f6\7k\2\2\u00f6\u00f7\7g\2\2\u00f7\u00f8\7t\2\2"+
		"\u00f8\u00f9\7u\2\2\u00f9 \3\2\2\2\u00fa\u00fb\7u\2\2\u00fb\u00fc\7s\2"+
		"\2\u00fc\u00fd\7n\2\2\u00fd\u00fe\7a\2\2\u00fe\u00ff\7n\2\2\u00ff\u0100"+
		"\7c\2\2\u0100\u0101\7v\2\2\u0101\u0102\7k\2\2\u0102\u0103\7v\2\2\u0103"+
		"\u0104\7w\2\2\u0104\u0105\7f\2\2\u0105\u0106\7g\2\2\u0106\"\3\2\2\2\u0107"+
		"\u0108\7u\2\2\u0108\u0109\7s\2\2\u0109\u010a\7n\2\2\u010a\u010b\7a\2\2"+
		"\u010b\u010c\7n\2\2\u010c\u010d\7q\2\2\u010d\u010e\7p\2\2\u010e\u010f"+
		"\7i\2\2\u010f\u0110\7k\2\2\u0110\u0111\7v\2\2\u0111\u0112\7w\2\2\u0112"+
		"\u0113\7f\2\2\u0113\u0114\7g\2\2\u0114$\3\2\2\2\u0115\u0116\7w\2\2\u0116"+
		"\u0117\7p\2\2\u0117\u0118\7k\2\2\u0118\u0119\7v\2\2\u0119\u011a\7u\2\2"+
		"\u011a&\3\2\2\2\u011b\u011c\7t\2\2\u011c\u011d\7g\2\2\u011d\u011e\7n\2"+
		"\2\u011e\u011f\7c\2\2\u011f\u0120\7v\2\2\u0120\u0121\7k\2\2\u0121\u0122"+
		"\7q\2\2\u0122\u0123\7p\2\2\u0123\u0124\7u\2\2\u0124\u0125\7j\2\2\u0125"+
		"\u0126\7k\2\2\u0126\u0127\7r\2\2\u0127(\3\2\2\2\u0128\u0129\7u\2\2\u0129"+
		"\u012a\7v\2\2\u012a\u012b\7t\2\2\u012b\u012c\7k\2\2\u012c\u012d\7p\2\2"+
		"\u012d\u012e\7i\2\2\u012e*\3\2\2\2\u012f\u0130\7p\2\2\u0130\u0131\7w\2"+
		"\2\u0131\u0132\7o\2\2\u0132\u0133\7d\2\2\u0133\u0134\7g\2\2\u0134\u0135"+
		"\7t\2\2\u0135,\3\2\2\2\u0136\u0137\7f\2\2\u0137\u0138\7c\2\2\u0138\u0139"+
		"\7v\2\2\u0139\u013a\7g\2\2\u013a.\3\2\2\2\u013b\u013c\7f\2\2\u013c\u013d"+
		"\7c\2\2\u013d\u013e\7v\2\2\u013e\u013f\7g\2\2\u013f\u0140\7a\2\2\u0140"+
		"\u0141\7v\2\2\u0141\u0142\7k\2\2\u0142\u0143\7o\2\2\u0143\u0144\7g\2\2"+
		"\u0144\60\3\2\2\2\u0145\u0146\7{\2\2\u0146\u0147\7g\2\2\u0147\u0148\7"+
		"u\2\2\u0148\u0149\7p\2\2\u0149\u014a\7q\2\2\u014a\62\3\2\2\2\u014b\u014c"+
		"\7v\2\2\u014c\u014d\7k\2\2\u014d\u014e\7g\2\2\u014e\u014f\7t\2\2\u014f"+
		"\64\3\2\2\2\u0150\u0151\7d\2\2\u0151\u0152\7k\2\2\u0152\u0153\7p\2\2\u0153"+
		"\66\3\2\2\2\u0154\u0155\7n\2\2\u0155\u0156\7q\2\2\u0156\u0157\7e\2\2\u0157"+
		"\u0158\7c\2\2\u0158\u0159\7v\2\2\u0159\u015a\7k\2\2\u015a\u015b\7q\2\2"+
		"\u015b\u015c\7p\2\2\u015c8\3\2\2\2\u015d\u015e\7|\2\2\u015e\u015f\7k\2"+
		"\2\u015f\u0160\7r\2\2\u0160\u0161\7e\2\2\u0161\u0162\7q\2\2\u0162\u0163"+
		"\7f\2\2\u0163\u0164\7g\2\2\u0164:\3\2\2\2\u0165\u0166\7f\2\2\u0166\u0167"+
		"\7k\2\2\u0167\u0168\7u\2\2\u0168\u0169\7v\2\2\u0169\u016a\7c\2\2\u016a"+
		"\u016b\7p\2\2\u016b\u016c\7e\2\2\u016c\u016d\7g\2\2\u016d<\3\2\2\2\u016e"+
		"\u016f\7f\2\2\u016f\u0170\7w\2\2\u0170\u0171\7t\2\2\u0171\u0172\7c\2\2"+
		"\u0172\u0173\7v\2\2\u0173\u0174\7k\2\2\u0174\u0175\7q\2\2\u0175\u0176"+
		"\7p\2\2\u0176>\3\2\2\2\u0177\u0178\7v\2\2\u0178\u0179\7k\2\2\u0179\u017a"+
		"\7o\2\2\u017a\u017b\7g\2\2\u017b@\3\2\2\2\u017c\u017d\7w\2\2\u017d\u017e"+
		"\7p\2\2\u017e\u017f\7s\2\2\u017f\u0180\7w\2\2\u0180\u0181\7q\2\2\u0181"+
		"\u0182\7v\2\2\u0182\u0183\7g\2\2\u0183\u0184\7f\2\2\u0184B\3\2\2\2\u0185"+
		"\u0186\7e\2\2\u0186\u0187\7q\2\2\u0187\u0188\7w\2\2\u0188\u0189\7p\2\2"+
		"\u0189\u018a\7v\2\2\u018aD\3\2\2\2\u018b\u018c\7u\2\2\u018c\u018d\7w\2"+
		"\2\u018d\u018e\7o\2\2\u018eF\3\2\2\2\u018f\u0190\7c\2\2\u0190\u0191\7"+
		"x\2\2\u0191\u0192\7g\2\2\u0192\u0193\7t\2\2\u0193\u0194\7c\2\2\u0194\u0195"+
		"\7i\2\2\u0195\u0196\7g\2\2\u0196H\3\2\2\2\u0197\u0198\7o\2\2\u0198\u0199"+
		"\7k\2\2\u0199\u019a\7p\2\2\u019aJ\3\2\2\2\u019b\u019c\7o\2\2\u019c\u019d"+
		"\7c\2\2\u019d\u019e\7z\2\2\u019eL\3\2\2\2\u019f\u01a0\7e\2\2\u01a0\u01a1"+
		"\7q\2\2\u01a1\u01a2\7w\2\2\u01a2\u01a3\7p\2\2\u01a3\u01a4\7v\2\2\u01a4"+
		"\u01a5\7a\2\2\u01a5\u01a6\7f\2\2\u01a6\u01a7\7k\2\2\u01a7\u01a8\7u\2\2"+
		"\u01a8\u01a9\7v\2\2\u01a9\u01aa\7k\2\2\u01aa\u01ab\7p\2\2\u01ab\u01ac"+
		"\7e\2\2\u01ac\u01ad\7v\2\2\u01adN\3\2\2\2\u01ae\u01af\7o\2\2\u01af\u01b0"+
		"\7g\2\2\u01b0\u01b1\7f\2\2\u01b1\u01b2\7k\2\2\u01b2\u01b3\7c\2\2\u01b3"+
		"\u01b4\7p\2\2\u01b4P\3\2\2\2\u01b5\u01b6\7r\2\2\u01b6\u01b7\7g\2\2\u01b7"+
		"\u01b8\7t\2\2\u01b8\u01b9\7e\2\2\u01b9\u01ba\7g\2\2\u01ba\u01bb\7p\2\2"+
		"\u01bb\u01bc\7v\2\2\u01bc\u01bd\7k\2\2\u01bd\u01be\7n\2\2\u01be\u01bf"+
		"\7g\2\2\u01bfR\3\2\2\2\u01c0\u01c1\7q\2\2\u01c1\u01c2\7p\2\2\u01c2\u01c3"+
		"\7g\2\2\u01c3\u01c4\7a\2\2\u01c4\u01c5\7v\2\2\u01c5\u01c6\7q\2\2\u01c6"+
		"\u01c7\7a\2\2\u01c7\u01c8\7q\2\2\u01c8\u01c9\7p\2\2\u01c9\u01ca\7g\2\2"+
		"\u01caT\3\2\2\2\u01cb\u01cc\7q\2\2\u01cc\u01cd\7p\2\2\u01cd\u01ce\7g\2"+
		"\2\u01ce\u01cf\7a\2\2\u01cf\u01d0\7v\2\2\u01d0\u01d1\7q\2\2\u01d1\u01d2"+
		"\7a\2\2\u01d2\u01d3\7o\2\2\u01d3\u01d4\7c\2\2\u01d4\u01d5\7p\2\2\u01d5"+
		"\u01d6\7{\2\2\u01d6V\3\2\2\2\u01d7\u01d8\7o\2\2\u01d8\u01d9\7c\2\2\u01d9"+
		"\u01da\7p\2\2\u01da\u01db\7{\2\2\u01db\u01dc\7a\2\2\u01dc\u01dd\7v\2\2"+
		"\u01dd\u01de\7q\2\2\u01de\u01df\7a\2\2\u01df\u01e0\7q\2\2\u01e0\u01e1"+
		"\7p\2\2\u01e1\u01e2\7g\2\2\u01e2X\3\2\2\2\u01e3\u01e4\7o\2\2\u01e4\u01e5"+
		"\7c\2\2\u01e5\u01e6\7p\2\2\u01e6\u01e7\7{\2\2\u01e7\u01e8\7a\2\2\u01e8"+
		"\u01e9\7v\2\2\u01e9\u01ea\7q\2\2\u01ea\u01eb\7a\2\2\u01eb\u01ec\7o\2\2"+
		"\u01ec\u01ed\7c\2\2\u01ed\u01ee\7p\2\2\u01ee\u01ef\7{\2\2\u01efZ\3\2\2"+
		"\2\u01f0\u01f1\7{\2\2\u01f1\u01f2\7g\2\2\u01f2\u01f3\7u\2\2\u01f3\\\3"+
		"\2\2\2\u01f4\u01f5\7p\2\2\u01f5\u01f6\7q\2\2\u01f6^\3\2\2\2\u01f7\u01f8"+
		"\7w\2\2\u01f8\u01f9\7u\2\2\u01f9\u01fa\7f\2\2\u01fa`\3\2\2\2\u01fb\u01fc"+
		"\7r\2\2\u01fc\u01fd\7g\2\2\u01fd\u01fe\7t\2\2\u01fe\u01ff\7e\2\2\u01ff"+
		"\u0200\7g\2\2\u0200\u0201\7p\2\2\u0201\u0202\7v\2\2\u0202b\3\2\2\2\u0203"+
		"\u0204\7r\2\2\u0204\u0205\7g\2\2\u0205\u0206\7t\2\2\u0206\u0207\7e\2\2"+
		"\u0207\u0208\7g\2\2\u0208\u0209\7p\2\2\u0209\u020a\7v\2\2\u020a\u020b"+
		"\7a\2\2\u020b\u020c\7\63\2\2\u020cd\3\2\2\2\u020d\u020e\7r\2\2\u020e\u020f"+
		"\7g\2\2\u020f\u0210\7t\2\2\u0210\u0211\7e\2\2\u0211\u0212\7g\2\2\u0212"+
		"\u0213\7p\2\2\u0213\u0214\7v\2\2\u0214\u0215\7a\2\2\u0215\u0216\7\64\2"+
		"\2\u0216f\3\2\2\2\u0217\u0218\7<\2\2\u0218h\3\2\2\2\u0219\u021a\7=\2\2"+
		"\u021aj\3\2\2\2\u021b\u021c\7}\2\2\u021cl\3\2\2\2\u021d\u021e\7\177\2"+
		"\2\u021en\3\2\2\2\u021f\u0220\7]\2\2\u0220p\3\2\2\2\u0221\u0222\7_\2\2"+
		"\u0222r\3\2\2\2\u0223\u0224\7.\2\2\u0224t\3\2\2\2\u0225\u0229\t\2\2\2"+
		"\u0226\u0228\t\3\2\2\u0227\u0226\3\2\2\2\u0228\u022b\3\2\2\2\u0229\u0227"+
		"\3\2\2\2\u0229\u022a\3\2\2\2\u022av\3\2\2\2\u022b\u0229\3\2\2\2\u022c"+
		"\u022e\t\4\2\2\u022d\u022c\3\2\2\2\u022e\u022f\3\2\2\2\u022f\u022d\3\2"+
		"\2\2\u022f\u0230\3\2\2\2\u0230x\3\2\2\2\u0231\u0237\7$\2\2\u0232\u0236"+
		"\n\5\2\2\u0233\u0234\7^\2\2\u0234\u0236\13\2\2\2\u0235\u0232\3\2\2\2\u0235"+
		"\u0233\3\2\2\2\u0236\u0239\3\2\2\2\u0237\u0235\3\2\2\2\u0237\u0238\3\2"+
		"\2\2\u0238\u023a\3\2\2\2\u0239\u0237\3\2\2\2\u023a\u023b\7$\2\2\u023b"+
		"z\3\2\2\2\u023c\u0240\7<\2\2\u023d\u023f\13\2\2\2\u023e\u023d\3\2\2\2"+
		"\u023f\u0242\3\2\2\2\u0240\u0241\3\2\2\2\u0240\u023e\3\2\2\2\u0241\u0243"+
		"\3\2\2\2\u0242\u0240\3\2\2\2\u0243\u0244\7=\2\2\u0244\u0245\7=\2\2\u0245"+
		"|\3\2\2\2\u0246\u024a\7%\2\2\u0247\u0249\n\6\2\2\u0248\u0247\3\2\2\2\u0249"+
		"\u024c\3\2\2\2\u024a\u0248\3\2\2\2\u024a\u024b\3\2\2\2\u024b~\3\2\2\2"+
		"\u024c\u024a\3\2\2\2\u024d\u024f\7\17\2\2\u024e\u024d\3\2\2\2\u024e\u024f"+
		"\3\2\2\2\u024f\u0251\3\2\2\2\u0250\u0252\7\f\2\2\u0251\u0250\3\2\2\2\u0252"+
		"\u0253\3\2\2\2\u0253\u0251\3\2\2\2\u0253\u0254\3\2\2\2\u0254\u0080\3\2"+
		"\2\2\u0255\u0257\t\7\2\2\u0256\u0255\3\2\2\2\u0257\u0258\3\2\2\2\u0258"+
		"\u0256\3\2\2\2\u0258\u0259\3\2\2\2\u0259\u025a\3\2\2\2\u025a\u025b\bA"+
		"\2\2\u025b\u0082\3\2\2\2\f\2\u0229\u022f\u0235\u0237\u0240\u024a\u024e"+
		"\u0253\u0258\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}