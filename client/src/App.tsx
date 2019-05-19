import React, { useState, useEffect } from 'react'

import { client as swaggerClient } from './swagger'


function App() {
  const init: any = null
  const [client, setClient] = useState(init)
  const [author, setAuthor] = useState(null)

  useEffect(() => {
    swaggerClient.then((res: any) => {
      setClient(res)
    })
  }, [])

  useEffect(() => {
    if (client) {
      // const newAuthor = {
      //   firstName: 'Test',
      //   lastName: 'Testando',
      //   age: 55,
      //   books: ["book-2-3", "book-2-4"]
      // }
      // client.apis.author.authorCreate({ data: newAuthor }).then((resp: any) => {
      //   setAuthor(resp.data)
      // })
    }

  }, [client,])

  return (
    <code>
      {JSON.stringify(author)}
    </code>
  );
}



export default App;
