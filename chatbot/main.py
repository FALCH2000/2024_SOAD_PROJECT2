import functions_framework
import json
from markupsafe import escape
from google.cloud import language_v1

def analyze_text(text):
    client = language_v1.LanguageServiceClient()

    # The text to analyze
    document = language_v1.types.Document(
        content=text, type_=language_v1.types.Document.Type.PLAIN_TEXT
    )

    # Detects the sentiment of the text
    sentiment = client.analyze_sentiment(
        request={"document": document}
    ).document_sentiment

    return sentiment

# Function to interpret sentiment score
def interpret_sentiment(score):
    if score < -0.25:
        return "Negative"
    elif score > 0.25:
        return "Positive"
    else:
        return "Neutral"

def generateAnswer(kind):
    responses = {
        'Negative': "I'm sorry to hear that. We will try to improve our service.",
        'Neutral': "I understand. Thank you for sharing.",
        'Positive': "That's wonderful to hear! We're glad you enjoyed your experience."
    }
    return responses.get(kind, "Unable to determine sentiment.")

@functions_framework.http
def chatbot_http(request):
    request_args = request.args
    path = (request.path)

    if path == "/" and request.method == 'GET':
        if request_args and "texto" in request_args:
            text = request_args["texto"]
            # ESTAS 2 LINEAS CONSUMEN CREDITOS SI SE USAN
            #sentiment = analyze_text(text)
            #kind = interpret_sentiment(sentiment.score)
            answer = generateAnswer('Neutral')
            return json.dumps(answer, ensure_ascii=False) 
        else:
            return json.dumps({"error": "No se ha enviado el texto a analizar"}, ensure_ascii=False)
    else:
        return json.dumps({"error": "Ruta no encontrada"}, ensure_ascii=False)