import System.Environment(getArgs)
import Text.ParserCombinators.Parsec
import Text.Regex.PCRE ((=~))
import Data.List
import Control.Monad
import System.IO (openFile, hPutStrLn, hPutStr, IOMode(WriteMode), hClose)
import qualified Data.Map as M

pathChar :: Parser Char
pathChar = oneOf "/_." <|> letter <|> digit

floatChar :: Parser Char
floatChar = digit <|> oneOf "."

traceSep :: Parser String
traceSep = string "\n==========="

traceHit :: Parser ()
traceHit = spaces >> string "Counting matches..." >> spaces >>
           string "Hit:" >> spaces

traceOrig :: Parser ()
traceOrig = spaces >> string "ORIGNAL:" >> spaces

logMatch :: Parser (String, String)
logMatch = do
  try $ many (string "Training FLANN." >> spaces >> string "Done." >> spaces)
  trace1 <- between traceHit traceSep (many1 pathChar)
  trace2 <- between traceOrig newline (many1 pathChar)
  return (traceName trace1, traceName trace2)

logHeader :: Parser ()
logHeader = spaces >> string "CANNOT MATCH THE SAME TRACE" >> spaces

timeSpec :: Parser Float
timeSpec = do
  spaces >> string "Total Time: "
  time <- many1 floatChar
  string " s." >> spaces
  return $ (read time :: Float)

logItem :: Parser [(String, String)]
logItem = do
  logHeader
  matches <- many logMatch
  timeSpec
  return matches

logParser :: Parser [[(String, String)]]
logParser = do
  res <- many logItem
  eof
  return res

traceName :: String -> String
traceName = (=~ "path[^/]*")

accumSum :: (Num a) => [a] -> [a]
accumSum = foldr (\x y -> (x + (head y)):y) [0]

main :: IO ()
main = do
  [ntraces, tfs, fi] <- getArgs
  let n1 = (read ntraces :: Int)
  traces <- fmap (map traceName . lines) $ readFile tfs
  let traceIdxMap = M.fromList $ zip traces [1..n1]
  let traceColor = M.fromList $ zip [1..n1] [1..n1]
  parseRes <- fmap (parse logParser "log") $ readFile fi
  let res = case parseRes of
              Right result -> map nub result
              Left err -> error $ show err
  fh1 <- openFile (ntraces++"_accum.dat") WriteMode
  mapM_ (hPutStrLn fh1 . show) $ reverse $ accumSum $ map length res
  fh2 <- openFile (ntraces++"_match.dat") WriteMode
  foldM_ (\m rs ->
              let m1 = foldr (addTrace traceIdxMap) m rs
              in do mapM_ (\(_, v) -> do
                             hPutStr fh2 $ show v
                             hPutStr fh2 " ") $ M.toList m
                    hPutStrLn fh2 ""
                    return m1) traceColor res
  hClose fh1
  hClose fh2
       where addTrace idx (t1, t2) m
                 | t1 < t2 = let ix = mapIx idx t1
                                 color = mapIx m ix
                                 ix2 = mapIx idx t2
                                 color2 = mapIx m ix2
                             in updateColor color2 color m
                 | otherwise = addTrace idx (t2, t1) m
             mapIx idx t = maybe (error ("key error" ++ show t)) id (M.lookup t idx)
             updateColor c1 c2 mp =
                 M.fromList $map (\(k, v) ->
                                      if v == c1
                                      then (k, c2)
                                      else (k, v)) $ M.toList mp
