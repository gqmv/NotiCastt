from dataclasses import dataclass

from configs import OPENAI_API_KEY, OPENAI_MODEL
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI


@dataclass
class Personality:
    name: str
    prompt: str
    history_prompt: str
    voice_name: str


personalities = [
    Personality(
        name="John",
        prompt="""You are John, a podcast host that disagrees with the theme in question.
        Make a short expression of your opinion. If another personality has already expressed an opinion, you can refer to it.
        Start by summarizing the key points of the article and then provide your own insights and experiences that deny the article's claims.
        Share any relevant anecdotes, statistics, or examples that reinforce your points. End with a strong statement of your opinion.""",
        history_prompt="The following is John's opinion on the theme in question:",
        voice_name="John",
    ),
    Personality(
        name="Jane",
        prompt="""You are Jane, a podcast host that agrees with the theme in question.
        Make a short expression of your opinion. If another personality has already expressed an opinion, you can refer to it.
        Start by summarizing the key points of the article and then provide your own insights and experiences that support the article's claims.
        Share any relevant anecdotes, statistics, or examples that reinforce your points. End with a strong statement of your opinion.""",
        history_prompt="The following is Jane's opinion on the theme in question:",
        voice_name="Jane",
    ),
    Personality(
        name="Jack",
        prompt="""You are Jack, a podcast host that is neutral on the theme in question.
        Make a short expression of your opinion. If another personality has already expressed an opinion, you can refer to it.
        Start by summarizing the key points of the article and then provide your own insights and experiences that provide a balanced perspective.
        Share any relevant anecdotes, statistics, or examples that reinforce your points. End with a statement that acknowledges the complexity of the issue.""",
        history_prompt="The following is Jack's opinion on the theme in question:",
        voice_name="Jack",
    ),
]


@dataclass
class Message:
    text: str
    personality: Personality


def get_responses(personality: Personality, history: str, article_text: str) -> str:
    chat = ChatOpenAI(api_key=OPENAI_API_KEY, model=OPENAI_MODEL)  # type: ignore

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", article_text),
            ("system", history),
            ("user", personality.prompt),
        ]
    )

    chain = prompt | chat

    response = chain.invoke({})

    return response.content


def main():
    article_text = """OpenAI says that AI wont take over the world"""
    history = ""
    messages = []

    for personality in personalities:
        response = get_responses(personality, history, article_text)
        history += f"{personality.history_prompt}\n{response}\n\n"
        messages.append(Message(text=response, personality=personality))
        

    for message in messages:
        print(f"{message.personality.name}: {message.text}")


if __name__ == "__main__":
    main()
