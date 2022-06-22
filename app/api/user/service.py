from common.res_code import SUCCESS, USER_NOT_FOUND, ERR_PASSWORD
from models.user.service import UserModel
from utils.tools import hash_password, encode_jwt
from protocols.user_protocols.register_protocol import RegisterProtocol
from protocols.user_protocols.login_protocol import LoginProtocol


class RegisterService:

    @classmethod
    def register(cls, request_obj: RegisterProtocol):
        """
        注册信息
        """
        # 将请求赋值给model对象
        user_obj = UserModel.set_json_response(request_obj)

        # 哈希密码
        password = hash_password(request_obj.password.data)

        # 插入数据库
        user_obj.password = password
        UserModel.insert_user_info(user_obj)
        return SUCCESS, {}


class LoginService:

    @classmethod
    def login(cls, request_obj: LoginProtocol):
        account = request_obj.username.data
        user = UserModel.query_user_by_account(account)

        if not user:
            return USER_NOT_FOUND, {}

        # 哈希密码
        password = hash_password(request_obj.password.data)

        # 校验密码是否正确
        if password != user.password:
            return ERR_PASSWORD, {}

        # 签发token
        jwt = encode_jwt({
            "user_id": user.id,
            "user_name": user.username
        })
        return SUCCESS, {"jwt": jwt}
