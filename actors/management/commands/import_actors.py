from django.core.management.base import BaseCommand, CommandParser


class Command(BaseCommand):

    def add_arguments(self, parser: CommandParser):
        parser.add_argument(
            'file_name',
            type=str,
            help='Nome do arquivo com atores',
        )

    def handle(self, *args, **options):
        file_name = options['file_name']

        print(f'MEU PRIMEIRO COMMAND!\n'
              f'NOME DO ARQUIVO: {file_name}')
