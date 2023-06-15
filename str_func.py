def convert_to_upper_str(plain_text: str) -> str:
    '''Преобразование всех букв в троке в зглавные'''
    return plain_text.upper()

def convert_to_title_str(plain_text: str) -> str:
    '''Преобразование каждого слова в специальный вид:
    каждое слово стоки plain_text начинается с заглавной буквы'''
    return plain_text.title()
