import FooterView from "../footerView";
import HeaderView from "../headerView";
import './instructionsView.css'

function InstructionsView() {
  return (
    <div>

    <HeaderView />

    <div className="instructions-container">

      <p>Nota: la página web está escrita en inglés. Si esto te supone un problema, ¡pide ayuda!</p>
      <p>My TFG is based in an algorithm that, taking a book from the online book platform The StoryGraph, does a "mood analysis" of the book and
        recommends a music playlist based on that, chosen from a wide and diverse selection of music. It is not done with AI; it is completely
        human-made.</p>
      <p>Thanks for being here! I am going to go through the things you are going to need:</p>
      <ul>
        <li>A laptop or computer to access the website (it is better than your phone).</li>
        <li>A book you love (or, at least, have read) and its ISBN (the number that "identifies" your book).</li>
        <li>A Spotify account that can create a list: a free account is enough if you do not have Spotify, but a premium account will make it easier to listen to the music.</li>
        <li>A desire to listen to music! Part of the process involves LISTENING to the music you previously generated and saved.</li>
      </ul>

      <p>There will be TWO QUESTIONNAIRES in this process.</p>

      <p>You start with the first questionnaire (click <a href='https://forms.gle/DHEcpGPHTHBbcGpPA' target="_blank">here</a>), which will be done while 
      using the website. When you finish it, you will have your music playlist ready!</p>

      <p>After giving yourself time to listen to the music (it would be helpful to spend no more than 5 days),
        you will fill out the second questionnaire (click <a href='https://forms.gle/kiufDFHxjU8TNoQg9' target="_blank">here</a>).</p>

      <p>Thank you again for your help!</p>
    
      <div className="instructions-container-go-back">
        <h2>
          <a href='/'>Back to the main page</a>
        </h2>
      </div>

    </div>

    <FooterView />

    </div>
  )
}

export default InstructionsView;