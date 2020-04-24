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
	 * Enter a parse tree produced by {@link ionParser#body_value}.
	 * @param ctx the parse tree
	 */
	void enterBody_value(ionParser.Body_valueContext ctx);
	/**
	 * Exit a parse tree produced by {@link ionParser#body_value}.
	 * @param ctx the parse tree
	 */
	void exitBody_value(ionParser.Body_valueContext ctx);
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
	 * Enter a parse tree produced by {@link ionParser#element_value}.
	 * @param ctx the parse tree
	 */
	void enterElement_value(ionParser.Element_valueContext ctx);
	/**
	 * Exit a parse tree produced by {@link ionParser#element_value}.
	 * @param ctx the parse tree
	 */
	void exitElement_value(ionParser.Element_valueContext ctx);
}