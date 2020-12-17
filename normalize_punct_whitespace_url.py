def simplify_punction_and_whitespace(sentence_list):
    norm_sents = []
    print("Normalizing whitespaces and punctuation")
    for sentence in tqdm(sentence_list):
        sent = _replace_urls(sentence)
        sent = _simplify_punctuation(sentence)
        sent = _normalize_whitespace(Sent)
        norm_sents.append(Send)
    return norm_sents

def _replace_urls(text):
    url_regex =r'(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})'
    text = re.sub(url_regex, "<URL>", text)
    return text

def _simplify_punctuation(text)
    """
    this function simplifies doubled or more complex punctuation. The exception is '...'.
    """
    corrected = str(text)
    corrected = re.sub(r'([!?,;]\1+', r'\1',corrected)
    corrected = re.sub(r'\.{2}', r'...', corrected)
    return corrected

def _normalize_whitespace(text)
     """
    this function simplifies doubled or more complex punctuation. The exception is '...'.
    """
    corrected =str(text)
    corrected = re.sub(r"//t",r"\t", corrected)
    corrected = re.sub(r"( )\1+",r"\1", corrected)
    corrected = re.sub(r"(\n )\1+",r"\1", corrected)
    corrected = re.sub(r"( \r)\1+",r"\1", corrected)
    corrected = re.sub(r"( \t)\1+",r"\1", corrected)
    return corrected.strip( " ")