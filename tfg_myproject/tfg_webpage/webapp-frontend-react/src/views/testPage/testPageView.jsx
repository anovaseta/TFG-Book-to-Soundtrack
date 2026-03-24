import React, { useState, useEffect } from 'react';
// UseState is a JS hook that allows us to declare a state variable inside a component

const fetchBooksFromDB = async (pk) => {
  try {
    // Success: Fetch data from the API
    console.log(url);
    const url = "http://localhost:8000/api/v1/books/" + pk;
    const response = await fetch(url, {
      method: 'GET',
      headers: {
        "Content-Type": "application/json"
      }
    });
    const data = await response.json();
    return data
  } catch (error) {
    // Error: Handle any problems with the request
    console.error("Error fetching books:", error);
  };
};

function TestPageView() {
  const [data, setData] = useState([]);

  useEffect(() => {
    setData(fetchBooksFromDB());
  }, []);

  return (
      <div>
          <h1>API test!!</h1>
          <p>This is the data returned by the API: {data}</p>
      </div>
  );
}

export default TestPageView;