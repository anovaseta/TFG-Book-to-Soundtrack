// You should have a prev button, and a status button to know which page to show (the others would be hidden)
import ChooseBook from "./chooseBook";
import { useState } from "react";

function MainFlowView() {

  const [visiblePage, setVisiblePage] = useState(0) // 0, 1, 2 or 3
  
  return (
    <div>

      <h1>Let's make a playlist!</h1>

      <button onClick={() => (
          setVisiblePage((visiblePage+1)%2)
          )}>
        Show or hide
      </button>

        {visiblePage == 0 && <ChooseBook/>}

    </div>

  );
}

export default MainFlowView;