from flask import Flask, render_template, request, jsonify
import random
app = Flask(__name__)

# Define routes
@app.route('/')
def index():
    return render_template('index.html')  # Render the HTML template


@app.route('/send_message', methods=['POST','GET'])
def send_message():
    user_message = request.json.get('message')  # Get the user message from the request
    # Process the user message, generate a bot response
    # For example, you might call your chatbot logic here
    # Simulating a bot response for demonstration purposes
    bot_response = "Bot: Thanks for your message: " + user_message


    # List of 10 sentences
    sentences = [
        "Our latest collection showcases trendy designs.",
        "Don't miss out on our exclusive offers!",
        "Visit our store for exciting discounts.",

        "New arrivals are now available in-store.",
        "Upgrade your wardrobe with our stylish range.",
        "Discover the perfect outfit for any occasion.",

        "Get your hands on our limited-time offers.",
        "Explore our collection for the latest fashion trends.",
        "Find the perfect fit at our store today.",

        "Shop now for the best deals on premium clothing.",
        "Elevate your style with our seasonal collection.",
        "Experience luxury with our high-quality garments."
    ]

    # Get a random set of three sentences from the list
    random_sentences = random.sample(sentences, 3)
    # Assign the random sentence to 'df'
    df = random_sentences
    x = random.randint(600, 1000)
    return jsonify({'bot_response': bot_response,'df':df,'x':x})
if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0', port=5111)  # Run the Flask app