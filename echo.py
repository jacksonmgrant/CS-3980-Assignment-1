#echo.py
#A script to echo the last word of an input sentence by Jackson Grant

def echo(text: str, repetitions: int = 3) -> str:
    """Imitate a real world echo."""
    word:str = text.split()[-1]
    if(repetitions == 1):
        return word
    else:
        return word + "\n" + echo(word[1:], repetitions - 1)

if __name__ == "__main__":
    text = input("Yell something at a mountain: ")
    print(echo(text))