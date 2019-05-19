from inflection import camelize

from drf_yasg.inspectors import SwaggerAutoSchema


class CamelCaseOperationIDAutoSchema(SwaggerAutoSchema):

    def get_operation_id(self, operation_keys):
        operation_id = super().get_operation_id(operation_keys)
        return camelize(operation_id, uppercase_first_letter=False)
