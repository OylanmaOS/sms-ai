import os
import google.generativeai as genai
from flask import Flask, request, jsonify

app = Flask(__name__)

# Gemini API Yapılandırması (Gemini Lite / Flash)
genai.configure(api_key=os.environ.get("GEMINI_API_KEY", "GEMINI_API_KEY_BURAYA"))
model = genai.GenerativeModel('gemini-1.5-flash')

# Senin Nokia 2220 Slide'ın hattına ait telefon numarası (+90...)
HEDEF_NUMARA = "+905412795479" 
    )
    response = model.generate_content(prompt)
    cevap = response.text.strip()
    return cevap[:157] if len(cevap) > 160 else cevap

@app.route('/baslat', methods=['GET'])
def otomatik_merhaba():
    """Sistem ilk açıldığında veya tetiklendiğinde telefona otomatik Merhaba mesajı yollar"""
    ilk_mesaj = "Merhaba! Yapay zeka sistemi aktif. Bana dilediğini sorabilirsin."
    
    # SMS gateway / köprü uygulamasına gidecek komut
    return jsonify({
        "action": "send_sms",
        "recipient": HEDEF_NUMARA,
        "message": ilk_mesaj
    })

@app.route('/sms-geldi', methods=['POST'])
def sms_isleyici():
    veri = request.json
    telefon_no = veri.get('sender')
    gelen_mesaj = veri.get('message')
    
    # Gelen mesajı Gemini'ye sor
    yapay_zeka_cevabi = geminiye_sor(gelen_mesaj)
    
    # Cevabı telefona geri gönder
    return jsonify({
        "action": "send_sms",
        "recipient": telefon_no,
        "message": yapay_zeka_cevabi
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)