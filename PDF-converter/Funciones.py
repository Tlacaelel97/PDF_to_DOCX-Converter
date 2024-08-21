from pdf2docx import Converter
from pathlib import Path


def _create_path() -> tuple:
    """Establece el Path a partir del nombre del archivo proporcionado por un input
    y el Path de la carpeta de salida

    Arguments:
        None

    Return:
        (tuple): (Path de entrada, Path de salida)
    """
    try:
        dir_in = Path("data\In")
        work_file = Path(input())
        fname, ext = work_file.split(".")
        pdf_file = dir_in / work_file

        dir_out = Path("data\Out")
        file_out = Path(fname + ".docx")
        word_file = dir_out / file_out

        return pdf_file, word_file
    except Exception as err:
        raise err


def convert() -> None:
    """Manda a llamar a la funcion create_path y crea ambos paths
    que se le suministran a pdf2docx para realizar la conversion del pdf y guardarlo en la
    dirección indicada, en caso de error, manda excepcion y finalmente cierra el converter.

    Keyword arguments:
        None

    Returns:
        None: Manda mensaje a consola si funciona, o err en caso de excepcion
    """
    try:
        pdf_file, word_file = _create_path()

        cv = Converter(pdf_file)
        cv.convert(word_file)

        print("Archivo Convertido con éxito")
    except Exception as err:
        raise err

    finally:
        cv.close()
