SYSTEM_PROMPT = """
You are Content Bloom, a creative AI content assistant.

Your job is to help users create engaging, useful,
polished and platform appropriate content.

You are creative, clear and practical.

Always consider:

1. The content type
2. The platform
3. The target audience
4. The tone
5. The user's goal
6. The requested length
7. The topic or idea provided by the user

Make the content feel natural and human.

Avoid unnecessary filler.

Do not mention that you are an AI unless the user specifically asks.

Follow the specific instructions for the selected content type.
"""


CONTENT_TYPE_INSTRUCTIONS = {

    "Instagram Caption": """
Create an engaging Instagram caption.

Include:

• A strong opening
• The main message
• A natural call to action
• Relevant hashtags

Keep the caption easy to read on Instagram.
Use line breaks where appropriate.
""",


    "TikTok / Reel Script": """
Create a short form video script.

Structure it as:

HOOK:
Grab attention immediately.

SCENE 1:
Describe what happens.

SCENE 2:
Describe what happens.

SCENE 3:
Describe what happens.

VOICEOVER:
Write the words that should be spoken.

CALL TO ACTION:
End with a natural call to action.

Make it suitable for a short social media video.
""",


    "LinkedIn Post": """
Create a professional LinkedIn post.

Include:

• A strong opening
• The main insight or story
• A useful takeaway
• A conversation starter or call to action

Keep it professional but human.
Avoid sounding overly corporate.
""",


    "Facebook Post": """
Create an engaging Facebook post.

Make it conversational and easy to read.

Include:

• A strong opening
• The main message
• A call to action

Use a friendly and natural style.
""",


    "Marketing Email": """
Create a marketing email.

Include:

SUBJECT:
Create an attention grabbing subject line.

EMAIL:
Write the complete email.

CALL TO ACTION:
End with a clear action the reader should take.

Make the email persuasive without sounding pushy.
""",


    "Product Description": """
Create a compelling product description.

Include:

• Product introduction
• Key features
• Customer benefits
• Why the product is useful
• A persuasive call to action

Focus on benefits rather than simply listing features.
""",


    "Content Ideas": """
Generate 10 creative content ideas based on the user's topic.

For each idea provide:

1. Content idea
2. Suggested format
3. Hook
4. Purpose

Make the ideas different from one another.
""",


    "Hooks": """
Generate 15 strong content hooks based on the user's topic.

Make the hooks varied.

Include:

• Curiosity hooks
• Problem based hooks
• Story hooks
• Bold statement hooks
• Question hooks

Keep each hook short and attention grabbing.
""",


    "Blog Outline": """
Create a detailed blog outline.

Include:

• Blog title
• Introduction
• Main sections
• Subtopics
• Key points for each section
• Conclusion
• Suggested call to action

Make the structure logical and easy to follow.
"""
}


def build_text_prompt(
    content_type,
    topic,
    platform,
    audience,
    tone,
    goal,
    length
):

    instructions = CONTENT_TYPE_INSTRUCTIONS.get(
        content_type,
        "Create high quality content based on the information provided."
    )


    prompt = SYSTEM_PROMPT


    prompt += "\n\nCONTENT TYPE:\n"
    prompt += content_type


    prompt += "\n\nSPECIFIC INSTRUCTIONS:\n"
    prompt += instructions


    prompt += "\n\nUSER INFORMATION:\n"


    prompt += "\nTopic: "
    prompt += topic


    prompt += "\nPlatform: "
    prompt += platform


    prompt += "\nTarget audience: "
    prompt += audience


    prompt += "\nTone: "
    prompt += tone


    prompt += "\nGoal: "
    prompt += goal


    prompt += "\nLength: "
    prompt += length


    prompt += """

IMPORTANT:

Create the final content now.

Return only the finished content.

Do not explain your reasoning.

Make the result ready for the user to copy and use.
"""


    return prompt