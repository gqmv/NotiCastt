import os
from os import environ

import azure.cognitiveservices.speech as speechsdk
from pydub import AudioSegment


def generate_audio_for_voices(texts, voices, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    try:
        subscription_key = os.environ.get("AZURE_KEY")
        region = "brazilsouth"  # Defina sua região corretamente

        if not subscription_key or not region:
            raise ValueError("Subscription key and region must be provided")

        audio_segments = []

        for i, voice_name in enumerate(voices):
            text = texts[i]
            audio_file_path = os.path.join(output_folder, f"{voice_name}_text_{i}.wav")

            # Configurações do serviço de fala
            speech_config = speechsdk.SpeechConfig(
                subscription=subscription_key, region=region
            )
            speech_config.speech_synthesis_voice_name = voice_name
            audio_config = speechsdk.audio.AudioOutputConfig(filename=audio_file_path)

            # Criar o sintetizador de fala
            synthesizer = speechsdk.SpeechSynthesizer(
                speech_config=speech_config, audio_config=audio_config
            )

            # Realizar a síntese
            result = synthesizer.speak_text_async(text).get()

            # Verificar o resultado
            if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
                print(
                    f"Synthesis finished for {voice_name}. Audio saved to {audio_file_path}"
                )
                # Adicionar ao segmento de áudio
                audio_segments.append(AudioSegment.from_wav(audio_file_path))
            elif result.reason == speechsdk.ResultReason.Canceled:
                cancellation_details = result.cancellation_details
                print(
                    f"Speech synthesis canceled for {voice_name}: {cancellation_details.reason}"
                )
                if cancellation_details.reason == speechsdk.CancellationReason.Error:
                    print(f"Error details: {cancellation_details.error_details}")

        # Combinar segmentos de áudio, se necessário
        if len(audio_segments) > 1:
            combined_audio = sum(audio_segments)
            combined_audio.export(
                os.path.join(output_folder, "combined_audio.wav"), format="wav"
            )
            print(
                f"Combined audio saved to {os.path.join(output_folder, 'combined_audio.wav')}"
            )
    except Exception as e:
        print(f"Error: {e}")


# Exemplo de uso
# texts_to_convert = [
#     "Olá! Isso é um exemplo de conversão de texto para fala usando a voz Francisa da Azure.",
#     "isto aqui vai ser um podcast de geração de noticias",
#     "sinta-se a vontade para mandar links para que possamos transforma-los em podcast!!.",
# ]
# voices_to_generate = [
#     "pt-BR-AntonioNeural",
#     "pt-BR-BrendaNeural",
#     "pt-BR-GiovannaNeural",
# ]
# output_folder = "audio_outputs"

# if not os.path.exists(output_folder):
#     os.makedirs(output_folder)

# generate_audio_for_voices(texts_to_convert, voices_to_generate, output_folder)