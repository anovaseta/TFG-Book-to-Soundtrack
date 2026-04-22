import FooterView from "../footerView";
import HeaderView from "../headerView";
import './instructionsView.css'

function InstructionsView() {
  return (
    <div>

    <HeaderView />

    <div className="instructions-container">

    <p>If you are here, you are probably helping me with my TFG. Thanks for being here! I am going to go through the things you are going to need:</p>
    <ul>
      <li>A good enough level of English (you can always ask me for help if you have any doubts)</li>
      <li>A Spotify account that can create a list: a free account is enough if you do not have Spotify, but a premium account will make it easier to listen to the music.</li>
    </ul>

    <p>There will be TWO SURVEYS in this process.</p>

    <p>The first survey will be done while using the website. It will ask you to do stuff step by step, and answer related questions. It may include:</p>
    <ul>
      <li>Choosing a book from a list</li>
      <li>Search for a book</li>
      <li>Create a Spotify playlist and fill it with tracks</li>
    </ul>

    <p>The second survey will involve listening to the resulting playlist (you may have a week to do that) and answer some questions about it.</p>

    <p>Thank you again for your help!</p>
    
    </div>

    <FooterView />

    </div>
  )
}

export default InstructionsView;