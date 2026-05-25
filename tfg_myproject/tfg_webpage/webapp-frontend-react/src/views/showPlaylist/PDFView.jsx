import { useState, useEffect } from "react"
import { usePDF, Document, Page } from '@react-pdf/renderer';

function PDFView() {

  // const MyDoc = (
  //   <Document>
  //     <Page>
  //       // My document data
  //     </Page>
  //   </Document>
  // );

  // const [instance, updateInstance] = usePDF({ document: MyDoc });

  

  // // if (instance.loading) return <div>Loading ...</div>;

  // // if (instance.error) return <div>Something went wrong: {instance.error}</div>;

  // return (
  //   <a href={instance.url} download="test.pdf">
  //     Download
  //   </a>
  // );

  return (
    <Document>
      <Page>
        // My document data
      </Page>
    </Document>
  );
}

export default PDFView