# content of test_sample.py
def func(x):
    return x + 1


def test_answer():
    assert func(3) == 5 #verifique se...

#para rodar o teste basta digitar pytest no terminal;
# Arquivos do tipo test_*.py ou *_test.py indicam que 
# se trata de um teste