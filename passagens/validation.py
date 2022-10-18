def campos_nao_podem_ser_iguais(origem, destino, lista_de_erros):
    '''Verifica se o destino e origem são iguais'''
    if origem.lower() == destino.lower():
        lista_de_erros['destino'] = 'Origem e destino não podem ser iguais'

def campo_tem_algum_numero(valor_campo, nome_campo,lista_de_erros):
    '''Verifica se os campos tem algum digito númerico'''
    if any(char.isdigit() for char in valor_campo):
        lista_de_erros[nome_campo] = 'Não pode incluir números neste campo'

def data_de_volta_nao_pode_ser_menor_que_data_ida(data_ida, data_volta, lista_de_erros):
    '''Verifica se a data de ida não é menor que a data de volta'''
    if data_ida >= data_volta:
        lista_de_erros ['data_ida'] = 'Data de ida não pode ser maior que a data de volta'
def data_de_ida_nao_pode_ser_menor_que_data_da_pesquisa(data_ida, data_pesquisa, lista_de_erros):
    '''Verifica se a data de ida não é menor que a data atual'''
    if data_ida < data_pesquisa:
        lista_de_erros['data_ida'] = 'Data de ida não pode ser menor que o dia de hoje'