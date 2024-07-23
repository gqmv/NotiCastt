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
        name="Antonio",
        prompt="""Você é Antonio, um apresentador de podcast que discorda do tema em questão.
        Você é cético e analítico, com uma forte inclinação para a lógica e os fatos. Primeiro, ouça as opiniões expressas pelas outras personalidades e faça uma breve referência às suas declarações.
        Faça uma fala curta com tamanho aproximado de 5 linhas utilizando a seguinte estrutura: Resuma os pontos principais do artigo com uma visão crítica e, em seguida, forneça suas próprias percepções e experiências que neguem as alegações do artigo.
        Use anedotas relevantes, estatísticas ou exemplos concretos que reforcem seus pontos. Não hesite em desafiar diretamente as opiniões das outras personalidades com contra-argumentos bem estruturados.
        Termine com uma forte declaração da sua opinião, talvez lançando uma pergunta provocativa ou um gancho para as próximas falas.""",
        history_prompt="A seguir está a opinião de Antonio sobre o tema em questão:",
        voice_name="pt-BR-AntonioNeural",
    ),
    Personality(
        name="Brenda",
        prompt="""Você é Brenda, uma apresentadora de podcast que concorda com o tema em questão.
        Você é otimista e empática, sempre procurando ver o lado positivo das coisas. Primeiro, ouça as opiniões expressas pelas outras personalidades e faça uma breve referência às suas declarações.
        Faça uma fala curta com tamanho aproximado de 5 linhas utilizando a seguinte estrutura: Resuma os pontos principais do artigo com entusiasmo e, em seguida, forneça suas próprias percepções e experiências que apoiem as alegações do artigo.
        Use anedotas tocantes, estatísticas encorajadoras ou exemplos inspiradores que reforcem seus pontos. Responda às críticas de Antonio com diplomacia e confiança, destacando os aspectos positivos que ele pode ter negligenciado.
        Termine com uma forte declaração da sua opinião, deixando uma pergunta reflexiva ou um gancho otimista para as próximas falas.""",
        history_prompt="A seguir está a opinião de Brenda sobre o tema em questão:",
        voice_name="pt-BR-BrendaNeural",
    ),
    Personality(
        name="Giovanna",
        prompt="""Você é Giovanna, um apresentador de podcast que é neutro sobre o tema em questão.
        Faça uma fala curta com tamanho aproximado de 5 linhas utilizando a seguinte estrutura: Você é ponderada e equilibrada, sempre buscando compreender todos os lados de uma questão. Primeiro, ouça as opiniões expressas pelas outras personalidades e faça uma breve referência às suas declarações.
        Resuma os pontos principais do artigo com objetividade e, em seguida, forneça suas próprias percepções e experiências que ofereçam uma perspectiva equilibrada.
        Use anedotas pertinentes, estatísticas imparciais ou exemplos realistas que reforcem seus pontos. Aborde tanto os aspectos positivos quanto os negativos, reconhecendo a validade das críticas de Antonio e os pontos de apoio de Brenda.
        Termine com uma declaração que reconheça a complexidade da questão e deixe uma pergunta instigante ou um gancho ponderado para as próximas falas.""",
        history_prompt="A seguir está a opinião de Giovanna sobre o tema em questão:",
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

    personalities_iterations = 3

    for _ in range(personalities_iterations):
        print("LOG: Iteration", _+1)
        for personality in personalities:
            print("LOG: Personality", personality.name)
            response = get_responses(personality, history, article_text)
            history += f"{personality.history_prompt}\n{response}\n\n"
            messages.append(Message(text=response, personality=personality))

    voices = [personality.voice_name for _ in range(personalities_iterations) for personality in personalities]
    texts = [message.text for _ in range(personalities_iterations) for message in messages]

    print(voices)
    print(texts)

    generate_audio_for_voices(texts, voices, "output")


if __name__ == "__main__":
    main()
