# Thiago Alves soares 2502664

## Desafio Prático: Caçando Mutantes e Garantindo a Robustez dos Testes

Este projeto demonstra como uma suíte de testes com boa cobertura ainda pode deixar mutantes sobreviverem, e como a análise de valor limite ajuda a fortalecer a validação da regra de negócio.

### Arquivos principais

- `credito.py`: regra de aprovação de empréstimo.
- `test_credito.py`: suíte de testes com casos de valor limite.
- `setup.cfg`: configuração do `mutmut`.
- `explicacao.md`: resposta curta sobre o que o `mutmut show` evidencia.

### Como executar

```bash
python -m pytest
```

### Observação sobre o mutmut

Neste ambiente Windows, o `mutmut` não executa nativamente. Para rodar a análise de mutação, use WSL ou um ambiente Linux compatível.