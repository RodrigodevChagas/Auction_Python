from excecoes import LanceInvalido


class Usuario:

#region - Construtora da classe Usuario, contém como parâmetros a carteira (dinheiro disponivel) e o nome.
    def __init__(self, nome, carteira):
    self.__nome = nome
    self.__carteira = carteira
#endregion

#region - Método para validar se o lance proposto é válido.
    def propoe_lance(self, leilao, valor):
        if not self._valor_eh_valido(valor):
            raise LanceInvalido('Não pode propor um lance com o valor maior que o valor da carteira')

        lance = Lance(self, valor)
        leilao.propoe(lance)

        self.__carteira -= valor
#endregion

#region - Getter para encapsulamento do nome.
    @property
    def nome(self):
        return self.__nome
#endregion

#region - Getter para encapsulamento da carteira.
    @property
    def carteira(self):
        return self.__carteira
    #endregion

# - Método que confere se ainda tem dinheiro disponivel na carteira
    def _valor_eh_valido(self, valor):
        return valor <= self.__carteira

class Lance:

# - Construtora da classe Lance, contém como parâmetros o usuario e valor.
    def __init__(self, usuario, valor):
        self.usuario = usuario
        self.valor = valor


class Leilao:

#region - Construtora da classe Leilão. Tem como parâmetro a descrição do item leiloado.
    def __init__(self, descricao):
        self.descricao = descricao
        self.__lances = []
        self.maior_lance = 0.0
        self.menor_lance = 0.0
#endregion

#region - Método para propor lances no leilão.
    def propoe(self, lance: Lance):
        if self._lance_eh_valido(lance):
            if not self._tem_lances():
                self.menor_lance = lance.valor
                self.primeiro_lance_usuario = lance.usuario.nome''

            self.maior_lance = lance.valor
            self.ultimo_lance_usuario = lance.usuario.nome

            self.__lances.append(lance)
#endregion

#region - Getter para o encapsulamento dos lances
    @property
    def lances(self):
        return self.__lances[:]
#endregion

#region - Getter para o encapsulamento dos lances
    def _tem_lances(self):
        return self.__lances
#endregion

#region - Método que confere se o úsuario do lance atual é diferente do lance anterior.
    def _usuarios_diferentes(self, lance):
        if self.__lances[-1].usuario != lance.usuario:
            return True
        raise LanceInvalido('O mesmo usuário não pode dar dois lances seguidos')
#endregion

#region - Método que confere se o valor do lance atual é maior que o do lance anterior.
    def _valor_maior_que_lance_anterior(self, lance):
        if lance.valor > self.__lances[-1].valor:
            return True
        raise LanceInvalido('O valor do lance deve ser maior que o lance anterior')
#endregion

# - Método que confere se o lance tem todos os componentes para que seja válido.
    def _lance_eh_valido(self, lance):
        return not self._tem_lances() or (self._usuarios_diferentes(lance) and
                                          self._valor_maior_que_lance_anterior(lance))
