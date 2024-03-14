import email

def load_tokens(email_path):
    with open(email_path, 'r', encoding ='utf-8') as f:
        entireMessage = email.message_from_file(f)
        tokens = []
        for line in email.iterators.body_line_iterator(entireMessage):
            tokens.extend(line.split())
    return tokens