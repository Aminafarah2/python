import click
from googletrans import Translator

def greet_player(name, language):
    translator = Translator(service_urls=['translate.googleapis.com'], timeout=5)

    # Set the source language to English
    source_language = 'en'

    try:
        greeting_translation = translator.translate(f'Hello, {name}!', src=source_language, dest=language)
        farewell_translation = translator.translate(f'Goodbye, {name}!', src=source_language, dest=language)

        click.echo(greeting_translation.text)
        click.echo(farewell_translation.text)

    except Exception as e:
        click.echo(f"Error translating: {e}")

@click.command()
@click.option('--name', prompt='Enter your name', help='Your name.')
@click.option('--language', prompt='Select language (en, es, fr, etc.)', help='Select language for greeting.')
def main(name, language):
    click.echo("Welcome to the Multilingual Greeting Game!")
    click.echo("-------------------------------")

    greet_player(name, language)

    click.echo("-------------------------------")
    click.echo("Thanks for playing!")

if __name__ == '__main__':
    main()
