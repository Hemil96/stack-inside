import click
import api
import json

@click.command()
@click.option('--name', prompt='Company name:',
              help='The person to greet.')
def cli(name):
    json_data = api.stackinside(name)
    if json_data != "n/a":
        dict_data = json.loads(json_data)

        click.echo("")
        click.echo("> Application and Data :")
        for each in dict_data["Application and Data"]:
            click.echo("-" + each)

        click.echo("")
        click.echo("> Utilities : ")
        for each in dict_data["Utilities"]:
            click.echo("-" + each)

        click.echo("")
        click.echo("> DevOps :")
        for each in dict_data["Application and Data"]:
            click.echo("-" + each)

        click.echo("")
        click.echo("> Business Tools :")
        for each in dict_data["Business Tools"]:
            click.echo("-" + each)
        click.echo("")
    else:
        click.echo("Company not found")




if __name__ == '__main__':
    cli()
