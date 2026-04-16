import React, { useState } from 'react'
import { useNavigate } from "react-router-dom"
import magnifyingGlass from "../../assets/magnifying-glass-solid-full.svg"
import bookAnim from '../../assets/book-anim.gif'
// import TextField from "@mui/material/TextField";
// UseState is a JS hook that allows us to declare a state variable inside a component

function FindBook() {

  const [searchItem, setSearchItem] = useState('')
  const [searchResultVisible, setSearchResultVisible] = useState(false)
  const [searchResult, setSearchResult] = useState(null)

  const navigate = useNavigate()

  async function apiCall(e){
    setSearchResultVisible(true)
    setSearchResult(null)
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
      if (response == 'error') {
        setSearchResult('error')
      }
      setSearchResult(response)
    } catch (error) {
      // Error: Handle any problems with the request
      console.error("Error fetching books:", error)
    };
  }

  function goToBookPage(bookId) {
    const url = '/flow/book/online/' + bookId
    navigate(url)
  }

  function displayArray(arr) {
    // console.log(arr)
    let l = arr.length
    // console.log(l)
    let inlinehtml = ''
    for (let i = 0; i < l; i++) {
      // console.log(i)
      // console.log(arr[i])
      inlinehtml += arr[i]
      if (i < l-1) {
        inlinehtml += ', '
      }
    }
    inlinehtml += ''
    // console.log(inlinehtml)
    return inlinehtml
  }

  return (
    <div className='choose-book-storygraph'>

      <div className='choose-book-storygraph-search'>
        <p>Use StoryGraph to search for your book.</p>
        <p>Tip: you can use the title and the author for the search, but the ISBN gives more accurate results.</p>
        <div className="choose-book-storygraph-search-form">
          <form onSubmit={apiCall}>
            <input type="search" id="book-search" name="bookSearch" value={searchItem} 
              onChange={(e) => (setSearchItem(e.target.value))} placeholder='f.ex. 9780008244125'/>
            <button type='submit'><img src={magnifyingGlass} alt = "Search"></img></button>
          </form>
        </div>
      </div>

      {searchResultVisible && 
        
        <div className='choose-book-storygraph-result'>
          {searchResult == null && 
            <div className='choose-book-storygraph-result-loading-page'>
              <img src={bookAnim} />
            </div>
          }
          {searchResult == 'error' &&
            <div className='choose-book-storygraph-result-not-found-page'>
              <h2>Oops... something went wrong</h2>
              <p>We could not find your wonderful book</p>
              <p>Try a different search prompt!</p>
            </div>
          }
          {searchResult != null & searchResult != 'error' &&
            <div className='choose-book-storygraph-result-book'>
              <h2>Is this your book?</h2>
              <img src = {searchResult.cover_source} alt = 'Cover not shown'/>
              <div className='choose-book-storygraph-result-book-text'>
                <h3>{searchResult.title}</h3>
                <p>{displayArray(searchResult.authors)}</p>
                <p>{searchResult.pages} pages</p>
                <p>First published in {searchResult.first_pub}</p>
                <p>Tags: {displayArray(searchResult.tags)}</p>
              </div>
              <div className='choose-book-storygraph-result-book-buttons'>
                <p>
                  <a onClick={() => (goToBookPage(searchResult.ISBN_UID))}>Yup</a>
                </p>
                <p>
                  <a onClick={() => {
                    setSearchResultVisible(false)
                    setSearchResult(null)
                  }}> Nah (go back)</a>
                </p>
              </div>
            </div>
          }
        </div>
        
      }

    </div>
  );
}

export default FindBook;