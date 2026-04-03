import React, { useState, useEffect } from 'react'
import axios from 'axios'
import { useNavigate } from "react-router-dom"
// import TextField from "@mui/material/TextField";
// UseState is a JS hook that allows us to declare a state variable inside a component

function FindBook() {

  const [searchItem, setSearchItem] = useState('')
  const [searchResultVisible, setSearchResultVisible] = useState(false)
  const [searchResult, setSearchResult] = useState([])

  const navigate = useNavigate()

  async function apiCall(e){
    e.preventDefault()
    e.target.clear
    try {
      // Success: Fetch data from the API
      const url = 'http://127.0.0.1:8000/api/v1/storygraph-search/'
      const response = await fetch(url, {
        method: 'POST',
        body: JSON.stringify({searchItem})
      }).then(response => response.json())
      console.log(response)
      setSearchResult(response)
      setSearchResultVisible(true)
    } catch (error) {
      // Error: Handle any problems with the request
      console.error("Error fetching books:", error)
    };
  }

  function goToBookPage(bookId) {
    const url = '/flow/book/' + bookId
    navigate(url)
  }

  return (
    <div>
      {searchResultVisible == false &&
        <div className='findBook'>
          <p>You can use the title and the author for the search, but the ISBN gives more accurate results.</p>
          <div className="searchForm">
            <form onSubmit={apiCall}>
              <label htmlFor="book-search">Search from StoryGraph:</label>
              <input type="search" id="book-search" value={searchItem} 
                onChange={(e) => (setSearchItem(e.target.value))} placeholder='f.ex. 9780008244125'/>
              <button type='submit'>Search</button>
            </form>
          </div>
        </div>
      }

      {searchResultVisible && 
        
        <div>
          <h2>Is this your book?</h2>
          <p>{searchResult.title}</p>
          <img src = {searchResult.cover_source} alt = 'Cover not shown'/>
          <button onClick={() => (goToBookPage(searchResult.ISBN_UID))}>
            Yes!
          </button>
          <button onClick={() => setSearchResultVisible(false)}>
            No...
          </button>
        </div>
        
      }

    </div>
  );
}

export default FindBook;