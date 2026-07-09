import re

from django.shortcuts import render


def title_case(text):
    return text.title()


def sentence_case(text):
    text = text.lower()
    return re.sub(r'(^\s*[a-z])|([.!?]\s+[a-z])', lambda match: match.group(0).upper(), text)


def camel_case(text):
    words = re.findall(r'[A-Za-z0-9]+', text)
    if not words:
        return ''
    first_word = words[0].lower()
    rest_words = ''.join(word.capitalize() for word in words[1:])
    return first_word + rest_words


def pascal_case(text):
    words = re.findall(r'[A-Za-z0-9]+', text)
    return ''.join(word.capitalize() for word in words)


def snake_case(text):
    words = re.findall(r'[A-Za-z0-9]+', text.lower())
    return '_'.join(words)


def home(request):
    result = None
    error = None

    if request.method == "POST":
        text = request.POST.get('text', '')
        cleaned_text = text.strip()
        operation = request.POST.get('operation')

        if not cleaned_text:
            error = "Please enter some text."
        elif cleaned_text.isdigit():
            error = "Only string is allowed, numbers are not allowed."
        elif operation == 'upper':
            result = text.upper()
        elif operation == 'lower':
            result = text.lower()
        elif operation == 'title':
            result = title_case(text)
        elif operation == 'sentence':
            result = sentence_case(text)
        elif operation == 'reverse':
            result = text[::-1]
        elif operation == 'remove_spaces':
            result = ' '.join(text.split())
        elif operation == 'trim':
            result = text.strip()
        elif operation == 'camel':
            result = camel_case(text)
        elif operation == 'pascal':
            result = pascal_case(text)
        elif operation == 'snake':
            result = snake_case(text)
        else:
            error = "Please select a valid conversion."

    return render(request, 'home.html', {
        'result': result,
        'error': error,
        'operation': request.POST.get('operation', ''),
        'text': request.POST.get('text', '')
    })
