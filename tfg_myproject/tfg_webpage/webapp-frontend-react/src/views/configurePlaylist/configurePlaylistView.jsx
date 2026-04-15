import { useState, useEffect } from "react"
import { useNavigate, useParams } from "react-router-dom"
import HeaderView from "../headerView"
import FooterView from "../footerView"
import './configurePlaylistView.css'
import rightArrow from '../../assets/right-long-solid-full.svg'

function ConfigurePlaylistView() {

  const params = useParams()
  const navigate = useNavigate()

  const [errorMessage, setErrorMessage] = useState(null)

  async function handleForm(formData) {
    const nTracks = formData.get("nPlaylist")
    let cast = Number(nTracks)
    console.log(cast)
    if (isNaN(cast)) {
      setErrorMessage("Input an integer between 5 and 30")
      return
    }
    if (nTracks == '') {
      setErrorMessage("Input an integer between 5 and 30")
      return
    }
    if (cast < 5 || cast > 30) {
      setErrorMessage("Input an integer between 5 and 30")
      return
    }
    setErrorMessage(null)

    // console.log(params['book_id'])

    const frontUrl = '/flow/book/' + params['mode'] + '/' + params['book_id'] + '/show-playlist/' + nTracks
    navigate(frontUrl)
  }

  return (
    <div className="configure-playlist">

      <HeaderView />

      <div className="configure-playlist-form">

        <h1>One last thing before you go...</h1>
        <h2>How many tracks do you want in your playlist? (a number between 5 and 30)</h2>

        <form action={(e) => (handleForm(e))}>
          <input onClick={() => (setErrorMessage(null))} type="search" id="n-playlist" name="nPlaylist" />
          <button type='submit'><img src={rightArrow} /></button>
          {errorMessage != null &&
            <p>{errorMessage}</p>
          }
        </form>
      
      </div>
      
      <FooterView />

    </div>
  )
}

export default ConfigurePlaylistView