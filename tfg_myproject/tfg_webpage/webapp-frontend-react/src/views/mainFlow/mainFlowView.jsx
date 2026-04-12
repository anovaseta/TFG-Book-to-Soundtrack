import { useNavigate } from "react-router-dom"
import HeaderView from "../headerView";
import FooterView from "../footerView";
import './mainFlowView.css'

function MainFlowView() {

  const navigate = useNavigate()
  
  return (
    <div className="mainflow">

      <HeaderView />

      <div className="mainflow-container">
        <h2 className="mainflow-container-title">Welcome to my project!</h2>

        <p className="mainflow-container-p1">You'll be able to select any (or almost any) book you desire, and through a complex (and even a little bit magical) transformation, 
          I will give to you a music playlist that hopefully matches the vibes of your book!</p>
        <p className="mainflow-container-p2">But first, you'll want to read through the <a href="/instructions">instructions and requirements</a> so that everything is clear.</p>

        <div className="mainflow-container-flow">
          <h2>
            <a href='/flow/choose-book'>Are you ready to make magic?</a>
          </h2>
        </div>

      </div>

      <FooterView />

    </div>

  );
}

export default MainFlowView;