import "./headerFooter.css"
import book from "../assets/book-solid-full.svg"
import music from "../assets/music-solid-full.svg"

function HeaderView() {
  return (
    <div className="header">
      <h1 className="header-title">
        <img src={book}></img>
        <span className="header-title-book">Book</span>
        -to-
        <span className="header-title-soundtrack">Soundtrack</span>
        <img src={music}></img>
      </h1>
    </div>
  )
}

export default HeaderView;