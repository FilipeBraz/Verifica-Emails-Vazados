🔐 Password Leak Checker

Verificador de senhas vazadas em Python utilizando a API do Have I Been Pwned.

O projeto permite:

🖥 Modo interativo via terminal
💻 Execução via CLI com argumentos
🌐 Interface Web com Flask
🔐 Integração em sistemas de cadastro
📊 Exibição de quantas vezes a senha apareceu em vazamentos

🚀 Como Funciona

A senha é convertida em hash SHA-1.
Apenas os 5 primeiros caracteres do hash são enviados para a API.
A API retorna possíveis correspondências.
O script verifica se o restante do hash está presente.
Se estiver, informa quantas vezes a senha apareceu.
Esse método utiliza o modelo k-Anonymity, garantindo que a senha completa nunca seja transmitida.

📦 Instalação

1️⃣ Clone o repositório
git clone https://github.com/seu-usuario/password-checker.git
cd password-checker

2️⃣ Instale as dependências
pip install -r requirements.txt

Ou manualmente:

pip install requests flask
🖥 Modos de Execução
🔹 1. Modo Interativo (Input)
python password_checker.py

O sistema solicitará a senha diretamente no terminal.

🔹 2. Modo CLI

Verificar senha diretamente via argumento:
python password_checker.py -p MinhaSenha123

🔹 3. Modo Web
python password_checker.py --web

Acesse no navegador:

http://127.0.0.1:5000
Interface simples para validação de senha via navegador.

🔐 Integração em Sistema de Cadastro

Você pode importar a função principal no seu backend:
from password_checker import check_password
result = check_password(senha_usuario)
if result["compromised"]:
    raise ValueError(
        f"Senha comprometida! Encontrada {result['count']} vezes em vazamentos."
    )

Ideal para:

Sistemas corporativos
APIs de autenticação
Aplicações SaaS
Políticas de senha forte

📊 Exemplo de Retorno da Função
{
    "compromised": True,
    "count": 15234
}
🛡 Segurança

Senha nunca é enviada diretamente
Implementação baseada em k-Anonymity
Comunicação via HTTPS
Código simples e auditável

Documentação oficial da API:
https://haveibeenpwned.com/API/v3#PwnedPasswords

📂 Estrutura do Projeto
password-checker/
│
├── password_checker.py
├── requirements.txt
└── README.md

📜 Licença

Uso educacional e interno.
Verifique os termos de uso da API antes de utilizar em produção.
