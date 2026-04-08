import { useState, useEffect } from "react"
import { useNavigate, useParams } from "react-router-dom"

function ShowPlaylistView() {

  const params = useParams()
  const navigate = useNavigate()

  async function fetchTracksFromAPI(book_id) {
    const url = "http://localhost:8000/api/v1/track-pool/"
    const response = await fetch(url, {
      method: 'POST',
      body: JSON.stringify({
        'book_id': book_id,
        'mode': params['mode']
      }),
    })
  }

  useEffect(() => (
    fetchTracksFromAPI(params['book_id'])
  ), [])

  return (
    <div>
      <h2>We compiled __ songs for you!</h2>
      <p>Number of tracks: {params['n_tracks']}</p>

    
      

    </div>
  )
}

export default ShowPlaylistView