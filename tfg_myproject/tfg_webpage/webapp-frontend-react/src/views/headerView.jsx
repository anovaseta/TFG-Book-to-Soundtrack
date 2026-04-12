import "./headerFooter.css"

function HeaderView() {
  return (
    <div className="header">
      <h1 className="header-title">
        <span class="fa-solid fa-book"></span>
        <span className="header-title-book">Book</span>
        -to-
        <span className="header-title-soundtrack">Soundtrack</span>
        <span class="fa-solid fa-music"></span>
      </h1>
    </div>
  )
}

export default HeaderView;