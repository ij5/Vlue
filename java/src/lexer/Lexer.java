package lexer;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.TreeMap;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import exceptions.AnalyzerException;

public class Lexer {
    private Map<TokenType, String> regEx;
    private List<Tokens> result;

    public Lexer(){
        regEx = new TreeMap<TokenType, String>();
        launchRegEx();
    }
}
