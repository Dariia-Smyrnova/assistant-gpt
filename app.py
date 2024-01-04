from flask import Flask, request, jsonify
from supabase import create_client
import os 

supabase = create_client(os.environ["SUPABASE_URL"], os.environ["SUPABASE_KEY"])

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    try:
        response = supabase.table('product').select("*").eq("brand", brand).execute().data
    except Exception as e:
        print(e)
        raise e
    return response

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    print("Received request: ", data)
    return jsonify(response)
