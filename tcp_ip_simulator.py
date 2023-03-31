class DataLinkLayer:
    def __init__(self):
        # Define qual é a camada abaixo desta
        self.lower_layer = NetworkLayer
        # Define qual é a camada acima desta
        self.upper_layer = StarTopologyHub

    def send_message(self, sender_machine, receiver_machine, message):
        print(f"\n\t{sender_machine}'s Data Link Layer: Sending message to Hub Control\n\t\tMessage: {message}")
        # Chama a camada superior para enviar a mensagem para hub de uma rede de topologia estrela e enviar para a máquina de destino
        self.upper_layer().send_message(sender_machine, receiver_machine, message)

    def receive_message(self, sender_machine, receiver_machine, message):
        print(f"\n\t{receiver_machine.user_name}'s Data Link Layer: Receiving message from Hub Controller"
              f"\n\t\tMessage: {message}")
        # Chama a camada inferior para repassar a mensagem para a camada de internet
        self.lower_layer().receive_message(sender_machine, receiver_machine, message)


class NetworkLayer:
    def __init__(self):
        # Define qual é a camada abaixo desta
        self.lower_layer = TransportLayer
        # Define qual é a camada acima desta
        self.upper_layer = DataLinkLayer

    def send_message(self, sender_machine, receiver_machine, message):
        print(f"\n\t{sender_machine}'s Network Layer: Sending message to Data Link Layer\n\t\tMessage: {message}")
        # Chama a camada superior para enviar a mensagem para a camada de rede
        self.upper_layer().send_message(sender_machine, receiver_machine, message)

    def receive_message(self, sender_machine, receiver_machine, message):
        print(f"\n\t{receiver_machine.user_name}'s Network Layer: Receiving message from Data Link Layer\n\t\tMessage: "
              f"{message}")
        # Chama a camada inferior para repassar a mensagem para a camada de transporte
        self.lower_layer().receive_message(sender_machine, receiver_machine, message)


class TransportLayer:
    def __init__(self):
        # Define qual é a camada abaixo desta
        self.lower_layer = ApplicationLayer
        # Define qual é a camada acima desta
        self.upper_layer = NetworkLayer

    def send_message(self, sender_machine, receiver_machine, message):
        print(f"\n\t{sender_machine}'s Transport Layer: Sending message to Internet Layer\n\t\tMessage: {message}")
        # Chama a camada superior para enviar a mensagem para a camada de internet
        self.upper_layer().send_message(sender_machine, receiver_machine, message)

    def receive_message(self, sender_machine, receiver_machine, message):
        print(f"\n\t{receiver_machine.user_name}'s Transport Layer: Receiving message from Internet Layer\n\t\tMessage:"
              f" {message}")
        # Chama a camada inferior para repassar a mensagem para a camada de aplicação
        self.lower_layer().receive_message(sender_machine, receiver_machine, message)


class ApplicationLayer:
    def __init__(self):
        self.upper_layer = TransportLayer

    def send_message(self, sender_machine, receiver_machine, message):
        print(f"\n\t{sender_machine}'s Application Layer: Sending message to Transport Layer\n\t\tMessage: {message}")
        # Chama a camada superior para enviar a mensagem para a camada de transporte
        self.upper_layer().send_message(sender_machine, receiver_machine, message)

    def receive_message(self, sender_machine, receiver_machine, message):
        # Printa a mensagem recebida ao usuário da máquina
        print(f"\n\t{receiver_machine.user_name}'s Application Layer: You receive a message from"
              f" {sender_machine}!\n\t\t"
              f"Message: {message}")


class Machine:
    # Método de inicialização da classe, que recebe um nome de usuário e um endereço MAC
    def __init__(self, user_name, mac_address):
        # Atribui os valores passados como parâmetro aos atributos da classe
        self.user_name = user_name
        self.mac_address = mac_address
        # Cria uma instância da camada de aplicação e da camada de rede
        self.application_layer = ApplicationLayer
        self.network_layer = DataLinkLayer

    # Método que envia uma mensagem para outra máquina na rede
    def send_message(self, receiver_machine, message):
        # Imprime na tela informações sobre o envio da mensagem
        print(f"\n\033[1;34mSending message from {self.user_name}'s machine {self.mac_address} to"
              f" {receiver_machine.user_name}"
              f"'s machine {receiver_machine.mac_address}\033[0m")
        # Chama o método send_message da camada de aplicação, passando como parâmetro o nome de usuário, a máquina 
        # destinatária e a mensagem a ser enviada
        self.application_layer().send_message(self.user_name, receiver_machine, message)

    # Método que recebe uma mensagem enviada por outra máquina na rede
    def receive_message(self, sender_machine, receiver_machine, message):
        # Imprime na tela informações sobre o recebimento da mensagem
        print(f"\n\n\033[1;34mReceiving message from {sender_machine} to {self.user_name}'s machine:"
              f" {self.mac_address}\033[0m")
        # Chama o método receive_message da camada de rede, passando como parâmetro a máquina de origem, a máquina 
        # destinatária e a mensagem recebida
        self.network_layer().receive_message(sender_machine, receiver_machine, message)


class StarTopologyHub:
    def __init__(self):
        # Inicializa a lista de máquinas com seus nomes e endereços MAC
        machine_a = Machine("Leonardo", "7F-D2-21-65-7F-85")
        machine_b = Machine("Angelica", "8A-5D-B6-50-DB-E2")
        machine_c = Machine("Otávio", "85-16-FC-21-20-34")
        machine_d = Machine("Hanna", "07-65-B4-F5-EF-C5")
        machine_e = Machine("Omar", "6C-1D-B2-D1-CA-43")

        self.machines = [machine_a, machine_b, machine_c, machine_d, machine_e]

        # Imprime mensagem informando que a máquina de destino está sendo procurada
        print("\n\n\033[1;33mFinding machine of destiny in a star topology...\033[0m")

    # Envia uma mensagem de uma máquina emissor para uma máquina receptor
    def send_message(self, sender_machine, receiver_machine, message):
        # Percorre a lista de máquinas para encontrar a máquina receptor
        for machine in self.machines:
            if machine.mac_address == receiver_machine.mac_address:
                # Se a máquina receptor é encontrada, envia a mensagem para ela e imprime mensagem informando
                print(f"\n\033[1;32mMachine of destiny {receiver_machine.mac_address} found! "
                      f"Sending data package...\033[0m")
                self.machines[self.machines.index(machine)].receive_message(sender_machine, receiver_machine, message)
                break
            else:
                # Se a máquina não é a máquina receptor, imprime mensagem informando
                print(f"\n\t\033[0;35mMachine {machine.mac_address} is different from machine of destiny: "
                      f"{receiver_machine.mac_address}\033[0m")


if __name__ == "__main__":
    # Cria cinco máquinas com seus nomes e endereços MAC
    machine_A = Machine("Leonardo", "7F-D2-21-65-7F-85")
    machine_B = Machine("Angelica", "8A-5D-B6-50-DB-E2")
    machine_C = Machine("Otávio", "85-16-FC-21-20-34")
    machine_D = Machine("Hanna", "07-65-B4-F5-EF-C5")
    machine_E = Machine("Omar", "6C-1D-B2-D1-CA-43")

    # Envia uma mensagem da máquina de sua escolha entre as criadas para alguma outra máquina
    machine_B.send_message(machine_E, "Hello there!")
