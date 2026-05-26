import { useState, useEffect } from "react"
import { usePDF, Page, Text, View, Document, StyleSheet, PDFViewer } from '@react-pdf/renderer';

function PDFView({PDFInfo}) {

  console.log(PDFInfo)

  // Create styles
  const styles = StyleSheet.create({
    page: {
      flexDirection: 'row',
      backgroundColor: '#ddcba6'
    },
    section: {
      margin: 10,
      padding: 10,
      flexGrow: 1
    }
  });

  const myPDF = () => (
    <Document>
      <Page size="A4" style={styles.page}>
        <View style={styles.section}>
          <Text>{PDFInfo['playlist'][0][1][0][0]}</Text>
        </View>
      </Page>
    </Document>
  )

  return (
    <PDFViewer>
      <myPDF />
    </PDFViewer>

  );
}

export default PDFView