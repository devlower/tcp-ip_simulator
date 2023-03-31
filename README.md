# Simulador da Pilha TCP/IP
### Disciplina de Láboratório de Redes
 &nbsp;&nbsp;&nbsp;&nbsp;Professor: Harrison Herman Silva
<br>
 &nbsp;&nbsp;&nbsp;&nbsp;Aluna: Tuanne Assenço

## Introdução

Este simulador foi implementado na linguagem Python e visa simular a troca de mensagens entre duas máquinas de uma rede local com topologia estrela. O tipo de mensagem enviada foi definido como texto. Além disso, o simulador apresenta o equivalente a um dump de sniffer de rede, onde cada camada da pilha TCP/IP é responsável por imprimir informações específicas sobre a mensagem enviada/recebida.

## Classes

### DataLinkLayer 
A classe `DataLinkLayer` é uma das classes responsáveis pela comunicação entre as máquinas em uma rede de computadores. Ela é responsável por enviar mensagens para a o Hub de uma rede de topologia estrela e repassar mensagens para a camada de baixo.

#### Métodos
- `__init__()`: inicializa a classe definindo qual a camada abaixo e acima da rede.
- `send_message(sender_machine, receiver_machine, message)`: envia uma mensagem para a camada de cima `StarTopologyHub` para que a mensagem seja repassada para a máquina de destino. Imprime informações sobre a mensagem enviada.
- `receive_message(sender_machine, receiver_machine, message)`: recebe uma mensagem da camada de cima `NetworkLayer` e repassa a mensagem para a camada de baixo `NetworkLayer`. Imprime informações sobre a mensagem recebida.

### NetworkLayer
A classe `NetworkLayer` é outra classe responsável pela comunicação entre as máquinas em uma rede de computadores. Ela é responsável por enviar mensagens para a camada de cima e repassar mensagens para a camada de baixo.

#### Métodos
- `__init__()`: inicializa a classe definindo qual a camada abaixo e acima da rede.
- `send_message(sender_machine, receiver_machine, message)`: envia uma mensagem para a camada de cima `NetworkLayer` para que a mensagem seja repassada para a máquina de destino. Imprime informações sobre a mensagem enviada.
- `receive_message(sender_machine, receiver_machine, message)`: recebe uma mensagem da camada de cima `TransportLayer` e repassa a mensagem para a camada de baixo `TransportLayer`. Imprime informações sobre a mensagem recebida.

### TransportLayer
A classe `TransportLayer` é outra classe responsável pela comunicação entre as máquinas em uma rede de computadores. Ela é responsável por enviar mensagens para a camada de cima e repassar mensagens para a camada de baixo.

#### Métodos
- `__init__()`: inicializa a classe definindo qual a camada abaixo e acima da rede.
- `send_message(sender_machine, receiver_machine, message)`: envia uma mensagem para a camada de cima `InternetLayer` para que a mensagem seja repassada para a máquina de destino. Imprime informações sobre a mensagem enviada.
- `receive_message(sender_machine, receiver_machine, message)`: recebe uma mensagem da camada de cima `ApplicationLayer` e repassa a mensagem para a camada de baixo `ApplicationLayer`. Imprime informações sobre a mensagem recebida.

### ApplicationLayer
A classe `ApplicationLayer` é a última classe responsável pela comunicação entre as máquinas em uma rede de computadores. Ela é responsável por enviar mensagens para a camada de cima.

#### Métodos
- `__init__()`: inicializa a classe definindo qual a camada abaixo e acima da rede.
- `send_message(sender_machine, receiver_machine, message)`: envia uma mensagem para a camada de cima `TransportLayer` para que a mensagem seja repassada para a máquina de destino. Imprime informações sobre a mensagem enviada.
- `receive_message(sender_machine, receiver_machine, message)`: imprime na tela a mensagem recebida pelo usuário da máquina.

### Machine
A classe `Machine` é responsável pela abstração das máquinas da rede que serão instanciadas. Além de trazer duas ações (métodos) para envio e recebimento de mensagens entre duas máquinas.

#### Métodos
- `__init__()`: inicializa a classe definindo o construtor com os parâmetros `user_name` e `mac_address` que serão os identificadores das máquinas existentes na rede. Além de instanciar as camadas de `ApplicationLayer` e `DataLinkLayer` que posteriormente serão responsáveis por enviar e receber os dados entre as máquinas.
- `send_message(sender_machine, receiver_machine, message)`: recebe como parâmetro a máquina responsável pelo envio de dados `sender_machine`, a máquina que vai receber os dados `receiver_machine` e o dado `message`, neste caso o dado é uma `string`. O método envia a mensagem para a camada de `ApplicationLayer` para que a mensagem seja repassada para as acima e posteriormente encontre a máquina de destino. O método também é responsável por imprimir informações sobre a mensagem enviada.
- `receive_message(sender_machine, receiver_machine, message)`: recebe como
parâmetro a máquina responsável pelo envio de dados `sender_machine`, a máquina que vai receber os dados `receiver_machine` e o dado `message`. O método envia a mensagem para a camada de `DataLinkLayer` para que a mensagem seja repassada para as abaixo e posteriormente encontre a máquina de destino. O método também é responsável por imprimir informações sobre a mensagem enviada.

### StarTopologyHub
A classe `StarTopologyHub` é responsável pela abstração do funcionamento de um hub inserido numa topologia estrela. O qual fará a identificação da máquina que receberá a mensagem e enviará para a camada de `DataLinkLayer` específica da máquina de destino.

#### Métodos
- `__init__()`: inicializa a classe instanciando as máquinas inseridas da rede. Cria uma lista com estas máquinas.
- `send_message(sender_machine, receiver_machine, message)`: recebe como parâmetro a máquina responsável pelo envio de dados `sender_machine`, a máquina que vai receber os dados `receiver_machine` e o dado `message`. O método utiliza um `for` loop para identificar qual é o MAC address da máquina de destino _______ envia a mensagem para a camada de `ApplicationLayer` para que a mensagem seja repassada para as acima e posteriormente encontre a máquina de destino. O método também é responsável por imprimir informações sobre a mensagem enviada.
- `receive_message(sender_machine, receiver_machine, message)`: recebe como parâmetro a máquina responsável pelo envio de dados `sender_machine`, a máquina que vai receber os dados `receiver_machine` e o dado `message`. O método envia a mensagem para a camada de `DataLinkLayer` para que a mensagem seja repassada para as abaixo e posteriormente encontre a máquina de destino. O método também é responsável por imprimir informação de que a mensagem está sendo recebida pela máquina .
