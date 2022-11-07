class UserMapperUpdateException(Exception):
    def __str__(self) -> str:
        return f"failed update user:\n{self.args}"
