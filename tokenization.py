import re

class tokenizer:
    def __init__(self,text):
        self.original_text = text
        self.cleaned_text = []

    def clean_and_tokenize(self):
        lower_text = self.original_text.lower()
        self.cleaned_text = re.findall(r'\b\w+\b', lower_text)
        return  self.cleaned_text

    def get_token(self):
        if not self.cleaned_text:
            return self.clean_and_tokenize()
        return self.cleaned_text

if __name__ == "__main__":
    text = "my name is Huzaifa Rashid"
    tokenizer = tokenizer(text)
    token = tokenizer.get_token()
    print(token)
