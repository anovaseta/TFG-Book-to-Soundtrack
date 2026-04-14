import { useState, useEffect } from "react"
import { useNavigate, useParams} from "react-router-dom"
import HeaderView from '../headerView'
import FooterView from '../footerView'
import './selectedBookView.css'
import bookAnim from '../../assets/book-anim.gif'

function SelectedBookView() {

  const params = useParams()
  const navigate = useNavigate()

  const [data, setData] = useState(null)
  const [synData, setSynData] = useState({})
  
  const fetchBookByISBNOrUID = async (id) => {
    try {
      // Success: Fetch data from the API
      var url = "http://localhost:8000/api/v1/isbn/";
      const response = await fetch(url, {
        method: 'POST',
        body: JSON.stringify({
          'book_id': id,
          'mode': params['mode']
        })
      }).then(response => response.json())
      console.log(response)
      setData(response)
    } catch (error) {
      // Error: Handle any problems with the request
      console.error("Error fetching books:", error);
    };
  }; 

  useEffect(() => {
    fetchBookByISBNOrUID(params['book_id'])
  }, [])

  function roundUsingToFixed(value, digits=2) {
    return parseFloat(value.toFixed(digits));
  }

  async function getTagSynonyms(tag){
    try {
      // Success: Fetch data from the API
      var url = "http://localhost:8000/api/v1/tag/" + tag;
      const response = await fetch(url, {
        method: 'GET',
      }).then(response => response.json())
      // console.log(response)

      const prevDict = synData
      // console.log(prevDict)
      const curDict = Object.assign({}, prevDict, response)
      console.log(curDict)
      setSynData(curDict)

    } catch (error) {
      // Error: Handle any problems with the request
      console.error("Error fetching books:", error);
    };
  }

  function delTagSynonyms(tag){
    // console.log(tag)
    const prevDict = synData
    // console.log(dict)
    const curDict = Object.assign({}, prevDict)
    delete curDict[tag]
    // console.log(dict)
    setSynData(curDict)
    console.log(synData)
  }

  function goToPlaylistCreationPage(pk) {
    const url = '/flow/book/' + params['mode'] + '/' + pk + '/create-playlist'
    navigate(url)
  }

  return (
    <div className="selected-book">
      <HeaderView />
      {data == null &&
        <div className="selected-book-loading-page">
          <img src={bookAnim} />
        </div>
      }
      {data != null &&
        <div>
          <h2>Book details</h2>
          <p>{data.title}</p>
          <p>{data.authors?.map((author) => (<li key={author}>{author} </li>))}</p>
          <p>{data.isbn_uid}</p>
          <img src = {data.cover_source} alt = 'Cover not shown'/>
          <div>
            <h3>Here are the most common mood labels associated to your book!</h3>
            {data.tag_weights?.map((t) => (
              <div>
              <p>{t[0]} with a {roundUsingToFixed(100*t[1])}% weight</p>
              {!synData[t[0]] 
                ? 
                <button value={t[0]} onClick={(e) => (getTagSynonyms(e.target.value))}>Get synonyms</button> 
                : 
                <div>
                <p>Strongest: {synData[t[0]]['strongest']?.map((t) => (<text>{t}, </text>))}</p>
                <p>Strong: {synData[t[0]]['strong']?.map((t) => (<text>{t}, </text>))}</p>
                <p>Weak: {synData[t[0]]['weak']?.map((t) => (<text>{t}, </text>))}</p>
                <button value={t[0]} onClick={(e) => (delTagSynonyms(e.target.value))}>Hide synonyms</button>
                </div>
              }
              </div>
            ))}
          </div>
          <div>
            <h3>Ready to create your playlist?</h3>
            <button onClick={() => (goToPlaylistCreationPage(params['book_id']))}>Go!</button>
          </div>
        </div>
      }
      <FooterView />
    </div>
  )
}

export default SelectedBookView