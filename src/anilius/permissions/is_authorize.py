from anilius.core.permission import Permission


class IsAuthorize(Permission):
    def has_perm(self, controller):
        return controller.is_authorize
