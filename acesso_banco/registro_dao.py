from acesso_banco.connection import executar


def inserir_registro(fk_servidor, fk_componente, fk_medida, valor_registro, momento):

    query = ("INSERT INTO Eyes_On_Server.Registro(id_registro, fk_servidor, fk_componente, fk_medida, valor_registro, "
             "momento_registro) VALUES (null, %s, %s, %s, %s, %s);")

    values = [fk_servidor, fk_componente, fk_medida, valor_registro, momento]

    executar(query, values)