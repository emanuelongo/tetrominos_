from Modulo.Modelo.Tetrominos import Tridominos


def test_tetromino_gira_90_grados():
    # Arrange

    tetromino = Tridominos()

    # Act
    resultado = tetromino.rotar_90_grados_i()

    # Assert
