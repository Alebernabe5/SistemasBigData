import os
from atproto import Client
from google import genai


API_KEY = os.environ.get('GEMINI_API_KEY') or "AIzaSyC_mU6Jl6-0Fkhr8ZSC9RjqxdTKQ8mPf1Q"

# Conexión Bluesky
client = Client()
client.login(BSKY_IDENTIFIER, BSKY_PASSWORD)

# Obtener feed
print("Obteniendo datos de Bluesky...")
feed = client.get_author_feed(actor="bsky.app", limit=10)
feed_text = ""
for item in feed.feed:
    feed_text += item.post.record.text + "\n"

# Conexión Gemini
genai_client = genai.Client(api_key=API_KEY)

# Prompt
prompt = f"Analiza el siguiente contenido de Bluesky y resume los temas clave en frases de pocas palabras: \n\n {feed_text}"

# Generar contenido (Usamos gemini-1.5-flash)
print("Consultando a Gemini...")
try:
    response = genai_client.models.generate_content(
        model="gemini-2.5-flash", 
        contents=prompt
    )
    # Resultado final
    print("\n" + "="*40)
    print("ANÁLISIS FINAL DE GEMINI:")
    print("="*40)
    print(response.text)
except Exception as e:
    print(f"Error inesperado: {e}")
