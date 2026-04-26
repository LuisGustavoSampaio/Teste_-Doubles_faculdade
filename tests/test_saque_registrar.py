import unittest
from unittest.mock import Mock

from model import ContaCorrente, Saque


class TestSaqueRegistrar(unittest.TestCase):
    def test_deve_registrar_saque_quando_conta_autoriza_operacao(self):
        # Arrange
        dummy_cliente = object()
        conta = ContaCorrente(dummy_cliente, numero=1)
        conta.sacar = Mock(return_value=True)  # Stub
        conta.historico.adicionar_transacao = Mock()  # Mock
        saque = Saque(100)

        # Act
        saque.registrar(conta)

        # Assert
        conta.sacar.assert_called_once_with(100)
        conta.historico.adicionar_transacao.assert_called_once_with(saque)


if __name__ == "__main__":
    unittest.main()
