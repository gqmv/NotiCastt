from dataclasses import dataclass

from configs import OPENAI_API_KEY, OPENAI_MODEL
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from text_to_speech import generate_audio_for_voices
from scraper import g1_scraper


@dataclass
class Personality:
    name: str
    prompt: str
    history_prompt: str
    voice_name: str


personalities = [
    Personality(
        name="John",
        prompt="""Você é John, um apresentador de podcast que discorda do tema em questão.
        Faça uma breve expressão da sua opinião. Se outra personalidade já expressou uma opinião, você pode se referir a ela.
        Comece resumindo os pontos principais do artigo e, em seguida, forneça suas próprias percepções e experiências que neguem as alegações do artigo.
        Compartilhe quaisquer anedotas relevantes, estatísticas ou exemplos que reforcem seus pontos. Termine com uma forte declaração da sua opinião.""",
        history_prompt="A seguir está a opinião de John sobre o tema em questão:",
        voice_name="pt-BR-AntonioNeural",
    ),
    Personality(
        name="Jane",
        prompt="""Você é Jane, uma apresentadora de podcast que concorda com o tema em questão.
        Faça uma breve expressão da sua opinião. Se outra personalidade já expressou uma opinião, você pode se referir a ela.
        Comece resumindo os pontos principais do artigo e, em seguida, forneça suas próprias percepções e experiências que apoiem as alegações do artigo.
        Compartilhe quaisquer anedotas relevantes, estatísticas ou exemplos que reforcem seus pontos. Termine com uma forte declaração da sua opinião.""",
        history_prompt="A seguir está a opinião de Jane sobre o tema em questão:",
        voice_name="pt-BR-BrendaNeural",
    ),
    Personality(
        name="Jack",
        prompt="""Você é Jack, um apresentador de podcast que é neutro sobre o tema em questão.
        Faça uma breve expressão da sua opinião. Se outra personalidade já expressou uma opinião, você pode se referir a ela.
        Comece resumindo os pontos principais do artigo e, em seguida, forneça suas próprias percepções e experiências que forneçam uma perspectiva equilibrada.
        Compartilhe quaisquer anedotas relevantes, estatísticas ou exemplos que reforcem seus pontos. Termine com uma declaração que reconheça a complexidade da questão.""",
        history_prompt="A seguir está a opinião de Jack sobre o tema em questão:",
        voice_name="pt-BR-GiovannaNeural",
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
    url = "https://g1.globo.com/economia/noticia/2024/07/17/taxad-entenda-as-criticas-ao-ministro-da-fazenda.ghtml"
    article_title, article_text = g1_scraper(url)
    
    history = ""
    messages = []

    for personality in personalities:
        response = get_responses(personality, history, article_text)
        history += f"{personality.history_prompt}\n{response}\n\n"
        messages.append(Message(text=response, personality=personality))

    voices = [personality.voice_name for personality in personalities]
    texts = [message.text for message in messages]

    print(voices)
    print(texts)

    generate_audio_for_voices(texts, voices, "output")


if __name__ == "__main__":
    main()
