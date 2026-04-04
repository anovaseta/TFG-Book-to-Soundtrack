import { useState } from "react"
import { useNavigate } from "react-router-dom"

function MainFlowView() {

  const navigate = useNavigate()
  
  return (
    <div>

      <h1>Let's make a playlist!</h1>

      <button onClick={() => (
          navigate('/flow/choose-book')
          )}>
        GO!
      </button>

    </div>

  );
}

export default MainFlowView;