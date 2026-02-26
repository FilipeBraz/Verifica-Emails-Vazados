import hashlib
import requests
import argparse
from flask import Flask, request, render_template_string

API_URL = "https://api.pwnedpasswords.com/range/{}"

# ==============================
# 🔐 Função Principal Reutilizável
# ==============================

def check_password(password: str) -> dict:
    sha1 = hashlib.sha1(password.encode()).hexdigest().upper()
    prefix = sha1[:5]
    suffix = sha1[5:]

    response = requests.get(API_URL.format(prefix))
    
    if response.status_code != 200:
        raise Exception("Erro ao consultar API.")

    hashes = (line.split(":") for line in response.text.splitlines())
    for h, count in hashes:
        if h == suffix:
            return {
                "compromised": True,
                "count": int(count)
            }

    return {
        "compromised": False,
        "count": 0
    }


# ==============================
# 🖥 Entrada via input()
# ==============================

def interactive_mode():
    password = input("Digite a senha para verificar: ")
    result = check_password(password)

    if result["compromised"]:
        print(f"\n⚠ Senha comprometida!")
        print(f"Encontrada {result['count']} vezes em vazamentos.")
    else:
        print("\n✅ Senha não encontrada em vazamentos conhecidos.")


# ==============================
# 💻 Modo CLI com argumentos
# ==============================

def cli_mode():
    parser = argparse.ArgumentParser(description="Verificador de senha vazada")
    parser.add_argument("-p", "--password", help="Senha para verificar")
    parser.add_argument("--web", action="store_true", help="Iniciar modo web")

    args = parser.parse_args()

    if args.web:
        start_web_app()
    elif args.password:
        result = check_password(args.password)
        if result["compromised"]:
            print(f"⚠ Senha comprometida! Encontrada {result['count']} vezes.")
        else:
            print("✅ Senha segura (não encontrada).")
    else:
        interactive_mode()


# ==============================
# 🌐 Interface Web com Flask
# ==============================

app = Flask(__name__)

HTML_TEMPLATE = """
<!doctype html>
<title>Verificador de Senhas</title>
<h2>Verificador de Senhas Vazadas</h2>
<form method="post">
  <input type="password" name="password" placeholder="Digite sua senha" required>
  <button type="submit">Verificar</button>
</form>

{% if result %}
    {% if result.compromised %}
        <p style="color:red;">
        ⚠ Senha comprometida! Encontrada {{ result.count }} vezes.
        </p>
    {% else %}
        <p style="color:green;">
        ✅ Senha não encontrada em vazamentos conhecidos.
        </p>
    {% endif %}
{% endif %}
"""

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        password = request.form["password"]
        result = check_password(password)
    return render_template_string(HTML_TEMPLATE, result=result)


def start_web_app():
    print("🌐 Iniciando servidor web em http://127.0.0.1:5000")
    app.run(debug=True)


# ==============================
# 🚀 Execução principal
# ==============================

if __name__ == "__main__":
    cli_mode()