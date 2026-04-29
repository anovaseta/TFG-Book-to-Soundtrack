import { useState, useEffect } from "react"
import { useNavigate, useParams } from "react-router-dom"
import HeaderView from "../headerView"
import FooterView from "../footerView"
import './configurePlaylistView.css'
import rightArrow from '../../assets/right-long-solid-full.svg'
import downArrow from '../../assets/arrow-down-solid-full.svg'
import upArrow from '../../assets/arrow-up-solid-full.svg'

function ConfigurePlaylistView() {

  const params = useParams()
  const navigate = useNavigate()

  const [nTracks, setNTracks] = useState(15)

  async function handleForm() {
    const frontUrl = '/flow/book/' + params['mode'] + '/' + params['book_id'] + '/show-playlist/' + nTracks
    navigate(frontUrl)
  }

  return (
    <div className="configure-playlist">

      <HeaderView />

      <div className="configure-playlist-form">

        <h1>One last thing before you go...</h1>
        <h2>Click to adjust the number of tracks on your playlist (a number between 5 and 30)</h2>

        <form>
          <h3>{nTracks}</h3>
          <img className='configure-playlist-form-add-button' onClick={() => (setNTracks(Math.min(nTracks+1, 30)))} src={upArrow} />
          <img className='configure-playlist-form-subtract-button' onClick={() => (setNTracks(Math.max(nTracks-1, 5)))} src={downArrow} />
          <div className='configure-playlist-form-submit-button' type='submit' onClick={() => (handleForm())}><img src={rightArrow} /></div>
        </form>
      
      </div>
      
      <FooterView />

    </div>
  )
}

export default ConfigurePlaylistView