from flask import Flask, render_template, request
import openai
from gtts import gTTS
import io
import base64
import speech_recognition as sr

app = Flask(__name__)
openai.api_key = "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"


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api', methods=['POST'])
def api():
    r = sr.Recognizer()
    prompt = request.form['prompt']
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=2048,
        n=1,
        stop=None,
        temperature=0.5,
    )
    text = response["choices"][0]["text"]
    # Use gTTS to generate an audio file
    tts = gTTS(text)
    fp = io.BytesIO()
    tts.write_to_fp(fp)
    # Encode the audio file in base64
    audio_data = base64.b64encode(fp.getvalue()).decode('utf-8')
    return render_template('index.html', text=text, audio_data=audio_data)

if __name__ == '__main__':
    app.run(debug=True)
