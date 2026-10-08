from credito import aprovar_emprestimo


def test_aprovacao_por_score():
    # Passa com score alto
    assert aprovar_emprestimo(850, 2000.00) is True


def test_aprovacao_por_renda():
    # Passa com renda alta
    assert aprovar_emprestimo(500, 8000.00) is True


def test_reprovacao():
    # Reprova com tudo baixo
    assert aprovar_emprestimo(300, 1500.00) is False


def test_aprovacao_no_limite_do_score():
    assert aprovar_emprestimo(700, 0.00) is True


def test_reprovacao_abaixo_do_limite_do_score():
    assert aprovar_emprestimo(699, 5000.00) is False


def test_reprovacao_no_limite_da_renda():
    assert aprovar_emprestimo(0, 5000.00) is False


def test_aprovacao_acima_do_limite_da_renda():
    assert aprovar_emprestimo(0, 5000.01) is True