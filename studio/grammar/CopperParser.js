// Generated from ../../../../grammar/Copper.g4 by ANTLR 4.9.2
// jshint ignore: start
import antlr4 from 'antlr4';
import CopperListener from './CopperListener.js';
const serializedATN = ["\u0003\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786",
    "\u5964\u0003M\u01b2\u0004\u0002\t\u0002\u0004\u0003\t\u0003\u0004\u0004",
    "\t\u0004\u0004\u0005\t\u0005\u0004\u0006\t\u0006\u0004\u0007\t\u0007",
    "\u0004\b\t\b\u0004\t\t\t\u0004\n\t\n\u0004\u000b\t\u000b\u0004\f\t\f",
    "\u0004\r\t\r\u0004\u000e\t\u000e\u0004\u000f\t\u000f\u0004\u0010\t\u0010",
    "\u0004\u0011\t\u0011\u0004\u0012\t\u0012\u0004\u0013\t\u0013\u0004\u0014",
    "\t\u0014\u0004\u0015\t\u0015\u0004\u0016\t\u0016\u0004\u0017\t\u0017",
    "\u0004\u0018\t\u0018\u0004\u0019\t\u0019\u0004\u001a\t\u001a\u0004\u001b",
    "\t\u001b\u0004\u001c\t\u001c\u0004\u001d\t\u001d\u0004\u001e\t\u001e",
    "\u0004\u001f\t\u001f\u0004 \t \u0004!\t!\u0004\"\t\"\u0004#\t#\u0004",
    "$\t$\u0004%\t%\u0004&\t&\u0004\'\t\'\u0004(\t(\u0004)\t)\u0004*\t*\u0004",
    "+\t+\u0004,\t,\u0004-\t-\u0004.\t.\u0004/\t/\u00040\t0\u00041\t1\u0004",
    "2\t2\u00043\t3\u00044\t4\u0003\u0002\u0003\u0002\u0007\u0002k\n\u0002",
    "\f\u0002\u000e\u0002n\u000b\u0002\u0003\u0002\u0003\u0002\u0003\u0003",
    "\u0003\u0003\u0003\u0003\u0003\u0003\u0005\u0003v\n\u0003\u0003\u0004",
    "\u0003\u0004\u0003\u0004\u0003\u0004\u0003\u0004\u0003\u0004\u0007\u0004",
    "~\n\u0004\f\u0004\u000e\u0004\u0081\u000b\u0004\u0003\u0004\u0003\u0004",
    "\u0003\u0005\u0003\u0005\u0003\u0005\u0003\u0005\u0003\u0005\u0003\u0005",
    "\u0007\u0005\u008b\n\u0005\f\u0005\u000e\u0005\u008e\u000b\u0005\u0003",
    "\u0005\u0003\u0005\u0003\u0006\u0003\u0006\u0003\u0006\u0005\u0006\u0095",
    "\n\u0006\u0003\u0007\u0003\u0007\u0003\u0007\u0003\u0007\u0003\u0007",
    "\u0005\u0007\u009c\n\u0007\u0003\b\u0003\b\u0003\b\u0003\b\u0003\b\u0003",
    "\b\u0007\b\u00a4\n\b\f\b\u000e\b\u00a7\u000b\b\u0003\b\u0003\b\u0003",
    "\t\u0003\t\u0003\t\u0003\t\u0003\t\u0003\t\u0007\t\u00b1\n\t\f\t\u000e",
    "\t\u00b4\u000b\t\u0003\t\u0003\t\u0003\n\u0003\n\u0003\n\u0003\n\u0003",
    "\n\u0003\n\u0007\n\u00be\n\n\f\n\u000e\n\u00c1\u000b\n\u0003\n\u0003",
    "\n\u0003\u000b\u0003\u000b\u0003\u000b\u0003\u000b\u0003\u000b\u0003",
    "\u000b\u0003\u000b\u0003\u000b\u0005\u000b\u00cd\n\u000b\u0003\f\u0003",
    "\f\u0003\f\u0003\f\u0003\f\u0003\f\u0003\f\u0005\f\u00d6\n\f\u0003\r",
    "\u0003\r\u0003\r\u0005\r\u00db\n\r\u0003\u000e\u0003\u000e\u0003\u000e",
    "\u0003\u000e\u0003\u000f\u0003\u000f\u0003\u000f\u0003\u000f\u0003\u0010",
    "\u0003\u0010\u0003\u0010\u0003\u0010\u0003\u0011\u0003\u0011\u0003\u0011",
    "\u0003\u0011\u0003\u0012\u0003\u0012\u0003\u0012\u0003\u0012\u0003\u0013",
    "\u0003\u0013\u0003\u0013\u0003\u0013\u0003\u0014\u0003\u0014\u0003\u0014",
    "\u0003\u0014\u0003\u0015\u0003\u0015\u0003\u0015\u0003\u0015\u0005\u0015",
    "\u00fd\n\u0015\u0003\u0016\u0003\u0016\u0003\u0016\u0003\u0016\u0003",
    "\u0017\u0003\u0017\u0003\u0017\u0003\u0017\u0003\u0018\u0003\u0018\u0003",
    "\u0018\u0003\u0018\u0003\u0019\u0003\u0019\u0003\u0019\u0003\u0019\u0003",
    "\u001a\u0003\u001a\u0003\u001a\u0003\u001a\u0003\u001b\u0003\u001b\u0003",
    "\u001b\u0007\u001b\u0116\n\u001b\f\u001b\u000e\u001b\u0119\u000b\u001b",
    "\u0003\u001c\u0003\u001c\u0003\u001d\u0003\u001d\u0003\u001e\u0003\u001e",
    "\u0003\u001f\u0003\u001f\u0003 \u0003 \u0003!\u0003!\u0003\"\u0003\"",
    "\u0003\"\u0003#\u0007#\u012b\n#\f#\u000e#\u012e\u000b#\u0003$\u0003",
    "$\u0003%\u0003%\u0003&\u0003&\u0003&\u0007&\u0137\n&\f&\u000e&\u013a",
    "\u000b&\u0003\'\u0003\'\u0003\'\u0007\'\u013f\n\'\f\'\u000e\'\u0142",
    "\u000b\'\u0003(\u0003(\u0003(\u0005(\u0147\n(\u0003)\u0003)\u0003)\u0007",
    ")\u014c\n)\f)\u000e)\u014f\u000b)\u0003*\u0003*\u0003*\u0007*\u0154",
    "\n*\f*\u000e*\u0157\u000b*\u0003+\u0003+\u0003+\u0003+\u0003+\u0003",
    "+\u0003+\u0005+\u0160\n+\u0003,\u0003,\u0003,\u0003,\u0003,\u0007,\u0167",
    "\n,\f,\u000e,\u016a\u000b,\u0003,\u0003,\u0005,\u016e\n,\u0003,\u0003",
    ",\u0003,\u0003,\u0003,\u0007,\u0175\n,\f,\u000e,\u0178\u000b,\u0005",
    ",\u017a\n,\u0003,\u0003,\u0005,\u017e\n,\u0003-\u0003-\u0003-\u0003",
    "-\u0003-\u0007-\u0185\n-\f-\u000e-\u0188\u000b-\u0003-\u0003-\u0003",
    ".\u0003.\u0003.\u0003.\u0003/\u0003/\u0005/\u0192\n/\u00030\u00030\u0003",
    "0\u00030\u00070\u0198\n0\f0\u000e0\u019b\u000b0\u00050\u019d\n0\u0003",
    "0\u00030\u00031\u00031\u00031\u00031\u00051\u01a5\n1\u00031\u00031\u0003",
    "2\u00032\u00032\u00052\u01ac\n2\u00033\u00033\u00034\u00034\u00034\u0002",
    "\u00025\u0002\u0004\u0006\b\n\f\u000e\u0010\u0012\u0014\u0016\u0018",
    "\u001a\u001c\u001e \"$&(*,.02468:<>@BDFHJLNPRTVXZ\\^`bdf\u0002\u000e",
    "\u0003\u0002\u0015\u001a\u0004\u0002\u0016\u0016\u001b \u0003\u0002",
    "!$\u0003\u0002%(\u0003\u0002),\u0003\u0002-0\u0004\u0002==LL\u0003\u0002",
    "BG\u0003\u0002>?\u0003\u0002@A\u0003\u0002/0\u0004\u0002\u00150HH\u0002",
    "\u01b9\u0002l\u0003\u0002\u0002\u0002\u0004u\u0003\u0002\u0002\u0002",
    "\u0006w\u0003\u0002\u0002\u0002\b\u0084\u0003\u0002\u0002\u0002\n\u0094",
    "\u0003\u0002\u0002\u0002\f\u009b\u0003\u0002\u0002\u0002\u000e\u009d",
    "\u0003\u0002\u0002\u0002\u0010\u00aa\u0003\u0002\u0002\u0002\u0012\u00b7",
    "\u0003\u0002\u0002\u0002\u0014\u00cc\u0003\u0002\u0002\u0002\u0016\u00d5",
    "\u0003\u0002\u0002\u0002\u0018\u00da\u0003\u0002\u0002\u0002\u001a\u00dc",
    "\u0003\u0002\u0002\u0002\u001c\u00e0\u0003\u0002\u0002\u0002\u001e\u00e4",
    "\u0003\u0002\u0002\u0002 \u00e8\u0003\u0002\u0002\u0002\"\u00ec\u0003",
    "\u0002\u0002\u0002$\u00f0\u0003\u0002\u0002\u0002&\u00f4\u0003\u0002",
    "\u0002\u0002(\u00f8\u0003\u0002\u0002\u0002*\u00fe\u0003\u0002\u0002",
    "\u0002,\u0102\u0003\u0002\u0002\u0002.\u0106\u0003\u0002\u0002\u0002",
    "0\u010a\u0003\u0002\u0002\u00022\u010e\u0003\u0002\u0002\u00024\u0112",
    "\u0003\u0002\u0002\u00026\u011a\u0003\u0002\u0002\u00028\u011c\u0003",
    "\u0002\u0002\u0002:\u011e\u0003\u0002\u0002\u0002<\u0120\u0003\u0002",
    "\u0002\u0002>\u0122\u0003\u0002\u0002\u0002@\u0124\u0003\u0002\u0002",
    "\u0002B\u0126\u0003\u0002\u0002\u0002D\u012c\u0003\u0002\u0002\u0002",
    "F\u012f\u0003\u0002\u0002\u0002H\u0131\u0003\u0002\u0002\u0002J\u0133",
    "\u0003\u0002\u0002\u0002L\u013b\u0003\u0002\u0002\u0002N\u0143\u0003",
    "\u0002\u0002\u0002P\u0148\u0003\u0002\u0002\u0002R\u0150\u0003\u0002",
    "\u0002\u0002T\u015f\u0003\u0002\u0002\u0002V\u017d\u0003\u0002\u0002",
    "\u0002X\u017f\u0003\u0002\u0002\u0002Z\u018b\u0003\u0002\u0002\u0002",
    "\\\u0191\u0003\u0002\u0002\u0002^\u0193\u0003\u0002\u0002\u0002`\u01a0",
    "\u0003\u0002\u0002\u0002b\u01ab\u0003\u0002\u0002\u0002d\u01ad\u0003",
    "\u0002\u0002\u0002f\u01af\u0003\u0002\u0002\u0002hk\u0005\u0004\u0003",
    "\u0002ik\u0007L\u0002\u0002jh\u0003\u0002\u0002\u0002ji\u0003\u0002",
    "\u0002\u0002kn\u0003\u0002\u0002\u0002lj\u0003\u0002\u0002\u0002lm\u0003",
    "\u0002\u0002\u0002mo\u0003\u0002\u0002\u0002nl\u0003\u0002\u0002\u0002",
    "op\u0007\u0002\u0002\u0003p\u0003\u0003\u0002\u0002\u0002qv\u0005\u0006",
    "\u0004\u0002rv\u0005\b\u0005\u0002sv\u0005\u000e\b\u0002tv\u0005\u0010",
    "\t\u0002uq\u0003\u0002\u0002\u0002ur\u0003\u0002\u0002\u0002us\u0003",
    "\u0002\u0002\u0002ut\u0003\u0002\u0002\u0002v\u0005\u0003\u0002\u0002",
    "\u0002wx\u0007\u0003\u0002\u0002xy\u0007:\u0002\u0002yz\u0005f4\u0002",
    "z\u007f\u00075\u0002\u0002{~\u0005\n\u0006\u0002|~\u0007L\u0002\u0002",
    "}{\u0003\u0002\u0002\u0002}|\u0003\u0002\u0002\u0002~\u0081\u0003\u0002",
    "\u0002\u0002\u007f}\u0003\u0002\u0002\u0002\u007f\u0080\u0003\u0002",
    "\u0002\u0002\u0080\u0082\u0003\u0002\u0002\u0002\u0081\u007f\u0003\u0002",
    "\u0002\u0002\u0082\u0083\u00076\u0002\u0002\u0083\u0007\u0003\u0002",
    "\u0002\u0002\u0084\u0085\u0007\u0004\u0002\u0002\u0085\u0086\u0007:",
    "\u0002\u0002\u0086\u0087\u0005f4\u0002\u0087\u008c\u00075\u0002\u0002",
    "\u0088\u008b\u0005\f\u0007\u0002\u0089\u008b\u0007L\u0002\u0002\u008a",
    "\u0088\u0003\u0002\u0002\u0002\u008a\u0089\u0003\u0002\u0002\u0002\u008b",
    "\u008e\u0003\u0002\u0002\u0002\u008c\u008a\u0003\u0002\u0002\u0002\u008c",
    "\u008d\u0003\u0002\u0002\u0002\u008d\u008f\u0003\u0002\u0002\u0002\u008e",
    "\u008c\u0003\u0002\u0002\u0002\u008f\u0090\u00076\u0002\u0002\u0090",
    "\t\u0003\u0002\u0002\u0002\u0091\u0095\u0005\u0010\t\u0002\u0092\u0095",
    "\u0005\u000e\b\u0002\u0093\u0095\u0005\u0012\n\u0002\u0094\u0091\u0003",
    "\u0002\u0002\u0002\u0094\u0092\u0003\u0002\u0002\u0002\u0094\u0093\u0003",
    "\u0002\u0002\u0002\u0095\u000b\u0003\u0002\u0002\u0002\u0096\u009c\u0005",
    "0\u0019\u0002\u0097\u009c\u00052\u001a\u0002\u0098\u009c\u0005\u0012",
    "\n\u0002\u0099\u009c\u0005\u0010\t\u0002\u009a\u009c\u0005\u000e\b\u0002",
    "\u009b\u0096\u0003\u0002\u0002\u0002\u009b\u0097\u0003\u0002\u0002\u0002",
    "\u009b\u0098\u0003\u0002\u0002\u0002\u009b\u0099\u0003\u0002\u0002\u0002",
    "\u009b\u009a\u0003\u0002\u0002\u0002\u009c\r\u0003\u0002\u0002\u0002",
    "\u009d\u009e\u0007\u0005\u0002\u0002\u009e\u009f\u0007:\u0002\u0002",
    "\u009f\u00a0\u0005f4\u0002\u00a0\u00a5\u00075\u0002\u0002\u00a1\u00a4",
    "\u0005\u0016\f\u0002\u00a2\u00a4\u0007L\u0002\u0002\u00a3\u00a1\u0003",
    "\u0002\u0002\u0002\u00a3\u00a2\u0003\u0002\u0002\u0002\u00a4\u00a7\u0003",
    "\u0002\u0002\u0002\u00a5\u00a3\u0003\u0002\u0002\u0002\u00a5\u00a6\u0003",
    "\u0002\u0002\u0002\u00a6\u00a8\u0003\u0002\u0002\u0002\u00a7\u00a5\u0003",
    "\u0002\u0002\u0002\u00a8\u00a9\u00076\u0002\u0002\u00a9\u000f\u0003",
    "\u0002\u0002\u0002\u00aa\u00ab\u0007\u0006\u0002\u0002\u00ab\u00ac\u0007",
    ":\u0002\u0002\u00ac\u00ad\u0005f4\u0002\u00ad\u00b2\u00075\u0002\u0002",
    "\u00ae\u00b1\u0005\u0014\u000b\u0002\u00af\u00b1\u0007L\u0002\u0002",
    "\u00b0\u00ae\u0003\u0002\u0002\u0002\u00b0\u00af\u0003\u0002\u0002\u0002",
    "\u00b1\u00b4\u0003\u0002\u0002\u0002\u00b2\u00b0\u0003\u0002\u0002\u0002",
    "\u00b2\u00b3\u0003\u0002\u0002\u0002\u00b3\u00b5\u0003\u0002\u0002\u0002",
    "\u00b4\u00b2\u0003\u0002\u0002\u0002\u00b5\u00b6\u00076\u0002\u0002",
    "\u00b6\u0011\u0003\u0002\u0002\u0002\u00b7\u00b8\u0007\u0007\u0002\u0002",
    "\u00b8\u00b9\u0007:\u0002\u0002\u00b9\u00ba\u0005f4\u0002\u00ba\u00bf",
    "\u00075\u0002\u0002\u00bb\u00be\u0005\u0018\r\u0002\u00bc\u00be\u0007",
    "L\u0002\u0002\u00bd\u00bb\u0003\u0002\u0002\u0002\u00bd\u00bc\u0003",
    "\u0002\u0002\u0002\u00be\u00c1\u0003\u0002\u0002\u0002\u00bf\u00bd\u0003",
    "\u0002\u0002\u0002\u00bf\u00c0\u0003\u0002\u0002\u0002\u00c0\u00c2\u0003",
    "\u0002\u0002\u0002\u00c1\u00bf\u0003\u0002\u0002\u0002\u00c2\u00c3\u0007",
    "6\u0002\u0002\u00c3\u0013\u0003\u0002\u0002\u0002\u00c4\u00cd\u0005",
    "\u001a\u000e\u0002\u00c5\u00cd\u0005\u001e\u0010\u0002\u00c6\u00cd\u0005",
    " \u0011\u0002\u00c7\u00cd\u0005\"\u0012\u0002\u00c8\u00cd\u0005$\u0013",
    "\u0002\u00c9\u00cd\u0005&\u0014\u0002\u00ca\u00cd\u0005(\u0015\u0002",
    "\u00cb\u00cd\u0005*\u0016\u0002\u00cc\u00c4\u0003\u0002\u0002\u0002",
    "\u00cc\u00c5\u0003\u0002\u0002\u0002\u00cc\u00c6\u0003\u0002\u0002\u0002",
    "\u00cc\u00c7\u0003\u0002\u0002\u0002\u00cc\u00c8\u0003\u0002\u0002\u0002",
    "\u00cc\u00c9\u0003\u0002\u0002\u0002\u00cc\u00ca\u0003\u0002\u0002\u0002",
    "\u00cc\u00cb\u0003\u0002\u0002\u0002\u00cd\u0015\u0003\u0002\u0002\u0002",
    "\u00ce\u00d6\u0005\u001c\u000f\u0002\u00cf\u00d6\u0005\u001e\u0010\u0002",
    "\u00d0\u00d6\u0005 \u0011\u0002\u00d1\u00d6\u0005\"\u0012\u0002\u00d2",
    "\u00d6\u0005&\u0014\u0002\u00d3\u00d6\u0005(\u0015\u0002\u00d4\u00d6",
    "\u0005*\u0016\u0002\u00d5\u00ce\u0003\u0002\u0002\u0002\u00d5\u00cf",
    "\u0003\u0002\u0002\u0002\u00d5\u00d0\u0003\u0002\u0002\u0002\u00d5\u00d1",
    "\u0003\u0002\u0002\u0002\u00d5\u00d2\u0003\u0002\u0002\u0002\u00d5\u00d3",
    "\u0003\u0002\u0002\u0002\u00d5\u00d4\u0003\u0002\u0002\u0002\u00d6\u0017",
    "\u0003\u0002\u0002\u0002\u00d7\u00db\u0005,\u0017\u0002\u00d8\u00db",
    "\u0005.\u0018\u0002\u00d9\u00db\u0005\u001e\u0010\u0002\u00da\u00d7",
    "\u0003\u0002\u0002\u0002\u00da\u00d8\u0003\u0002\u0002\u0002\u00da\u00d9",
    "\u0003\u0002\u0002\u0002\u00db\u0019\u0003\u0002\u0002\u0002\u00dc\u00dd",
    "\u0007\b\u0002\u0002\u00dd\u00de\u0007:\u0002\u0002\u00de\u00df\u0005",
    "6\u001c\u0002\u00df\u001b\u0003\u0002\u0002\u0002\u00e0\u00e1\u0007",
    "\b\u0002\u0002\u00e1\u00e2\u0007:\u0002\u0002\u00e2\u00e3\u00058\u001d",
    "\u0002\u00e3\u001d\u0003\u0002\u0002\u0002\u00e4\u00e5\u0007\t\u0002",
    "\u0002\u00e5\u00e6\u0007:\u0002\u0002\u00e6\u00e7\u0005B\"\u0002\u00e7",
    "\u001f\u0003\u0002\u0002\u0002\u00e8\u00e9\u0007\n\u0002\u0002\u00e9",
    "\u00ea\u0007:\u0002\u0002\u00ea\u00eb\u0005F$\u0002\u00eb!\u0003\u0002",
    "\u0002\u0002\u00ec\u00ed\u0007\u000b\u0002\u0002\u00ed\u00ee\u0007:",
    "\u0002\u0002\u00ee\u00ef\u0005F$\u0002\u00ef#\u0003\u0002\u0002\u0002",
    "\u00f0\u00f1\u0007\f\u0002\u0002\u00f1\u00f2\u0007:\u0002\u0002\u00f2",
    "\u00f3\u0005@!\u0002\u00f3%\u0003\u0002\u0002\u0002\u00f4\u00f5\u0007",
    "\r\u0002\u0002\u00f5\u00f6\u0007:\u0002\u0002\u00f6\u00f7\u0005@!\u0002",
    "\u00f7\'\u0003\u0002\u0002\u0002\u00f8\u00f9\u0007\u000e\u0002\u0002",
    "\u00f9\u00fc\u0007:\u0002\u0002\u00fa\u00fd\u0005F$\u0002\u00fb\u00fd",
    "\u0005> \u0002\u00fc\u00fa\u0003\u0002\u0002\u0002\u00fc\u00fb\u0003",
    "\u0002\u0002\u0002\u00fd)\u0003\u0002\u0002\u0002\u00fe\u00ff\u0007",
    "\u000f\u0002\u0002\u00ff\u0100\u0007:\u0002\u0002\u0100\u0101\u0005",
    "F$\u0002\u0101+\u0003\u0002\u0002\u0002\u0102\u0103\u0007\b\u0002\u0002",
    "\u0103\u0104\u0007:\u0002\u0002\u0104\u0105\u0005:\u001e\u0002\u0105",
    "-\u0003\u0002\u0002\u0002\u0106\u0107\u0007\u0010\u0002\u0002\u0107",
    "\u0108\u0007:\u0002\u0002\u0108\u0109\u0005<\u001f\u0002\u0109/\u0003",
    "\u0002\u0002\u0002\u010a\u010b\u0007\u0011\u0002\u0002\u010b\u010c\u0007",
    ":\u0002\u0002\u010c\u010d\u0005f4\u0002\u010d1\u0003\u0002\u0002\u0002",
    "\u010e\u010f\u0007\u0012\u0002\u0002\u010f\u0110\u0007:\u0002\u0002",
    "\u0110\u0111\u00054\u001b\u0002\u01113\u0003\u0002\u0002\u0002\u0112",
    "\u0117\u0005f4\u0002\u0113\u0114\u0007;\u0002\u0002\u0114\u0116\u0005",
    "f4\u0002\u0115\u0113\u0003\u0002\u0002\u0002\u0116\u0119\u0003\u0002",
    "\u0002\u0002\u0117\u0115\u0003\u0002\u0002\u0002\u0117\u0118\u0003\u0002",
    "\u0002\u0002\u01185\u0003\u0002\u0002\u0002\u0119\u0117\u0003\u0002",
    "\u0002\u0002\u011a\u011b\t\u0002\u0002\u0002\u011b7\u0003\u0002\u0002",
    "\u0002\u011c\u011d\t\u0003\u0002\u0002\u011d9\u0003\u0002\u0002\u0002",
    "\u011e\u011f\t\u0004\u0002\u0002\u011f;\u0003\u0002\u0002\u0002\u0120",
    "\u0121\t\u0005\u0002\u0002\u0121=\u0003\u0002\u0002\u0002\u0122\u0123",
    "\t\u0006\u0002\u0002\u0123?\u0003\u0002\u0002\u0002\u0124\u0125\t\u0007",
    "\u0002\u0002\u0125A\u0003\u0002\u0002\u0002\u0126\u0127\u0005D#\u0002",
    "\u0127\u0128\u0007=\u0002\u0002\u0128C\u0003\u0002\u0002\u0002\u0129",
    "\u012b\n\b\u0002\u0002\u012a\u0129\u0003\u0002\u0002\u0002\u012b\u012e",
    "\u0003\u0002\u0002\u0002\u012c\u012a\u0003\u0002\u0002\u0002\u012c\u012d",
    "\u0003\u0002\u0002\u0002\u012dE\u0003\u0002\u0002\u0002\u012e\u012c",
    "\u0003\u0002\u0002\u0002\u012f\u0130\u0007I\u0002\u0002\u0130G\u0003",
    "\u0002\u0002\u0002\u0131\u0132\u0005J&\u0002\u0132I\u0003\u0002\u0002",
    "\u0002\u0133\u0138\u0005L\'\u0002\u0134\u0135\u00072\u0002\u0002\u0135",
    "\u0137\u0005L\'\u0002\u0136\u0134\u0003\u0002\u0002\u0002\u0137\u013a",
    "\u0003\u0002\u0002\u0002\u0138\u0136\u0003\u0002\u0002\u0002\u0138\u0139",
    "\u0003\u0002\u0002\u0002\u0139K\u0003\u0002\u0002\u0002\u013a\u0138",
    "\u0003\u0002\u0002\u0002\u013b\u0140\u0005N(\u0002\u013c\u013d\u0007",
    "1\u0002\u0002\u013d\u013f\u0005N(\u0002\u013e\u013c\u0003\u0002\u0002",
    "\u0002\u013f\u0142\u0003\u0002\u0002\u0002\u0140\u013e\u0003\u0002\u0002",
    "\u0002\u0140\u0141\u0003\u0002\u0002\u0002\u0141M\u0003\u0002\u0002",
    "\u0002\u0142\u0140\u0003\u0002\u0002\u0002\u0143\u0146\u0005P)\u0002",
    "\u0144\u0145\t\t\u0002\u0002\u0145\u0147\u0005P)\u0002\u0146\u0144\u0003",
    "\u0002\u0002\u0002\u0146\u0147\u0003\u0002\u0002\u0002\u0147O\u0003",
    "\u0002\u0002\u0002\u0148\u014d\u0005R*\u0002\u0149\u014a\t\n\u0002\u0002",
    "\u014a\u014c\u0005R*\u0002\u014b\u0149\u0003\u0002\u0002\u0002\u014c",
    "\u014f\u0003\u0002\u0002\u0002\u014d\u014b\u0003\u0002\u0002\u0002\u014d",
    "\u014e\u0003\u0002\u0002\u0002\u014eQ\u0003\u0002\u0002\u0002\u014f",
    "\u014d\u0003\u0002\u0002\u0002\u0150\u0155\u0005T+\u0002\u0151\u0152",
    "\t\u000b\u0002\u0002\u0152\u0154\u0005T+\u0002\u0153\u0151\u0003\u0002",
    "\u0002\u0002\u0154\u0157\u0003\u0002\u0002\u0002\u0155\u0153\u0003\u0002",
    "\u0002\u0002\u0155\u0156\u0003\u0002\u0002\u0002\u0156S\u0003\u0002",
    "\u0002\u0002\u0157\u0155\u0003\u0002\u0002\u0002\u0158\u0159\u00073",
    "\u0002\u0002\u0159\u015a\u0005H%\u0002\u015a\u015b\u00074\u0002\u0002",
    "\u015b\u0160\u0003\u0002\u0002\u0002\u015c\u0160\u0005b2\u0002\u015d",
    "\u0160\u0005`1\u0002\u015e\u0160\u0005V,\u0002\u015f\u0158\u0003\u0002",
    "\u0002\u0002\u015f\u015c\u0003\u0002\u0002\u0002\u015f\u015d\u0003\u0002",
    "\u0002\u0002\u015f\u015e\u0003\u0002\u0002\u0002\u0160U\u0003\u0002",
    "\u0002\u0002\u0161\u0162\u0007\u0013\u0002\u0002\u0162\u0163\u00073",
    "\u0002\u0002\u0163\u0168\u0005Z.\u0002\u0164\u0165\u0007;\u0002\u0002",
    "\u0165\u0167\u0005Z.\u0002\u0166\u0164\u0003\u0002\u0002\u0002\u0167",
    "\u016a\u0003\u0002\u0002\u0002\u0168\u0166\u0003\u0002\u0002\u0002\u0168",
    "\u0169\u0003\u0002\u0002\u0002\u0169\u016b\u0003\u0002\u0002\u0002\u016a",
    "\u0168\u0003\u0002\u0002\u0002\u016b\u016d\u00074\u0002\u0002\u016c",
    "\u016e\u0005X-\u0002\u016d\u016c\u0003\u0002\u0002\u0002\u016d\u016e",
    "\u0003\u0002\u0002\u0002\u016e\u017e\u0003\u0002\u0002\u0002\u016f\u0170",
    "\u0005f4\u0002\u0170\u0179\u00073\u0002\u0002\u0171\u0176\u0005H%\u0002",
    "\u0172\u0173\u0007;\u0002\u0002\u0173\u0175\u0005H%\u0002\u0174\u0172",
    "\u0003\u0002\u0002\u0002\u0175\u0178\u0003\u0002\u0002\u0002\u0176\u0174",
    "\u0003\u0002\u0002\u0002\u0176\u0177\u0003\u0002\u0002\u0002\u0177\u017a",
    "\u0003\u0002\u0002\u0002\u0178\u0176\u0003\u0002\u0002\u0002\u0179\u0171",
    "\u0003\u0002\u0002\u0002\u0179\u017a\u0003\u0002\u0002\u0002\u017a\u017b",
    "\u0003\u0002\u0002\u0002\u017b\u017c\u00074\u0002\u0002\u017c\u017e",
    "\u0003\u0002\u0002\u0002\u017d\u0161\u0003\u0002\u0002\u0002\u017d\u016f",
    "\u0003\u0002\u0002\u0002\u017eW\u0003\u0002\u0002\u0002\u017f\u0180",
    "\u0007\u0014\u0002\u0002\u0180\u0181\u00075\u0002\u0002\u0181\u0186",
    "\u0005Z.\u0002\u0182\u0183\u0007;\u0002\u0002\u0183\u0185\u0005Z.\u0002",
    "\u0184\u0182\u0003\u0002\u0002\u0002\u0185\u0188\u0003\u0002\u0002\u0002",
    "\u0186\u0184\u0003\u0002\u0002\u0002\u0186\u0187\u0003\u0002\u0002\u0002",
    "\u0187\u0189\u0003\u0002\u0002\u0002\u0188\u0186\u0003\u0002\u0002\u0002",
    "\u0189\u018a\u00076\u0002\u0002\u018aY\u0003\u0002\u0002\u0002\u018b",
    "\u018c\u0005f4\u0002\u018c\u018d\u0007:\u0002\u0002\u018d\u018e\u0005",
    "\\/\u0002\u018e[\u0003\u0002\u0002\u0002\u018f\u0192\u0005H%\u0002\u0190",
    "\u0192\u0005^0\u0002\u0191\u018f\u0003\u0002\u0002\u0002\u0191\u0190",
    "\u0003\u0002\u0002\u0002\u0192]\u0003\u0002\u0002\u0002\u0193\u019c",
    "\u00077\u0002\u0002\u0194\u0199\u0005H%\u0002\u0195\u0196\u0007;\u0002",
    "\u0002\u0196\u0198\u0005H%\u0002\u0197\u0195\u0003\u0002\u0002\u0002",
    "\u0198\u019b\u0003\u0002\u0002\u0002\u0199\u0197\u0003\u0002\u0002\u0002",
    "\u0199\u019a\u0003\u0002\u0002\u0002\u019a\u019d\u0003\u0002\u0002\u0002",
    "\u019b\u0199\u0003\u0002\u0002\u0002\u019c\u0194\u0003\u0002\u0002\u0002",
    "\u019c\u019d\u0003\u0002\u0002\u0002\u019d\u019e\u0003\u0002\u0002\u0002",
    "\u019e\u019f\u00078\u0002\u0002\u019f_\u0003\u0002\u0002\u0002\u01a0",
    "\u01a1\u00079\u0002\u0002\u01a1\u01a4\u0005f4\u0002\u01a2\u01a3\u0007",
    "<\u0002\u0002\u01a3\u01a5\u0005f4\u0002\u01a4\u01a2\u0003\u0002\u0002",
    "\u0002\u01a4\u01a5\u0003\u0002\u0002\u0002\u01a5\u01a6\u0003\u0002\u0002",
    "\u0002\u01a6\u01a7\u00076\u0002\u0002\u01a7a\u0003\u0002\u0002\u0002",
    "\u01a8\u01ac\u0007J\u0002\u0002\u01a9\u01ac\u0007I\u0002\u0002\u01aa",
    "\u01ac\u0005d3\u0002\u01ab\u01a8\u0003\u0002\u0002\u0002\u01ab\u01a9",
    "\u0003\u0002\u0002\u0002\u01ab\u01aa\u0003\u0002\u0002\u0002\u01acc",
    "\u0003\u0002\u0002\u0002\u01ad\u01ae\t\f\u0002\u0002\u01aee\u0003\u0002",
    "\u0002\u0002\u01af\u01b0\t\r\u0002\u0002\u01b0g\u0003\u0002\u0002\u0002",
    "(jlu}\u007f\u008a\u008c\u0094\u009b\u00a3\u00a5\u00b0\u00b2\u00bd\u00bf",
    "\u00cc\u00d5\u00da\u00fc\u0117\u012c\u0138\u0140\u0146\u014d\u0155\u015f",
    "\u0168\u016d\u0176\u0179\u017d\u0186\u0191\u0199\u019c\u01a4\u01ab"].join("");


const atn = new antlr4.atn.ATNDeserializer().deserialize(serializedATN);

const decisionsToDFA = atn.decisionToState.map( (ds, index) => new antlr4.dfa.DFA(ds, index) );

const sharedContextCache = new antlr4.PredictionContextCache();

export default class CopperParser extends antlr4.Parser {

    static grammarFileName = "Copper.g4";
    static literalNames = [ null, "'model'", "'view'", "'measure'", "'dimension'", 
                            "'join'", "'type'", "'expression'", "'label'", 
                            "'description'", "'primary_key'", "'hidden'", 
                            "'value_format'", "'units'", "'relationship'", 
                            "'from'", "'extends'", "'Aggregate'", "'OVER'", 
                            "'string'", "'number'", "'date'", "'time'", 
                            "'timestamp'", "'boolean'", "'sum'", "'count'", 
                            "'average'", "'min'", "'max'", "'count_distinct'", 
                            "'left_outer'", "'inner'", "'full_outer'", "'cross'", 
                            "'one_to_one'", "'one_to_many'", "'many_to_one'", 
                            "'many_to_many'", "'usd'", "'percent'", "'percent_2'", 
                            "'decimal_2'", "'yes'", "'no'", "'true'", "'false'", 
                            "'and'", "'or'", "'('", "')'", "'{'", "'}'", 
                            "'['", "']'", "'${'", "':'", "','", "'.'", "';;'", 
                            "'+'", "'-'", "'*'", "'/'", "'=='", "'!='", 
                            "'>='", "'<='", "'>'", "'<'" ];
    static symbolicNames = [ null, "MODEL", "VIEW", "MEASURE", "DIMENSION", 
                             "JOIN", "TYPE", "EXPRESSION", "LABEL", "DESCRIPTION", 
                             "PRIMARY_KEY", "HIDDEN_", "VALUE_FORMAT", "UNITS", 
                             "RELATIONSHIP", "FROM", "EXTENDS", "AGGREGATE", 
                             "OVER", "STRING", "NUMBER", "DATE", "TIME", 
                             "TIMESTAMP", "BOOLEAN", "SUM", "COUNT", "AVERAGE", 
                             "MIN", "MAX", "COUNT_DISTINCT", "LEFT_OUTER", 
                             "INNER", "FULL_OUTER", "CROSS", "ONE_TO_ONE", 
                             "ONE_TO_MANY", "MANY_TO_ONE", "MANY_TO_MANY", 
                             "USD", "PERCENT", "PERCENT_2", "DECIMAL_2", 
                             "YES", "NO", "TRUE", "FALSE", "AND", "OR", 
                             "LPAREN", "RPAREN", "LBRACE", "RBRACE", "LBRACKET", 
                             "RBRACKET", "DOLLAR_LBRACE", "COLON", "COMMA", 
                             "DOT", "DOUBLE_SEMICOLON", "PLUS", "MINUS", 
                             "MULTIPLY", "DIVIDE", "EQUALS", "NOT_EQUALS", 
                             "GTE", "LTE", "GREATER_THAN", "LESS_THAN", 
                             "IDENTIFIER", "STRING_LITERAL", "NUMBER_LITERAL", 
                             "COMMENT", "NEWLINE", "WS" ];
    static ruleNames = [ "program", "statement", "modelStatement", "viewStatement", 
                         "modelElement", "viewElement", "measureStatement", 
                         "dimensionStatement", "joinStatement", "dimensionParameter", 
                         "measureParameter", "joinParameter", "typeParameter", 
                         "measureTypeParameter", "expressionParameter", 
                         "labelParameter", "descriptionParameter", "primaryKeyParameter", 
                         "hiddenParameter", "valueFormatParameter", "unitsParameter", 
                         "joinTypeParameter", "relationshipParameter", "fromStatement", 
                         "extendsStatement", "identifierList", "dimensionType", 
                         "measureType", "joinType", "relationshipType", 
                         "formatName", "booleanValue", "daxExpression", 
                         "daxContent", "stringLiteral", "expression", "logicalOrExpression", 
                         "logicalAndExpression", "comparisonExpression", 
                         "additiveExpression", "multiplicativeExpression", 
                         "primary", "functionCall", "overClause", "namedArgument", 
                         "value_", "list_", "fieldReference", "literal", 
                         "booleanLiteral", "identifier" ];

    constructor(input) {
        super(input);
        this._interp = new antlr4.atn.ParserATNSimulator(this, atn, decisionsToDFA, sharedContextCache);
        this.ruleNames = CopperParser.ruleNames;
        this.literalNames = CopperParser.literalNames;
        this.symbolicNames = CopperParser.symbolicNames;
    }

    get atn() {
        return atn;
    }


	program() {
	    let localctx = new ProgramContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 0, CopperParser.RULE_program);
	    var _la = 0; // Token type
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 106;
	        this._errHandler.sync(this);
	        _la = this._input.LA(1);
	        while((((_la) & ~0x1f) == 0 && ((1 << _la) & ((1 << CopperParser.MODEL) | (1 << CopperParser.VIEW) | (1 << CopperParser.MEASURE) | (1 << CopperParser.DIMENSION))) !== 0) || _la===CopperParser.NEWLINE) {
	            this.state = 104;
	            this._errHandler.sync(this);
	            switch(this._input.LA(1)) {
	            case CopperParser.MODEL:
	            case CopperParser.VIEW:
	            case CopperParser.MEASURE:
	            case CopperParser.DIMENSION:
	                this.state = 102;
	                this.statement();
	                break;
	            case CopperParser.NEWLINE:
	                this.state = 103;
	                this.match(CopperParser.NEWLINE);
	                break;
	            default:
	                throw new antlr4.error.NoViableAltException(this);
	            }
	            this.state = 108;
	            this._errHandler.sync(this);
	            _la = this._input.LA(1);
	        }
	        this.state = 109;
	        this.match(CopperParser.EOF);
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}


	statement() {
	    let localctx = new StatementContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 2, CopperParser.RULE_statement);
	    try {
	        this.state = 115;
	        this._errHandler.sync(this);
	        switch(this._input.LA(1)) {
	        case CopperParser.MODEL:
	            this.enterOuterAlt(localctx, 1);
	            this.state = 111;
	            this.modelStatement();
	            break;
	        case CopperParser.VIEW:
	            this.enterOuterAlt(localctx, 2);
	            this.state = 112;
	            this.viewStatement();
	            break;
	        case CopperParser.MEASURE:
	            this.enterOuterAlt(localctx, 3);
	            this.state = 113;
	            this.measureStatement();
	            break;
	        case CopperParser.DIMENSION:
	            this.enterOuterAlt(localctx, 4);
	            this.state = 114;
	            this.dimensionStatement();
	            break;
	        default:
	            throw new antlr4.error.NoViableAltException(this);
	        }
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}


	modelStatement() {
	    let localctx = new ModelStatementContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 4, CopperParser.RULE_modelStatement);
	    var _la = 0; // Token type
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 117;
	        this.match(CopperParser.MODEL);
	        this.state = 118;
	        this.match(CopperParser.COLON);
	        this.state = 119;
	        this.identifier();
	        this.state = 120;
	        this.match(CopperParser.LBRACE);
	        this.state = 125;
	        this._errHandler.sync(this);
	        _la = this._input.LA(1);
	        while((((_la) & ~0x1f) == 0 && ((1 << _la) & ((1 << CopperParser.MEASURE) | (1 << CopperParser.DIMENSION) | (1 << CopperParser.JOIN))) !== 0) || _la===CopperParser.NEWLINE) {
	            this.state = 123;
	            this._errHandler.sync(this);
	            switch(this._input.LA(1)) {
	            case CopperParser.MEASURE:
	            case CopperParser.DIMENSION:
	            case CopperParser.JOIN:
	                this.state = 121;
	                this.modelElement();
	                break;
	            case CopperParser.NEWLINE:
	                this.state = 122;
	                this.match(CopperParser.NEWLINE);
	                break;
	            default:
	                throw new antlr4.error.NoViableAltException(this);
	            }
	            this.state = 127;
	            this._errHandler.sync(this);
	            _la = this._input.LA(1);
	        }
	        this.state = 128;
	        this.match(CopperParser.RBRACE);
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}


	viewStatement() {
	    let localctx = new ViewStatementContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 6, CopperParser.RULE_viewStatement);
	    var _la = 0; // Token type
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 130;
	        this.match(CopperParser.VIEW);
	        this.state = 131;
	        this.match(CopperParser.COLON);
	        this.state = 132;
	        this.identifier();
	        this.state = 133;
	        this.match(CopperParser.LBRACE);
	        this.state = 138;
	        this._errHandler.sync(this);
	        _la = this._input.LA(1);
	        while((((_la) & ~0x1f) == 0 && ((1 << _la) & ((1 << CopperParser.MEASURE) | (1 << CopperParser.DIMENSION) | (1 << CopperParser.JOIN) | (1 << CopperParser.FROM) | (1 << CopperParser.EXTENDS))) !== 0) || _la===CopperParser.NEWLINE) {
	            this.state = 136;
	            this._errHandler.sync(this);
	            switch(this._input.LA(1)) {
	            case CopperParser.MEASURE:
	            case CopperParser.DIMENSION:
	            case CopperParser.JOIN:
	            case CopperParser.FROM:
	            case CopperParser.EXTENDS:
	                this.state = 134;
	                this.viewElement();
	                break;
	            case CopperParser.NEWLINE:
	                this.state = 135;
	                this.match(CopperParser.NEWLINE);
	                break;
	            default:
	                throw new antlr4.error.NoViableAltException(this);
	            }
	            this.state = 140;
	            this._errHandler.sync(this);
	            _la = this._input.LA(1);
	        }
	        this.state = 141;
	        this.match(CopperParser.RBRACE);
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}


	modelElement() {
	    let localctx = new ModelElementContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 8, CopperParser.RULE_modelElement);
	    try {
	        this.state = 146;
	        this._errHandler.sync(this);
	        switch(this._input.LA(1)) {
	        case CopperParser.DIMENSION:
	            this.enterOuterAlt(localctx, 1);
	            this.state = 143;
	            this.dimensionStatement();
	            break;
	        case CopperParser.MEASURE:
	            this.enterOuterAlt(localctx, 2);
	            this.state = 144;
	            this.measureStatement();
	            break;
	        case CopperParser.JOIN:
	            this.enterOuterAlt(localctx, 3);
	            this.state = 145;
	            this.joinStatement();
	            break;
	        default:
	            throw new antlr4.error.NoViableAltException(this);
	        }
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}


	viewElement() {
	    let localctx = new ViewElementContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 10, CopperParser.RULE_viewElement);
	    try {
	        this.state = 153;
	        this._errHandler.sync(this);
	        switch(this._input.LA(1)) {
	        case CopperParser.FROM:
	            this.enterOuterAlt(localctx, 1);
	            this.state = 148;
	            this.fromStatement();
	            break;
	        case CopperParser.EXTENDS:
	            this.enterOuterAlt(localctx, 2);
	            this.state = 149;
	            this.extendsStatement();
	            break;
	        case CopperParser.JOIN:
	            this.enterOuterAlt(localctx, 3);
	            this.state = 150;
	            this.joinStatement();
	            break;
	        case CopperParser.DIMENSION:
	            this.enterOuterAlt(localctx, 4);
	            this.state = 151;
	            this.dimensionStatement();
	            break;
	        case CopperParser.MEASURE:
	            this.enterOuterAlt(localctx, 5);
	            this.state = 152;
	            this.measureStatement();
	            break;
	        default:
	            throw new antlr4.error.NoViableAltException(this);
	        }
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}


	measureStatement() {
	    let localctx = new MeasureStatementContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 12, CopperParser.RULE_measureStatement);
	    var _la = 0; // Token type
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 155;
	        this.match(CopperParser.MEASURE);
	        this.state = 156;
	        this.match(CopperParser.COLON);
	        this.state = 157;
	        this.identifier();
	        this.state = 158;
	        this.match(CopperParser.LBRACE);
	        this.state = 163;
	        this._errHandler.sync(this);
	        _la = this._input.LA(1);
	        while((((_la) & ~0x1f) == 0 && ((1 << _la) & ((1 << CopperParser.TYPE) | (1 << CopperParser.EXPRESSION) | (1 << CopperParser.LABEL) | (1 << CopperParser.DESCRIPTION) | (1 << CopperParser.HIDDEN_) | (1 << CopperParser.VALUE_FORMAT) | (1 << CopperParser.UNITS))) !== 0) || _la===CopperParser.NEWLINE) {
	            this.state = 161;
	            this._errHandler.sync(this);
	            switch(this._input.LA(1)) {
	            case CopperParser.TYPE:
	            case CopperParser.EXPRESSION:
	            case CopperParser.LABEL:
	            case CopperParser.DESCRIPTION:
	            case CopperParser.HIDDEN_:
	            case CopperParser.VALUE_FORMAT:
	            case CopperParser.UNITS:
	                this.state = 159;
	                this.measureParameter();
	                break;
	            case CopperParser.NEWLINE:
	                this.state = 160;
	                this.match(CopperParser.NEWLINE);
	                break;
	            default:
	                throw new antlr4.error.NoViableAltException(this);
	            }
	            this.state = 165;
	            this._errHandler.sync(this);
	            _la = this._input.LA(1);
	        }
	        this.state = 166;
	        this.match(CopperParser.RBRACE);
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}


	dimensionStatement() {
	    let localctx = new DimensionStatementContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 14, CopperParser.RULE_dimensionStatement);
	    var _la = 0; // Token type
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 168;
	        this.match(CopperParser.DIMENSION);
	        this.state = 169;
	        this.match(CopperParser.COLON);
	        this.state = 170;
	        this.identifier();
	        this.state = 171;
	        this.match(CopperParser.LBRACE);
	        this.state = 176;
	        this._errHandler.sync(this);
	        _la = this._input.LA(1);
	        while((((_la) & ~0x1f) == 0 && ((1 << _la) & ((1 << CopperParser.TYPE) | (1 << CopperParser.EXPRESSION) | (1 << CopperParser.LABEL) | (1 << CopperParser.DESCRIPTION) | (1 << CopperParser.PRIMARY_KEY) | (1 << CopperParser.HIDDEN_) | (1 << CopperParser.VALUE_FORMAT) | (1 << CopperParser.UNITS))) !== 0) || _la===CopperParser.NEWLINE) {
	            this.state = 174;
	            this._errHandler.sync(this);
	            switch(this._input.LA(1)) {
	            case CopperParser.TYPE:
	            case CopperParser.EXPRESSION:
	            case CopperParser.LABEL:
	            case CopperParser.DESCRIPTION:
	            case CopperParser.PRIMARY_KEY:
	            case CopperParser.HIDDEN_:
	            case CopperParser.VALUE_FORMAT:
	            case CopperParser.UNITS:
	                this.state = 172;
	                this.dimensionParameter();
	                break;
	            case CopperParser.NEWLINE:
	                this.state = 173;
	                this.match(CopperParser.NEWLINE);
	                break;
	            default:
	                throw new antlr4.error.NoViableAltException(this);
	            }
	            this.state = 178;
	            this._errHandler.sync(this);
	            _la = this._input.LA(1);
	        }
	        this.state = 179;
	        this.match(CopperParser.RBRACE);
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}


	joinStatement() {
	    let localctx = new JoinStatementContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 16, CopperParser.RULE_joinStatement);
	    var _la = 0; // Token type
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 181;
	        this.match(CopperParser.JOIN);
	        this.state = 182;
	        this.match(CopperParser.COLON);
	        this.state = 183;
	        this.identifier();
	        this.state = 184;
	        this.match(CopperParser.LBRACE);
	        this.state = 189;
	        this._errHandler.sync(this);
	        _la = this._input.LA(1);
	        while((((_la) & ~0x1f) == 0 && ((1 << _la) & ((1 << CopperParser.TYPE) | (1 << CopperParser.EXPRESSION) | (1 << CopperParser.RELATIONSHIP))) !== 0) || _la===CopperParser.NEWLINE) {
	            this.state = 187;
	            this._errHandler.sync(this);
	            switch(this._input.LA(1)) {
	            case CopperParser.TYPE:
	            case CopperParser.EXPRESSION:
	            case CopperParser.RELATIONSHIP:
	                this.state = 185;
	                this.joinParameter();
	                break;
	            case CopperParser.NEWLINE:
	                this.state = 186;
	                this.match(CopperParser.NEWLINE);
	                break;
	            default:
	                throw new antlr4.error.NoViableAltException(this);
	            }
	            this.state = 191;
	            this._errHandler.sync(this);
	            _la = this._input.LA(1);
	        }
	        this.state = 192;
	        this.match(CopperParser.RBRACE);
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}


	dimensionParameter() {
	    let localctx = new DimensionParameterContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 18, CopperParser.RULE_dimensionParameter);
	    try {
	        this.state = 202;
	        this._errHandler.sync(this);
	        switch(this._input.LA(1)) {
	        case CopperParser.TYPE:
	            this.enterOuterAlt(localctx, 1);
	            this.state = 194;
	            this.typeParameter();
	            break;
	        case CopperParser.EXPRESSION:
	            this.enterOuterAlt(localctx, 2);
	            this.state = 195;
	            this.expressionParameter();
	            break;
	        case CopperParser.LABEL:
	            this.enterOuterAlt(localctx, 3);
	            this.state = 196;
	            this.labelParameter();
	            break;
	        case CopperParser.DESCRIPTION:
	            this.enterOuterAlt(localctx, 4);
	            this.state = 197;
	            this.descriptionParameter();
	            break;
	        case CopperParser.PRIMARY_KEY:
	            this.enterOuterAlt(localctx, 5);
	            this.state = 198;
	            this.primaryKeyParameter();
	            break;
	        case CopperParser.HIDDEN_:
	            this.enterOuterAlt(localctx, 6);
	            this.state = 199;
	            this.hiddenParameter();
	            break;
	        case CopperParser.VALUE_FORMAT:
	            this.enterOuterAlt(localctx, 7);
	            this.state = 200;
	            this.valueFormatParameter();
	            break;
	        case CopperParser.UNITS:
	            this.enterOuterAlt(localctx, 8);
	            this.state = 201;
	            this.unitsParameter();
	            break;
	        default:
	            throw new antlr4.error.NoViableAltException(this);
	        }
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}


	measureParameter() {
	    let localctx = new MeasureParameterContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 20, CopperParser.RULE_measureParameter);
	    try {
	        this.state = 211;
	        this._errHandler.sync(this);
	        switch(this._input.LA(1)) {
	        case CopperParser.TYPE:
	            this.enterOuterAlt(localctx, 1);
	            this.state = 204;
	            this.measureTypeParameter();
	            break;
	        case CopperParser.EXPRESSION:
	            this.enterOuterAlt(localctx, 2);
	            this.state = 205;
	            this.expressionParameter();
	            break;
	        case CopperParser.LABEL:
	            this.enterOuterAlt(localctx, 3);
	            this.state = 206;
	            this.labelParameter();
	            break;
	        case CopperParser.DESCRIPTION:
	            this.enterOuterAlt(localctx, 4);
	            this.state = 207;
	            this.descriptionParameter();
	            break;
	        case CopperParser.HIDDEN_:
	            this.enterOuterAlt(localctx, 5);
	            this.state = 208;
	            this.hiddenParameter();
	            break;
	        case CopperParser.VALUE_FORMAT:
	            this.enterOuterAlt(localctx, 6);
	            this.state = 209;
	            this.valueFormatParameter();
	            break;
	        case CopperParser.UNITS:
	            this.enterOuterAlt(localctx, 7);
	            this.state = 210;
	            this.unitsParameter();
	            break;
	        default:
	            throw new antlr4.error.NoViableAltException(this);
	        }
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}


	joinParameter() {
	    let localctx = new JoinParameterContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 22, CopperParser.RULE_joinParameter);
	    try {
	        this.state = 216;
	        this._errHandler.sync(this);
	        switch(this._input.LA(1)) {
	        case CopperParser.TYPE:
	            this.enterOuterAlt(localctx, 1);
	            this.state = 213;
	            this.joinTypeParameter();
	            break;
	        case CopperParser.RELATIONSHIP:
	            this.enterOuterAlt(localctx, 2);
	            this.state = 214;
	            this.relationshipParameter();
	            break;
	        case CopperParser.EXPRESSION:
	            this.enterOuterAlt(localctx, 3);
	            this.state = 215;
	            this.expressionParameter();
	            break;
	        default:
	            throw new antlr4.error.NoViableAltException(this);
	        }
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}


	typeParameter() {
	    let localctx = new TypeParameterContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 24, CopperParser.RULE_typeParameter);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 218;
	        this.match(CopperParser.TYPE);
	        this.state = 219;
	        this.match(CopperParser.COLON);
	        this.state = 220;
	        this.dimensionType();
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}


	measureTypeParameter() {
	    let localctx = new MeasureTypeParameterContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 26, CopperParser.RULE_measureTypeParameter);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 222;
	        this.match(CopperParser.TYPE);
	        this.state = 223;
	        this.match(CopperParser.COLON);
	        this.state = 224;
	        this.measureType();
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}


	expressionParameter() {
	    let localctx = new ExpressionParameterContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 28, CopperParser.RULE_expressionParameter);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 226;
	        this.match(CopperParser.EXPRESSION);
	        this.state = 227;
	        this.match(CopperParser.COLON);
	        this.state = 228;
	        this.daxExpression();
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}


	labelParameter() {
	    let localctx = new LabelParameterContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 30, CopperParser.RULE_labelParameter);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 230;
	        this.match(CopperParser.LABEL);
	        this.state = 231;
	        this.match(CopperParser.COLON);
	        this.state = 232;
	        this.stringLiteral();
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}


	descriptionParameter() {
	    let localctx = new DescriptionParameterContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 32, CopperParser.RULE_descriptionParameter);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 234;
	        this.match(CopperParser.DESCRIPTION);
	        this.state = 235;
	        this.match(CopperParser.COLON);
	        this.state = 236;
	        this.stringLiteral();
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}


	primaryKeyParameter() {
	    let localctx = new PrimaryKeyParameterContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 34, CopperParser.RULE_primaryKeyParameter);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 238;
	        this.match(CopperParser.PRIMARY_KEY);
	        this.state = 239;
	        this.match(CopperParser.COLON);
	        this.state = 240;
	        this.booleanValue();
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}


	hiddenParameter() {
	    let localctx = new HiddenParameterContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 36, CopperParser.RULE_hiddenParameter);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 242;
	        this.match(CopperParser.HIDDEN_);
	        this.state = 243;
	        this.match(CopperParser.COLON);
	        this.state = 244;
	        this.booleanValue();
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}


	valueFormatParameter() {
	    let localctx = new ValueFormatParameterContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 38, CopperParser.RULE_valueFormatParameter);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 246;
	        this.match(CopperParser.VALUE_FORMAT);
	        this.state = 247;
	        this.match(CopperParser.COLON);
	        this.state = 250;
	        this._errHandler.sync(this);
	        switch(this._input.LA(1)) {
	        case CopperParser.STRING_LITERAL:
	            this.state = 248;
	            this.stringLiteral();
	            break;
	        case CopperParser.USD:
	        case CopperParser.PERCENT:
	        case CopperParser.PERCENT_2:
	        case CopperParser.DECIMAL_2:
	            this.state = 249;
	            this.formatName();
	            break;
	        default:
	            throw new antlr4.error.NoViableAltException(this);
	        }
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}


	unitsParameter() {
	    let localctx = new UnitsParameterContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 40, CopperParser.RULE_unitsParameter);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 252;
	        this.match(CopperParser.UNITS);
	        this.state = 253;
	        this.match(CopperParser.COLON);
	        this.state = 254;
	        this.stringLiteral();
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}


	joinTypeParameter() {
	    let localctx = new JoinTypeParameterContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 42, CopperParser.RULE_joinTypeParameter);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 256;
	        this.match(CopperParser.TYPE);
	        this.state = 257;
	        this.match(CopperParser.COLON);
	        this.state = 258;
	        this.joinType();
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}


	relationshipParameter() {
	    let localctx = new RelationshipParameterContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 44, CopperParser.RULE_relationshipParameter);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 260;
	        this.match(CopperParser.RELATIONSHIP);
	        this.state = 261;
	        this.match(CopperParser.COLON);
	        this.state = 262;
	        this.relationshipType();
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}


	fromStatement() {
	    let localctx = new FromStatementContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 46, CopperParser.RULE_fromStatement);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 264;
	        this.match(CopperParser.FROM);
	        this.state = 265;
	        this.match(CopperParser.COLON);
	        this.state = 266;
	        this.identifier();
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}


	extendsStatement() {
	    let localctx = new ExtendsStatementContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 48, CopperParser.RULE_extendsStatement);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 268;
	        this.match(CopperParser.EXTENDS);
	        this.state = 269;
	        this.match(CopperParser.COLON);
	        this.state = 270;
	        this.identifierList();
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}


	identifierList() {
	    let localctx = new IdentifierListContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 50, CopperParser.RULE_identifierList);
	    var _la = 0; // Token type
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 272;
	        this.identifier();
	        this.state = 277;
	        this._errHandler.sync(this);
	        _la = this._input.LA(1);
	        while(_la===CopperParser.COMMA) {
	            this.state = 273;
	            this.match(CopperParser.COMMA);
	            this.state = 274;
	            this.identifier();
	            this.state = 279;
	            this._errHandler.sync(this);
	            _la = this._input.LA(1);
	        }
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}


	dimensionType() {
	    let localctx = new DimensionTypeContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 52, CopperParser.RULE_dimensionType);
	    var _la = 0; // Token type
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 280;
	        _la = this._input.LA(1);
	        if(!((((_la) & ~0x1f) == 0 && ((1 << _la) & ((1 << CopperParser.STRING) | (1 << CopperParser.NUMBER) | (1 << CopperParser.DATE) | (1 << CopperParser.TIME) | (1 << CopperParser.TIMESTAMP) | (1 << CopperParser.BOOLEAN))) !== 0))) {
	        this._errHandler.recoverInline(this);
	        }
	        else {
	        	this._errHandler.reportMatch(this);
	            this.consume();
	        }
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}


	measureType() {
	    let localctx = new MeasureTypeContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 54, CopperParser.RULE_measureType);
	    var _la = 0; // Token type
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 282;
	        _la = this._input.LA(1);
	        if(!((((_la) & ~0x1f) == 0 && ((1 << _la) & ((1 << CopperParser.NUMBER) | (1 << CopperParser.SUM) | (1 << CopperParser.COUNT) | (1 << CopperParser.AVERAGE) | (1 << CopperParser.MIN) | (1 << CopperParser.MAX) | (1 << CopperParser.COUNT_DISTINCT))) !== 0))) {
	        this._errHandler.recoverInline(this);
	        }
	        else {
	        	this._errHandler.reportMatch(this);
	            this.consume();
	        }
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}


	joinType() {
	    let localctx = new JoinTypeContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 56, CopperParser.RULE_joinType);
	    var _la = 0; // Token type
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 284;
	        _la = this._input.LA(1);
	        if(!(((((_la - 31)) & ~0x1f) == 0 && ((1 << (_la - 31)) & ((1 << (CopperParser.LEFT_OUTER - 31)) | (1 << (CopperParser.INNER - 31)) | (1 << (CopperParser.FULL_OUTER - 31)) | (1 << (CopperParser.CROSS - 31)))) !== 0))) {
	        this._errHandler.recoverInline(this);
	        }
	        else {
	        	this._errHandler.reportMatch(this);
	            this.consume();
	        }
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}


	relationshipType() {
	    let localctx = new RelationshipTypeContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 58, CopperParser.RULE_relationshipType);
	    var _la = 0; // Token type
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 286;
	        _la = this._input.LA(1);
	        if(!(((((_la - 35)) & ~0x1f) == 0 && ((1 << (_la - 35)) & ((1 << (CopperParser.ONE_TO_ONE - 35)) | (1 << (CopperParser.ONE_TO_MANY - 35)) | (1 << (CopperParser.MANY_TO_ONE - 35)) | (1 << (CopperParser.MANY_TO_MANY - 35)))) !== 0))) {
	        this._errHandler.recoverInline(this);
	        }
	        else {
	        	this._errHandler.reportMatch(this);
	            this.consume();
	        }
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}


	formatName() {
	    let localctx = new FormatNameContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 60, CopperParser.RULE_formatName);
	    var _la = 0; // Token type
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 288;
	        _la = this._input.LA(1);
	        if(!(((((_la - 39)) & ~0x1f) == 0 && ((1 << (_la - 39)) & ((1 << (CopperParser.USD - 39)) | (1 << (CopperParser.PERCENT - 39)) | (1 << (CopperParser.PERCENT_2 - 39)) | (1 << (CopperParser.DECIMAL_2 - 39)))) !== 0))) {
	        this._errHandler.recoverInline(this);
	        }
	        else {
	        	this._errHandler.reportMatch(this);
	            this.consume();
	        }
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}


	booleanValue() {
	    let localctx = new BooleanValueContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 62, CopperParser.RULE_booleanValue);
	    var _la = 0; // Token type
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 290;
	        _la = this._input.LA(1);
	        if(!(((((_la - 43)) & ~0x1f) == 0 && ((1 << (_la - 43)) & ((1 << (CopperParser.YES - 43)) | (1 << (CopperParser.NO - 43)) | (1 << (CopperParser.TRUE - 43)) | (1 << (CopperParser.FALSE - 43)))) !== 0))) {
	        this._errHandler.recoverInline(this);
	        }
	        else {
	        	this._errHandler.reportMatch(this);
	            this.consume();
	        }
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}


	daxExpression() {
	    let localctx = new DaxExpressionContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 64, CopperParser.RULE_daxExpression);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 292;
	        this.daxContent();
	        this.state = 293;
	        this.match(CopperParser.DOUBLE_SEMICOLON);
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}


	daxContent() {
	    let localctx = new DaxContentContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 66, CopperParser.RULE_daxContent);
	    var _la = 0; // Token type
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 298;
	        this._errHandler.sync(this);
	        _la = this._input.LA(1);
	        while((((_la) & ~0x1f) == 0 && ((1 << _la) & ((1 << CopperParser.MODEL) | (1 << CopperParser.VIEW) | (1 << CopperParser.MEASURE) | (1 << CopperParser.DIMENSION) | (1 << CopperParser.JOIN) | (1 << CopperParser.TYPE) | (1 << CopperParser.EXPRESSION) | (1 << CopperParser.LABEL) | (1 << CopperParser.DESCRIPTION) | (1 << CopperParser.PRIMARY_KEY) | (1 << CopperParser.HIDDEN_) | (1 << CopperParser.VALUE_FORMAT) | (1 << CopperParser.UNITS) | (1 << CopperParser.RELATIONSHIP) | (1 << CopperParser.FROM) | (1 << CopperParser.EXTENDS) | (1 << CopperParser.AGGREGATE) | (1 << CopperParser.OVER) | (1 << CopperParser.STRING) | (1 << CopperParser.NUMBER) | (1 << CopperParser.DATE) | (1 << CopperParser.TIME) | (1 << CopperParser.TIMESTAMP) | (1 << CopperParser.BOOLEAN) | (1 << CopperParser.SUM) | (1 << CopperParser.COUNT) | (1 << CopperParser.AVERAGE) | (1 << CopperParser.MIN) | (1 << CopperParser.MAX) | (1 << CopperParser.COUNT_DISTINCT) | (1 << CopperParser.LEFT_OUTER))) !== 0) || ((((_la - 32)) & ~0x1f) == 0 && ((1 << (_la - 32)) & ((1 << (CopperParser.INNER - 32)) | (1 << (CopperParser.FULL_OUTER - 32)) | (1 << (CopperParser.CROSS - 32)) | (1 << (CopperParser.ONE_TO_ONE - 32)) | (1 << (CopperParser.ONE_TO_MANY - 32)) | (1 << (CopperParser.MANY_TO_ONE - 32)) | (1 << (CopperParser.MANY_TO_MANY - 32)) | (1 << (CopperParser.USD - 32)) | (1 << (CopperParser.PERCENT - 32)) | (1 << (CopperParser.PERCENT_2 - 32)) | (1 << (CopperParser.DECIMAL_2 - 32)) | (1 << (CopperParser.YES - 32)) | (1 << (CopperParser.NO - 32)) | (1 << (CopperParser.TRUE - 32)) | (1 << (CopperParser.FALSE - 32)) | (1 << (CopperParser.AND - 32)) | (1 << (CopperParser.OR - 32)) | (1 << (CopperParser.LPAREN - 32)) | (1 << (CopperParser.RPAREN - 32)) | (1 << (CopperParser.LBRACE - 32)) | (1 << (CopperParser.RBRACE - 32)) | (1 << (CopperParser.LBRACKET - 32)) | (1 << (CopperParser.RBRACKET - 32)) | (1 << (CopperParser.DOLLAR_LBRACE - 32)) | (1 << (CopperParser.COLON - 32)) | (1 << (CopperParser.COMMA - 32)) | (1 << (CopperParser.DOT - 32)) | (1 << (CopperParser.PLUS - 32)) | (1 << (CopperParser.MINUS - 32)) | (1 << (CopperParser.MULTIPLY - 32)) | (1 << (CopperParser.DIVIDE - 32)))) !== 0) || ((((_la - 64)) & ~0x1f) == 0 && ((1 << (_la - 64)) & ((1 << (CopperParser.EQUALS - 64)) | (1 << (CopperParser.NOT_EQUALS - 64)) | (1 << (CopperParser.GTE - 64)) | (1 << (CopperParser.LTE - 64)) | (1 << (CopperParser.GREATER_THAN - 64)) | (1 << (CopperParser.LESS_THAN - 64)) | (1 << (CopperParser.IDENTIFIER - 64)) | (1 << (CopperParser.STRING_LITERAL - 64)) | (1 << (CopperParser.NUMBER_LITERAL - 64)) | (1 << (CopperParser.COMMENT - 64)) | (1 << (CopperParser.WS - 64)))) !== 0)) {
	            this.state = 295;
	            _la = this._input.LA(1);
	            if(_la<=0 || _la===CopperParser.DOUBLE_SEMICOLON || _la===CopperParser.NEWLINE) {
	            this._errHandler.recoverInline(this);
	            }
	            else {
	            	this._errHandler.reportMatch(this);
	                this.consume();
	            }
	            this.state = 300;
	            this._errHandler.sync(this);
	            _la = this._input.LA(1);
	        }
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}


	stringLiteral() {
	    let localctx = new StringLiteralContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 68, CopperParser.RULE_stringLiteral);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 301;
	        this.match(CopperParser.STRING_LITERAL);
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}


	expression() {
	    let localctx = new ExpressionContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 70, CopperParser.RULE_expression);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 303;
	        this.logicalOrExpression();
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}


	logicalOrExpression() {
	    let localctx = new LogicalOrExpressionContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 72, CopperParser.RULE_logicalOrExpression);
	    var _la = 0; // Token type
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 305;
	        this.logicalAndExpression();
	        this.state = 310;
	        this._errHandler.sync(this);
	        _la = this._input.LA(1);
	        while(_la===CopperParser.OR) {
	            this.state = 306;
	            this.match(CopperParser.OR);
	            this.state = 307;
	            this.logicalAndExpression();
	            this.state = 312;
	            this._errHandler.sync(this);
	            _la = this._input.LA(1);
	        }
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}


	logicalAndExpression() {
	    let localctx = new LogicalAndExpressionContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 74, CopperParser.RULE_logicalAndExpression);
	    var _la = 0; // Token type
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 313;
	        this.comparisonExpression();
	        this.state = 318;
	        this._errHandler.sync(this);
	        _la = this._input.LA(1);
	        while(_la===CopperParser.AND) {
	            this.state = 314;
	            this.match(CopperParser.AND);
	            this.state = 315;
	            this.comparisonExpression();
	            this.state = 320;
	            this._errHandler.sync(this);
	            _la = this._input.LA(1);
	        }
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}


	comparisonExpression() {
	    let localctx = new ComparisonExpressionContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 76, CopperParser.RULE_comparisonExpression);
	    var _la = 0; // Token type
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 321;
	        this.additiveExpression();
	        this.state = 324;
	        this._errHandler.sync(this);
	        _la = this._input.LA(1);
	        if(((((_la - 64)) & ~0x1f) == 0 && ((1 << (_la - 64)) & ((1 << (CopperParser.EQUALS - 64)) | (1 << (CopperParser.NOT_EQUALS - 64)) | (1 << (CopperParser.GTE - 64)) | (1 << (CopperParser.LTE - 64)) | (1 << (CopperParser.GREATER_THAN - 64)) | (1 << (CopperParser.LESS_THAN - 64)))) !== 0)) {
	            this.state = 322;
	            _la = this._input.LA(1);
	            if(!(((((_la - 64)) & ~0x1f) == 0 && ((1 << (_la - 64)) & ((1 << (CopperParser.EQUALS - 64)) | (1 << (CopperParser.NOT_EQUALS - 64)) | (1 << (CopperParser.GTE - 64)) | (1 << (CopperParser.LTE - 64)) | (1 << (CopperParser.GREATER_THAN - 64)) | (1 << (CopperParser.LESS_THAN - 64)))) !== 0))) {
	            this._errHandler.recoverInline(this);
	            }
	            else {
	            	this._errHandler.reportMatch(this);
	                this.consume();
	            }
	            this.state = 323;
	            this.additiveExpression();
	        }

	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}


	additiveExpression() {
	    let localctx = new AdditiveExpressionContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 78, CopperParser.RULE_additiveExpression);
	    var _la = 0; // Token type
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 326;
	        this.multiplicativeExpression();
	        this.state = 331;
	        this._errHandler.sync(this);
	        _la = this._input.LA(1);
	        while(_la===CopperParser.PLUS || _la===CopperParser.MINUS) {
	            this.state = 327;
	            _la = this._input.LA(1);
	            if(!(_la===CopperParser.PLUS || _la===CopperParser.MINUS)) {
	            this._errHandler.recoverInline(this);
	            }
	            else {
	            	this._errHandler.reportMatch(this);
	                this.consume();
	            }
	            this.state = 328;
	            this.multiplicativeExpression();
	            this.state = 333;
	            this._errHandler.sync(this);
	            _la = this._input.LA(1);
	        }
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}


	multiplicativeExpression() {
	    let localctx = new MultiplicativeExpressionContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 80, CopperParser.RULE_multiplicativeExpression);
	    var _la = 0; // Token type
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 334;
	        this.primary();
	        this.state = 339;
	        this._errHandler.sync(this);
	        _la = this._input.LA(1);
	        while(_la===CopperParser.MULTIPLY || _la===CopperParser.DIVIDE) {
	            this.state = 335;
	            _la = this._input.LA(1);
	            if(!(_la===CopperParser.MULTIPLY || _la===CopperParser.DIVIDE)) {
	            this._errHandler.recoverInline(this);
	            }
	            else {
	            	this._errHandler.reportMatch(this);
	                this.consume();
	            }
	            this.state = 336;
	            this.primary();
	            this.state = 341;
	            this._errHandler.sync(this);
	            _la = this._input.LA(1);
	        }
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}


	primary() {
	    let localctx = new PrimaryContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 82, CopperParser.RULE_primary);
	    try {
	        this.state = 349;
	        this._errHandler.sync(this);
	        var la_ = this._interp.adaptivePredict(this._input,26,this._ctx);
	        switch(la_) {
	        case 1:
	            this.enterOuterAlt(localctx, 1);
	            this.state = 342;
	            this.match(CopperParser.LPAREN);
	            this.state = 343;
	            this.expression();
	            this.state = 344;
	            this.match(CopperParser.RPAREN);
	            break;

	        case 2:
	            this.enterOuterAlt(localctx, 2);
	            this.state = 346;
	            this.literal();
	            break;

	        case 3:
	            this.enterOuterAlt(localctx, 3);
	            this.state = 347;
	            this.fieldReference();
	            break;

	        case 4:
	            this.enterOuterAlt(localctx, 4);
	            this.state = 348;
	            this.functionCall();
	            break;

	        }
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}


	functionCall() {
	    let localctx = new FunctionCallContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 84, CopperParser.RULE_functionCall);
	    var _la = 0; // Token type
	    try {
	        this.state = 379;
	        this._errHandler.sync(this);
	        switch(this._input.LA(1)) {
	        case CopperParser.AGGREGATE:
	            localctx = new AggregateFuncContext(this, localctx);
	            this.enterOuterAlt(localctx, 1);
	            this.state = 351;
	            this.match(CopperParser.AGGREGATE);
	            this.state = 352;
	            this.match(CopperParser.LPAREN);
	            this.state = 353;
	            this.namedArgument();
	            this.state = 358;
	            this._errHandler.sync(this);
	            _la = this._input.LA(1);
	            while(_la===CopperParser.COMMA) {
	                this.state = 354;
	                this.match(CopperParser.COMMA);
	                this.state = 355;
	                this.namedArgument();
	                this.state = 360;
	                this._errHandler.sync(this);
	                _la = this._input.LA(1);
	            }
	            this.state = 361;
	            this.match(CopperParser.RPAREN);
	            this.state = 363;
	            this._errHandler.sync(this);
	            _la = this._input.LA(1);
	            if(_la===CopperParser.OVER) {
	                this.state = 362;
	                this.overClause();
	            }

	            break;
	        case CopperParser.STRING:
	        case CopperParser.NUMBER:
	        case CopperParser.DATE:
	        case CopperParser.TIME:
	        case CopperParser.TIMESTAMP:
	        case CopperParser.BOOLEAN:
	        case CopperParser.SUM:
	        case CopperParser.COUNT:
	        case CopperParser.AVERAGE:
	        case CopperParser.MIN:
	        case CopperParser.MAX:
	        case CopperParser.COUNT_DISTINCT:
	        case CopperParser.LEFT_OUTER:
	        case CopperParser.INNER:
	        case CopperParser.FULL_OUTER:
	        case CopperParser.CROSS:
	        case CopperParser.ONE_TO_ONE:
	        case CopperParser.ONE_TO_MANY:
	        case CopperParser.MANY_TO_ONE:
	        case CopperParser.MANY_TO_MANY:
	        case CopperParser.USD:
	        case CopperParser.PERCENT:
	        case CopperParser.PERCENT_2:
	        case CopperParser.DECIMAL_2:
	        case CopperParser.YES:
	        case CopperParser.NO:
	        case CopperParser.TRUE:
	        case CopperParser.FALSE:
	        case CopperParser.IDENTIFIER:
	            localctx = new SimpleFuncContext(this, localctx);
	            this.enterOuterAlt(localctx, 2);
	            this.state = 365;
	            this.identifier();
	            this.state = 366;
	            this.match(CopperParser.LPAREN);
	            this.state = 375;
	            this._errHandler.sync(this);
	            _la = this._input.LA(1);
	            if(((((_la - 17)) & ~0x1f) == 0 && ((1 << (_la - 17)) & ((1 << (CopperParser.AGGREGATE - 17)) | (1 << (CopperParser.STRING - 17)) | (1 << (CopperParser.NUMBER - 17)) | (1 << (CopperParser.DATE - 17)) | (1 << (CopperParser.TIME - 17)) | (1 << (CopperParser.TIMESTAMP - 17)) | (1 << (CopperParser.BOOLEAN - 17)) | (1 << (CopperParser.SUM - 17)) | (1 << (CopperParser.COUNT - 17)) | (1 << (CopperParser.AVERAGE - 17)) | (1 << (CopperParser.MIN - 17)) | (1 << (CopperParser.MAX - 17)) | (1 << (CopperParser.COUNT_DISTINCT - 17)) | (1 << (CopperParser.LEFT_OUTER - 17)) | (1 << (CopperParser.INNER - 17)) | (1 << (CopperParser.FULL_OUTER - 17)) | (1 << (CopperParser.CROSS - 17)) | (1 << (CopperParser.ONE_TO_ONE - 17)) | (1 << (CopperParser.ONE_TO_MANY - 17)) | (1 << (CopperParser.MANY_TO_ONE - 17)) | (1 << (CopperParser.MANY_TO_MANY - 17)) | (1 << (CopperParser.USD - 17)) | (1 << (CopperParser.PERCENT - 17)) | (1 << (CopperParser.PERCENT_2 - 17)) | (1 << (CopperParser.DECIMAL_2 - 17)) | (1 << (CopperParser.YES - 17)) | (1 << (CopperParser.NO - 17)) | (1 << (CopperParser.TRUE - 17)) | (1 << (CopperParser.FALSE - 17)))) !== 0) || ((((_la - 49)) & ~0x1f) == 0 && ((1 << (_la - 49)) & ((1 << (CopperParser.LPAREN - 49)) | (1 << (CopperParser.DOLLAR_LBRACE - 49)) | (1 << (CopperParser.IDENTIFIER - 49)) | (1 << (CopperParser.STRING_LITERAL - 49)) | (1 << (CopperParser.NUMBER_LITERAL - 49)))) !== 0)) {
	                this.state = 367;
	                this.expression();
	                this.state = 372;
	                this._errHandler.sync(this);
	                _la = this._input.LA(1);
	                while(_la===CopperParser.COMMA) {
	                    this.state = 368;
	                    this.match(CopperParser.COMMA);
	                    this.state = 369;
	                    this.expression();
	                    this.state = 374;
	                    this._errHandler.sync(this);
	                    _la = this._input.LA(1);
	                }
	            }

	            this.state = 377;
	            this.match(CopperParser.RPAREN);
	            break;
	        default:
	            throw new antlr4.error.NoViableAltException(this);
	        }
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}


	overClause() {
	    let localctx = new OverClauseContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 86, CopperParser.RULE_overClause);
	    var _la = 0; // Token type
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 381;
	        this.match(CopperParser.OVER);
	        this.state = 382;
	        this.match(CopperParser.LBRACE);
	        this.state = 383;
	        this.namedArgument();
	        this.state = 388;
	        this._errHandler.sync(this);
	        _la = this._input.LA(1);
	        while(_la===CopperParser.COMMA) {
	            this.state = 384;
	            this.match(CopperParser.COMMA);
	            this.state = 385;
	            this.namedArgument();
	            this.state = 390;
	            this._errHandler.sync(this);
	            _la = this._input.LA(1);
	        }
	        this.state = 391;
	        this.match(CopperParser.RBRACE);
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}


	namedArgument() {
	    let localctx = new NamedArgumentContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 88, CopperParser.RULE_namedArgument);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 393;
	        this.identifier();
	        this.state = 394;
	        this.match(CopperParser.COLON);
	        this.state = 395;
	        this.value_();
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}


	value_() {
	    let localctx = new Value_Context(this, this._ctx, this.state);
	    this.enterRule(localctx, 90, CopperParser.RULE_value_);
	    try {
	        this.state = 399;
	        this._errHandler.sync(this);
	        switch(this._input.LA(1)) {
	        case CopperParser.AGGREGATE:
	        case CopperParser.STRING:
	        case CopperParser.NUMBER:
	        case CopperParser.DATE:
	        case CopperParser.TIME:
	        case CopperParser.TIMESTAMP:
	        case CopperParser.BOOLEAN:
	        case CopperParser.SUM:
	        case CopperParser.COUNT:
	        case CopperParser.AVERAGE:
	        case CopperParser.MIN:
	        case CopperParser.MAX:
	        case CopperParser.COUNT_DISTINCT:
	        case CopperParser.LEFT_OUTER:
	        case CopperParser.INNER:
	        case CopperParser.FULL_OUTER:
	        case CopperParser.CROSS:
	        case CopperParser.ONE_TO_ONE:
	        case CopperParser.ONE_TO_MANY:
	        case CopperParser.MANY_TO_ONE:
	        case CopperParser.MANY_TO_MANY:
	        case CopperParser.USD:
	        case CopperParser.PERCENT:
	        case CopperParser.PERCENT_2:
	        case CopperParser.DECIMAL_2:
	        case CopperParser.YES:
	        case CopperParser.NO:
	        case CopperParser.TRUE:
	        case CopperParser.FALSE:
	        case CopperParser.LPAREN:
	        case CopperParser.DOLLAR_LBRACE:
	        case CopperParser.IDENTIFIER:
	        case CopperParser.STRING_LITERAL:
	        case CopperParser.NUMBER_LITERAL:
	            this.enterOuterAlt(localctx, 1);
	            this.state = 397;
	            this.expression();
	            break;
	        case CopperParser.LBRACKET:
	            this.enterOuterAlt(localctx, 2);
	            this.state = 398;
	            this.list_();
	            break;
	        default:
	            throw new antlr4.error.NoViableAltException(this);
	        }
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}


	list_() {
	    let localctx = new List_Context(this, this._ctx, this.state);
	    this.enterRule(localctx, 92, CopperParser.RULE_list_);
	    var _la = 0; // Token type
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 401;
	        this.match(CopperParser.LBRACKET);
	        this.state = 410;
	        this._errHandler.sync(this);
	        _la = this._input.LA(1);
	        if(((((_la - 17)) & ~0x1f) == 0 && ((1 << (_la - 17)) & ((1 << (CopperParser.AGGREGATE - 17)) | (1 << (CopperParser.STRING - 17)) | (1 << (CopperParser.NUMBER - 17)) | (1 << (CopperParser.DATE - 17)) | (1 << (CopperParser.TIME - 17)) | (1 << (CopperParser.TIMESTAMP - 17)) | (1 << (CopperParser.BOOLEAN - 17)) | (1 << (CopperParser.SUM - 17)) | (1 << (CopperParser.COUNT - 17)) | (1 << (CopperParser.AVERAGE - 17)) | (1 << (CopperParser.MIN - 17)) | (1 << (CopperParser.MAX - 17)) | (1 << (CopperParser.COUNT_DISTINCT - 17)) | (1 << (CopperParser.LEFT_OUTER - 17)) | (1 << (CopperParser.INNER - 17)) | (1 << (CopperParser.FULL_OUTER - 17)) | (1 << (CopperParser.CROSS - 17)) | (1 << (CopperParser.ONE_TO_ONE - 17)) | (1 << (CopperParser.ONE_TO_MANY - 17)) | (1 << (CopperParser.MANY_TO_ONE - 17)) | (1 << (CopperParser.MANY_TO_MANY - 17)) | (1 << (CopperParser.USD - 17)) | (1 << (CopperParser.PERCENT - 17)) | (1 << (CopperParser.PERCENT_2 - 17)) | (1 << (CopperParser.DECIMAL_2 - 17)) | (1 << (CopperParser.YES - 17)) | (1 << (CopperParser.NO - 17)) | (1 << (CopperParser.TRUE - 17)) | (1 << (CopperParser.FALSE - 17)))) !== 0) || ((((_la - 49)) & ~0x1f) == 0 && ((1 << (_la - 49)) & ((1 << (CopperParser.LPAREN - 49)) | (1 << (CopperParser.DOLLAR_LBRACE - 49)) | (1 << (CopperParser.IDENTIFIER - 49)) | (1 << (CopperParser.STRING_LITERAL - 49)) | (1 << (CopperParser.NUMBER_LITERAL - 49)))) !== 0)) {
	            this.state = 402;
	            this.expression();
	            this.state = 407;
	            this._errHandler.sync(this);
	            _la = this._input.LA(1);
	            while(_la===CopperParser.COMMA) {
	                this.state = 403;
	                this.match(CopperParser.COMMA);
	                this.state = 404;
	                this.expression();
	                this.state = 409;
	                this._errHandler.sync(this);
	                _la = this._input.LA(1);
	            }
	        }

	        this.state = 412;
	        this.match(CopperParser.RBRACKET);
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}


	fieldReference() {
	    let localctx = new FieldReferenceContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 94, CopperParser.RULE_fieldReference);
	    var _la = 0; // Token type
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 414;
	        this.match(CopperParser.DOLLAR_LBRACE);
	        this.state = 415;
	        this.identifier();
	        this.state = 418;
	        this._errHandler.sync(this);
	        _la = this._input.LA(1);
	        if(_la===CopperParser.DOT) {
	            this.state = 416;
	            this.match(CopperParser.DOT);
	            this.state = 417;
	            this.identifier();
	        }

	        this.state = 420;
	        this.match(CopperParser.RBRACE);
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}


	literal() {
	    let localctx = new LiteralContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 96, CopperParser.RULE_literal);
	    try {
	        this.state = 425;
	        this._errHandler.sync(this);
	        switch(this._input.LA(1)) {
	        case CopperParser.NUMBER_LITERAL:
	            this.enterOuterAlt(localctx, 1);
	            this.state = 422;
	            this.match(CopperParser.NUMBER_LITERAL);
	            break;
	        case CopperParser.STRING_LITERAL:
	            this.enterOuterAlt(localctx, 2);
	            this.state = 423;
	            this.match(CopperParser.STRING_LITERAL);
	            break;
	        case CopperParser.TRUE:
	        case CopperParser.FALSE:
	            this.enterOuterAlt(localctx, 3);
	            this.state = 424;
	            this.booleanLiteral();
	            break;
	        default:
	            throw new antlr4.error.NoViableAltException(this);
	        }
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}


	booleanLiteral() {
	    let localctx = new BooleanLiteralContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 98, CopperParser.RULE_booleanLiteral);
	    var _la = 0; // Token type
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 427;
	        _la = this._input.LA(1);
	        if(!(_la===CopperParser.TRUE || _la===CopperParser.FALSE)) {
	        this._errHandler.recoverInline(this);
	        }
	        else {
	        	this._errHandler.reportMatch(this);
	            this.consume();
	        }
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}


	identifier() {
	    let localctx = new IdentifierContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 100, CopperParser.RULE_identifier);
	    var _la = 0; // Token type
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 429;
	        _la = this._input.LA(1);
	        if(!(((((_la - 19)) & ~0x1f) == 0 && ((1 << (_la - 19)) & ((1 << (CopperParser.STRING - 19)) | (1 << (CopperParser.NUMBER - 19)) | (1 << (CopperParser.DATE - 19)) | (1 << (CopperParser.TIME - 19)) | (1 << (CopperParser.TIMESTAMP - 19)) | (1 << (CopperParser.BOOLEAN - 19)) | (1 << (CopperParser.SUM - 19)) | (1 << (CopperParser.COUNT - 19)) | (1 << (CopperParser.AVERAGE - 19)) | (1 << (CopperParser.MIN - 19)) | (1 << (CopperParser.MAX - 19)) | (1 << (CopperParser.COUNT_DISTINCT - 19)) | (1 << (CopperParser.LEFT_OUTER - 19)) | (1 << (CopperParser.INNER - 19)) | (1 << (CopperParser.FULL_OUTER - 19)) | (1 << (CopperParser.CROSS - 19)) | (1 << (CopperParser.ONE_TO_ONE - 19)) | (1 << (CopperParser.ONE_TO_MANY - 19)) | (1 << (CopperParser.MANY_TO_ONE - 19)) | (1 << (CopperParser.MANY_TO_MANY - 19)) | (1 << (CopperParser.USD - 19)) | (1 << (CopperParser.PERCENT - 19)) | (1 << (CopperParser.PERCENT_2 - 19)) | (1 << (CopperParser.DECIMAL_2 - 19)) | (1 << (CopperParser.YES - 19)) | (1 << (CopperParser.NO - 19)) | (1 << (CopperParser.TRUE - 19)) | (1 << (CopperParser.FALSE - 19)))) !== 0) || _la===CopperParser.IDENTIFIER)) {
	        this._errHandler.recoverInline(this);
	        }
	        else {
	        	this._errHandler.reportMatch(this);
	            this.consume();
	        }
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}


}

CopperParser.EOF = antlr4.Token.EOF;
CopperParser.MODEL = 1;
CopperParser.VIEW = 2;
CopperParser.MEASURE = 3;
CopperParser.DIMENSION = 4;
CopperParser.JOIN = 5;
CopperParser.TYPE = 6;
CopperParser.EXPRESSION = 7;
CopperParser.LABEL = 8;
CopperParser.DESCRIPTION = 9;
CopperParser.PRIMARY_KEY = 10;
CopperParser.HIDDEN_ = 11;
CopperParser.VALUE_FORMAT = 12;
CopperParser.UNITS = 13;
CopperParser.RELATIONSHIP = 14;
CopperParser.FROM = 15;
CopperParser.EXTENDS = 16;
CopperParser.AGGREGATE = 17;
CopperParser.OVER = 18;
CopperParser.STRING = 19;
CopperParser.NUMBER = 20;
CopperParser.DATE = 21;
CopperParser.TIME = 22;
CopperParser.TIMESTAMP = 23;
CopperParser.BOOLEAN = 24;
CopperParser.SUM = 25;
CopperParser.COUNT = 26;
CopperParser.AVERAGE = 27;
CopperParser.MIN = 28;
CopperParser.MAX = 29;
CopperParser.COUNT_DISTINCT = 30;
CopperParser.LEFT_OUTER = 31;
CopperParser.INNER = 32;
CopperParser.FULL_OUTER = 33;
CopperParser.CROSS = 34;
CopperParser.ONE_TO_ONE = 35;
CopperParser.ONE_TO_MANY = 36;
CopperParser.MANY_TO_ONE = 37;
CopperParser.MANY_TO_MANY = 38;
CopperParser.USD = 39;
CopperParser.PERCENT = 40;
CopperParser.PERCENT_2 = 41;
CopperParser.DECIMAL_2 = 42;
CopperParser.YES = 43;
CopperParser.NO = 44;
CopperParser.TRUE = 45;
CopperParser.FALSE = 46;
CopperParser.AND = 47;
CopperParser.OR = 48;
CopperParser.LPAREN = 49;
CopperParser.RPAREN = 50;
CopperParser.LBRACE = 51;
CopperParser.RBRACE = 52;
CopperParser.LBRACKET = 53;
CopperParser.RBRACKET = 54;
CopperParser.DOLLAR_LBRACE = 55;
CopperParser.COLON = 56;
CopperParser.COMMA = 57;
CopperParser.DOT = 58;
CopperParser.DOUBLE_SEMICOLON = 59;
CopperParser.PLUS = 60;
CopperParser.MINUS = 61;
CopperParser.MULTIPLY = 62;
CopperParser.DIVIDE = 63;
CopperParser.EQUALS = 64;
CopperParser.NOT_EQUALS = 65;
CopperParser.GTE = 66;
CopperParser.LTE = 67;
CopperParser.GREATER_THAN = 68;
CopperParser.LESS_THAN = 69;
CopperParser.IDENTIFIER = 70;
CopperParser.STRING_LITERAL = 71;
CopperParser.NUMBER_LITERAL = 72;
CopperParser.COMMENT = 73;
CopperParser.NEWLINE = 74;
CopperParser.WS = 75;

CopperParser.RULE_program = 0;
CopperParser.RULE_statement = 1;
CopperParser.RULE_modelStatement = 2;
CopperParser.RULE_viewStatement = 3;
CopperParser.RULE_modelElement = 4;
CopperParser.RULE_viewElement = 5;
CopperParser.RULE_measureStatement = 6;
CopperParser.RULE_dimensionStatement = 7;
CopperParser.RULE_joinStatement = 8;
CopperParser.RULE_dimensionParameter = 9;
CopperParser.RULE_measureParameter = 10;
CopperParser.RULE_joinParameter = 11;
CopperParser.RULE_typeParameter = 12;
CopperParser.RULE_measureTypeParameter = 13;
CopperParser.RULE_expressionParameter = 14;
CopperParser.RULE_labelParameter = 15;
CopperParser.RULE_descriptionParameter = 16;
CopperParser.RULE_primaryKeyParameter = 17;
CopperParser.RULE_hiddenParameter = 18;
CopperParser.RULE_valueFormatParameter = 19;
CopperParser.RULE_unitsParameter = 20;
CopperParser.RULE_joinTypeParameter = 21;
CopperParser.RULE_relationshipParameter = 22;
CopperParser.RULE_fromStatement = 23;
CopperParser.RULE_extendsStatement = 24;
CopperParser.RULE_identifierList = 25;
CopperParser.RULE_dimensionType = 26;
CopperParser.RULE_measureType = 27;
CopperParser.RULE_joinType = 28;
CopperParser.RULE_relationshipType = 29;
CopperParser.RULE_formatName = 30;
CopperParser.RULE_booleanValue = 31;
CopperParser.RULE_daxExpression = 32;
CopperParser.RULE_daxContent = 33;
CopperParser.RULE_stringLiteral = 34;
CopperParser.RULE_expression = 35;
CopperParser.RULE_logicalOrExpression = 36;
CopperParser.RULE_logicalAndExpression = 37;
CopperParser.RULE_comparisonExpression = 38;
CopperParser.RULE_additiveExpression = 39;
CopperParser.RULE_multiplicativeExpression = 40;
CopperParser.RULE_primary = 41;
CopperParser.RULE_functionCall = 42;
CopperParser.RULE_overClause = 43;
CopperParser.RULE_namedArgument = 44;
CopperParser.RULE_value_ = 45;
CopperParser.RULE_list_ = 46;
CopperParser.RULE_fieldReference = 47;
CopperParser.RULE_literal = 48;
CopperParser.RULE_booleanLiteral = 49;
CopperParser.RULE_identifier = 50;

class ProgramContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = CopperParser.RULE_program;
    }

	EOF() {
	    return this.getToken(CopperParser.EOF, 0);
	};

	statement = function(i) {
	    if(i===undefined) {
	        i = null;
	    }
	    if(i===null) {
	        return this.getTypedRuleContexts(StatementContext);
	    } else {
	        return this.getTypedRuleContext(StatementContext,i);
	    }
	};

	NEWLINE = function(i) {
		if(i===undefined) {
			i = null;
		}
	    if(i===null) {
	        return this.getTokens(CopperParser.NEWLINE);
	    } else {
	        return this.getToken(CopperParser.NEWLINE, i);
	    }
	};


	enterRule(listener) {
	    if(listener instanceof CopperListener ) {
	        listener.enterProgram(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof CopperListener ) {
	        listener.exitProgram(this);
		}
	}


}



class StatementContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = CopperParser.RULE_statement;
    }

	modelStatement() {
	    return this.getTypedRuleContext(ModelStatementContext,0);
	};

	viewStatement() {
	    return this.getTypedRuleContext(ViewStatementContext,0);
	};

	measureStatement() {
	    return this.getTypedRuleContext(MeasureStatementContext,0);
	};

	dimensionStatement() {
	    return this.getTypedRuleContext(DimensionStatementContext,0);
	};

	enterRule(listener) {
	    if(listener instanceof CopperListener ) {
	        listener.enterStatement(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof CopperListener ) {
	        listener.exitStatement(this);
		}
	}


}



class ModelStatementContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = CopperParser.RULE_modelStatement;
    }

	MODEL() {
	    return this.getToken(CopperParser.MODEL, 0);
	};

	COLON() {
	    return this.getToken(CopperParser.COLON, 0);
	};

	identifier() {
	    return this.getTypedRuleContext(IdentifierContext,0);
	};

	LBRACE() {
	    return this.getToken(CopperParser.LBRACE, 0);
	};

	RBRACE() {
	    return this.getToken(CopperParser.RBRACE, 0);
	};

	modelElement = function(i) {
	    if(i===undefined) {
	        i = null;
	    }
	    if(i===null) {
	        return this.getTypedRuleContexts(ModelElementContext);
	    } else {
	        return this.getTypedRuleContext(ModelElementContext,i);
	    }
	};

	NEWLINE = function(i) {
		if(i===undefined) {
			i = null;
		}
	    if(i===null) {
	        return this.getTokens(CopperParser.NEWLINE);
	    } else {
	        return this.getToken(CopperParser.NEWLINE, i);
	    }
	};


	enterRule(listener) {
	    if(listener instanceof CopperListener ) {
	        listener.enterModelStatement(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof CopperListener ) {
	        listener.exitModelStatement(this);
		}
	}


}



class ViewStatementContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = CopperParser.RULE_viewStatement;
    }

	VIEW() {
	    return this.getToken(CopperParser.VIEW, 0);
	};

	COLON() {
	    return this.getToken(CopperParser.COLON, 0);
	};

	identifier() {
	    return this.getTypedRuleContext(IdentifierContext,0);
	};

	LBRACE() {
	    return this.getToken(CopperParser.LBRACE, 0);
	};

	RBRACE() {
	    return this.getToken(CopperParser.RBRACE, 0);
	};

	viewElement = function(i) {
	    if(i===undefined) {
	        i = null;
	    }
	    if(i===null) {
	        return this.getTypedRuleContexts(ViewElementContext);
	    } else {
	        return this.getTypedRuleContext(ViewElementContext,i);
	    }
	};

	NEWLINE = function(i) {
		if(i===undefined) {
			i = null;
		}
	    if(i===null) {
	        return this.getTokens(CopperParser.NEWLINE);
	    } else {
	        return this.getToken(CopperParser.NEWLINE, i);
	    }
	};


	enterRule(listener) {
	    if(listener instanceof CopperListener ) {
	        listener.enterViewStatement(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof CopperListener ) {
	        listener.exitViewStatement(this);
		}
	}


}



class ModelElementContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = CopperParser.RULE_modelElement;
    }

	dimensionStatement() {
	    return this.getTypedRuleContext(DimensionStatementContext,0);
	};

	measureStatement() {
	    return this.getTypedRuleContext(MeasureStatementContext,0);
	};

	joinStatement() {
	    return this.getTypedRuleContext(JoinStatementContext,0);
	};

	enterRule(listener) {
	    if(listener instanceof CopperListener ) {
	        listener.enterModelElement(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof CopperListener ) {
	        listener.exitModelElement(this);
		}
	}


}



class ViewElementContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = CopperParser.RULE_viewElement;
    }

	fromStatement() {
	    return this.getTypedRuleContext(FromStatementContext,0);
	};

	extendsStatement() {
	    return this.getTypedRuleContext(ExtendsStatementContext,0);
	};

	joinStatement() {
	    return this.getTypedRuleContext(JoinStatementContext,0);
	};

	dimensionStatement() {
	    return this.getTypedRuleContext(DimensionStatementContext,0);
	};

	measureStatement() {
	    return this.getTypedRuleContext(MeasureStatementContext,0);
	};

	enterRule(listener) {
	    if(listener instanceof CopperListener ) {
	        listener.enterViewElement(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof CopperListener ) {
	        listener.exitViewElement(this);
		}
	}


}



class MeasureStatementContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = CopperParser.RULE_measureStatement;
    }

	MEASURE() {
	    return this.getToken(CopperParser.MEASURE, 0);
	};

	COLON() {
	    return this.getToken(CopperParser.COLON, 0);
	};

	identifier() {
	    return this.getTypedRuleContext(IdentifierContext,0);
	};

	LBRACE() {
	    return this.getToken(CopperParser.LBRACE, 0);
	};

	RBRACE() {
	    return this.getToken(CopperParser.RBRACE, 0);
	};

	measureParameter = function(i) {
	    if(i===undefined) {
	        i = null;
	    }
	    if(i===null) {
	        return this.getTypedRuleContexts(MeasureParameterContext);
	    } else {
	        return this.getTypedRuleContext(MeasureParameterContext,i);
	    }
	};

	NEWLINE = function(i) {
		if(i===undefined) {
			i = null;
		}
	    if(i===null) {
	        return this.getTokens(CopperParser.NEWLINE);
	    } else {
	        return this.getToken(CopperParser.NEWLINE, i);
	    }
	};


	enterRule(listener) {
	    if(listener instanceof CopperListener ) {
	        listener.enterMeasureStatement(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof CopperListener ) {
	        listener.exitMeasureStatement(this);
		}
	}


}



class DimensionStatementContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = CopperParser.RULE_dimensionStatement;
    }

	DIMENSION() {
	    return this.getToken(CopperParser.DIMENSION, 0);
	};

	COLON() {
	    return this.getToken(CopperParser.COLON, 0);
	};

	identifier() {
	    return this.getTypedRuleContext(IdentifierContext,0);
	};

	LBRACE() {
	    return this.getToken(CopperParser.LBRACE, 0);
	};

	RBRACE() {
	    return this.getToken(CopperParser.RBRACE, 0);
	};

	dimensionParameter = function(i) {
	    if(i===undefined) {
	        i = null;
	    }
	    if(i===null) {
	        return this.getTypedRuleContexts(DimensionParameterContext);
	    } else {
	        return this.getTypedRuleContext(DimensionParameterContext,i);
	    }
	};

	NEWLINE = function(i) {
		if(i===undefined) {
			i = null;
		}
	    if(i===null) {
	        return this.getTokens(CopperParser.NEWLINE);
	    } else {
	        return this.getToken(CopperParser.NEWLINE, i);
	    }
	};


	enterRule(listener) {
	    if(listener instanceof CopperListener ) {
	        listener.enterDimensionStatement(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof CopperListener ) {
	        listener.exitDimensionStatement(this);
		}
	}


}



class JoinStatementContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = CopperParser.RULE_joinStatement;
    }

	JOIN() {
	    return this.getToken(CopperParser.JOIN, 0);
	};

	COLON() {
	    return this.getToken(CopperParser.COLON, 0);
	};

	identifier() {
	    return this.getTypedRuleContext(IdentifierContext,0);
	};

	LBRACE() {
	    return this.getToken(CopperParser.LBRACE, 0);
	};

	RBRACE() {
	    return this.getToken(CopperParser.RBRACE, 0);
	};

	joinParameter = function(i) {
	    if(i===undefined) {
	        i = null;
	    }
	    if(i===null) {
	        return this.getTypedRuleContexts(JoinParameterContext);
	    } else {
	        return this.getTypedRuleContext(JoinParameterContext,i);
	    }
	};

	NEWLINE = function(i) {
		if(i===undefined) {
			i = null;
		}
	    if(i===null) {
	        return this.getTokens(CopperParser.NEWLINE);
	    } else {
	        return this.getToken(CopperParser.NEWLINE, i);
	    }
	};


	enterRule(listener) {
	    if(listener instanceof CopperListener ) {
	        listener.enterJoinStatement(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof CopperListener ) {
	        listener.exitJoinStatement(this);
		}
	}


}



class DimensionParameterContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = CopperParser.RULE_dimensionParameter;
    }

	typeParameter() {
	    return this.getTypedRuleContext(TypeParameterContext,0);
	};

	expressionParameter() {
	    return this.getTypedRuleContext(ExpressionParameterContext,0);
	};

	labelParameter() {
	    return this.getTypedRuleContext(LabelParameterContext,0);
	};

	descriptionParameter() {
	    return this.getTypedRuleContext(DescriptionParameterContext,0);
	};

	primaryKeyParameter() {
	    return this.getTypedRuleContext(PrimaryKeyParameterContext,0);
	};

	hiddenParameter() {
	    return this.getTypedRuleContext(HiddenParameterContext,0);
	};

	valueFormatParameter() {
	    return this.getTypedRuleContext(ValueFormatParameterContext,0);
	};

	unitsParameter() {
	    return this.getTypedRuleContext(UnitsParameterContext,0);
	};

	enterRule(listener) {
	    if(listener instanceof CopperListener ) {
	        listener.enterDimensionParameter(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof CopperListener ) {
	        listener.exitDimensionParameter(this);
		}
	}


}



class MeasureParameterContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = CopperParser.RULE_measureParameter;
    }

	measureTypeParameter() {
	    return this.getTypedRuleContext(MeasureTypeParameterContext,0);
	};

	expressionParameter() {
	    return this.getTypedRuleContext(ExpressionParameterContext,0);
	};

	labelParameter() {
	    return this.getTypedRuleContext(LabelParameterContext,0);
	};

	descriptionParameter() {
	    return this.getTypedRuleContext(DescriptionParameterContext,0);
	};

	hiddenParameter() {
	    return this.getTypedRuleContext(HiddenParameterContext,0);
	};

	valueFormatParameter() {
	    return this.getTypedRuleContext(ValueFormatParameterContext,0);
	};

	unitsParameter() {
	    return this.getTypedRuleContext(UnitsParameterContext,0);
	};

	enterRule(listener) {
	    if(listener instanceof CopperListener ) {
	        listener.enterMeasureParameter(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof CopperListener ) {
	        listener.exitMeasureParameter(this);
		}
	}


}



class JoinParameterContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = CopperParser.RULE_joinParameter;
    }

	joinTypeParameter() {
	    return this.getTypedRuleContext(JoinTypeParameterContext,0);
	};

	relationshipParameter() {
	    return this.getTypedRuleContext(RelationshipParameterContext,0);
	};

	expressionParameter() {
	    return this.getTypedRuleContext(ExpressionParameterContext,0);
	};

	enterRule(listener) {
	    if(listener instanceof CopperListener ) {
	        listener.enterJoinParameter(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof CopperListener ) {
	        listener.exitJoinParameter(this);
		}
	}


}



class TypeParameterContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = CopperParser.RULE_typeParameter;
    }

	TYPE() {
	    return this.getToken(CopperParser.TYPE, 0);
	};

	COLON() {
	    return this.getToken(CopperParser.COLON, 0);
	};

	dimensionType() {
	    return this.getTypedRuleContext(DimensionTypeContext,0);
	};

	enterRule(listener) {
	    if(listener instanceof CopperListener ) {
	        listener.enterTypeParameter(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof CopperListener ) {
	        listener.exitTypeParameter(this);
		}
	}


}



class MeasureTypeParameterContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = CopperParser.RULE_measureTypeParameter;
    }

	TYPE() {
	    return this.getToken(CopperParser.TYPE, 0);
	};

	COLON() {
	    return this.getToken(CopperParser.COLON, 0);
	};

	measureType() {
	    return this.getTypedRuleContext(MeasureTypeContext,0);
	};

	enterRule(listener) {
	    if(listener instanceof CopperListener ) {
	        listener.enterMeasureTypeParameter(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof CopperListener ) {
	        listener.exitMeasureTypeParameter(this);
		}
	}


}



class ExpressionParameterContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = CopperParser.RULE_expressionParameter;
    }

	EXPRESSION() {
	    return this.getToken(CopperParser.EXPRESSION, 0);
	};

	COLON() {
	    return this.getToken(CopperParser.COLON, 0);
	};

	daxExpression() {
	    return this.getTypedRuleContext(DaxExpressionContext,0);
	};

	enterRule(listener) {
	    if(listener instanceof CopperListener ) {
	        listener.enterExpressionParameter(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof CopperListener ) {
	        listener.exitExpressionParameter(this);
		}
	}


}



class LabelParameterContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = CopperParser.RULE_labelParameter;
    }

	LABEL() {
	    return this.getToken(CopperParser.LABEL, 0);
	};

	COLON() {
	    return this.getToken(CopperParser.COLON, 0);
	};

	stringLiteral() {
	    return this.getTypedRuleContext(StringLiteralContext,0);
	};

	enterRule(listener) {
	    if(listener instanceof CopperListener ) {
	        listener.enterLabelParameter(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof CopperListener ) {
	        listener.exitLabelParameter(this);
		}
	}


}



class DescriptionParameterContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = CopperParser.RULE_descriptionParameter;
    }

	DESCRIPTION() {
	    return this.getToken(CopperParser.DESCRIPTION, 0);
	};

	COLON() {
	    return this.getToken(CopperParser.COLON, 0);
	};

	stringLiteral() {
	    return this.getTypedRuleContext(StringLiteralContext,0);
	};

	enterRule(listener) {
	    if(listener instanceof CopperListener ) {
	        listener.enterDescriptionParameter(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof CopperListener ) {
	        listener.exitDescriptionParameter(this);
		}
	}


}



class PrimaryKeyParameterContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = CopperParser.RULE_primaryKeyParameter;
    }

	PRIMARY_KEY() {
	    return this.getToken(CopperParser.PRIMARY_KEY, 0);
	};

	COLON() {
	    return this.getToken(CopperParser.COLON, 0);
	};

	booleanValue() {
	    return this.getTypedRuleContext(BooleanValueContext,0);
	};

	enterRule(listener) {
	    if(listener instanceof CopperListener ) {
	        listener.enterPrimaryKeyParameter(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof CopperListener ) {
	        listener.exitPrimaryKeyParameter(this);
		}
	}


}



class HiddenParameterContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = CopperParser.RULE_hiddenParameter;
    }

	HIDDEN_() {
	    return this.getToken(CopperParser.HIDDEN_, 0);
	};

	COLON() {
	    return this.getToken(CopperParser.COLON, 0);
	};

	booleanValue() {
	    return this.getTypedRuleContext(BooleanValueContext,0);
	};

	enterRule(listener) {
	    if(listener instanceof CopperListener ) {
	        listener.enterHiddenParameter(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof CopperListener ) {
	        listener.exitHiddenParameter(this);
		}
	}


}



class ValueFormatParameterContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = CopperParser.RULE_valueFormatParameter;
    }

	VALUE_FORMAT() {
	    return this.getToken(CopperParser.VALUE_FORMAT, 0);
	};

	COLON() {
	    return this.getToken(CopperParser.COLON, 0);
	};

	stringLiteral() {
	    return this.getTypedRuleContext(StringLiteralContext,0);
	};

	formatName() {
	    return this.getTypedRuleContext(FormatNameContext,0);
	};

	enterRule(listener) {
	    if(listener instanceof CopperListener ) {
	        listener.enterValueFormatParameter(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof CopperListener ) {
	        listener.exitValueFormatParameter(this);
		}
	}


}



class UnitsParameterContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = CopperParser.RULE_unitsParameter;
    }

	UNITS() {
	    return this.getToken(CopperParser.UNITS, 0);
	};

	COLON() {
	    return this.getToken(CopperParser.COLON, 0);
	};

	stringLiteral() {
	    return this.getTypedRuleContext(StringLiteralContext,0);
	};

	enterRule(listener) {
	    if(listener instanceof CopperListener ) {
	        listener.enterUnitsParameter(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof CopperListener ) {
	        listener.exitUnitsParameter(this);
		}
	}


}



class JoinTypeParameterContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = CopperParser.RULE_joinTypeParameter;
    }

	TYPE() {
	    return this.getToken(CopperParser.TYPE, 0);
	};

	COLON() {
	    return this.getToken(CopperParser.COLON, 0);
	};

	joinType() {
	    return this.getTypedRuleContext(JoinTypeContext,0);
	};

	enterRule(listener) {
	    if(listener instanceof CopperListener ) {
	        listener.enterJoinTypeParameter(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof CopperListener ) {
	        listener.exitJoinTypeParameter(this);
		}
	}


}



class RelationshipParameterContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = CopperParser.RULE_relationshipParameter;
    }

	RELATIONSHIP() {
	    return this.getToken(CopperParser.RELATIONSHIP, 0);
	};

	COLON() {
	    return this.getToken(CopperParser.COLON, 0);
	};

	relationshipType() {
	    return this.getTypedRuleContext(RelationshipTypeContext,0);
	};

	enterRule(listener) {
	    if(listener instanceof CopperListener ) {
	        listener.enterRelationshipParameter(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof CopperListener ) {
	        listener.exitRelationshipParameter(this);
		}
	}


}



class FromStatementContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = CopperParser.RULE_fromStatement;
    }

	FROM() {
	    return this.getToken(CopperParser.FROM, 0);
	};

	COLON() {
	    return this.getToken(CopperParser.COLON, 0);
	};

	identifier() {
	    return this.getTypedRuleContext(IdentifierContext,0);
	};

	enterRule(listener) {
	    if(listener instanceof CopperListener ) {
	        listener.enterFromStatement(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof CopperListener ) {
	        listener.exitFromStatement(this);
		}
	}


}



class ExtendsStatementContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = CopperParser.RULE_extendsStatement;
    }

	EXTENDS() {
	    return this.getToken(CopperParser.EXTENDS, 0);
	};

	COLON() {
	    return this.getToken(CopperParser.COLON, 0);
	};

	identifierList() {
	    return this.getTypedRuleContext(IdentifierListContext,0);
	};

	enterRule(listener) {
	    if(listener instanceof CopperListener ) {
	        listener.enterExtendsStatement(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof CopperListener ) {
	        listener.exitExtendsStatement(this);
		}
	}


}



class IdentifierListContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = CopperParser.RULE_identifierList;
    }

	identifier = function(i) {
	    if(i===undefined) {
	        i = null;
	    }
	    if(i===null) {
	        return this.getTypedRuleContexts(IdentifierContext);
	    } else {
	        return this.getTypedRuleContext(IdentifierContext,i);
	    }
	};

	COMMA = function(i) {
		if(i===undefined) {
			i = null;
		}
	    if(i===null) {
	        return this.getTokens(CopperParser.COMMA);
	    } else {
	        return this.getToken(CopperParser.COMMA, i);
	    }
	};


	enterRule(listener) {
	    if(listener instanceof CopperListener ) {
	        listener.enterIdentifierList(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof CopperListener ) {
	        listener.exitIdentifierList(this);
		}
	}


}



class DimensionTypeContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = CopperParser.RULE_dimensionType;
    }

	STRING() {
	    return this.getToken(CopperParser.STRING, 0);
	};

	NUMBER() {
	    return this.getToken(CopperParser.NUMBER, 0);
	};

	DATE() {
	    return this.getToken(CopperParser.DATE, 0);
	};

	TIME() {
	    return this.getToken(CopperParser.TIME, 0);
	};

	TIMESTAMP() {
	    return this.getToken(CopperParser.TIMESTAMP, 0);
	};

	BOOLEAN() {
	    return this.getToken(CopperParser.BOOLEAN, 0);
	};

	enterRule(listener) {
	    if(listener instanceof CopperListener ) {
	        listener.enterDimensionType(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof CopperListener ) {
	        listener.exitDimensionType(this);
		}
	}


}



class MeasureTypeContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = CopperParser.RULE_measureType;
    }

	SUM() {
	    return this.getToken(CopperParser.SUM, 0);
	};

	COUNT() {
	    return this.getToken(CopperParser.COUNT, 0);
	};

	AVERAGE() {
	    return this.getToken(CopperParser.AVERAGE, 0);
	};

	MIN() {
	    return this.getToken(CopperParser.MIN, 0);
	};

	MAX() {
	    return this.getToken(CopperParser.MAX, 0);
	};

	COUNT_DISTINCT() {
	    return this.getToken(CopperParser.COUNT_DISTINCT, 0);
	};

	NUMBER() {
	    return this.getToken(CopperParser.NUMBER, 0);
	};

	enterRule(listener) {
	    if(listener instanceof CopperListener ) {
	        listener.enterMeasureType(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof CopperListener ) {
	        listener.exitMeasureType(this);
		}
	}


}



class JoinTypeContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = CopperParser.RULE_joinType;
    }

	LEFT_OUTER() {
	    return this.getToken(CopperParser.LEFT_OUTER, 0);
	};

	INNER() {
	    return this.getToken(CopperParser.INNER, 0);
	};

	FULL_OUTER() {
	    return this.getToken(CopperParser.FULL_OUTER, 0);
	};

	CROSS() {
	    return this.getToken(CopperParser.CROSS, 0);
	};

	enterRule(listener) {
	    if(listener instanceof CopperListener ) {
	        listener.enterJoinType(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof CopperListener ) {
	        listener.exitJoinType(this);
		}
	}


}



class RelationshipTypeContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = CopperParser.RULE_relationshipType;
    }

	ONE_TO_ONE() {
	    return this.getToken(CopperParser.ONE_TO_ONE, 0);
	};

	ONE_TO_MANY() {
	    return this.getToken(CopperParser.ONE_TO_MANY, 0);
	};

	MANY_TO_ONE() {
	    return this.getToken(CopperParser.MANY_TO_ONE, 0);
	};

	MANY_TO_MANY() {
	    return this.getToken(CopperParser.MANY_TO_MANY, 0);
	};

	enterRule(listener) {
	    if(listener instanceof CopperListener ) {
	        listener.enterRelationshipType(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof CopperListener ) {
	        listener.exitRelationshipType(this);
		}
	}


}



class FormatNameContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = CopperParser.RULE_formatName;
    }

	USD() {
	    return this.getToken(CopperParser.USD, 0);
	};

	PERCENT() {
	    return this.getToken(CopperParser.PERCENT, 0);
	};

	PERCENT_2() {
	    return this.getToken(CopperParser.PERCENT_2, 0);
	};

	DECIMAL_2() {
	    return this.getToken(CopperParser.DECIMAL_2, 0);
	};

	enterRule(listener) {
	    if(listener instanceof CopperListener ) {
	        listener.enterFormatName(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof CopperListener ) {
	        listener.exitFormatName(this);
		}
	}


}



class BooleanValueContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = CopperParser.RULE_booleanValue;
    }

	YES() {
	    return this.getToken(CopperParser.YES, 0);
	};

	NO() {
	    return this.getToken(CopperParser.NO, 0);
	};

	TRUE() {
	    return this.getToken(CopperParser.TRUE, 0);
	};

	FALSE() {
	    return this.getToken(CopperParser.FALSE, 0);
	};

	enterRule(listener) {
	    if(listener instanceof CopperListener ) {
	        listener.enterBooleanValue(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof CopperListener ) {
	        listener.exitBooleanValue(this);
		}
	}


}



class DaxExpressionContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = CopperParser.RULE_daxExpression;
    }

	daxContent() {
	    return this.getTypedRuleContext(DaxContentContext,0);
	};

	DOUBLE_SEMICOLON() {
	    return this.getToken(CopperParser.DOUBLE_SEMICOLON, 0);
	};

	enterRule(listener) {
	    if(listener instanceof CopperListener ) {
	        listener.enterDaxExpression(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof CopperListener ) {
	        listener.exitDaxExpression(this);
		}
	}


}



class DaxContentContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = CopperParser.RULE_daxContent;
    }

	DOUBLE_SEMICOLON = function(i) {
		if(i===undefined) {
			i = null;
		}
	    if(i===null) {
	        return this.getTokens(CopperParser.DOUBLE_SEMICOLON);
	    } else {
	        return this.getToken(CopperParser.DOUBLE_SEMICOLON, i);
	    }
	};


	NEWLINE = function(i) {
		if(i===undefined) {
			i = null;
		}
	    if(i===null) {
	        return this.getTokens(CopperParser.NEWLINE);
	    } else {
	        return this.getToken(CopperParser.NEWLINE, i);
	    }
	};


	enterRule(listener) {
	    if(listener instanceof CopperListener ) {
	        listener.enterDaxContent(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof CopperListener ) {
	        listener.exitDaxContent(this);
		}
	}


}



class StringLiteralContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = CopperParser.RULE_stringLiteral;
    }

	STRING_LITERAL() {
	    return this.getToken(CopperParser.STRING_LITERAL, 0);
	};

	enterRule(listener) {
	    if(listener instanceof CopperListener ) {
	        listener.enterStringLiteral(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof CopperListener ) {
	        listener.exitStringLiteral(this);
		}
	}


}



class ExpressionContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = CopperParser.RULE_expression;
    }

	logicalOrExpression() {
	    return this.getTypedRuleContext(LogicalOrExpressionContext,0);
	};

	enterRule(listener) {
	    if(listener instanceof CopperListener ) {
	        listener.enterExpression(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof CopperListener ) {
	        listener.exitExpression(this);
		}
	}


}



class LogicalOrExpressionContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = CopperParser.RULE_logicalOrExpression;
    }

	logicalAndExpression = function(i) {
	    if(i===undefined) {
	        i = null;
	    }
	    if(i===null) {
	        return this.getTypedRuleContexts(LogicalAndExpressionContext);
	    } else {
	        return this.getTypedRuleContext(LogicalAndExpressionContext,i);
	    }
	};

	OR = function(i) {
		if(i===undefined) {
			i = null;
		}
	    if(i===null) {
	        return this.getTokens(CopperParser.OR);
	    } else {
	        return this.getToken(CopperParser.OR, i);
	    }
	};


	enterRule(listener) {
	    if(listener instanceof CopperListener ) {
	        listener.enterLogicalOrExpression(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof CopperListener ) {
	        listener.exitLogicalOrExpression(this);
		}
	}


}



class LogicalAndExpressionContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = CopperParser.RULE_logicalAndExpression;
    }

	comparisonExpression = function(i) {
	    if(i===undefined) {
	        i = null;
	    }
	    if(i===null) {
	        return this.getTypedRuleContexts(ComparisonExpressionContext);
	    } else {
	        return this.getTypedRuleContext(ComparisonExpressionContext,i);
	    }
	};

	AND = function(i) {
		if(i===undefined) {
			i = null;
		}
	    if(i===null) {
	        return this.getTokens(CopperParser.AND);
	    } else {
	        return this.getToken(CopperParser.AND, i);
	    }
	};


	enterRule(listener) {
	    if(listener instanceof CopperListener ) {
	        listener.enterLogicalAndExpression(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof CopperListener ) {
	        listener.exitLogicalAndExpression(this);
		}
	}


}



class ComparisonExpressionContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = CopperParser.RULE_comparisonExpression;
    }

	additiveExpression = function(i) {
	    if(i===undefined) {
	        i = null;
	    }
	    if(i===null) {
	        return this.getTypedRuleContexts(AdditiveExpressionContext);
	    } else {
	        return this.getTypedRuleContext(AdditiveExpressionContext,i);
	    }
	};

	EQUALS() {
	    return this.getToken(CopperParser.EQUALS, 0);
	};

	NOT_EQUALS() {
	    return this.getToken(CopperParser.NOT_EQUALS, 0);
	};

	GTE() {
	    return this.getToken(CopperParser.GTE, 0);
	};

	LTE() {
	    return this.getToken(CopperParser.LTE, 0);
	};

	GREATER_THAN() {
	    return this.getToken(CopperParser.GREATER_THAN, 0);
	};

	LESS_THAN() {
	    return this.getToken(CopperParser.LESS_THAN, 0);
	};

	enterRule(listener) {
	    if(listener instanceof CopperListener ) {
	        listener.enterComparisonExpression(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof CopperListener ) {
	        listener.exitComparisonExpression(this);
		}
	}


}



class AdditiveExpressionContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = CopperParser.RULE_additiveExpression;
    }

	multiplicativeExpression = function(i) {
	    if(i===undefined) {
	        i = null;
	    }
	    if(i===null) {
	        return this.getTypedRuleContexts(MultiplicativeExpressionContext);
	    } else {
	        return this.getTypedRuleContext(MultiplicativeExpressionContext,i);
	    }
	};

	PLUS = function(i) {
		if(i===undefined) {
			i = null;
		}
	    if(i===null) {
	        return this.getTokens(CopperParser.PLUS);
	    } else {
	        return this.getToken(CopperParser.PLUS, i);
	    }
	};


	MINUS = function(i) {
		if(i===undefined) {
			i = null;
		}
	    if(i===null) {
	        return this.getTokens(CopperParser.MINUS);
	    } else {
	        return this.getToken(CopperParser.MINUS, i);
	    }
	};


	enterRule(listener) {
	    if(listener instanceof CopperListener ) {
	        listener.enterAdditiveExpression(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof CopperListener ) {
	        listener.exitAdditiveExpression(this);
		}
	}


}



class MultiplicativeExpressionContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = CopperParser.RULE_multiplicativeExpression;
    }

	primary = function(i) {
	    if(i===undefined) {
	        i = null;
	    }
	    if(i===null) {
	        return this.getTypedRuleContexts(PrimaryContext);
	    } else {
	        return this.getTypedRuleContext(PrimaryContext,i);
	    }
	};

	MULTIPLY = function(i) {
		if(i===undefined) {
			i = null;
		}
	    if(i===null) {
	        return this.getTokens(CopperParser.MULTIPLY);
	    } else {
	        return this.getToken(CopperParser.MULTIPLY, i);
	    }
	};


	DIVIDE = function(i) {
		if(i===undefined) {
			i = null;
		}
	    if(i===null) {
	        return this.getTokens(CopperParser.DIVIDE);
	    } else {
	        return this.getToken(CopperParser.DIVIDE, i);
	    }
	};


	enterRule(listener) {
	    if(listener instanceof CopperListener ) {
	        listener.enterMultiplicativeExpression(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof CopperListener ) {
	        listener.exitMultiplicativeExpression(this);
		}
	}


}



class PrimaryContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = CopperParser.RULE_primary;
    }

	LPAREN() {
	    return this.getToken(CopperParser.LPAREN, 0);
	};

	expression() {
	    return this.getTypedRuleContext(ExpressionContext,0);
	};

	RPAREN() {
	    return this.getToken(CopperParser.RPAREN, 0);
	};

	literal() {
	    return this.getTypedRuleContext(LiteralContext,0);
	};

	fieldReference() {
	    return this.getTypedRuleContext(FieldReferenceContext,0);
	};

	functionCall() {
	    return this.getTypedRuleContext(FunctionCallContext,0);
	};

	enterRule(listener) {
	    if(listener instanceof CopperListener ) {
	        listener.enterPrimary(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof CopperListener ) {
	        listener.exitPrimary(this);
		}
	}


}



class FunctionCallContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = CopperParser.RULE_functionCall;
    }


	 
		copyFrom(ctx) {
			super.copyFrom(ctx);
		}

}


class SimpleFuncContext extends FunctionCallContext {

    constructor(parser, ctx) {
        super(parser);
        super.copyFrom(ctx);
    }

	identifier() {
	    return this.getTypedRuleContext(IdentifierContext,0);
	};

	LPAREN() {
	    return this.getToken(CopperParser.LPAREN, 0);
	};

	RPAREN() {
	    return this.getToken(CopperParser.RPAREN, 0);
	};

	expression = function(i) {
	    if(i===undefined) {
	        i = null;
	    }
	    if(i===null) {
	        return this.getTypedRuleContexts(ExpressionContext);
	    } else {
	        return this.getTypedRuleContext(ExpressionContext,i);
	    }
	};

	COMMA = function(i) {
		if(i===undefined) {
			i = null;
		}
	    if(i===null) {
	        return this.getTokens(CopperParser.COMMA);
	    } else {
	        return this.getToken(CopperParser.COMMA, i);
	    }
	};


	enterRule(listener) {
	    if(listener instanceof CopperListener ) {
	        listener.enterSimpleFunc(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof CopperListener ) {
	        listener.exitSimpleFunc(this);
		}
	}


}

CopperParser.SimpleFuncContext = SimpleFuncContext;

class AggregateFuncContext extends FunctionCallContext {

    constructor(parser, ctx) {
        super(parser);
        super.copyFrom(ctx);
    }

	AGGREGATE() {
	    return this.getToken(CopperParser.AGGREGATE, 0);
	};

	LPAREN() {
	    return this.getToken(CopperParser.LPAREN, 0);
	};

	namedArgument = function(i) {
	    if(i===undefined) {
	        i = null;
	    }
	    if(i===null) {
	        return this.getTypedRuleContexts(NamedArgumentContext);
	    } else {
	        return this.getTypedRuleContext(NamedArgumentContext,i);
	    }
	};

	RPAREN() {
	    return this.getToken(CopperParser.RPAREN, 0);
	};

	COMMA = function(i) {
		if(i===undefined) {
			i = null;
		}
	    if(i===null) {
	        return this.getTokens(CopperParser.COMMA);
	    } else {
	        return this.getToken(CopperParser.COMMA, i);
	    }
	};


	overClause() {
	    return this.getTypedRuleContext(OverClauseContext,0);
	};

	enterRule(listener) {
	    if(listener instanceof CopperListener ) {
	        listener.enterAggregateFunc(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof CopperListener ) {
	        listener.exitAggregateFunc(this);
		}
	}


}

CopperParser.AggregateFuncContext = AggregateFuncContext;

class OverClauseContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = CopperParser.RULE_overClause;
    }

	OVER() {
	    return this.getToken(CopperParser.OVER, 0);
	};

	LBRACE() {
	    return this.getToken(CopperParser.LBRACE, 0);
	};

	namedArgument = function(i) {
	    if(i===undefined) {
	        i = null;
	    }
	    if(i===null) {
	        return this.getTypedRuleContexts(NamedArgumentContext);
	    } else {
	        return this.getTypedRuleContext(NamedArgumentContext,i);
	    }
	};

	RBRACE() {
	    return this.getToken(CopperParser.RBRACE, 0);
	};

	COMMA = function(i) {
		if(i===undefined) {
			i = null;
		}
	    if(i===null) {
	        return this.getTokens(CopperParser.COMMA);
	    } else {
	        return this.getToken(CopperParser.COMMA, i);
	    }
	};


	enterRule(listener) {
	    if(listener instanceof CopperListener ) {
	        listener.enterOverClause(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof CopperListener ) {
	        listener.exitOverClause(this);
		}
	}


}



class NamedArgumentContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = CopperParser.RULE_namedArgument;
    }

	identifier() {
	    return this.getTypedRuleContext(IdentifierContext,0);
	};

	COLON() {
	    return this.getToken(CopperParser.COLON, 0);
	};

	value_() {
	    return this.getTypedRuleContext(Value_Context,0);
	};

	enterRule(listener) {
	    if(listener instanceof CopperListener ) {
	        listener.enterNamedArgument(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof CopperListener ) {
	        listener.exitNamedArgument(this);
		}
	}


}



class Value_Context extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = CopperParser.RULE_value_;
    }

	expression() {
	    return this.getTypedRuleContext(ExpressionContext,0);
	};

	list_() {
	    return this.getTypedRuleContext(List_Context,0);
	};

	enterRule(listener) {
	    if(listener instanceof CopperListener ) {
	        listener.enterValue_(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof CopperListener ) {
	        listener.exitValue_(this);
		}
	}


}



class List_Context extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = CopperParser.RULE_list_;
    }

	LBRACKET() {
	    return this.getToken(CopperParser.LBRACKET, 0);
	};

	RBRACKET() {
	    return this.getToken(CopperParser.RBRACKET, 0);
	};

	expression = function(i) {
	    if(i===undefined) {
	        i = null;
	    }
	    if(i===null) {
	        return this.getTypedRuleContexts(ExpressionContext);
	    } else {
	        return this.getTypedRuleContext(ExpressionContext,i);
	    }
	};

	COMMA = function(i) {
		if(i===undefined) {
			i = null;
		}
	    if(i===null) {
	        return this.getTokens(CopperParser.COMMA);
	    } else {
	        return this.getToken(CopperParser.COMMA, i);
	    }
	};


	enterRule(listener) {
	    if(listener instanceof CopperListener ) {
	        listener.enterList_(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof CopperListener ) {
	        listener.exitList_(this);
		}
	}


}



class FieldReferenceContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = CopperParser.RULE_fieldReference;
    }

	DOLLAR_LBRACE() {
	    return this.getToken(CopperParser.DOLLAR_LBRACE, 0);
	};

	identifier = function(i) {
	    if(i===undefined) {
	        i = null;
	    }
	    if(i===null) {
	        return this.getTypedRuleContexts(IdentifierContext);
	    } else {
	        return this.getTypedRuleContext(IdentifierContext,i);
	    }
	};

	RBRACE() {
	    return this.getToken(CopperParser.RBRACE, 0);
	};

	DOT() {
	    return this.getToken(CopperParser.DOT, 0);
	};

	enterRule(listener) {
	    if(listener instanceof CopperListener ) {
	        listener.enterFieldReference(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof CopperListener ) {
	        listener.exitFieldReference(this);
		}
	}


}



class LiteralContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = CopperParser.RULE_literal;
    }

	NUMBER_LITERAL() {
	    return this.getToken(CopperParser.NUMBER_LITERAL, 0);
	};

	STRING_LITERAL() {
	    return this.getToken(CopperParser.STRING_LITERAL, 0);
	};

	booleanLiteral() {
	    return this.getTypedRuleContext(BooleanLiteralContext,0);
	};

	enterRule(listener) {
	    if(listener instanceof CopperListener ) {
	        listener.enterLiteral(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof CopperListener ) {
	        listener.exitLiteral(this);
		}
	}


}



class BooleanLiteralContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = CopperParser.RULE_booleanLiteral;
    }

	TRUE() {
	    return this.getToken(CopperParser.TRUE, 0);
	};

	FALSE() {
	    return this.getToken(CopperParser.FALSE, 0);
	};

	enterRule(listener) {
	    if(listener instanceof CopperListener ) {
	        listener.enterBooleanLiteral(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof CopperListener ) {
	        listener.exitBooleanLiteral(this);
		}
	}


}



class IdentifierContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = CopperParser.RULE_identifier;
    }

	IDENTIFIER() {
	    return this.getToken(CopperParser.IDENTIFIER, 0);
	};

	STRING() {
	    return this.getToken(CopperParser.STRING, 0);
	};

	NUMBER() {
	    return this.getToken(CopperParser.NUMBER, 0);
	};

	DATE() {
	    return this.getToken(CopperParser.DATE, 0);
	};

	TIME() {
	    return this.getToken(CopperParser.TIME, 0);
	};

	TIMESTAMP() {
	    return this.getToken(CopperParser.TIMESTAMP, 0);
	};

	BOOLEAN() {
	    return this.getToken(CopperParser.BOOLEAN, 0);
	};

	SUM() {
	    return this.getToken(CopperParser.SUM, 0);
	};

	COUNT() {
	    return this.getToken(CopperParser.COUNT, 0);
	};

	AVERAGE() {
	    return this.getToken(CopperParser.AVERAGE, 0);
	};

	MIN() {
	    return this.getToken(CopperParser.MIN, 0);
	};

	MAX() {
	    return this.getToken(CopperParser.MAX, 0);
	};

	COUNT_DISTINCT() {
	    return this.getToken(CopperParser.COUNT_DISTINCT, 0);
	};

	LEFT_OUTER() {
	    return this.getToken(CopperParser.LEFT_OUTER, 0);
	};

	INNER() {
	    return this.getToken(CopperParser.INNER, 0);
	};

	FULL_OUTER() {
	    return this.getToken(CopperParser.FULL_OUTER, 0);
	};

	CROSS() {
	    return this.getToken(CopperParser.CROSS, 0);
	};

	ONE_TO_ONE() {
	    return this.getToken(CopperParser.ONE_TO_ONE, 0);
	};

	ONE_TO_MANY() {
	    return this.getToken(CopperParser.ONE_TO_MANY, 0);
	};

	MANY_TO_ONE() {
	    return this.getToken(CopperParser.MANY_TO_ONE, 0);
	};

	MANY_TO_MANY() {
	    return this.getToken(CopperParser.MANY_TO_MANY, 0);
	};

	USD() {
	    return this.getToken(CopperParser.USD, 0);
	};

	PERCENT() {
	    return this.getToken(CopperParser.PERCENT, 0);
	};

	PERCENT_2() {
	    return this.getToken(CopperParser.PERCENT_2, 0);
	};

	DECIMAL_2() {
	    return this.getToken(CopperParser.DECIMAL_2, 0);
	};

	YES() {
	    return this.getToken(CopperParser.YES, 0);
	};

	NO() {
	    return this.getToken(CopperParser.NO, 0);
	};

	TRUE() {
	    return this.getToken(CopperParser.TRUE, 0);
	};

	FALSE() {
	    return this.getToken(CopperParser.FALSE, 0);
	};

	enterRule(listener) {
	    if(listener instanceof CopperListener ) {
	        listener.enterIdentifier(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof CopperListener ) {
	        listener.exitIdentifier(this);
		}
	}


}




CopperParser.ProgramContext = ProgramContext; 
CopperParser.StatementContext = StatementContext; 
CopperParser.ModelStatementContext = ModelStatementContext; 
CopperParser.ViewStatementContext = ViewStatementContext; 
CopperParser.ModelElementContext = ModelElementContext; 
CopperParser.ViewElementContext = ViewElementContext; 
CopperParser.MeasureStatementContext = MeasureStatementContext; 
CopperParser.DimensionStatementContext = DimensionStatementContext; 
CopperParser.JoinStatementContext = JoinStatementContext; 
CopperParser.DimensionParameterContext = DimensionParameterContext; 
CopperParser.MeasureParameterContext = MeasureParameterContext; 
CopperParser.JoinParameterContext = JoinParameterContext; 
CopperParser.TypeParameterContext = TypeParameterContext; 
CopperParser.MeasureTypeParameterContext = MeasureTypeParameterContext; 
CopperParser.ExpressionParameterContext = ExpressionParameterContext; 
CopperParser.LabelParameterContext = LabelParameterContext; 
CopperParser.DescriptionParameterContext = DescriptionParameterContext; 
CopperParser.PrimaryKeyParameterContext = PrimaryKeyParameterContext; 
CopperParser.HiddenParameterContext = HiddenParameterContext; 
CopperParser.ValueFormatParameterContext = ValueFormatParameterContext; 
CopperParser.UnitsParameterContext = UnitsParameterContext; 
CopperParser.JoinTypeParameterContext = JoinTypeParameterContext; 
CopperParser.RelationshipParameterContext = RelationshipParameterContext; 
CopperParser.FromStatementContext = FromStatementContext; 
CopperParser.ExtendsStatementContext = ExtendsStatementContext; 
CopperParser.IdentifierListContext = IdentifierListContext; 
CopperParser.DimensionTypeContext = DimensionTypeContext; 
CopperParser.MeasureTypeContext = MeasureTypeContext; 
CopperParser.JoinTypeContext = JoinTypeContext; 
CopperParser.RelationshipTypeContext = RelationshipTypeContext; 
CopperParser.FormatNameContext = FormatNameContext; 
CopperParser.BooleanValueContext = BooleanValueContext; 
CopperParser.DaxExpressionContext = DaxExpressionContext; 
CopperParser.DaxContentContext = DaxContentContext; 
CopperParser.StringLiteralContext = StringLiteralContext; 
CopperParser.ExpressionContext = ExpressionContext; 
CopperParser.LogicalOrExpressionContext = LogicalOrExpressionContext; 
CopperParser.LogicalAndExpressionContext = LogicalAndExpressionContext; 
CopperParser.ComparisonExpressionContext = ComparisonExpressionContext; 
CopperParser.AdditiveExpressionContext = AdditiveExpressionContext; 
CopperParser.MultiplicativeExpressionContext = MultiplicativeExpressionContext; 
CopperParser.PrimaryContext = PrimaryContext; 
CopperParser.FunctionCallContext = FunctionCallContext; 
CopperParser.OverClauseContext = OverClauseContext; 
CopperParser.NamedArgumentContext = NamedArgumentContext; 
CopperParser.Value_Context = Value_Context; 
CopperParser.List_Context = List_Context; 
CopperParser.FieldReferenceContext = FieldReferenceContext; 
CopperParser.LiteralContext = LiteralContext; 
CopperParser.BooleanLiteralContext = BooleanLiteralContext; 
CopperParser.IdentifierContext = IdentifierContext; 
