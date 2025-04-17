import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.pagos import procesar_pago


def test_pago_exitoso():
    # Configurar mock con saldo suficiente
    mock_verificador = MagicMock(return_value=200.0)
    assert procesar_pago("usuario1", 150.0, mock_verificador) is True
    mock_verificador.assert_called_once_with("usuario1")

def test_pago_fallido():
    # Configurar mock con saldo insuficiente
    mock_verificador = MagicMock(return_value=100.0)
    assert procesar_pago("usuario2", 150.0, mock_verificador) is False
    mock_verificador.assert_called_once_with("usuario2")

def test_pago_limite_exacto():
    # Configurar mock con saldo igual al monto
    mock_verificador = MagicMock(return_value=100.0)
    assert procesar_pago("usuario3", 100.0, mock_verificador) is True
    mock_verificador.assert_called_once_with("usuario3")
