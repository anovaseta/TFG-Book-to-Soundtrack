import React, { useState, useEffect } from 'react';
import axios from 'axios';
// UseState is a JS hook that allows us to declare a state variable inside a component

function FindBook() {

  const [visibleComp, setVisibleComp] = useState('0') // 0 or 1

  return (
      <div>
          <p>How do you want to choose your book?</p>
          <select name='selectBook' onChange={(event) => setVisibleComp(event.target.value)}>
            <option value = '0' >Choose book from StoryGraph (need ISBN)</option>
            <option value = '1'>Choose locally from a list of 600+ books</option>
          </select>

          {visibleComp == '1' && <BookList/>}

      </div>
  );
}

export default FindBook;