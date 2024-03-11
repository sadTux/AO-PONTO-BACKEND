import csv
import os
import random
import re
import string
import uuid
from datetime import datetime
from io import BytesIO

import magic

from app import error

__all__ = [
    "generate_cpf",
    "save_file",
    "delete_file",
    "save_csv_file",
    "list_files",
    "generate_code",
    "camel_to_kebab",
    "camel_to_snake_case",
]


def camel_to_kebab(camel_str):
    """
    Converte uma string em notação CamelCase para kebab-case.

    Parâmetros:
    camel_str (str): A string em CamelCase para ser convertida em kebab-case.

    Retorna:
    str: A string formatada em kebab-case.

    Exemplos:
    >>> camel_to_kebab('fileSystem')
    'file-system'

    >>> camel_to_kebab('CamelCaseString')
    'camel-case-string'

    >>> camel_to_kebab('HTTPRequest')
    'http-request'
    """
    # Insere um hífen antes de qualquer letra maiúscula e converte a string para minúsculas
    kebab_str = re.sub(r"(?<!^)(?=[A-Z])", "-", camel_str).lower()
    return kebab_str


def camel_to_snake_case(camel_str):
    """
    Converte uma string em notação CamelCase para snake-case.

    Parâmetros:
    camel_str (str): A string em CamelCase para ser convertida em snake-case.

    Retorna:
    str: A string formatada em snake-case.

    Exemplos:
    >>> camel_to_snake_case('fileSystem')
    'file_system'

    >>> camel_to_snake_case('CamelCaseString')
    'camel_case_string'

    >>> camel_to_snake_case('HTTPRequest')
    'http_request'
    """
    # Insere um underscore antes de qualquer letra maiúscula e converte a string para minúsculas
    kebab_str = re.sub(r"(?<!^)(?=[A-Z])", "_", camel_str).lower()
    return kebab_str


async def save_file(path: str, file: bytes, type: str) -> str:
    """Salva arquivos

    Args:
        path (str): Diretorio onde sera salvo o arquivo
        file (UploadFile): fastapi file upload
        type (str): tipo do file obs: 'video' , 'image' ...

    Raises:
        CustomException: 400 Arquivo ou diretorio não encontrado
        CustomException: 422 Formato de media invalido

    Returns:
        str: Retorna o nome do arquivo
    """
    if not os.path.exists(path):
        raise error.CustomException(
            status_code=400,
            detail="Arquivo ou diretorio não encontrado",
        )
    w_file = BytesIO()
    w_file.write(await file.read())
    w_file.seek(0)
    if str(magic.from_buffer(w_file.read(), True)).split("/")[0] != type:
        raise error.CustomException(422, "Formato de media invalido")
    w_file.seek(0)
    name = str(uuid.uuid4())
    filename = os.path.join(path, name)
    with open(filename, "wb") as f:
        f.write(w_file.getbuffer())
    return name


def save_csv_file(path: str, header: list, data: list) -> str:
    """Salva arquivos CSV.

    Args:
        path (str): Diretorio onde sera salvo o arquivo
        header (list): cabeçalho das colunas.
        data (list): dado das colunas.

    Returns:
        str: retorna o nome do arquivo que a que foi salvo.
    Raises:
        FileNotFoundError: Arquivo ou diretorio nao encontrado
    Examples:
        >>> header = ['c1','c2','c3']
        >>> data = [['l1c1','l2c2','l1c3'],['l2c1','l2c2','l3c3'] ]
        >>> path = './app/uploads/'
        >>> filename = save_csv_file(path, header, data)
    """

    name = str(uuid.uuid4())
    filename = f"{path}{name}"
    try:
        with open(filename, "w") as f:
            writer = csv.writer(f)
            writer.writerow(header)
            writer.writerows(data)
    except FileNotFoundError:
        raise error.CustomException(404, "Arquivo ou diretorio não encontrado")
    return name


def delete_file(path: str, filename: str) -> bool:
    """Exclui um arquivo atraves de seu caminho e nome

    Args:
        path (str): Diretorio onde encontra-se o arquivo
        filename (str): Nome do arquivo a ser excludio
    Raises:
        FileNotFoundError: Arquivo ou diretorio nao encontrado
    Returns:
        bool: retorna true em caso de sucesso
    """
    try:
        os.remove(f"{path}{filename}")
        return True
    except FileNotFoundError:
        raise error.CustomException(404, "Arquivo ou diretorio não encontrado")


def list_files(path: str) -> list:
    """Lista todos os arquivos de um diretorio

    Args:
        path (str): Diretorio para listar arquivos

    Returns:
        list: lista contendo nome de todos os arquivos de um diretorio
    """
    onlyfiles = [
        f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))
    ]
    return onlyfiles


def generate_cpf() -> str:
    """Gera um CPF valido

    Returns:
        str: retorna um CPF valido
    """
    cpf = [random.randint(0, 9) for x in range(9)]
    for _ in range(2):
        val = sum([(len(cpf) + 1 - i) * v for i, v in enumerate(cpf)]) % 11
        cpf.append(11 - val if val > 1 else 0)
    return "".join(str(digit) for digit in cpf)


def generate_code():
    """Código para verificação de email"""
    random_number = str(random.randint(1000, 9999))
    random_char = random.choice(string.ascii_uppercase) + random.choice(
        string.ascii_uppercase
    )
    return random_char + random_number
