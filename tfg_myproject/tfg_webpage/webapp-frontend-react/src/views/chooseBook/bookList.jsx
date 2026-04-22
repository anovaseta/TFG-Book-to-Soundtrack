import React, { useState, useEffect } from 'react';
import bookAnim from '../../assets/book-anim.gif'
import { useNavigate } from 'react-router-dom';
// UseState is a JS hook that allows us to declare a state variable inside a component

function BookList() {
  // console.log('vjsajcjs')
  const [data, setData] = useState([])
  const [listIndex, setListIndex] = useState(0) // From 0 to 12, included
  const [dataFraction, setDataFraction] = useState(null) 

  const navigate = useNavigate()

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
      let dataFr = response.slice(0, 50)
      // console.log(dataFr)
      // Now we divide the faction in arrays of three, for display purposes
      let dataDisplay = []
      let count = 0
      for (let i = 0; i < dataFr.length; i += 3) {
        // console.log(i, i+1, i+2)
        dataDisplay.push([count, [dataFr[i], dataFr[i+1], dataFr[i+2]]])
        count += 1
      }
      console.log(dataDisplay)
      setDataFraction(dataDisplay)
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
    let dataFr = data.slice(start, end)

    // Now we divide the faction in arrays of three, for display purposes
    let dataDisplay = []
    let count = 0
    for (let i = 0; i < dataFr.length; i += 3) {
      // console.log(i, i+1, i+2)
      dataDisplay.push([count, [dataFr[i], dataFr[i+1], dataFr[i+2]]])
      count += 1
    }
    console.log(dataDisplay)
    setDataFraction(dataDisplay)
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

  const arr = Array(13).keys()

  return (

    <div className='choose-book-list-container'>
      <div className='choose-book-list-message'>
        <h2>Welcome to the local library</h2>
        <p>Feel free to choose any book from the ones that are available</p>
      </div>
      <div className='choose-book-list-list'>
        <div className='choose-book-list-list-search-tools'>
          <button onClick={() => (updateData(listIndex-1))}>
            Prev
          </button>
          {arr.map((i) => 
            <button style={{
              backgroundColor: i == listIndex && 'inherit',
              color: i == listIndex && '#681132',
              textDecoration: i == listIndex && 'underline',
            }} onClick={() => (updateData(i))}>
              {i+1}
            </button>
          )}
          <button onClick={() => (updateData(listIndex+1))}>
            Next
          </button>
        </div>
        {dataFraction == null &&
          <div className='choose-book-list-list-loading-page'>
            <img src={bookAnim} />
          </div>
        }
        {dataFraction != null &&
          <div className='choose-book-list-list-books'>
            <p>Showing books {listIndex*50+1}-{Math.min((listIndex+1)*50, 635)} of {data.length}. Books are ordered by author's name.</p>
            {dataFraction && dataFraction.map((d) => (
              <div className={'choose-book-list-list-books-div-' + d[0]}>
                {d[1].map((book) => (
                  <div>
                    {book && 
                      <div className={'choose-book-list-list-books-div-' + d[0] + '-' + book.id}
                        onClick={() => (navigate('/flow/book/offline/' + book.isbn_uid))}>
                        <img src = {book.cover_source} alt = 'Cover not shown'/>
                        <div className={'choose-book-list-list-books-div-' + d[0] + '-' + book.id + '-text'}>
                          <h3>{book.title}</h3>
                          <p>{book.authors && displayArray(book.authors)}</p>
                          <p>{book.pages} pages</p>
                          <p>First published in {book.first_published_year}</p>
                        </div>
                      </div>
                    }
                  </div>
                ))}    
              </div>
            ))}
          </div>
        }
      </div>
    </div>
  );
}

export default BookList;