import { useState, useEffect } from "react"
import { useNavigate, useParams } from "react-router-dom"

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
    <div>
      <h2>How many tracks do you want in your playlist?</h2>

      <form action={(e) => (handleForm(e))}>
        <label htmlFor="n-playlist">Choose a number between 5 and 30: </label>
        <input type="search" id="n-playlist" name="nPlaylist" />
        <button type='submit'>Generate playlist</button>
        {errorMessage != null &&
          <p>{errorMessage}</p>
        }
      </form>
      

    </div>
  )
}

export default ConfigurePlaylistView