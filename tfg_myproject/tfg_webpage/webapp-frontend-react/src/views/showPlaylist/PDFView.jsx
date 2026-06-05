import { usePDF, Page, Text, View, Document, StyleSheet, Image, Link, Font } from '@react-pdf/renderer';

function PDFView({PDFInfo}) {

  const colorArray = [
    ['#66c2a5', '#84ceb7'],
    ['#fc8d62', '#fca381'],
    ['#8da0cb', '#a3b3d5'],
    ['#e78ac3', '#eba1cf'],
    ['#a6d854', '#b7df76'],
    ['#ffe058', '#ffe882'],
    ['#e5c494', '#eacfa9'],
    ['#b3b3b3', '#c2c2c2'],
    ['#8c564b', '#a3776e'],
    ['#fa4d56', '#fb7077']
  ]

  // Create styles
  const styles = StyleSheet.create({
    page: {
      flexDirection: 'column',
      backgroundColor: '#ddcba6'
    },
    section_header: {
      backgroundColor: '#864e3e',
      padding: 10,
      fontSize: 30
    },
    section_book: {
      position: 'relative',
      top: 60,
      backgroundColor: '#d4966f',
      margin: 30,
      padding: 10,
      borderRadius: 15
    },
    book_cover: {
      height: 150,
      width: 100,
      marginLeft: 10
    },
    book_content: {
      padding: 15,
    },
    section_music: {
      backgroundColor: '#597e91',
      margin: 30,
      padding: 20,
      borderRadius: 15
    },
    music_item: {
      flexDirection: 'row', 
      width: 235, 
      maxWidth: 235, 
      maxHeight: 30,
    },
    music_item_text: {
      whiteSpace: 'nowrap',
      overflow: 'hidden', 
      textOverflow: 'ellipsis',
      textDecoration: 'none',
      textDecorationColor: 'none',
      paddingLeft: 5
    },
    music_cover: {
      height: 30,
      width: 30
    }
  });

  let playlistDisplay = []
    let count = 0
    for (let i = 0; i < PDFInfo['playlist'].length; i += 2) {
      // console.log(i, i+1, i+2)
      if (PDFInfo['playlist'].length % 2 == 1) {
        if (i == PDFInfo['playlist'].length - 1) {
          playlistDisplay.push([count, [PDFInfo['playlist'][i]]])
        } else {
          playlistDisplay.push([count, [PDFInfo['playlist'][i], PDFInfo['playlist'][i+1]]])
        }
      } else {
        playlistDisplay.push([count, [PDFInfo['playlist'][i], PDFInfo['playlist'][i+1]]])
      }

      count += 1
      
    }
    // console.log(playlistDisplay)

    console.log(PDFInfo)

  return (
    <Document>
      <Page size="A4" style={styles.page}> 
        <View style={styles.section_header}>
          <Text>Book-To-Soundtrack</Text>
        </View>
        <View style={styles.section_book}>
          <Text style={{padding: 10}}>You chose the book<Text style={{fontWeight:'bold'}}> {PDFInfo['title']}</Text> by<Text style={{fontWeight:'bold'}}> {PDFInfo['authors'][0]}</Text></Text>
          {/* <Image style={styles.book_cover} src={PDFInfo['cover_source']}></Image> */}
          <View style={styles.book_content}>
            <Text>The book has the following moods: </Text>
            {PDFInfo['tag_weights'].map((item, index) => {
              return (
                <View style={{backgroundColor: colorArray[index][0], margin: 10, borderRadius: 5}}>
                <Text style={{padding: 5}}>{item[0]} with a {parseFloat(item[1].toFixed(2))} weight</Text>
                </View>
              )
            }
            )}
            <View style={styles.book_content}>
              <Text>And through a complex, mythical, magical transformation...</Text>
            </View>
          </View>
        </View>
      </Page>
      <Page size="A4" style={styles.page}>
        <View style={styles.section_header}>
          <Text>Book-To-Soundtrack</Text>
        </View>
        <View style={styles.section_music}>
          <Text style={{paddingBottom: 15}}>...we chose this playlist for you!</Text>
          <View>
            {playlistDisplay.map((item, index) => {
              return (
                <View style={{flexDirection: 'row', padding: 5}}>
                  {item[1].map((item2, index2) => {
                    return (
                      <View style={styles.music_item}>
                        <Link src={item2[4]} target='_blank' style={{textDecoration: 'none', flexDirection: 'row'}}>
                          <Image src={item2[5]} style={styles.music_cover} />
                          <Text style={styles.music_item_text}>{item2[0]}</Text>
                        </Link>
                      </View>
                    )
                  })}
                  
                </View>
              )
            })}
          </View>
        </View>
      </Page>
    </Document>
  );
}

export default PDFView