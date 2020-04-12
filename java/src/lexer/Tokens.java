package lexer;

public class Tokens {
    private int beginIndex;
    private int endIndex;
    private TokenType tokenType;
    private  String tokenString;

    public Tokens(int beginIndex, int endIndex, TokenType tokenType, String tokenString){
        super();
        this.beginIndex = beginIndex;
        this.endIndex = endIndex;
        this.tokenType = tokenType;
        this.tokenString = tokenString;
    }
    public int getBeginIndex(){
        return beginIndex;
    }
    public int getEndIndex(){
        return endIndex;
    }
    public TokenType getTokenType(){
        return tokenType;
    }
    public String getTokenString(){
        return tokenString;
    }

    public String toString(){
        return "Token [beginIndex="+beginIndex+", endIndex="+endIndex+", tokenType="+tokenType+", tokenString=\""+tokenString+"\"]";
    }
}
