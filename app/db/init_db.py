from app import core, models, schema

__all__ = ["pop_db"]


role = [
	{
		"nome": "Admin",
		"access_level": 10,
	},
	{
		"nome": "Gestor",
		"access_level": 5,
	},
	{
		"nome": "Diretor",
		"access_level": 4,
	},
	{
		"nome": "Nutricionista",
		"access_level": 3,
	},
	{
		"nome": "Professor",
		"access_level": 2,
	},
	{
		"nome": "Merendeira",
		"access_level":1,
	}
]

usuarios = [
    {
        "cpf":"gestor",
        "senha":"string123456",
        "email":"teste@example.com",
    }
]

escolas = [
	{
		"nome": "CES EMILIA DE FIGUEIREDO",
		"inep_codigo": "51036010",
		"uf": "MT",
		"municipio": "Cuiabá",
		"categoria_administrativa": "Pública",
		"endereco": "AV GENERAL VALLE, SN 78010-100 Cuiabá - MT.",
	},
	{
		"nome": "CRECHE SAO FRANCISCO DE ASSIS",
		"inep_codigo": "51036339",
		"uf": "MT",
		"municipio": "Cuiabá",
		"categoria_administrativa": "Pública",
		"endereco": "RUA ENGENHEIRO RICARDO FRANCO, CENTRO NORTE. 78005-000 Cuiabá - MT.",
	},
	{
		"nome": "EE ALINA DO NASCIMENTO TOCANTINS",
		"inep_codigo": "51036479",
		"uf": "MT",
		"municipio": "Cuiabá",
		"categoria_administrativa": "Pública",
		"endereco": "AVENIDA IPIRANGA, 2560 CIDADE ALTA. 78030-500 Cuiabá - MT.",
	}
]


def pop_db() -> None:
	"""Caso exista dados iniciais no banco da aplicação, escrever sua inserçao"""
	
	for data in escolas:
		if models.Escolas.get("nome", data["nome"]):
			pass
		else:
			escola_data = models.Escolas(**data)
			escola_data.create()

	for data in role:
		if models.Papel.get("nome", data["nome"]):
			pass
		else:
			role_data = models.Papel(**data)
			role_data.create()
	role_admin = models.Papel.get("nome", "Admin")
	if role_admin:
		if models.Usuario.get(
			"cpf",
			core.settings.FIRST_SUPERUSER
			if core.settings.FIRST_SUPERUSER
			else "admin",
		):
			pass
		else:
			usuario_schema = schema.PostUsuario(
				cpf=core.settings.FIRST_SUPERUSER
				if core.settings.FIRST_SUPERUSER
				else "admin",
				senha=core.settings.FIRST_SUPERUSER_PASSWORD
				if core.settings.FIRST_SUPERUSER_PASSWORD
				else "admin",
				email="juniormarans@gmail.com",
				active=True,
			)
			user_data = models.Usuario(**usuario_schema.model_dump())
			user_data.create()
	role_gestor = models.Papel.get("nome","Admin")
	if role_gestor:
		if models.Usuario.get(
			"cpf",
			usuarios[0]["cpf"],
		):
			pass
		else:
			usuario_schema = schema.PostUsuario(
				cpf=usuarios[0]["cpf"],
				email=usuarios[0]["email"],
				senha=usuarios[0]["senha"],
				papel_uuid=role_gestor.uuid,
				papel_name=role_gestor.nome,
				access_level=str(role_gestor.access_level),
				active=True,
			)
			user_data = models.Usuario(**usuario_schema.model_dump())
			user_data.create()
