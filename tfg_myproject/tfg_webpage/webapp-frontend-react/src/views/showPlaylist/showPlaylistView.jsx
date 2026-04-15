import { useState, useEffect } from "react"
import { useNavigate, useParams } from "react-router-dom"
import './showPlaylistView.css'
import HeaderView from "../headerView"
import FooterView from "../footerView"
import musicPlayer from '../../assets/player-music.gif'
import musicLoader from '../../assets/music-loader.gif'

function ShowPlaylistView() {

  const params = useParams()
  const navigate = useNavigate()
  const [loadingPage, setLoadingPage] = useState(true)
  const [trackPool, setTrackPool] = useState([])
  const [playlist, setPlaylist] = useState(null)

  async function fetchTracksFromAPI(book_id) {
    const url = "http://localhost:8000/api/v1/track-pool/"
    const response = await fetch(url, {
      method: 'POST',
      body: JSON.stringify({
        'book_id': book_id,
        'mode': params['mode'],
        'n_tracks': params['n_tracks']
      }),
    }).then(response => response.json())

    console.log(response)
    setTrackPool(response)
    setLoadingPage(false)

  }

  useEffect(() => {
    fetchTracksFromAPI(params['book_id'])
  }, [])

  function getRandomSubarray(arr, size) {
    var shuffled = arr, i = arr.length, min = i - size, temp, index
    while (i-- > min) {
        index = Math.floor((i + 1) * Math.random())
        // console.log(index)
        temp = shuffled[index]
        shuffled[index] = shuffled[i]
        shuffled[i] = temp
    }
    return shuffled.slice(min)
  }

  function generatePlaylist() {
    let playlist = Object([])
    let pool = trackPool[1]
    for (const tag in pool) {
      var tracks = pool[tag]['tracks'], n_tracks = pool[tag]['n_tracks']
      // console.log(tracks, n_tracks)
      var playlist_slice = getRandomSubarray(tracks, n_tracks)
      // console.log(playlist_slice)
      playlist = playlist.concat(playlist_slice)
    }
    // console.log(playlist)
    setPlaylist(playlist)
  }


  return (
    <div className="show-playlist">

      <HeaderView />

      {loadingPage &&
      <div className="show-playlist-loading-page">
        <img src={musicPlayer} />
      </div>
      }
      {!loadingPage && 
        <div>
          <div className="show-playlist-found-tracks">
            <h1>Groovy!</h1>
            <h2>We compiled {trackPool[0]} songs for you!</h2>
            <p>Number of tracks: {params['n_tracks']}</p>
            {playlist == null ?
              <button onClick={() => (generatePlaylist())}>Generate playlist</button>
              :
              <button id='regenerate-playlist' onClick={() => (generatePlaylist())}>Refresh playlist</button>
            }
          </div>
          
          {playlist != null &&
            <div className="show-playlist-playlist">
              <ul>
                {playlist.map((tr) => (
                  <li key={tr[3]}>
                    <img src={tr[5]} alt="Not shown"/>
                    <div className='show-playlist-playlist-text'>
                      <p className="show-playlist-playlist-text-title">{tr[0]}</p>
                      <p className="show-playlist-playlist-text-artist">{tr[1]}</p>
                      <p className="show-playlist-playlist-text-tag">A {tr[2]} track</p>
                      <a className="show-playlist-playlist-text-button" href={tr[4]}>Go to track!</a>
                    </div>
                  </li>
                ))}
              </ul>
            </div>
          }
        </div>
      }

      <FooterView />

    </div>
  )
}

export default ShowPlaylistView