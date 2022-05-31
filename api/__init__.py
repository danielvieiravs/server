import config

from flask_restful import Api, Resource

from medium.medium import get_posts

api = Api(prefix=config.API_PREFIX)


class MediumAPI(Resource):
    def get(self, user_id):
        posts, error = get_posts(user_id=user_id)

        data = {
            "posts": posts,
            "error": error
        }

        if posts is None:
            return data, 400

        return data, 200


api.add_resource(MediumAPI, "/medium/posts/<string:user_id>")
