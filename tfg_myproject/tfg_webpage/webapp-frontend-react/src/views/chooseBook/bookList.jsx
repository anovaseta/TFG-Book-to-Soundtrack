import React, { useState, useEffect } from 'react';
import axios from 'axios';
// UseState is a JS hook that allows us to declare a state variable inside a component

function BookList() {
  // console.log('vjsajcjs')
  const [data, setData] = useState([])
  const [listIndex, setListIndex] = useState(0) // From 0 to 12, included
  const [dataFraction, setDataFraction] = useState([]) 

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
      // console.log(response)
      setData(response)
      setDataFraction(response.slice(0,50))
    } catch (error) {
      // Error: Handle any problems with the request
      console.error("Error fetching books:", error);
    };
  }; 

  useEffect(() => {
    fetchBooksFromDB(null);
  }, []);

  function updateData(i){
    if (i == -1 || i == 13) return
    setListIndex(i)
    const start = i * 50
    const end = start + 50
    setDataFraction(data.slice(start,end))
  }

  const arr = Array(13).keys()

  return (
      <div>
        <button onClick={() => (updateData(listIndex-1))}>
          Prev
        </button>
        {arr.map((i) => 
          <button onClick={() => (updateData(i))}>
            {i}
          </button>
        )}
        <button onClick={() => (updateData(listIndex+1))}>
          Next
        </button>
        <p>{listIndex}</p>
          <ul>
            {dataFraction.map((book) => (
              <li key={book.id}>
                <p>{book.id}</p>
                <a href={'/flow/book/offline/'+book.isbn_uid}>{book.title}</a>
                <p>Written by: {book.authors.map((author) => (<text>{author} </text>))}</p>
                <p>{book.isbn_uid}</p>
                <img src = {book.cover_source} alt = 'Cover not shown'/>
              </li>
            ))}
          </ul>
      </div>
  );
}

export default BookList;