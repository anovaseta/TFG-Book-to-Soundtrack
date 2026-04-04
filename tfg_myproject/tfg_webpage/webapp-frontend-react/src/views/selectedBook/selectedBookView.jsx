import { useState, useEffect } from "react"
import { useNavigate, useParams} from "react-router-dom"

function SelectedBookView() {

  const params = useParams()

  const [data, setData] = useState([])
  
  const fetchBookByISBNOrUID = async (id) => {
    try {
      // Success: Fetch data from the API
      var url = "http://localhost:8000/api/v1/isbn/" + id;
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
    fetchBookByISBNOrUID(params['book_id'])
  }, [])

  

  return (
    <div>
      <p>{data.title}</p>
      <p>{data.authors?.map((author) => (<li key={author}>{author} </li>))}</p>
      <p>{data.isbn_uid}</p>
      <img src = {data.cover_source} alt = 'Cover not shown'/>
    </div>
  )
}

export default SelectedBookView