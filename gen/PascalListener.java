// Generated from D:/antlr4/sample\Pascal.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link PascalParser}.
 */
public interface PascalListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link PascalParser#program}.
	 * @param ctx the parse tree
	 */
	void enterProgram(PascalParser.ProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link PascalParser#program}.
	 * @param ctx the parse tree
	 */
	void exitProgram(PascalParser.ProgramContext ctx);
	/**
	 * Enter a parse tree produced by {@link PascalParser#infoPart}.
	 * @param ctx the parse tree
	 */
	void enterInfoPart(PascalParser.InfoPartContext ctx);
	/**
	 * Exit a parse tree produced by {@link PascalParser#infoPart}.
	 * @param ctx the parse tree
	 */
	void exitInfoPart(PascalParser.InfoPartContext ctx);
	/**
	 * Enter a parse tree produced by {@link PascalParser#variableDeclarationPart}.
	 * @param ctx the parse tree
	 */
	void enterVariableDeclarationPart(PascalParser.VariableDeclarationPartContext ctx);
	/**
	 * Exit a parse tree produced by {@link PascalParser#variableDeclarationPart}.
	 * @param ctx the parse tree
	 */
	void exitVariableDeclarationPart(PascalParser.VariableDeclarationPartContext ctx);
	/**
	 * Enter a parse tree produced by {@link PascalParser#variableDeclaration}.
	 * @param ctx the parse tree
	 */
	void enterVariableDeclaration(PascalParser.VariableDeclarationContext ctx);
	/**
	 * Exit a parse tree produced by {@link PascalParser#variableDeclaration}.
	 * @param ctx the parse tree
	 */
	void exitVariableDeclaration(PascalParser.VariableDeclarationContext ctx);
	/**
	 * Enter a parse tree produced by {@link PascalParser#identifierList}.
	 * @param ctx the parse tree
	 */
	void enterIdentifierList(PascalParser.IdentifierListContext ctx);
	/**
	 * Exit a parse tree produced by {@link PascalParser#identifierList}.
	 * @param ctx the parse tree
	 */
	void exitIdentifierList(PascalParser.IdentifierListContext ctx);
	/**
	 * Enter a parse tree produced by {@link PascalParser#varType}.
	 * @param ctx the parse tree
	 */
	void enterVarType(PascalParser.VarTypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link PascalParser#varType}.
	 * @param ctx the parse tree
	 */
	void exitVarType(PascalParser.VarTypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link PascalParser#block}.
	 * @param ctx the parse tree
	 */
	void enterBlock(PascalParser.BlockContext ctx);
	/**
	 * Exit a parse tree produced by {@link PascalParser#block}.
	 * @param ctx the parse tree
	 */
	void exitBlock(PascalParser.BlockContext ctx);
	/**
	 * Enter a parse tree produced by {@link PascalParser#statements}.
	 * @param ctx the parse tree
	 */
	void enterStatements(PascalParser.StatementsContext ctx);
	/**
	 * Exit a parse tree produced by {@link PascalParser#statements}.
	 * @param ctx the parse tree
	 */
	void exitStatements(PascalParser.StatementsContext ctx);
	/**
	 * Enter a parse tree produced by {@link PascalParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterStatement(PascalParser.StatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link PascalParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitStatement(PascalParser.StatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link PascalParser#writelnReadln}.
	 * @param ctx the parse tree
	 */
	void enterWritelnReadln(PascalParser.WritelnReadlnContext ctx);
	/**
	 * Exit a parse tree produced by {@link PascalParser#writelnReadln}.
	 * @param ctx the parse tree
	 */
	void exitWritelnReadln(PascalParser.WritelnReadlnContext ctx);
	/**
	 * Enter a parse tree produced by {@link PascalParser#readln}.
	 * @param ctx the parse tree
	 */
	void enterReadln(PascalParser.ReadlnContext ctx);
	/**
	 * Exit a parse tree produced by {@link PascalParser#readln}.
	 * @param ctx the parse tree
	 */
	void exitReadln(PascalParser.ReadlnContext ctx);
	/**
	 * Enter a parse tree produced by {@link PascalParser#writeln}.
	 * @param ctx the parse tree
	 */
	void enterWriteln(PascalParser.WritelnContext ctx);
	/**
	 * Exit a parse tree produced by {@link PascalParser#writeln}.
	 * @param ctx the parse tree
	 */
	void exitWriteln(PascalParser.WritelnContext ctx);
	/**
	 * Enter a parse tree produced by {@link PascalParser#assignmentStatement}.
	 * @param ctx the parse tree
	 */
	void enterAssignmentStatement(PascalParser.AssignmentStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link PascalParser#assignmentStatement}.
	 * @param ctx the parse tree
	 */
	void exitAssignmentStatement(PascalParser.AssignmentStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link PascalParser#expressions}.
	 * @param ctx the parse tree
	 */
	void enterExpressions(PascalParser.ExpressionsContext ctx);
	/**
	 * Exit a parse tree produced by {@link PascalParser#expressions}.
	 * @param ctx the parse tree
	 */
	void exitExpressions(PascalParser.ExpressionsContext ctx);
	/**
	 * Enter a parse tree produced by {@link PascalParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterExpression(PascalParser.ExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link PascalParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitExpression(PascalParser.ExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link PascalParser#operators}.
	 * @param ctx the parse tree
	 */
	void enterOperators(PascalParser.OperatorsContext ctx);
	/**
	 * Exit a parse tree produced by {@link PascalParser#operators}.
	 * @param ctx the parse tree
	 */
	void exitOperators(PascalParser.OperatorsContext ctx);
	/**
	 * Enter a parse tree produced by {@link PascalParser#blockBody}.
	 * @param ctx the parse tree
	 */
	void enterBlockBody(PascalParser.BlockBodyContext ctx);
	/**
	 * Exit a parse tree produced by {@link PascalParser#blockBody}.
	 * @param ctx the parse tree
	 */
	void exitBlockBody(PascalParser.BlockBodyContext ctx);
}