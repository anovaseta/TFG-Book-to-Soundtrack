import React, { useState, useEffect } from 'react';
// UseState is a JS hook that allows us to declare a state variable inside a component

function TestPageView() {
  // console.log('vjsajcjs')
  const [data, setData] = useState([]);

  const fetchBooksFromDB = async (pk) => {
    try {
      // Success: Fetch data from the API
      const url = "http://localhost:8000/api/v1/books/" + pk;
      const response = await fetch(url, {
        method: 'GET',
      });
      const d = await response.json();
      debugger;
      setData(d)
    } catch (error) {
      // Error: Handle any problems with the request
      console.error("Error fetching books:", error);
    };
  }; 

  useEffect(() => {
    fetchBooksFromDB('1');
  }, []);

  return (
      <div>
          <h1>API test!!</h1>
          <p>This is the data returned by the API: {data}</p>
          <p></p>
      </div>
  );
}

export default TestPageView;