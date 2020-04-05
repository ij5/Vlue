package simplelang;

import java.io.FileInputStream;
import java.io.IOException;
import java.util.logging.Level;
import java.util.logging.Logger;
import org.antlr.v4.runtime.ANTLRFileStream;
import org.antlr.runtime.ANTLRInputStream;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.CommonTokenStream;

public class Simplelang {
    public static void main(String[] args){
        try{
            CharStream input = (CharStream) new ANTLRFileStream("test.simple");
            simplelangLexer lexer = new simplelangLexer(input);
            simplelangParser parser = new simplelangParser(new CommenTokenStream(lexer));
            parser.addParseListener(new simplerlangCustomListener());
            parser.program();
        }catch(IOException ex){
            Logger.getLogger(Simplelang.class.getName()).log(Level.SEVERE, null, ex);
        }
    }
}