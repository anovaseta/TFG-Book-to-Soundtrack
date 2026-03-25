import React, { useState, useEffect } from 'react';
import axios from 'axios';
// UseState is a JS hook that allows us to declare a state variable inside a component

function TestPageView() {
  // console.log('vjsajcjs')
  const [data, setData] = useState([]);

  const fetchBooksFromDB = async (pk) => {
    try {
      // Success: Fetch data from the API
      if (pk != null) {
        var url = "http://localhost:8000/api/v1/books/" + pk;
      } else {
        var url = "http://localhost:8000/api/v1/books/";
      }
      const response = await fetch(url, {
        method: 'GET',
      }).then(response => response.json())
      console.log(response)
      setData(response)
    } catch (error) {
      // Error: Handle any problems with the request
      console.error("Error fetching books:", error);
    };
  }; 

  useEffect(() => {
    fetchBooksFromDB(null);
  }, []);

  return (
      <div>
          <h1>API test!!</h1>
          <p>This is the data returned by the API: </p>
          <ul>
            {data.map((book) => (
              <p>{book.title}</p>
            ))}
          </ul>
      </div>
  );
}

export default TestPageView;