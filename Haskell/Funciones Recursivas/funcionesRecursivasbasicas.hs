suma :: Int->Int->Int
suma a b = a + b

resta :: Int->Int->Int
resta a b = a - b

multi :: Int->Int->Int
multi a b = if a == 1 then b
            else suma b (multi (resta a 1) b)

division :: Int->Int->Int
division a b = if a < b then 0
               else suma 1 (division (resta a b) b)

modulo :: Int->Int->Int
modulo a b = if a < b then a
             else modulo (resta a b) b

binario :: Int->Int
binario a = if (division a 2) == 0 then a
            else suma (modulo a 2) (multi 10 (binario (division a 2)))

decimal :: Int->Int
decimal a = if (division a 10) ==0 then a
            else suma (modulo a 10) (multi 2 (decimal (division a 10)))
            
palindromo::Int->Bool
palindromo a = comparar a (invertir a)

comparar::Int->Int->Bool
comparar a b = (if a == b then True else False)			

contar :: Int -> Int
contar n | n < 10 = 1
         | otherwise = 1 + contar (division n 10)
		 
invertir::Int->Int
invertir a | a < 10 = a
           | otherwise = ((modulo a 10)*10^((contar a)-1) + (invertir (division a 10)))
