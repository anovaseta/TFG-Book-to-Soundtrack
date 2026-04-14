import React, { useState, useEffect } from 'react'
import axios from 'axios'
import BookList from './bookList'
import FindBook from './findBook'
import HeaderView from '../headerView'
import FooterView from '../footerView'
import './chooseBookView.css'
import book from "../../assets/book-solid-full.svg"
// UseState is a JS hook that allows us to declare a state variable inside a component

function ChooseBookView() {

  const [visibleComp, setVisibleComp] = useState(null) // '0', '1'

  return (
      <div className='choose-book'>

        <HeaderView />

        <div className='choose-book-container'>
          <p className='choose-book-container-title'>
            <img src={book}></img> The Book Hub
          </p>
          <div className='choose-book-container-select'>
            <p>You choose your book from: 
              <button 
              style={{
                backgroundColor: visibleComp == '0' && "#d4966f",
                color: visibleComp == '0' && "#681132",
                textDecoration: visibleComp == '0' && "underline"
              }} 
              onClick={() => setVisibleComp('0')}>StoryGraph</button>
              <button 
              style={{
                backgroundColor: visibleComp == '1' && "#d4966f",
                color: visibleComp == '1' && "#681132",
                textDecoration: visibleComp == '1' && "underline"
              }} 
              onClick={() => setVisibleComp('1')}>Local database</button>
            </p>
          </div>
        </div>

        {visibleComp == '0' && <FindBook/>}
        {visibleComp == '1' && <BookList/>}
        
        <FooterView />

      </div>
  );
}

export default ChooseBookView;