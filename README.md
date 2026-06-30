# 📖​🎶​WELCOME TO MY BACHELOR'S THESIS PROJECT

This project, called 'Book-to-Soundtrack', takes a book (any book!) as input and, after some **algorithm magic**, develops a music playlist as output that coincides with the vibes of the book. 
As part of the project, a **full stack website** was created to allow user interaction. <a href="https://tfg-book-to-soundtrack-site.onrender.com/" target="_blank">Click here to go to my website</a> (Ctrl+Click to open in a new tab).


## 🌟 Highlights

- 🗄️​Dataset built from scratch! 600+ books📖 and 6000+ music tracks🎶​.
- 🔀Cross-platform project: books from <a href="https://thestorygraph.com/" target="_blank">*The StoryGraph*</a>, music from <a href="https://www.last.fm/es/" target="_blank">*LastFM*</a> and *Spotify*.
- [Edit: not available] 🛜Online mode! Fetch any book from *The StoryGraph* with a quick search.
- Back end and API developed in Django.
- Front end developed in React (JS).
- Website available <a href="https://tfg-book-to-soundtrack-site.onrender.com/" target="_blank">here</a>.

## ✍️ About me

It's me, Noa (Marina)! I'm a software engineer and developer with a unique and creative point of view. Places where you can find me:
<br> <br>
<a href="https://www.linkedin.com/in/anovaseta" target="_blank"><image src="tfg_myproject/project_misc/static/linkedin-svgrepo-com.svg" alt="LinkedIn" width=30 height=30 align="left" /></a>
<br> <br> <br> 
Personal website coming soon!

## ℹ️ Project overview

### Project structure diagram

<image src="tfg_myproject/project_misc/Diagramas/Project-diagram.svg" align="center" />
<br>

The **dataset**📊​ is the central part of this project: done from scratch and the basis through which the other parts function.

The **algorithm**🧬​ relies heavily on queries done to the database to function.

The **website**🌐 allows users to interact with the algorithm and database, providing a smooth, presentable interface.

### 'Book-to-Soundtrack' algorithm

- The user chooses a book📖​ (either from the **600+ books of our database** or a book of their choosing through **online mode**).
- The **mood labels**💞​ that identify the book are obtained from *The StoryGraph*.
- Those labels are expanded via a **synonym search**👥​ in *Thesaurus*.
- The labels and its synonyms are used in *LastFM* to obtain **related music**🎶​.
- *Spotify* is used to obtain links to the songs.
