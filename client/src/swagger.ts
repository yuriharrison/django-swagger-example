const Swagger = require('swagger-client')

const schema_url = 'http://localhost:8000/swagger.json'
export const client = Swagger(schema_url)