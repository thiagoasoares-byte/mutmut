# Thiago Alves soares 2502664

Neste ambiente, o mutmut não executa nativamente no Windows; o show desse mutante de borda normalmente evidencia a troca de `>= 700` para `> 700`.
Isso faz o caso de score 700 perder a aprovação, enquanto os testes antigos só cobriam valores acima do limite.
A análise de valor limite importa porque valida exatamente no limite, abaixo e acima dele, matando mutantes que testes genéricos deixam passar.