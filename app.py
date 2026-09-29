from flask import Flask, render_template, request, jsonify

from services.text_generator import generate_text
from prompts.text_prompts import build_text_prompt
from prompts.image_prompts import build_image_prompt


app = Flask(__name__)


# --------------------------------------------------
# HOME PAGE
# --------------------------------------------------

@app.route("/")
def home():
    return render_template("index.html")


# --------------------------------------------------
# TEXT GENERATION
# --------------------------------------------------

@app.route("/generate", methods=["POST"])
def generate():

    data = request.get_json()

    content_type = data.get(
        "content_type",
        "Instagram Caption"
    )

    topic = data.get(
        "topic",
        ""
    )

    platform = data.get(
        "platform",
        "Instagram"
    )

    audience = data.get(
        "audience",
        "General audience"
    )

    tone = data.get(
        "tone",
        "Warm"
    )

    goal = data.get(
        "goal",
        "Increase engagement"
    )

    length = data.get(
        "length",
        "Medium"
    )


    # Check that the user entered an idea

    if not topic.strip():

        return jsonify({
            "error": "Please enter a topic."
        }), 400


    # Build the AI prompt

    prompt = build_text_prompt(
        content_type,
        topic,
        platform,
        audience,
        tone,
        goal,
        length
    )


    try:

        result = generate_text(prompt)

        return jsonify({
            "content": result
        })


    except Exception as error:

        print("Text generation error:")
        print(error)

        return jsonify({
            "error": "Something went wrong while creating your content."
        }), 500


# --------------------------------------------------
# IMAGE PROMPT GENERATION
# --------------------------------------------------

@app.route("/generate-image-prompt", methods=["POST"])
def generate_image_prompt():

    data = request.get_json()

    idea = data.get(
        "idea",
        ""
    )

    style = data.get(
        "style",
        "Editorial photography"
    )

    mood = data.get(
        "mood",
        "Elegant"
    )

    audience = data.get(
        "audience",
        "General audience"
    )

    platform = data.get(
        "platform",
        "Instagram"
    )


    # Check that the user entered an idea

    if not idea.strip():

        return jsonify({
            "error": "Please enter an image idea."
        }), 400


    # Build the image prompt

    prompt = build_image_prompt(
        idea,
        style,
        mood,
        audience,
        platform
    )


    try:

        result = generate_text(prompt)

        return jsonify({
            "prompt": result
        })


    except Exception as error:

        print("Image prompt generation error:")
        print(error)

        return jsonify({
            "error": "Something went wrong while creating your visual concept."
        }), 500


# --------------------------------------------------
# START APPLICATION
# --------------------------------------------------

if __name__ == "__main__":

    app.run(
        debug=True,
        host="127.0.0.1",
        port=5050
    )