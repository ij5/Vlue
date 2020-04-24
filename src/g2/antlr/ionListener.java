// Generated from ion.g4 by ANTLR 4.8
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link ionParser}.
 */
public interface ionListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link ionParser#root}.
	 * @param ctx the parse tree
	 */
	void enterRoot(ionParser.RootContext ctx);
	/**
	 * Exit a parse tree produced by {@link ionParser#root}.
	 * @param ctx the parse tree
	 */
	void exitRoot(ionParser.RootContext ctx);
	/**
	 * Enter a parse tree produced by {@link ionParser#body}.
	 * @param ctx the parse tree
	 */
	void enterBody(ionParser.BodyContext ctx);
	/**
	 * Exit a parse tree produced by {@link ionParser#body}.
	 * @param ctx the parse tree
	 */
	void exitBody(ionParser.BodyContext ctx);
	/**
	 * Enter a parse tree produced by {@link ionParser#elements}.
	 * @param ctx the parse tree
	 */
	void enterElements(ionParser.ElementsContext ctx);
	/**
	 * Exit a parse tree produced by {@link ionParser#elements}.
	 * @param ctx the parse tree
	 */
	void exitElements(ionParser.ElementsContext ctx);
	/**
	 * Enter a parse tree produced by {@link ionParser#head}.
	 * @param ctx the parse tree
	 */
	void enterHead(ionParser.HeadContext ctx);
	/**
	 * Exit a parse tree produced by {@link ionParser#head}.
	 * @param ctx the parse tree
	 */
	void exitHead(ionParser.HeadContext ctx);
	/**
	 * Enter a parse tree produced by {@link ionParser#empty}.
	 * @param ctx the parse tree
	 */
	void enterEmpty(ionParser.EmptyContext ctx);
	/**
	 * Exit a parse tree produced by {@link ionParser#empty}.
	 * @param ctx the parse tree
	 */
	void exitEmpty(ionParser.EmptyContext ctx);
	/**
	 * Enter a parse tree produced by {@link ionParser#attr}.
	 * @param ctx the parse tree
	 */
	void enterAttr(ionParser.AttrContext ctx);
	/**
	 * Exit a parse tree produced by {@link ionParser#attr}.
	 * @param ctx the parse tree
	 */
	void exitAttr(ionParser.AttrContext ctx);
	/**
	 * Enter a parse tree produced by {@link ionParser#attr_equal}.
	 * @param ctx the parse tree
	 */
	void enterAttr_equal(ionParser.Attr_equalContext ctx);
	/**
	 * Exit a parse tree produced by {@link ionParser#attr_equal}.
	 * @param ctx the parse tree
	 */
	void exitAttr_equal(ionParser.Attr_equalContext ctx);
	/**
	 * Enter a parse tree produced by {@link ionParser#other}.
	 * @param ctx the parse tree
	 */
	void enterOther(ionParser.OtherContext ctx);
	/**
	 * Exit a parse tree produced by {@link ionParser#other}.
	 * @param ctx the parse tree
	 */
	void exitOther(ionParser.OtherContext ctx);
}