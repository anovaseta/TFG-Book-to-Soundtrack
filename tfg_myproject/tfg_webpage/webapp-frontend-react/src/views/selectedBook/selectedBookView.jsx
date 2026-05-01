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

  const colorArray = [
    ['#66c2a5', '#84ceb7'],
    ['#fc8d62', '#fca381'],
    ['#8da0cb', '#a3b3d5'],
    ['#e78ac3', '#eba1cf'],
    ['#a6d854', '#b7df76'],
    ['#ffe058', '#ffe882'],
    ['#e5c494', '#eacfa9'],
    ['#b3b3b3', '#c2c2c2'],
    ['#8c564b', '#a3776e'],
    ['#fa4d56', '#fb7077']
  ]
  
  const fetchBookByISBNOrUID = async (id) => {
    try {
      // Success: Fetch data from the API
      // var baseUrl = "http://localhost:8000/"
      var baseUrl = "https://tfg-book-to-soundtrack.onrender.com/"
      var url = baseUrl + "api/v1/isbn/";
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
      // var baseUrl = "http://localhost:8000/"
      var baseUrl = "https://tfg-book-to-soundtrack.onrender.com/"
      var url = baseUrl + "api/v1/tag/" + tag;
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

  function goToPlaylistCreationPage(pk) {
    const url = '/flow/book/' + params['mode'] + '/' + pk + '/create-playlist'
    navigate(url)
  }

  return (
    <div>

    <HeaderView />

    <div className="selected-book">

      {data == null &&
        <div className="selected-book-loading-page">
          <img src={bookAnim} />
        </div>
      }
      {data != null &&
        <div className="selected-book-main-page">
          <div className="selected-book-main-page-details">
            <img src = {data.cover_source} alt = 'Cover not shown'/>
            <div className="selected-book-main-page-details-text">
              <h2>So you chose <span>{data.title}</span> by <span>{displayArray(data.authors)}</span></h2>
              <p>{data.description}</p>
            </div>
          </div>
          <div className="selected-book-main-page-tag-information">
            <h2 className="selected-book-main-page-tag-information-title">This book has the following mood composition!</h2>
            <div className="selected-book-main-page-tag-information-tags">
              <ul>
                  {data.tag_weights?.map((t, i) => (
                      <li>
                        <p style={{backgroundColor: colorArray[i][0]}}>
                          <span style={{fontWeight: "bold"}}>{t[0]}</span> with a {roundUsingToFixed(100*t[1])}% weight
                        </p>
                      </li>
                  ))}
              </ul>
            </div>
            <div className="selected-book-main-page-tag-information-pie-chart">
                <ul>
                  {data.tag_weights?.map((t, i) => {
                    let accum = 0
                    for (let j = 0; j < i; j++) {
                      // console.log(roundUsingToFixed(100*data.tag_weights[j][1]))
                      accum += roundUsingToFixed(100*data.tag_weights[j][1])
                    }
                    return  (
                      <li index={i} data-percentage={roundUsingToFixed(100*t[1])} data-color={colorArray[i][0]} accum={accum}>
                        <span style={{fontWeight: "bold"}}>{t[0]}</span>
                      </li>
                    )
                  })}
                </ul>
            </div>
            <div className="selected-book-main-page-tag-information-see-more">
              <h2>These mood or emotion tags are going to determine the type of music that you will get</h2>
              <h3>Click to see the synonyms of each tag!</h3>
              <div className="selected-book-main-page-tag-information-see-more-synonyms">
                {data.tag_weights?.map((t, i) => (
                  <div data-color-og={colorArray[i][0]} data-color-muted={colorArray[i][1]} onClick={(e) => (getTagSynonyms(t[0]))}
                    className="selected-book-main-page-tag-information-see-more-synonyms-element">
                    {!synData[t[0]] 
                      ? 
                      <button value={t[0]} onClick={(e) => (getTagSynonyms(e.target.value))}>{t[0]}</button> 
                      : 
                      <button value={t[0]} onClick={(e) => (delTagSynonyms(e.target.value))}>{t[0]}</button>
                    }
                    {synData[t[0]] && 
                      <div>
                        <p>Strongest: {synData[t[0]]['strongest']?.map((t) => (<text>{t}, </text>))}</p>
                        <p>Strong: {synData[t[0]]['strong']?.map((t) => (<text>{t}, </text>))}</p>
                        <p>Weak: {synData[t[0]]['weak']?.map((t) => (<text>{t}, </text>))}</p>
                      </div>
                    }
                  </div>
                ))}
              </div>
              <div className="selected-book-main-page-next-page">
                <h3 onClick={() => (goToPlaylistCreationPage(params['book_id']))}>Ready to create your playlist?</h3>
              </div>
            </div>
          </div>
          
        </div>
      }

    </div>

    <FooterView />

    </div>
  )
}

export default SelectedBookView