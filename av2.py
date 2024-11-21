class Pessoa:
    def __init__(self, nome, idade, cpf, endereco):
        self.nome = nome
        self.idade = idade
        self._cpf = cpf  # Encapsulamento
        self.endereco = endereco

    def mostrar_informacoes(self):
        print(f'Nome: {self.nome}, Idade: {self.idade}, CPF: {
              self._cpf}, Endereço: {self.endereco}')


class Paciente(Pessoa):
    def __init__(self, nome, idade, cpf, endereco, historico):
        # Aqui chamei o construtor da classe Pessoa
        super().__init__(nome, idade, cpf, endereco)
        self.historico = historico
        self.prontuarios = []  # Criei uma lista para armazenar os prontuários

    def mostrar_informacoes(self):
        super().mostrar_informacoes()
        print(f'Histórico: {self.historico}')
        self.listar_prontuarios()  

    def adicionar_prontuario(self, prontuario):
        self.prontuarios.append(prontuario)
        print(f"Prontuário adicionado para o paciente: {self.nome}")

    def listar_prontuarios(self):
        if self.prontuarios:
            print("Prontuários:")
            for prontuario in self.prontuarios:
                # Aqui o método __str__ da classe Prontuario será usado
                print(prontuario)
        else:
            print("Nenhum prontuário registrado.")


class Medico(Pessoa):
    def __init__(self, nome, idade, cpf, endereco, especialidade):
        super().__init__(nome, idade, cpf, endereco)
        self.especialidade = especialidade

    def mostrar_informacoes(self):
        super().mostrar_informacoes()
        print(f'Especialidade: {self.especialidade}')


class Consulta:
    def __init__(self, paciente, medico, data_consulta):
        self.paciente = paciente
        self.medico = medico
        self.data_consulta = data_consulta

    def mostrar_consulta(self):
        print(f'Paciente: {self.paciente.nome}, Médico: {
              self.medico.nome}, Data: {self.data_consulta}')


class Prontuario:
    def __init__(self, paciente, diagnostico, observacao):
        self.paciente = paciente
        self._diagnostico = diagnostico  # Encapsulamento
        self.observacao = observacao

    def adicionar_observacao(self, observacao):
        self.observacao = observacao

    def __str__(self):
        return f'Paciente: {self.paciente.nome}, Diagnóstico: {self._diagnostico}, Observação: {self.observacao}'


# Código principal
paciente1 = Paciente("Diogo", 22, "12345678900", "Rua A, nº 10", "Sem histórico")

medico1 = Medico("Dr. Igor", 40, "22455677899",
                 "Avenida B, nº 20", "Cardiologista")

consulta1 = Consulta(paciente1, medico1, "20/11/2024")

prontuario1 = Prontuario(paciente1, "Hipertensão", "Acompanhamento mensal")

# Adicionando o prontuário ao paciente
paciente1.adicionar_prontuario(prontuario1)


print("\nInformações do Paciente:")
paciente1.mostrar_informacoes()

print("\nInformações da Consulta:")
consulta1.mostrar_consulta()

print("\nInformações do Prontuário:")
paciente1.listar_prontuarios()
