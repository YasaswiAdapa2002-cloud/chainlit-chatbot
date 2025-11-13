import os
import chainlit as cl
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

# --------------------------
# 1. Configure Gemini model
# --------------------------
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0.7
)

# --------------------------
# 2. Create base prompt
# --------------------------
prompt = ChatPromptTemplate.from_template("""
You are a knowledgeable AI assistant.

Topic: {topic}
Question: {question}

Answer the question clearly and concisely. If the question is unrelated to the topic,
politely remind the user to stay on topic.
""")

# Combine model and prompt
def ask_about_topic(topic: str, question: str) -> str:
    chain = prompt | llm
    result = chain.invoke({"topic": topic, "question": question})
    return result.content


# --------------------------
# 3. Chainlit flow logic
# --------------------------
@cl.on_chat_start
async def start():
    await cl.Message(content="👋 Hi! Please enter a topic you'd like to discuss.").send()


@cl.on_message
async def chat(message: cl.Message):
    # Get Chainlit session object
    session = cl.user_session
    user_input = message.content.strip().lower()

    # Step 1: If no topic stored yet → treat this as topic input
    if not session.get("topic"):
        session.set("topic", user_input)
        await cl.Message(
            content=f"✅ Great! The topic is **{user_input}**.\n\nNow ask me any questions about this topic.\n(Type 'exit' or 'quit' to stop.)"
        ).send()
        return

    # Step 2: Handle exit commands
    if user_input in ["exit", "quit"]:
        topic = session.get("topic")
        session.set("topic",None)  # clear stored data
        await cl.Message(
            content=f"👋 Ending chat on **{topic}**. You can start a new topic anytime!"
        ).send()
        return

    # Step 3: Normal Q&A flow
    topic = session.get("topic")
    answer = ask_about_topic(topic, user_input)

    await cl.Message(content=answer).send()

    # Prompt for next question
    await cl.Message(
        content="💬 You can ask another question about this topic or type 'exit' to stop."
    ).send()
