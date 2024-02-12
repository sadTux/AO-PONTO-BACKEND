from fastapi import APIRouter, Header

from app import auth, core, error, models, schema, util
from app.db import _db

router = APIRouter(tags=["login"])


@router.post("/login/access-token", response_model=schema.LoginResponse)
def post_login(login: schema.Login):
    """Logar"""
    try:
        user = models.Usuario.login("cpf", login.username, login.password)
        key = [user.access_level]
        sub = {
            "user_uuid": str(user.uuid),
            "key": [i for i in range(1, 10 + 1)] if 10 in key else key,
        }
        token = auth.encode_token(
            sub,
            core.settings.ACCESS_TOKEN_EXPIRE_MINUTES,
        )
        response = schema.LoginResponse(token=token, user=user)
        return response
    except Exception as e:
        raise error.custom_HTTPException(e)


@router.post(
    "/forgot-my-password/", response_model=schema.ForgotPasswordResponse
)
async def forgot_my_password(email: schema.ForgotPassword):
    """Esqueci minha senha"""
    try:
        user = models.Usuario.get("email", email.email)
        if not user:
            raise error.CustomException(404, "Email nao encontrado")
        code = util.generate_code()
        util.send_email(
            email.email,
            core.settings.PROJECT_NAME,
            util.template_string(
                "reset_password.html",
                {
                    "code": code,
                },
            ),
        )
        hash_to_string = core.get_password_hash(code).decode("utf-8")

        sub = {"code": hash_to_string, "uuid": str(user.uuid)}
        response = schema.ForgotPasswordResponse(
            token=auth.encode_token(
                sub,
                core.settings.RESET_PASSWORD_TOKEN_EXPIRATION_MINUTES,
            )
        )
        return response
    except Exception as e:
        raise error.custom_HTTPException(e)


@router.post("/forgot-my-password/code")
async def forgot_my_password_code(
    code: str,
    Authentication: str = Header(...),
):
    """Compara o codigo enviado para o email"""
    code = util.normalize_uper(code)

    token_content = auth.decode_token(Authentication)
    core.verify_password(code, token_content["code"])
    sub = {"status": "approved", "uuid": token_content["uuid"]}
    response = schema.ForgotPasswordResponse(
        token=auth.encode_token(
            sub,
            core.settings.RESET_PASSWORD_TOKEN_EXPIRATION_MINUTES,
        )
    )
    return response


@router.put("/new-password/")
def put_password(
    password: schema.ChangePassword, Authentication: str = Header(...)
):
    """Altera a senha do usuario"""
    sub = auth.decode_token(Authentication)
    models.Usuario.update(
        sub["uuid"],
        **password.model_dump(
            exclude_unset=True,
        )
    )
    return "Senha alterada"
